---
name: explainer
description: "用户要做 vibe 知识科普、动态图解、课件或把大纲/讲稿做成短视频时用：拆分镜、套风格卡用 HyperFrames（HTML）生成全部画面与字幕（可选配音），逐帧截图自检后导出。不生成真人画面；产品界面只用用户提供的真实截图。 Use when someone wants a vibe-style knowledge explainer, animated diagram, or lesson-style short video from a topic or script. Storyboards one idea per shot, applies a style card, generates frames in code with captions (optional TTS), samples frames for QA, and exports. No synthetic human footage; product UI only from user screenshots."
---


# explainer

学习路径位置：**用进工作**。底层渲染：**HyperFrames**（官方文档为准）。目前仅支持 **Mac**（云端可做开发自检，正式验收待 Mac 实测）。

## 红线

1. 产品界面只用真实截图或录屏，不用代码画假界面
2. 不生成真人画面，不模仿他人声音
3. 字体只用免费商用字体（本包模板内 `templates/short-explainer/fonts/`（含 OFL.txt））
4. GSAP、字体均本地打包，渲染不依赖外网 CDN
5. 不承诺达到某个模型的画面水平；承诺「一句话出一条能用的办公视频」
6. HyperFrames 渲染结束后终端可能显示其桌面 App 推广文字——**只在终端，不进视频**；向用户说明即可

## 工作流

1. **收束 brief**：受众、要讲清的 1 个核心问题、时长（默认约 30 秒 vibe 科普可调）、横竖屏
2. **拆分镜**：每镜一个观点；画面类型（标题卡 / 步骤卡 / 图解卡 / 数据卡 / 金句卡）+ 字幕文案 → 见 `references/storyboard.md`
3. **套风格卡**：从 `shared/styles/` 选 1 张（`clean-office` 或 `chalk-explain`），说明为什么 → `references/style-usage.md`
4. **代码生成画面**：基于 `templates/` 的 HyperFrames HTML；复用 `shared/overlays/`；无真实截图则留白提醒
5. **字幕 / 配音**：默认 SRT（`shared/subtitle-tts`）；配音可选，第一版推荐「只出字幕、不配音」；其他模式标「等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入」
6. **逐帧截图自检**：每个镜头至少 1 帧；**必须真的打开看图**——查文字溢出、叠字、安全区、黑帧
7. **输出**：MP4 + SRT + 分镜表 + 自检截图目录 + 一句关键选择理由

## 模板

短示例模板：`templates/short-explainer/`（本地 `npm install` 后 `npx hyperframes render`）。

## 交付时讲理由

例如：「我选了 clean-office，因为受众是职场同事，深色办公风比黑板风更合适。」

## 安装包说明

本目录是 CI/`scripts/build_dist.py` 生成的**自包含安装包**。请整夹复制到各工具的 skills 目录；不要手改 `dist/`，改源码后重新运行构建脚本。
