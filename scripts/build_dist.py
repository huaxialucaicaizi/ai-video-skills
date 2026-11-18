#!/usr/bin/env python3
"""Build self-contained skill packages under dist/ from explicit manifests.

Canonical fonts: shared/fonts/ → synced into explainer template fonts/ (+ OFL.txt).

Usage:
  python3 scripts/build_dist.py
  python3 scripts/build_dist.py --check
  python3 scripts/build_dist.py --sizes
"""

from __future__ import annotations

import argparse
import filecmp
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED_FONTS = ROOT / "shared" / "fonts"
TEMPLATE_DIR = ROOT / "code-video" / "explainer" / "templates" / "short-explainer"
TEMPLATE_FONTS = TEMPLATE_DIR / "fonts"
DIST = ROOT / "dist"
FONT_FILES = ("NotoSansSC-Regular.woff", "NotoSansSC-Bold.woff", "OFL.txt")

# Explicit package manifests (only what each skill needs).
# Paths are relative to package root after copy; sources listed as (kind, src, dst).
# kind: file | tree | skill | fonts_into_template | license
MANIFESTS: dict[str, list[tuple]] = {
    "video-router": [
        ("skill", ROOT / "video-router" / "SKILL.md", "SKILL.md"),
        ("tree", ROOT / "video-router" / "agents", "agents"),
        ("tree", ROOT / "video-router" / "references", "references"),
        ("file", ROOT / "scripts" / "doctor.sh", "doctor.sh"),
        ("license",),
    ],
    "talking-head": [
        ("skill", ROOT / "edit-video" / "talking-head" / "SKILL.md", "SKILL.md"),
        ("tree", ROOT / "edit-video" / "talking-head" / "agents", "agents"),
        ("tree", ROOT / "edit-video" / "talking-head" / "references", "references"),
        ("tree", ROOT / "edit-video" / "talking-head" / "examples", "examples"),
        ("tree", ROOT / "shared" / "overlays", "shared/overlays"),
        ("tree", ROOT / "shared" / "styles", "shared/styles"),
        ("tree", ROOT / "shared" / "subtitle-tts", "shared/subtitle-tts"),
        ("file", ROOT / "scripts" / "doctor.sh", "doctor.sh"),
        ("license",),
        # no fonts / templates — talking-head does not render HyperFrames frames in v1
    ],
    "explainer": [
        ("skill", ROOT / "code-video" / "explainer" / "SKILL.md", "SKILL.md"),
        ("tree", ROOT / "code-video" / "explainer" / "agents", "agents"),
        ("tree", ROOT / "code-video" / "explainer" / "references", "references"),
        ("tree", ROOT / "code-video" / "explainer" / "examples", "examples"),
        ("tree", ROOT / "code-video" / "explainer" / "templates", "templates"),
        ("tree", ROOT / "shared" / "overlays", "shared/overlays"),
        ("tree", ROOT / "shared" / "styles", "shared/styles"),
        ("tree", ROOT / "shared" / "subtitle-tts", "shared/subtitle-tts"),
        ("fonts_into_template", "templates/short-explainer/fonts"),
        ("file", ROOT / "scripts" / "doctor.sh", "doctor.sh"),
        ("license",),
    ],
}


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def sync_template_fonts() -> None:
    if not SHARED_FONTS.is_dir():
        die(f"missing {SHARED_FONTS}")
    TEMPLATE_FONTS.mkdir(parents=True, exist_ok=True)
    for name in FONT_FILES:
        src = SHARED_FONTS / name
        if not src.exists():
            die(f"missing font/license file: {src}")
        shutil.copy2(src, TEMPLATE_FONTS / name)
    print(f"OK synced fonts → {TEMPLATE_FONTS.relative_to(ROOT)}")


def ensure_template_local_font_urls() -> None:
    index = TEMPLATE_DIR / "index.html"
    text = index.read_text(encoding="utf-8")
    if re.search(r"url\([\"']?\.\./", text):
        die(f"{index.relative_to(ROOT)} still has ../ asset URLs")
    updated = text
    updated = re.sub(
        r"url\([\"']?[^\"')]*NotoSansSC-Regular\.woff[\"']?\)",
        'url("./fonts/NotoSansSC-Regular.woff")',
        updated,
    )
    updated = re.sub(
        r"url\([\"']?[^\"')]*NotoSansSC-Bold\.woff[\"']?\)",
        'url("./fonts/NotoSansSC-Bold.woff")',
        updated,
    )
    updated = updated.replace(
        "/* Fonts from repo shared/fonts (OFL) — relative path, no CDN */",
        "/* Fonts: ./fonts (synced from shared/fonts, OFL) — no CDN, no parent traversal */",
    )
    if updated != text:
        index.write_text(updated, encoding="utf-8")
        print(f"OK updated font URLs in {index.relative_to(ROOT)}")
    else:
        print(f"OK font URLs already local in {index.relative_to(ROOT)}")


def _copy_tree(src: Path, dst: Path) -> None:
    def _ignore(_dir: str, names: list[str]) -> set[str]:
        skip = set()
        for n in names:
            if n in {"node_modules", "renders", ".hyperframes", ".DS_Store"}:
                skip.add(n)
            if n.endswith(".mp4"):
                skip.add(n)
        return skip

    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=_ignore)


def _rewrite_skill_md(text: str, *, package: str) -> str:
    install_note = (
        "\n## 安装包说明\n\n"
        "本目录是 CI/`scripts/build_dist.py` 生成的**自包含安装包**。"
        "请整夹复制到各工具的 skills 目录；不要手改 `dist/`，改源码后重新运行构建脚本。\n"
    )

    if package == "video-router":
        # Keep source wording for missing-skill tip; normalize doctor paths for the package.
        text = re.sub(
            r"4\. \*\*环境检查（Mac）\*\*：.*",
            "4. **环境检查（Mac）**：运行本包内 `./doctor.sh`（检查 Node.js、**ffmpeg**、Python 等）。"
            "缺什么指给 setup-doctor（ai-from-zero）。",
            text,
        )
        # Related section: keep tip + local doctor; drop monorepo-only paths
        if "## 相关" in text:
            related = (
                "## 相关\n\n"
                "- 路由细则：`references/route-table.md`\n"
                "- 环境脚本：`./doctor.sh`\n"
                "- 若目标 skill 未安装：提示用户安装对应 dist 包（`dist/explainer/` 或 `dist/talking-head/`），"
                "安装步骤见仓库 README「安装（Mac）」一节\n"
            )
            text = re.sub(r"## 相关\n\n.*?(?=\n## |\Z)", related, text, flags=re.S)
        if "安装包说明" not in text:
            text += install_note
        return text

    if package == "explainer":
        text = text.replace(
            "仓库 `shared/fonts` + OFL",
            "本包模板内 `templates/short-explainer/fonts/`（含 OFL.txt）",
        )
        if "安装包说明" not in text:
            text += install_note
        return text

    if package == "talking-head":
        if "安装包说明" not in text:
            text += install_note
        return text

    return text


def _rewrite_package_text(text: str, *, package: str) -> str:
    """Normalize monorepo paths so the package is self-contained."""
    text = text.replace("仓库：`../scripts/doctor.sh`；安装包：`./doctor.sh`", "本包：`./doctor.sh`")
    text = text.replace("见本 skill 根目录 `./doctor.sh`；仓库内为 `scripts/doctor.sh`", "见本 skill 根目录 `./doctor.sh`")
    text = text.replace("（仓库内为 `scripts/doctor.sh`）", "")
    text = text.replace("`../scripts/doctor.sh`", "`./doctor.sh`")
    text = text.replace("`scripts/doctor.sh`", "`./doctor.sh`")
    text = text.replace("仓库 `scripts/doctor.sh`", "本包 `./doctor.sh`")
    text = text.replace("见仓库 `scripts/doctor.sh`", "见本包根目录 `./doctor.sh`")
    if package == "explainer":
        text = text.replace(
            "由 `scripts/build_dist.py` 从仓库 `shared/fonts/` 同步，含 OFL.txt",
            "本目录 `./fonts/`（含 OFL.txt；构建时从仓库 shared/fonts 同步）",
        )
        text = text.replace("`shared/fonts/`", "`templates/short-explainer/fonts/`")
        text = text.replace("`shared/fonts`", "`templates/short-explainer/fonts`")
        text = text.replace(
            "仓库 `shared/fonts` + OFL",
            "本包模板内 `templates/short-explainer/fonts/`（含 OFL.txt）",
        )
        text = text.replace(
            "`code-video/explainer/references/style-usage.md`",
            "`references/style-usage.md`",
        )
    elif package == "talking-head":
        text = text.replace(
            "再读 `code-video/explainer/references/style-usage.md`",
            "再读对应 yaml 注释与本包 `shared/styles/SCHEMA.md`",
        )
        text = text.replace("`code-video/explainer/references/style-usage.md`", "`shared/styles/SCHEMA.md`")
    return text


def _rewrite_copied_text_files(pkg: Path) -> None:
    for path in pkg.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".html", ".css", ".txt", ".yaml", ".yml", ".sh"}:
            continue
        if path.name in {"LICENSE", "NOTICE", "OFL.txt"}:
            continue
        raw = path.read_text(encoding="utf-8")
        updated = _rewrite_package_text(raw, package=pkg.name)
        if updated != raw:
            path.write_text(updated, encoding="utf-8")


def _apply_item(pkg: Path, item: tuple) -> None:
    kind = item[0]
    if kind == "skill":
        _, src, dst = item
        text = _rewrite_skill_md(Path(src).read_text(encoding="utf-8"), package=pkg.name)
        text = _rewrite_package_text(text, package=pkg.name)
        out = pkg / dst
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    elif kind == "file":
        _, src, dst = item
        out = pkg / dst
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)
    elif kind == "tree":
        _, src, dst = item
        _copy_tree(Path(src), pkg / dst)
    elif kind == "fonts_into_template":
        _, dst = item
        out = pkg / dst
        out.mkdir(parents=True, exist_ok=True)
        for name in FONT_FILES:
            shutil.copy2(SHARED_FONTS / name, out / name)
    elif kind == "license":
        for name in ("LICENSE", "NOTICE"):
            src = ROOT / name
            if not src.exists():
                die(f"missing {src}")
            shutil.copy2(src, pkg / name)
    else:
        die(f"unknown manifest kind: {kind}")


def build_package(out_root: Path, name: str) -> Path:
    pkg = out_root / name
    if pkg.exists():
        shutil.rmtree(pkg)
    pkg.mkdir(parents=True)
    for item in MANIFESTS[name]:
        _apply_item(pkg, item)
    _rewrite_copied_text_files(pkg)
    # Guards
    if name == "explainer":
        html = (pkg / "templates" / "short-explainer" / "index.html").read_text(encoding="utf-8")
        if re.search(r"url\([\"']?\.\./", html):
            die("dist/explainer template still has parent-traversal font URLs")
        ofl = pkg / "templates" / "short-explainer" / "fonts" / "OFL.txt"
        if not ofl.exists():
            die("explainer template fonts missing OFL.txt")
    # video-router / talking-head must not ship fonts
    if name in {"video-router", "talking-head"}:
        for p in pkg.rglob("*"):
            if p.suffix.lower() in {".woff", ".woff2", ".otf", ".ttf"}:
                die(f"{name} must not include font file: {p.relative_to(pkg)}")
    if not (pkg / "LICENSE").exists() or not (pkg / "NOTICE").exists():
        die(f"{name} missing LICENSE/NOTICE")
    print(f"OK built {name}")
    return pkg


def package_size_bytes(pkg: Path) -> int:
    total = 0
    for p in pkg.rglob("*"):
        if p.is_file():
            total += p.stat().st_size
    return total


def print_sizes(out_root: Path) -> None:
    for name in ("video-router", "talking-head", "explainer"):
        pkg = out_root / name
        if not pkg.exists():
            die(f"missing {pkg}")
        n = package_size_bytes(pkg)
        print(f"SIZE {name}: {n} bytes ({n / 1024 / 1024:.2f} MiB)")


def build_all(out_root: Path) -> None:
    sync_template_fonts()
    ensure_template_local_font_urls()
    out_root.mkdir(parents=True, exist_ok=True)
    for name in ("video-router", "talking-head", "explainer"):
        p = out_root / name
        if p.exists():
            shutil.rmtree(p)
    for name in ("video-router", "talking-head", "explainer"):
        build_package(out_root, name)
    (out_root / "README.md").write_text(
        "# dist/\n\n"
        "由 `scripts/build_dist.py` 按显式清单生成的自包含 skill 安装包。\n\n"
        "- `video-router/`：只路由，不渲染；需与另两个包一起安装才能用起来\n"
        "- `talking-head/`：口播流程 + overlays/styles/subtitle-tts（无字体/模板）\n"
        "- `explainer/`：科普渲染模板 + overlays/styles/subtitle-tts + 模板内字体（OFL）\n\n"
        "每个包都含 `LICENSE` 与 `NOTICE`。不要手改；改源码后重新运行构建脚本。\n\n"
        "Generated by `scripts/build_dist.py` from explicit manifests. "
        "Do not hand-edit; re-run after source changes.\n",
        encoding="utf-8",
    )
    print_sizes(out_root)


def _dir_diff(a: Path, b: Path) -> list[str]:
    problems: list[str] = []
    if not a.exists() or not b.exists():
        return [f"missing tree: {a} or {b}"]
    cmp = filecmp.dircmp(a, b, ignore=[".DS_Store"])

    def walk(c: filecmp.dircmp) -> None:
        for name in c.left_only:
            problems.append(f"only in {c.left}: {name}")
        for name in c.right_only:
            problems.append(f"only in {c.right}: {name}")
        for name in c.diff_files:
            problems.append(f"differ: {Path(c.left) / name}")
        for name in c.funny_files:
            problems.append(f"funny: {Path(c.left) / name}")
        for sub in c.subdirs.values():
            walk(sub)

    walk(cmp)
    return problems


def check_mode() -> None:
    with tempfile.TemporaryDirectory(prefix="ai-video-skills-dist-") as tmp:
        out = Path(tmp) / "dist"
        build_all(out)
        if not DIST.exists():
            die("committed dist/ missing; run scripts/build_dist.py and commit")
        problems: list[str] = []
        for name in ("explainer", "talking-head", "video-router"):
            problems.extend(_dir_diff(DIST / name, out / name))
        if (DIST / "README.md").exists() or (out / "README.md").exists():
            if not filecmp.cmp(DIST / "README.md", out / "README.md", shallow=False):
                problems.append("differ: dist/README.md")
        if problems:
            print("dist/ is out of date vs scripts/build_dist.py:", file=sys.stderr)
            for p in problems[:80]:
                print(f"  - {p}", file=sys.stderr)
            raise SystemExit(1)
    print("OK dist/ matches build_dist.py output")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--sizes", action="store_true", help="print sizes of committed dist/ only")
    args = ap.parse_args()
    if args.sizes:
        print_sizes(DIST)
        return
    if args.check:
        check_mode()
    else:
        build_all(DIST)
        print(f"OK wrote {DIST}")


if __name__ == "__main__":
    main()
