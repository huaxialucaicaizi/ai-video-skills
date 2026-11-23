#!/usr/bin/env python3
"""CI validators for ai-video-skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

# Banned product-name tokens assembled without spelling them as literals in source,
# so a plain-text repo search for those spellings stays empty.
_FORBIDDEN_LITERAL = [bytes([0xE5, 0x85, 0x83, 0xE5, 0xAE, 0x9D]).decode("utf-8")]
_FORBIDDEN_CI = ["code" + "buddy", "work" + "buddy"]

SKILL_DIRS = [
    ROOT / "video-router",
    ROOT / "code-video" / "explainer",
    ROOT / "edit-video" / "talking-head",
]

SKIP_PARTS = {"node_modules", ".git", "tmp-render", "qa-frames", "renders", "release"}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def validate_skill_frontmatter() -> None:
    for d in SKILL_DIRS:
        skill = d / "SKILL.md"
        if not skill.exists():
            fail(f"missing {skill.relative_to(ROOT)}")
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---"):
            fail(f"{skill.relative_to(ROOT)} must start with frontmatter")
        parts = text.split("---", 2)
        if len(parts) < 3:
            fail(f"{skill.relative_to(ROOT)} invalid frontmatter")
        fm = yaml.safe_load(parts[1])
        if not isinstance(fm, dict):
            fail(f"{skill.relative_to(ROOT)} frontmatter not a mapping")
        name = fm.get("name")
        desc = fm.get("description")
        if not name or not desc:
            fail(f"{skill.relative_to(ROOT)} needs name and description")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(name)):
            fail(f"name {name!r} must be kebab-case")
        if str(name) != d.name:
            fail(f"name {name!r} must match folder {d.name}")
        if len(str(desc)) > 1024:
            fail(f"{skill.relative_to(ROOT)} description exceeds 1024 chars")
        if len(str(desc)) > 500:
            print(f"WARN: {skill.relative_to(ROOT)} description length {len(str(desc))} > 500")
        print(f"OK skill frontmatter: {d.relative_to(ROOT)} ({name})")


def validate_openai_yaml() -> None:
    for d in SKILL_DIRS:
        path = d / "agents" / "openai.yaml"
        if not path.exists():
            fail(f"missing {path.relative_to(ROOT)}")
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        iface = (data or {}).get("interface") or {}
        for key in ("display_name", "short_description", "default_prompt"):
            if key not in iface:
                fail(f"{path.relative_to(ROOT)} missing interface.{key}")
        print(f"OK openai.yaml: {path.relative_to(ROOT)}")


def validate_examples_fiction_mark() -> None:
    md_files = [
        p
        for p in ROOT.glob("**/examples/**/*")
        if p.is_file() and p.suffix.lower() in {".md", ".txt"}
    ]
    if not md_files:
        fail("no examples markdown found")
    for p in md_files:
        text = p.read_text(encoding="utf-8")
        if "虚构示例" not in text:
            fail(f"{p.relative_to(ROOT)} must contain 虚构示例")
        print(f"OK fiction mark: {p.relative_to(ROOT)}")


def validate_triggers() -> None:
    for skill in ("video-router", "explainer", "talking-head"):
        base = ROOT / "tests" / "triggers" / skill
        for name in ("should-trigger.txt", "should-not-trigger.txt"):
            path = base / name
            if not path.exists():
                fail(f"missing {path.relative_to(ROOT)}")
            lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
            if len(lines) != 10:
                fail(f"{path.relative_to(ROOT)} must have exactly 10 lines, got {len(lines)}")
        print(f"OK triggers: {skill} 10+10")


def _line_at(text: str, idx: int) -> str:
    start = text.rfind("\n", 0, idx) + 1
    end = text.find("\n", idx)
    if end < 0:
        end = len(text)
    return text[start:end]


def validate_forbidden_words() -> None:
    exts = {".md", ".yml", ".yaml", ".txt", ".py", ".sh", ".html", ".css", ".js", ".json"}
    patterns = [re.compile(re.escape(w), re.IGNORECASE) for w in _FORBIDDEN_CI]
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in exts and path.name not in {"LICENSE", "NOTICE"}:
            continue
        # skip this validator's own source (assembles banned tokens without spelling them)
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for word in _FORBIDDEN_LITERAL:
            if word in text:
                fail(f"forbidden word in {path.relative_to(ROOT)}")
        for pat in patterns:
            m = pat.search(text)
            if m:
                line = _line_at(text, m.start())
                fail(
                    f"forbidden product-name token in {path.relative_to(ROOT)}: "
                    f"{line.strip()[:120]}"
                )
    print("OK forbidden-word scan")


def main() -> None:
    validate_skill_frontmatter()
    validate_openai_yaml()
    validate_examples_fiction_mark()
    validate_triggers()
    validate_forbidden_words()
    print("All CI content checks passed.")


if __name__ == "__main__":
    main()
