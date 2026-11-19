# shared/subtitle-tts

字幕与配音共用模块。第一版：**字幕可交付**；**配音只留接口与选项**，等 Mac 实测后再接入默认引擎。

## 字幕（本周可用）

- 输出格式：SRT（UTF-8）
- 默认：每个镜头一句总结字幕，落在安全区内；1080 竖屏字幕字号 ≥ 48px（见风格卡 `typography.min_subtitle_px`）
- 工具脚本：`srt.py`（把带时间戳的字幕条目写成 `.srt`）

## 配音（接口预留）

默认选型**尚未选定**。流程已定：在 **Mac** 上用同一段中文稿实测 **Qwen3-TTS（优先 0.6B-CustomVoice）** 与 **CosyVoice**，比较效果与速度后定默认。

| 选项 | 说明 | 状态 |
| --- | --- | --- |
| `subtitles_only` | 只出字幕、不配音 | **第一版默认可用** |
| `preset_voice` | 预置音色配音 | 待 Mac 实测后接入 |
| `clone_self` | 仅允许用户克隆**自己的**声音 | 待 Mac 实测后接入；禁止克隆他人 |

实现入口：`tts_interface.py` 中的 `TTSRequest` / `synthesize()`。当前 `synthesize()` 在非 `subtitles_only` 时返回明确错误，提示「等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入」。

## 红线

- 不模仿他人声音；不生成真人画面
- 不采用数字人方案
- 许可证以各模型官方模型卡为准（核实过的摘要见仓库 README「依赖」）
