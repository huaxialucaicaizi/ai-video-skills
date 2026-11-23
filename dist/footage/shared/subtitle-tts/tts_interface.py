#!/usr/bin/env python3
"""TTS interface stub for ai-video-skills.

配音引擎等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入。
第一版请优先使用 mode='subtitles_only'。
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


class TTSMode(str, Enum):
    SUBTITLES_ONLY = "subtitles_only"
    PRESET_VOICE = "preset_voice"
    CLONE_SELF = "clone_self"


@dataclass
class TTSRequest:
    text: str
    mode: TTSMode = TTSMode.SUBTITLES_ONLY
    voice_id: Optional[str] = None  # preset id; clone_self 时指向用户自有样本
    out_wav: Optional[Path] = None


@dataclass
class TTSResult:
    ok: bool
    mode: TTSMode
    message: str
    audio_path: Optional[Path] = None


def synthesize(req: TTSRequest) -> TTSResult:
    """Synthesize speech or acknowledge subtitles-only.

    Non-subtitle modes are intentionally unimplemented until Mac bake-off.
    """
    if req.mode == TTSMode.SUBTITLES_ONLY:
        return TTSResult(
            ok=True,
            mode=req.mode,
            message="只出字幕、不配音（第一版默认）。",
            audio_path=None,
        )

    if req.mode == TTSMode.CLONE_SELF and not req.voice_id:
        return TTSResult(
            ok=False,
            mode=req.mode,
            message="clone_self 需要用户提供自己的声音样本标识；禁止克隆他人声音。",
        )

    return TTSResult(
        ok=False,
        mode=req.mode,
        message=(
            "配音尚未接入：等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入。"
            "请改用 mode=subtitles_only，或等待默认引擎选定。"
        ),
        audio_path=None,
    )


if __name__ == "__main__":
    r = synthesize(TTSRequest(text="虚构示例", mode=TTSMode.SUBTITLES_ONLY))
    print(r)
    r2 = synthesize(TTSRequest(text="虚构示例", mode=TTSMode.PRESET_VOICE))
    print(r2)
