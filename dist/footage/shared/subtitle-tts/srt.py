#!/usr/bin/env python3
"""Write UTF-8 SRT from timed caption entries."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Caption:
    start_s: float
    end_s: float
    text: str


def _ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, milli = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{milli:03d}"


def captions_to_srt(captions: list[Caption]) -> str:
    lines: list[str] = []
    for i, c in enumerate(captions, start=1):
        text = " ".join(c.text.strip().split())
        lines.append(str(i))
        lines.append(f"{_ts(c.start_s)} --> {_ts(c.end_s)}")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


def write_srt(path: str | Path, captions: list[Caption]) -> Path:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(captions_to_srt(captions), encoding="utf-8")
    return out


if __name__ == "__main__":
    demo = [
        Caption(0.0, 3.0, "虚构示例：开场字幕"),
        Caption(3.0, 6.0, "虚构示例：第二句"),
    ]
    print(captions_to_srt(demo))
