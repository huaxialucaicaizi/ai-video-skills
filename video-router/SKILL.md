---
name: video-router
description: "用户想做办公视频但还没选风格时用：最多问 3 个问题，按 10 种风格路由到 explainer / data-story / promo / animation / talking-head / footage / clip-long / screencast；数字人拒绝，表外类型「暂不支持」，并检查 Mac 剪辑环境（含 ffmpeg）。Use when someone wants an office video but has not picked a style; asks at most three questions and routes across the ten styles."
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
3. **按路由表分流**（见 `references/route-table.md`）：
   - 知识科普 / PPT课件 → `explainer`（`dist/explainer/`）
   - 数据动画 → `data-story`（`dist/data-story/`）
   - 宣传片 / 金句快闪 → `promo`（`dist/promo/`）
   - 动画短片/MV → `animation`（`dist/animation/`）
   - AI/科技口播 → `talking-head`（`dist/talking-head/`）
   - 实拍探店/Vlog/开箱/带货 → `footage`（`dist/footage/`）
   - 长视频切片 → `clip-long`（`dist/clip-long/`）
   - 软件教程录屏 → `screencast`（`dist/screencast/`）
   - 数字人等红线项 → 拒绝；表外类型 →「暂不支持」
4. **环境检查（Mac）**：运行 `../scripts/doctor.sh`（仓库内）或安装包内的 `./doctor.sh`（检查 Node.js、**ffmpeg**、Python 等）。缺什么指给 setup-doctor（ai-from-zero）。
5. **若目标 skill 未安装**：不要假装已交接。明确提示用户安装对应 `dist/<skill>/`（见路由表与 README「安装（Mac）」）；建议一次装齐（router 只负责分流）。
6. **输出**：选定的子 skill + 一句理由 + 缺失环境清单；或「暂不支持」+ 归属类型说明。

## 交付时讲理由

交付路由结果后，用一两句话说明最关键的一个选择为什么这样做。

## 相关

- 路由细则：`references/route-table.md`
- 环境脚本（仓库）：`../scripts/doctor.sh`
- 安装：请复制 `dist/video-router/`（由 `scripts/build_dist.py` 生成）；推荐一次装齐全部 `dist/` 包
