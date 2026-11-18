# 如何套风格卡

1. 读 `shared/styles/SCHEMA.md`，再读目标 yaml（如 `clean-office.yaml`）。
2. 把 `palette` 写成 CSS 变量；`radius_px`、安全区、最小字号全部落地，不要「大约」。
3. `motion`：入场用 fade-up + 风格卡 easing；需要强调时用 punch-number；进度条按 brief 时间走完（`progress_follows_brief`）。
4. 避开 `forbidden` 列表（紫色渐变、满屏 emoji、每页三卡片套路等）。
5. 交付时写一句选卡理由。

| 卡 | 适合 |
| --- | --- |
| clean-office | 职场同事、工具科普、偏正式 |
| chalk-explain | 课堂感、概念入门、轻松讲解 |
