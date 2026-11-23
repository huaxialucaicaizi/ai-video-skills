---
name: clip-long
description: "用户要把长视频切成短片段时用：转写→挑高光时间码→ffmpeg 剪切→竖屏再构图→字幕。半自动；引擎效果待 Mac 实测。Use to turn long videos into clips: transcript → highlight timestamps → ffmpeg cuts → vertical reframe → captions."
---

# clip-long

学习路径位置：**用进工作**。路线：**古法剪辑**（半自动）。目前仅支持 **Mac**。转写/再构图全流程：**待 Mac 实测**。

## 红线

1. 只用用户提供的长视频；不生成画面
2. 不把未授权整片公开进仓库
3. 未实测步骤标「待 Mac 实测」

## 工作流

1. **转写**带时间戳（引擎待 Mac 实测）
2. **挑高光**：每条给起止时间与理由 → `references/highlight-picking.md`
3. **ffmpeg 剪切**草案 → `references/ffmpeg-clips.md`
4. **竖屏再构图**策略（居中/跟脸，待 Mac 实测）
5. **字幕** SRT 草稿
