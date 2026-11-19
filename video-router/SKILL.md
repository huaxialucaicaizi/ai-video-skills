---
name: video-router
description: "用户想做或剪一条视频、但还没说清是知识科普还是口播时用：最多问 3 个问题，判断走 explainer 还是 talking-head；其他视频类型明确回复「暂不支持」，并顺便检查 Mac 剪辑环境（含 ffmpeg）。不生成真人画面。 Use when someone wants a video but has not chosen between a code-generated explainer and a talking-head edit. Asks at most three questions, routes to explainer or talking-head, replies「暂不支持」for other types, and checks the Mac video toolchain. Does not generate human footage."
---

# video-router

学习路径位置：**用进工作**（办公视频入口）。目前仅支持 **Mac**。

## 红线

1. 产品界面只用真实截图或录屏，不用代码画假界面
2. 不生成真人画面，不模仿他人声音
3. 剪映操作步骤要实测，标注剪映版本号
4. 新闻截图标来源
5. 对外只承诺「一句话出一条能用的办公视频」
6. 字体只用免费商用字体（思源黑体 / Noto Sans SC 等 OFL）
7. 不采用数字人方案

## 工作流

1. **用户给什么**：一句话需求 + 有没有素材（口播视频 / 录屏 / 只有主题或讲稿）
2. **最多问 3 个问题**（见 `references/route-table.md`）：
   - 有没有拍好的真人/录屏素材？
   - 要科普讲解还是口播剪辑？
   - 横竖屏与大致时长？
3. **只分两类**：
   - 无真人素材、要知识科普/图解/课件风 → 交给 `explainer`（安装包：`dist/explainer/`）
   - 有真人口播/讲解录屏要剪 → 交给 `talking-head`（安装包：`dist/talking-head/`）
   - 其他（数据动画、宣传片、Vlog、长视频切片等）→ 明确回复「暂不支持」
4. **环境检查（Mac）**：运行 `../scripts/doctor.sh`（仓库内）或安装包内的 `./doctor.sh`（检查 Node.js、**ffmpeg**、Python 等）。缺什么指给 setup-doctor（ai-from-zero）。
5. **若目标 skill 未安装**：不要假装已交接。明确提示用户去安装对应 dist 包——科普装 `dist/explainer/`，口播装 `dist/talking-head/`——步骤见仓库 README「安装（Mac）」一节；并建议三个包一起装（router 只负责分流）。
6. **输出**：选定的子 skill + 一句理由 + 缺失环境清单；或「暂不支持」+ 归属类型说明。

## 交付时讲理由

交付路由结果后，用一两句话说明最关键的一个选择为什么这样做。

## 相关

- 路由细则：`references/route-table.md`
- 环境脚本（仓库）：`../scripts/doctor.sh`
- 安装：请复制 `dist/video-router/`（由 `scripts/build_dist.py` 生成的自包含包）；推荐同时安装 `dist/explainer/` 与 `dist/talking-head/`
