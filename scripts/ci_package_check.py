#!/usr/bin/env python3
"""Copy a dist package to a temp dir and verify relative refs stay inside the package.

Usage:
  python3 scripts/ci_package_check.py dist/video-router
  python3 scripts/ci_package_check.py dist/talking-head --run-doctor
  python3 scripts/ci_package_check.py dist/explainer
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TEXT_SUFFIXES = {
    ".md",
    ".html",
    ".css",
    ".js",
    ".json",
    ".yaml",
    ".yml",
    ".txt",
    ".py",
    ".sh",
}

BACKTICK_RE = re.compile(r"`([^`\n]+)`")
URL_RE = re.compile(r"url\((['\"]?)([^)'\"]+)\1\)")
HREF_SRC_RE = re.compile(r"""(?:href|src)=(['"])([^'"]+)\1""", re.I)

# Known package-relative path prefixes / file patterns we ship
PATH_PREFIXES = (
    "agents/",
    "references/",
    "examples/",
    "templates/",
    "shared/",
    "fonts/",
    "./fonts/",
    "./doctor.sh",
    "doctor.sh",
    "SKILL.md",
    "LICENSE",
    "NOTICE",
    "OFL.txt",
    "index.html",
    "package.json",
    "package-lock.json",
    "README.md",
)

SKIP_EXACT = {
    "scripts/build_dist.py",
    "CI/scripts/build_dist.py",
}


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def looks_like_package_ref(s: str) -> bool:
    s = s.strip().strip("，。；;,.）)")
    if not s or "://" in s or s.startswith("mailto:"):
        return False
    if s.startswith("/") or s.startswith("~"):
        return False
    if s in SKIP_EXACT:
        return False
    if s.startswith("dist/"):
        return False
    if "node_modules/" in s:
        return False
    if "*" in s or "?" in s:
        return False
    if " " in s:
        return False
    if s in {".", "..", "./", "../"}:
        return False
    # Must look like a path we care about
    if s.startswith(PATH_PREFIXES) or s.startswith("./"):
        return True
    if s.startswith(("code-video/", "edit-video/", "video-router/", "scripts/")):
        # monorepo paths must be rewritten out of packages; still flag them
        return True
    if "/" in s and (s.endswith("/") or "." in Path(s).name):
        if any(s.startswith(p) for p in PATH_PREFIXES):
            return True
        if Path(s).suffix.lower() in TEXT_SUFFIXES | {".woff", ".woff2"}:
            return True
    if s in {"doctor.sh", "SKILL.md", "LICENSE", "NOTICE", "OFL.txt", "index.html", "package.json"}:
        return True
    return False


def collect_refs(pkg: Path) -> list[tuple[Path, str]]:
    found: list[tuple[Path, str]] = []
    for path in pkg.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE", "NOTICE"}:
            continue
        if path.name in {"package-lock.json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in BACKTICK_RE.finditer(text):
            cand = m.group(1).strip()
            if looks_like_package_ref(cand):
                found.append((path, cand))
        for m in URL_RE.finditer(text):
            cand = m.group(2).strip()
            if looks_like_package_ref(cand):
                found.append((path, cand))
        for m in HREF_SRC_RE.finditer(text):
            cand = m.group(2).strip()
            if looks_like_package_ref(cand) and not cand.startswith("http"):
                found.append((path, cand))
    return found


def resolve_ref(pkg: Path, from_file: Path, ref: str) -> Path:
    clean = ref.strip()
    if ".." in Path(clean).parts:
        die(f"parent traversal in ref in {from_file.relative_to(pkg)}: {ref}")

    candidates: list[Path] = []
    if clean.startswith("./") or clean.startswith("../"):
        candidates.append((from_file.parent / clean).resolve())
    elif "/" in clean:
        # package-root relative skill docs convention
        candidates.append((pkg / clean.lstrip("./")).resolve())
        # also allow file-relative
        candidates.append((from_file.parent / clean).resolve())
    else:
        # bare filename: prefer sibling of the mentioning file, then package root
        candidates.append((from_file.parent / clean).resolve())
        candidates.append((pkg / clean).resolve())

    pkg_root = pkg.resolve()
    existing: list[Path] = []
    for target in candidates:
        try:
            target.relative_to(pkg_root)
        except ValueError:
            continue
        if target.exists():
            existing.append(target)
    if existing:
        return existing[0]
    # return first in-package candidate for missing reporting
    for target in candidates:
        try:
            target.relative_to(pkg_root)
            return target
        except ValueError:
            continue
    die(f"ref escapes package root in {from_file.relative_to(pkg)}: {ref}")
    raise AssertionError("unreachable")


def check_package(src: Path, *, run_doctor: bool) -> None:
    if not src.is_dir():
        die(f"missing package dir: {src}")
    with tempfile.TemporaryDirectory(prefix=f"pkg-{src.name}-") as tmp:
        dst = Path(tmp) / src.name
        shutil.copytree(
            src,
            dst,
            ignore=shutil.ignore_patterns("node_modules", "renders", ".hyperframes", "*.mp4"),
        )
        print(f"== check {src} in {dst} ==")
        for required in ("SKILL.md", "doctor.sh", "LICENSE", "NOTICE"):
            if not (dst / required).exists():
                die(f"missing required {required}")
        refs = collect_refs(dst)
        missing: list[str] = []
        for from_file, ref in refs:
            target = resolve_ref(dst, from_file, ref)
            if not target.exists():
                missing.append(f"{from_file.relative_to(dst)} → {ref}")
        if missing:
            die("missing relative refs:\n  - " + "\n  - ".join(missing))
        # No parent-traversal asset paths in package text files
        for path in dst.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if path.name == "package-lock.json":
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for m in re.finditer(r"""(?:url\(|src=|href=|`)(\.\./[^`'\"\s)]*)""", text):
                frag = m.group(1)
                if frag in {"../", ".."}:
                    continue
                die(f"found parent-traversal path in {path.relative_to(dst)}: {frag}")
        print(f"OK path check: {src.name} ({len(refs)} refs scanned)")
        if run_doctor:
            doctor = dst / "doctor.sh"
            doctor.chmod(doctor.stat().st_mode | 0o111)
            print(f"== run {doctor} ==")
            subprocess.run([str(doctor)], check=True, cwd=str(dst))
            print(f"OK doctor.sh in {src.name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("package", type=Path, help="path to dist/<name>")
    ap.add_argument("--run-doctor", action="store_true")
    args = ap.parse_args()
    check_package(args.package.resolve(), run_doctor=args.run_doctor)


if __name__ == "__main__":
    main()
