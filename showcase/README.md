# showcase/（开发中，Claude）

10 种风格成品样片的工作目录，给 Rui 录教程「成品展示」用；做好后再把手法沉淀回各 skill 的模板。

- `kit/`：共享动效套件（背景、逐字遮罩出现、卡片、画线、计数、转场、标记笔）。本地字体 + 本地 GSAP，不连外网
- `explainer/`：知识科普样片「什么是 AI Agent」，30 秒，6 个镜头（已渲染自检）

渲染：把 `kit/` 复制进样片目录（HyperFrames 不允许 `../` 引用），`npm install` 后
`npx hyperframes render --output ./renders/<name>.mp4 --workers 4`

参考与禁用清单见 ai-skills-hq/交接/ai-video-skills-开发交接.md。
