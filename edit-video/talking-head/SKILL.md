---
name: talking-head
description: "用户有真人口播或讲解录屏、要剪 AI/科技/工具类口播时用：带时间戳转写，去口癖、停顿和重复，标出需要 B-roll 的位置并用 overlays 模板生成，叠上字幕，逐帧截图自检后导出，并给出剪映精修清单。不生成真人画面，不模仿他人声音；产品界面只用用户提供的真实截图。 Use when someone has a talking-head or tool-demo recording to edit for AI/tech explainers. Transcribes with timestamps, removes fillers and repeats, marks and generates B-roll from overlay templates, overlays captions, checks sampled frames, exports, and hands over a CapCut (JianYing) polish checklist. No synthetic humans or cloned third-party voices."
---


# talking-head

学习路径位置：**用进工作**。本周范围：AI / 科技 / 工具类口播粗剪。**独立设计**，不基于、不拷贝任何既有热点口播 skill 仓库内容。目前仅支持 **Mac**。

## 红线

1. 不生成真人画面；真人画面只用用户自己的素材
2. 不模仿他人声音；不采用数字人
3. 产品界面只用用户真实截图或录屏
4. 剪映步骤须实测并标注版本——未实测处写「待 Mac 实测」
5. 测试口播只在本地跑，不把自愿样片放进仓库；公开示例仅用授权清楚的 CC BY 等并注明出处（没有就不放）

## 工作流

1. **转写**：带时间戳转写，输出逐字稿，先给用户确认错字（引擎候选：faster-whisper / SenseVoice；中文效果待 Mac 实测）
2. **去口癖、停顿和重复**：嗯、啊、那个；过长停顿；重复句；列出删减供确认（阈值阈值待 Mac 实测）
3. **标 B-roll 位置**：产品名、数字、步骤、新概念；每处标时间与理由 → `references/broll-rules.md`
4. **套 overlays**：复用 `shared/overlays/` 概念 / 步骤 / 数据 / 截图卡
5. **叠层与导出**：真人底层 + B-roll + 字幕；底层渲染用 HyperFrames（待与素材路径在 Mac 实测打通）
6. **逐帧自检**：剪辑点与每张卡片都截图并打开核对
7. **剪映精修清单**：`references/jianying-checklist.md`（步骤待 Mac 实测后补版本号）

详见 `references/workflow.md`。

## 交付时讲理由

例如：「产品名出现的三处我都标了截图卡，因为观众需要立刻认出你说的是哪个界面。」
