---
name: data-story
description: "用户要把表格或指标做成数据动画短视频时用：读入 CSV/指标，套风格卡，用 HyperFrames 生成柱/折线动画与字幕，逐帧自检后导出。不编造真实业务数据；示例数据必须在画面标明「示例数据」。Use when someone wants a short data-motion video from a CSV or metrics. Builds HyperFrames bar/line animations with captions; sample data must be labelled 示例数据 on screen."
---

# data-story

学习路径位置：**用进工作**。路线：**代码生成**（全自动）。目前仅支持 **Mac**（云端可冒烟；正式验收待 Mac 实测）。

## 红线

1. 不编造真实业务 KPI；虚构/演示数据必须在画面标明「示例数据」
2. 产品界面只用用户真实截图；没有就留白
3. 字体只用免费商用字体（模板内 `./fonts/` + OFL）
4. 不生成真人画面、不用数字人

## 工作流

1. 收束 brief：要讲清的 1 个数据结论、时长、横竖屏
2. 确认数据来源：用户 CSV 或明确标注的示例数据
3. 套风格卡（`shared/styles/`）→ 基于 `templates/short-data-story/` 生成画面
4. 字幕默认只出字幕不配音（配音待 Mac 实测）
5. 逐帧自检后导出 MP4

短模板：`templates/short-data-story/`（含虚构 CSV，画面带「示例数据」角标）。
