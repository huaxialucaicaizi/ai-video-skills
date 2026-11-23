# 风格卡 SCHEMA

PPT 下周沿用同一格式。字段以本文件为准；`shared/styles/*.yaml` 必须能被解析且含下列键。

## 必填字段

```yaml
id: clean-office                 # kebab-case，与文件名一致
name: 清爽办公                   # 中文显示名
version: 1
palette:
  primary: "#……"                 # 约 60%
  secondary: "#……"               # 约 30%
  accent: "#……"                  # 约 10%
  background: "#……"
  text: "#……"
fonts:
  display: 思源黑体 / Noto Sans SC   # 须免费商用；仓库内附 OFL
  body: 思源黑体 / Noto Sans SC
typography:
  min_body_px: 32                # 1080 宽竖屏：正文 / 标签 / 代码 ≥ 32
  min_label_px: 32
  min_code_px: 32
  min_subtitle_px: 48            # 字幕 ≥ 48
layout:
  safe_margin_x_px: 80           # 左右安全区（1080 竖屏建议）
  safe_margin_y_px: 160          # 上下安全区
  safe_margin_px: 64             # 兼容旧字段：若未写 x/y，用此值四边
  grid: 12-col
  radius_px: 0                   # 明确写，避免默认「AI 味」大圆角
motion:
  enter: fade-up                 # 入场
  emphasis: punch-number         # 强调
  easing: power3.out             # GSAP / 等价缓动名
  enter_overshoot: true          # 带回弹的出场（对标第 2 轮 Remotion 流畅度）
  typewriter: optional           # 逐字打出：代码块等场景可用
  progress_follows_brief: true   # 进度条等计时元素按 brief 时间点走完
graphics:
  language: 扁平色块 + 细线图标
charts:
  style: 简洁柱/折线，无 3D
forbidden:
  - 默认紫色渐变
  - 满屏 emoji
  - 每页三卡片套路
```

## 使用规则

1. explainer / overlays 套卡前先读对应 yaml，再读对应 yaml 注释与本包风格说明。
2. 渲染全程用项目内字体文件，不从 Google Fonts / jsDelivr 拉字体。
3. GSAP 用 npm 本地安装，不从 CDN 加载（国内网络不稳定）。
4. 选卡后交付时用一两句话说明为什么选这张卡。
