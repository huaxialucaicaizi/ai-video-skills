<a id="top"></a>

<div align="center">

# AI Video Skills · AI 视频 Skill

**面向 10 种办公视频风格的 AI 视频 skill 仓库：用「代码生成」和「古法剪辑」两条 AI 剪辑路径，实现全自动或半自动的视频剪辑。**<br>
AI video skills for 10 office video styles, built on two AI editing paths, code-generated and traditional editing, for fully or semi-automated video editing.

[中文](#zh) | [English](#en)

</div>

---

<a id="zh"></a>

## 中文

### 目录
- [一句话介绍](#zh-intro)
- [学习路径](#zh-path)
- [核心思路](#zh-idea)
- [完整仓库结构](#zh-structure)
- [10 种视频怎么分](#zh-types)
- [口播按 B-roll 来源分 6 种](#zh-broll)
- [本版已交付 skill](#zh-skills)
- [安装（Mac）](#zh-install)
- [Mac 实测状态](#zh-mac)
- [HyperFrames](#zh-hyperframes)
- [配音](#zh-voiceover)
- [红线（摘要）](#zh-guardrails)
- [公开示例与素材](#zh-samples)
- [开发与 CI](#zh-ci)
- [作者](#zh-author)
- [许可证](#zh-license)

<a id="zh-intro"></a>
### 一句话介绍

面向 10 种办公视频风格的 AI 视频 skill 仓库：用「代码生成」和「古法剪辑」两条 AI 剪辑路径，实现全自动或半自动的视频剪辑。本版已交付全部 10 种风格对应 skill（见「10 种视频怎么分」与「本版已交付 skill」）；客户端触发与部分半自动合成步骤仍标「待 Mac 实测」。底层渲染默认 **HyperFrames**（[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)，以[官方文档](https://hyperframes.heygen.com/introduction)为准）。许可证 **Apache-2.0**。

**目前仅支持 Mac。** 云端可用于开发自检；凡标注「待 Mac 实测」的条目，不以 Linux 结果冒充已验收。部分项已在 iMac 实测，见下方「Mac 实测状态」。

![知识科普模板实际渲染截图（虚构示例内容）](assets/readme/explainer-frames.png)

*知识科普模板实际渲染截图（虚构示例内容）*

<a id="zh-path"></a>
### 学习路径

```
知道看什么 → 会提问 → 装上工具 → 做出作品 → 【用进工作】→ 做自己的 skill
                                              ▲
                                   本仓库（视频）挂在这里
```

PPT / 数据分析 / 设计等同挂在「用进工作」下的其他仓库。

<a id="zh-idea"></a>
### 核心思路

10 种风格分别走两条 AI 剪辑路径：代码生成、古法剪辑（软件教程录屏为两者混合）：

| 路线 | 说明 | 自动化 |
| --- | --- | --- |
| 代码生成 | 图形、文字、数据、界面由代码生成 | 全自动 |
| 古法剪辑 | 真人、实物、现场用用户素材；AI 粗剪 + 剪映精修 | 半自动 |
| 混合 | 古法剪主线，代码生成的包装件和 B-roll 叠上去 | 半自动 |

<a id="zh-structure"></a>
### 完整仓库结构

```
ai-video-skills/
├── video-router/           ✅ 本版：按 10 种风格分流
├── code-video/
│   ├── explainer/          ✅ 知识科普 / PPT课件转视频
│   ├── data-story/         ✅ 数据动画（示例数据须标注）
│   ├── promo/              ✅ 产品宣传片 + 文字快闪/金句卡
│   └── animation/          ✅ 动画短片 / MV 风
├── edit-video/
│   ├── talking-head/       ✅ AI / 科技 / 工具类口播
│   ├── footage/            ✅ 探店 / Vlog / 开箱 / 带货实拍
│   ├── clip-long/          ✅ 长视频切片
│   └── screencast/         ✅ 软件教程录屏（混合）
├── shared/
│   ├── subtitle-tts/       ✅ 字幕 SRT；配音接口预留
│   ├── overlays/           ✅ 概念 / 步骤 / 数据 / 截图 + screencast
│   └── styles/             ✅ SCHEMA + 2 张风格卡
├── dist/                   ✅ 各 skill 自包含安装包
├── examples/
├── tests/
└── scripts/
```

图例：✅ 本版已交付 skill / 模板或流程文档。客户端触发与部分合成步骤仍标「待 Mac 实测」。

<a id="zh-types"></a>
### 10 种视频怎么分

来源：框架稿第 1 节。本版 10 种均已交付对应 skill；标 ✅。客户端触发 / 实拍合成等仍「待 Mac 实测」的，见下方 Mac 实测表与各 skill 正文。

| 视频类型 | 路线 | 交给谁 | 自动化程度 | 状态 |
| --- | --- | --- | --- | --- |
| 知识科普 / 动态图解 | 代码生成 | `code-video/explainer` | 全自动 | ✅ |
| 数据动画 | 代码生成 | `code-video/data-story` | 全自动 | ✅ |
| 产品宣传片 | 代码生成 | `code-video/promo` | 全自动（产品界面只用真实截图或录屏；否则「示例」占位） | ✅ |
| 文字快闪 / 金句卡 | 代码生成 | `code-video/promo` | 全自动 | ✅ |
| 动画短片 / MV | 代码生成 | `code-video/animation` | 全自动（默认可静音；无版权音乐） | ✅ |
| PPT / 课件转视频 | 代码生成 | `code-video/explainer` | 全自动 | ✅ |
| 口播 / 真人出镜 | 古法剪辑 | `edit-video/talking-head` | 半自动：AI 粗剪 + 剪映精修 | ✅（本版仅 AI/科技/工具类） |
| 实拍（Vlog、探店、开箱、带货） | 古法剪辑 | `edit-video/footage` | 半自动（流程待 Mac 实测） | ✅ |
| 长视频切片 | 古法剪辑 | `edit-video/clip-long` | 半自动（流程待 Mac 实测） | ✅ |
| 软件教程录屏 | 混合 | `edit-video/screencast` | 半自动（叠层合成待 Mac 实测） | ✅ |

`video-router`：按上表 10 种分流；数字人拒绝；表外类型回复「暂不支持」。

<a id="zh-broll"></a>
### 口播按 B-roll 来源分 6 种

| 口播类型 | B-roll 从哪来 | 自动化程度 | 状态 |
| --- | --- | --- | --- |
| AI / 科技 / 工具类 | B-roll 大多用代码生成 | 基本全自动 | ✅ |
| 知识讲解 | B-roll 用代码生成 | 全自动 | 🔜 |
| 新闻资讯 | 代码生成 + 新闻截图标来源 | 全自动 | 🔜 |
| 观点 / 职场 / 情感 | 重点在字幕节奏和金句卡 | 粗剪 + 用户精修 | 🔜 |
| 测评 / 带货 | 用户实拍 + 代码做价格卡和对比表 | 半自动 | 🔜 |
| 访谈 / 对谈 | 多机位切换 | 古法为主 | 🔜 |

<a id="zh-skills"></a>
### 本版已交付 skill

| Skill | 路径 | 使用场景 | 做什么 |
| --- | --- | --- | --- |
| **Video-router · 视频入口** | `video-router/` | 还没选风格，先分流并检查环境 | 按 10 种风格路由；数字人拒绝；表外「暂不支持」 |
| **Explainer · 知识科普** | `code-video/explainer/` | 主题 / 大纲 / 课件 → 无真人出镜科普短视频 | HyperFrames 模板 + 风格卡 + 字幕 + 逐帧自检 |
| **Data-story · 数据动画** | `code-video/data-story/` | CSV / 指标做成数据动画 | 短模板渲染；画面须标「示例数据」 |
| **Promo · 宣传片/金句** | `code-video/promo/` | 产品宣传片或文字快闪 / 金句卡 | 两套模板；界面用真实截图或「示例」占位 |
| **Animation · 动画短片** | `code-video/animation/` | 动画短片 / MV 风节拍动画 | 形状+文字节拍模板；默认可静音 |
| **Talking-head · AI/科技口播** | `edit-video/talking-head/` | 真人口播要 AI/科技/工具类粗剪 | 转写 → 去口癖 → B-roll → overlays → 剪映清单 |
| **Footage · 实拍粗剪** | `edit-video/footage/` | 探店 / Vlog / 开箱 / 带货实拍 | 镜头表、ffmpeg 粗剪列表、字幕、剪映清单 |
| **Clip-long · 长视频切片** | `edit-video/clip-long/` | 长视频切短、竖屏再构图 | 转写 → 高光时间码 → ffmpeg → 字幕 |
| **Screencast · 软件教程** | `edit-video/screencast/` | 软件录屏教程要步骤/放大/键盘提示 | 混合：录屏主线 + overlays |

共享模块：`shared/overlays/`、`shared/styles/`、`shared/subtitle-tts/`（配音接口预留，待 Mac 实测）。

**本版不做：** 数字人方案、Windows。

<a id="zh-install"></a>
### 安装（Mac）

`dist/` 由 `scripts/build_dist.py` 按显式清单生成并带齐依赖；每个包含 `LICENSE` 与 `NOTICE`；**不要手改 `dist/`**，改源码后重新运行构建脚本再提交。**推荐一次装齐全部 `dist/` 包**（router 只分流，单独装用不起来）。

#### 三个包的关系

| 包 | 做什么 | 依赖 |
| --- | --- | --- |
| `dist/video-router/` | 按 10 种风格分流；不渲染 | 单独用不起来 |
| `dist/explainer/` | 知识科普 / 课件（含模板与字体） | 可独立渲染 |
| `dist/data-story/` | 数据动画模板（示例数据角标） | 可独立渲染 |
| `dist/promo/` | 宣传片 + 金句快闪两套模板 | 可独立渲染 |
| `dist/animation/` | 动画短片 / MV 风模板 | 可独立渲染 |
| `dist/talking-head/` | AI/科技口播流程（无渲染字体） | 流程文档 |
| `dist/footage/` | 实拍半自动粗剪 | 流程文档 |
| `dist/clip-long/` | 长视频切片 | 流程文档 |
| `dist/screencast/` | 软件教程 overlays | 流程文档 |

#### 主路径：Claude 桌面版（上传 zip）

1. 生成三个 zip（或手动把 `dist/` 下三个文件夹分别打成 zip；不要只贴 `SKILL.md`）：

```bash
make release
# → release/<skill>.zip（共 9 个：router + 8 个子 skill）
```

2. 打开 **Claude 桌面版**，进入 Skills（技能）相关设置。
3. 分别上传上述 zip，并启用它们。
4. 菜单文案以你本机 Claude 桌面版为准（不同版本可能略有差异）；若找不到上传入口，改用下方「次路径」或查阅 Claude 当前帮助文档。

上传后可用这句话测 **Explainer** 是否触发（选自 `tests/triggers/explainer/should-trigger.txt`）：

> 做一条 vibe 知识科普短视频

（各客户端触发结果仍标「待 Mac 实测」。）

#### 次路径：Claude Code / 其他工具（复制文件夹）

把 `dist/<name>/` **整夹**复制到对应 skills 目录（不要直接拷嵌套源码目录）：

| 工具 | 目标目录 |
| --- | --- |
| Claude Code | 项目级 `.claude/skills/<name>/`，或用户级 `~/.claude/skills/<name>/` |
| Codex | 项目级 `.agents/skills/<name>/`，或用户级 `~/.agents/skills/<name>/` |
| DeepSeek Harness | 项目级 `.dsh/skills/<name>/` 或 `.agents/skills/<name>/`，或用户级 `~/.dsh/skills/<name>/` |

`<name>` 为 `explainer` / `talking-head` / `video-router`。DeepSeek Harness 主要扫描技能根下一层目录，因此必须用扁平的 `dist/<name>/`。

```bash
# Claude Code 示例（项目根）：复制全部 dist 包
mkdir -p .claude/skills
for d in dist/*/; do
  name="$(basename "$d")"
  [[ -f "$d/SKILL.md" ]] || continue
  cp -R "$d" ".claude/skills/$name"
done
```

#### 装好后渲染示例（explainer）

在**已安装的** skill 目录内（例如 Claude Code 项目 `.claude/skills/explainer/`，或从 zip 解压后的 explainer 包内）：

```bash
./doctor.sh
cd templates/short-explainer
npm install
npm run render
# → ./renders/short-explainer.mp4
```

#### 环境与 Node

仓库内也可直接跑环境检查（含 **ffmpeg**）：

```bash
./scripts/doctor.sh
```

`doctor.sh` 已在 iMac 实测通过（`pass=7 fail=0 warn=0`）。详见 [`tests/mac/2026-11-18-imac.md`](tests/mac/2026-11-18-imac.md)。

Node 版本（分工具报告，不要合成一条）：

- HyperFrames / 常见 Claude Code npm 路径：Node.js **22+**
- DeepSeek Harness：Node.js **>=24.9.0**（以 npm 包 `@deepseek-ai/dsh` 的 `engines` 为准；2026-11-18 查询版本 `0.2.2-rc.1`）

各客户端触发实测：**待 Mac 实测**（此前测试机未装 Claude 桌面版 / Claude Code / Codex / DeepSeek Harness）。

<a id="zh-mac"></a>
### Mac 实测状态

记录：[`tests/mac/2026-11-18-imac.md`](tests/mac/2026-11-18-imac.md)（iMac · Apple M4 · 16GB · macOS 27.0.1 · head `e1398bb`）

| 项 | 状态 |
| --- | --- |
| `scripts/doctor.sh` | ✅ 已实测 — [记录](tests/mac/2026-11-18-imac.md) |
| `short-explainer` 渲染（9s） | ✅ 已实测 — [记录](tests/mac/2026-11-18-imac.md) |
| 截帧 1.5s / 4.5s / 7.5s 自查 | ✅ 已实测 — [记录](tests/mac/2026-11-18-imac.md) |
| Claude 桌面版 / Claude Code / Codex / DeepSeek Harness 触发 | 待 Mac 实测 |
| Qwen3-TTS vs CosyVoice | 待 Mac 实测 |
| 转写引擎与去口癖 | 待 Mac 实测 |
| talking-head 叠层导出 | 待 Mac 实测 |
| 剪映精修步骤与版本 | 待 Mac 实测 |
| 完整 30s explainer | 待 Mac 实测（仓库暂无 30s 模板） |
| 前后对比 | 待 Mac 实测 |

观察（不改代码）：竖屏里正文/卡片偏小、内容偏窄，建议 30s 完整版再放大。见实测记录。

<a id="zh-hyperframes"></a>
### HyperFrames

- 要求：Node.js 22+、系统 ffmpeg
- GSAP、字体均本地安装/打包，渲染不依赖外网 CDN
- 字体权威副本在 `shared/fonts/`（OFL）；构建脚本同步到模板 `templates/short-explainer/fonts/`，HTML 只用 `./fonts/`（无 `../` 越界）
- 渲染结束后，终端可能显示 HyperFrames 桌面 App 的推广文字——**只在终端，不进视频**
- 短示例模板：源码 `code-video/explainer/templates/short-explainer/`；安装请用 `dist/explainer/`（**已在 iMac 实测**：HyperFrames 0.9.66，9.0s / 1080×1920，见 [记录](tests/mac/2026-11-18-imac.md)）

```bash
# 开发（仓库内）
cd code-video/explainer/templates/short-explainer
npm install && npm run render

# 或按安装包
# cd path/to/skills/explainer/templates/short-explainer && npm install && npm run render
```

重新生成安装包：

```bash
python3 scripts/build_dist.py
```

<a id="zh-voiceover"></a>
### 配音

第一版默认 **只出字幕、不配音**。预置音色 / 自有声音克隆接口见 `shared/subtitle-tts/`；**等 Qwen3-TTS vs CosyVoice 在 Mac 实测后接入**（仍为待 Mac 实测）。

<a id="zh-guardrails"></a>
### 红线（摘要）

- 不生成真人画面；不模仿他人声音；不用数字人
- 产品界面只用真实截图或录屏
- 公开示例只用授权清楚的素材并注明出处；没有就不放
- 不编造数字和出处；查不到写「待核实」
- 剪映步骤未实测不写死路径（标「待 Mac 实测」）

<a id="zh-samples"></a>
### 公开示例与素材

当前仓库**不附带**第三方口播样片。若后续增加公开示例，仅使用 CC BY 等授权清楚、允许修改的素材，并在本 README 注明出处与协议。

<a id="zh-ci"></a>
### 开发与 CI

```bash
python3 -m pip install pyyaml
python3 scripts/ci_validate.py
```

CI：校验各 `SKILL.md` frontmatter、`agents/openai.yaml`、examples「虚构示例」、触发测试 10+10、禁用词扫描、`build_dist.py --check`、三包脱离仓库路径检查、`dist/explainer` 严格 lint（0 error）后再 render 冒烟、macOS 上跑仓库与各包内 `doctor.sh`。

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者。

<a id="zh-license"></a>
### 许可证

Apache License 2.0。见 `LICENSE` 与 `NOTICE`。

[↑ 返回顶部](#top)

---

<a id="en"></a>

## English

### Contents
- [In one sentence](#en-intro)
- [Learning path](#en-path)
- [Core idea](#en-idea)
- [Full repository layout](#en-structure)
- [Ten video types](#en-types)
- [Six talking-head subtypes by B-roll source](#en-broll)
- [Skills in this release](#en-skills)
- [Install (Mac)](#en-install)
- [Mac verification status](#en-mac)
- [HyperFrames](#en-hyperframes)
- [Voiceover](#en-voiceover)
- [Guardrails (summary)](#en-guardrails)
- [Public samples](#en-samples)
- [Development & CI](#en-ci)
- [Author](#en-author)
- [License](#en-license)

<a id="en-intro"></a>
### In one sentence

AI video skills for 10 office video styles, built on two AI editing paths, code-generated and traditional editing, for fully or semi-automated video editing. This release ships skills for all 10 styles (see [Ten video types](#en-types) and [Skills in this release](#en-skills)); client triggers and some semi-auto compositing steps remain To be tested on Mac. Default renderer: **HyperFrames** ([heygen-com/hyperframes](https://github.com/heygen-com/hyperframes); follow the [official docs](https://hyperframes.heygen.com/introduction)). License: **Apache-2.0**.

**Mac only for v1.** Cloud Linux may be used for smoke tests; items marked "To be tested on Mac" are not claimed as accepted. Some items are already verified on an iMac — see [Mac verification status](#en-mac) below.

![Actual frames rendered from the short-explainer template (fictional sample content)](assets/readme/explainer-frames.png)

*Actual frames rendered from the short-explainer template (fictional sample content)*

<a id="en-path"></a>
### Learning path

```
Know what to read → Ask better → Install tools → Ship a first build → [Use it at work] → Make your own skill
                                                                    ▲
                                                         This repo (video) sits here
```

PPT / data / design skills hang under the same "Use it at work" slot in other repos.

<a id="en-idea"></a>
### Core idea

The 10 styles map to two AI editing paths: code generation and classic editing (software tutorial screencasts are a hybrid of both):

| Route | Meaning | Automation |
| --- | --- | --- |
| Code generation | Graphics, text, data, and UI produced in code | Fully automatic |
| Classic editing | People, objects, and live scenes from user footage; AI rough cut + CapCut polish | Semi-automatic |
| Hybrid | Classic-editing main line, with code-generated wrappers and B-roll layered on | Semi-automatic |

<a id="en-structure"></a>
### Full repository layout

```
ai-video-skills/
├── video-router/           ✅ routes all 10 styles
├── code-video/
│   ├── explainer/          ✅ knowledge / PPT → video
│   ├── data-story/         ✅ data motion (label sample data)
│   ├── promo/              ✅ product promo + kinetic/quote cards
│   └── animation/          ✅ short animation / MV-style
├── edit-video/
│   ├── talking-head/       ✅ AI / tech / tools talking-head
│   ├── footage/            ✅ vlog / shop / unbox / commerce
│   ├── clip-long/          ✅ long → clips
│   └── screencast/         ✅ software tutorial (hybrid)
├── shared/
│   ├── subtitle-tts/       ✅ SRT captions; TTS hooks reserved
│   ├── overlays/           ✅ concept / steps / data / screenshot + screencast
│   └── styles/             ✅ SCHEMA + 2 style cards
├── dist/                   ✅ self-contained install packages
├── examples/
├── tests/
└── scripts/
```

Legend: ✅ shipped this release. Client triggers and some semi-auto compositing steps remain "To be tested on Mac".

<a id="en-types"></a>
### Ten video types

Source: framework draft §1. All 10 styles ship a skill (✅). Client triggers / some semi-auto steps remain "To be tested on Mac".

| Video type | Route | Skill | Automation | Status |
| --- | --- | --- | --- | --- |
| Knowledge explainer / animated diagram | Code generation | `code-video/explainer` | Fully automatic | ✅ |
| Data motion | Code generation | `code-video/data-story` | Fully automatic | ✅ |
| Product promo | Code generation | `code-video/promo` | Fully automatic (real UI screenshots; else 示例 placeholder) | ✅ |
| Kinetic text / quote cards | Code generation | `code-video/promo` | Fully automatic | ✅ |
| Short animation / MV | Code generation | `code-video/animation` | Fully automatic (silent OK; no copyrighted music) | ✅ |
| PPT / lesson → video | Code generation | `code-video/explainer` | Fully automatic | ✅ |
| Talking-head | Classic editing | `edit-video/talking-head` | Semi-auto: AI rough cut + CapCut polish | ✅ (AI/tech/tools only in this release) |
| Live footage (vlog, shop, unbox, commerce) | Classic editing | `edit-video/footage` | Semi-automatic (workflow To be tested on Mac) | ✅ |
| Long-form clips | Classic editing | `edit-video/clip-long` | Semi-automatic (workflow To be tested on Mac) | ✅ |
| Software tutorial screencast | Hybrid | `edit-video/screencast` | Semi-automatic (compositing To be tested on Mac) | ✅ |

`video-router`: routes all 10 styles; rejects digital avatars; replies "not supported yet" for out-of-table types (the skill replies in Chinese).

<a id="en-broll"></a>
### Six talking-head subtypes by B-roll source

| Talking-head subtype | B-roll source | Automation | Status |
| --- | --- | --- | --- |
| AI / tech / tools | Mostly code-generated | Mostly automatic | ✅ |
| Knowledge lecture | Code-generated | Fully automatic | 🔜 |
| News | Code + sourced news screenshots | Fully automatic | 🔜 |
| Opinion / workplace / emotion | Caption rhythm + quote cards | Rough cut + user polish | 🔜 |
| Review / commerce | User footage + price/compare cards | Semi-automatic | 🔜 |
| Interview / dialogue | Multi-cam switching | Mostly manual | 🔜 |

<a id="en-skills"></a>
### Skills in this release

| Skill | Path | Use cases | What it does |
| --- | --- | --- | --- |
| **Video-router · 视频入口** | `video-router/` | Pick a style and check the toolchain | Routes all 10 styles; rejects digital avatars |
| **Explainer · 知识科普** | `code-video/explainer/` | Topic / outline / lesson → no on-camera host | HyperFrames template + style card + captions |
| **Data-story · 数据动画** | `code-video/data-story/` | CSV / metrics → data motion | Short template; on-screen sample-data label |
| **Promo · 宣传片/金句** | `code-video/promo/` | Product promo or kinetic / quote cards | Two templates; real UI or 示例 placeholder |
| **Animation · 动画短片** | `code-video/animation/` | Short animation / MV-style beat piece | Shapes + type on a beat grid; silent OK |
| **Talking-head · AI/科技口播** | `edit-video/talking-head/` | AI/tech/tools talking-head rough cut | Transcript → fillers → B-roll → overlays → CapCut list |
| **Footage · 实拍粗剪** | `edit-video/footage/` | Vlog / shop / unbox / commerce footage | Shot log, ffmpeg cut list, captions, CapCut list |
| **Clip-long · 长视频切片** | `edit-video/clip-long/` | Long video → short clips | Transcript → highlights → ffmpeg → captions |
| **Screencast · 软件教程** | `edit-video/screencast/` | Software tutorial screencast | Hybrid: screen main line + overlays |

Shared modules: `shared/overlays/`, `shared/styles/`, `shared/subtitle-tts/` (TTS still To be tested on Mac).

**Out of scope:** digital avatars, Windows.

<a id="en-install"></a>
### Install (Mac)

Packages under `dist/` are generated by `scripts/build_dist.py` from an explicit manifest, each with `LICENSE` + `NOTICE`. **Do not hand-edit `dist/`**; change sources, re-run the build script, then commit. **Install every `dist/` package together** (`video-router` alone only routes).

#### How the three packages relate

| Package | Role | Needs |
| --- | --- | --- |
| `dist/video-router/` | Routes all 10 styles; no rendering | Not useful alone |
| `dist/explainer/` | Knowledge / lesson templates + fonts | Can render alone |
| `dist/data-story/` | Data-motion template (sample-data badge) | Can render alone |
| `dist/promo/` | Promo + kinetic-card templates | Can render alone |
| `dist/animation/` | Animation / MV-style template | Can render alone |
| `dist/talking-head/` | AI/tech talking-head workflow | Docs alone |
| `dist/footage/` | Live-footage semi-auto workflow | Docs alone |
| `dist/clip-long/` | Long → clips workflow | Docs alone |
| `dist/screencast/` | Screencast overlays workflow | Docs alone |

#### Primary path: Claude desktop app (upload zips)

1. Build three zips (or zip each folder under `dist/` yourself; do not paste-only `SKILL.md`):

```bash
make release
# → release/<skill>.zip (9 packages: router + 8 skills)
```

2. Open the **Claude desktop app** and go to its Skills settings.
3. Upload each zip and enable the skill.
4. Exact menu labels vary by Claude desktop version; if you cannot find the upload entry, use the secondary path below or Claude's current help docs.

Type this prompt (Chinese, meaning "make a short vibe knowledge-explainer video"):

> 做一条 vibe 知识科普短视频

(Client trigger results still: To be tested on Mac.)

#### Secondary path: Claude Code / other tools (copy folders)

Copy the whole `dist/<name>/` folder into the tool's skills directory (do not install nested source folders from the monorepo):

| Tool | Destination |
| --- | --- |
| Claude Code | Project `.claude/skills/<name>/`, or user `~/.claude/skills/<name>/` |
| Codex | Project `.agents/skills/<name>/`, or user `~/.agents/skills/<name>/` |
| DeepSeek Harness | Project `.dsh/skills/<name>/` or `.agents/skills/<name>/`, or user `~/.dsh/skills/<name>/` |

`<name>` is `explainer` / `talking-head` / `video-router`. DeepSeek Harness mainly scans one level under the skills root, so use flat `dist/<name>/`.

```bash
# Claude Code example (project root): copy every dist package
mkdir -p .claude/skills
for d in dist/*/; do
  name="$(basename "$d")"
  [[ -f "$d/SKILL.md" ]] || continue
  cp -R "$d" ".claude/skills/$name"
done
```

#### Render after install (explainer)

Inside the **installed** skill folder (e.g. Claude Code project `.claude/skills/explainer/`, or the unpacked explainer package from a zip):

```bash
./doctor.sh
cd templates/short-explainer
npm install
npm run render
# → ./renders/short-explainer.mp4
```

#### Environment & Node

Repo-level check (includes **ffmpeg**):

```bash
./scripts/doctor.sh
```

`doctor.sh` already passed on an iMac (`pass=7 fail=0 warn=0`). See [`tests/mac/2026-11-18-imac.md`](tests/mac/2026-11-18-imac.md).

Node versions (report per tool; do not merge into one line):

- HyperFrames / common Claude Code npm path: Node.js **22+**
- DeepSeek Harness: Node.js **>=24.9.0** (from npm package `@deepseek-ai/dsh` `engines`; queried 2026-11-18 as `0.2.2-rc.1`)

Per-client trigger tests: **To be tested on Mac** (Claude desktop / Claude Code / Codex / DeepSeek Harness were not installed on the prior test machine).

<a id="en-mac"></a>
### Mac verification status

Log: [`tests/mac/2026-11-18-imac.md`](tests/mac/2026-11-18-imac.md) (iMac · Apple M4 · 16GB · macOS 27.0.1 · head `e1398bb`)

| Item | Status |
| --- | --- |
| `scripts/doctor.sh` | ✅ verified — [log](tests/mac/2026-11-18-imac.md) |
| `short-explainer` render (9s) | ✅ verified — [log](tests/mac/2026-11-18-imac.md) |
| Frame grabs at 1.5s / 4.5s / 7.5s | ✅ verified — [log](tests/mac/2026-11-18-imac.md) |
| Claude desktop / Claude Code / Codex / DeepSeek Harness triggers | To be tested on Mac |
| Qwen3-TTS vs CosyVoice | To be tested on Mac |
| Transcription + filler cleanup | To be tested on Mac |
| talking-head overlay export | To be tested on Mac |
| CapCut polish steps + version | To be tested on Mac |
| Full 30s explainer | To be tested on Mac (no 30s template in repo yet) |
| Before/after comparison | To be tested on Mac |

Observation (no code change): body/card text looks small on portrait, content is narrow; enlarge for a full 30s cut. See the Mac log.

<a id="en-hyperframes"></a>
### HyperFrames

- Requires: Node.js 22+, system ffmpeg
- GSAP and fonts are local; renders do not depend on CDN
- Canonical fonts live in `shared/fonts/` (OFL); the build syncs them into the template `fonts/` folder; HTML uses `./fonts/` only (no parent traversal)
- After render, the terminal may show HyperFrames desktop-app promo text — **terminal only, not in the video**
- Short template: source `code-video/explainer/templates/short-explainer/`; install via `dist/explainer/` (**verified on iMac**: HyperFrames 0.9.66, 9.0s / 1080×1920, see [log](tests/mac/2026-11-18-imac.md))

```bash
# dev in-repo
cd code-video/explainer/templates/short-explainer
npm install && npm run render

# or from installed package
# cd path/to/skills/explainer/templates/short-explainer && npm install && npm run render
```

Regenerate install packages:

```bash
python3 scripts/build_dist.py
```

<a id="en-voiceover"></a>
### Voiceover

v1 default: **captions only, no TTS**. Preset / self-clone hooks live in `shared/subtitle-tts/`; **wire after Qwen3-TTS vs CosyVoice Mac bake-off** (still To be tested on Mac).

<a id="en-guardrails"></a>
### Guardrails (summary)

- No synthetic humans, no cloning others' voices, no digital avatars
- Product UI only from real screenshots or recordings
- Public samples only with clear licenses + attribution; otherwise omit
- No invented numbers or sources; write "To be verified" when unknown
- CapCut steps stay unmarked until Mac-verified (mark "To be tested on Mac")

<a id="en-samples"></a>
### Public samples

No third-party talking-head clips are bundled. Future public samples must use clearly licensed, modification-allowed media (e.g. CC BY) with attribution here.

<a id="en-ci"></a>
### Development & CI

```bash
python3 -m pip install pyyaml
python3 scripts/ci_validate.py
```

CI validates frontmatter, `agents/openai.yaml`, the "fictional example" mark, 10+10 triggers, banned-token scan, `build_dist.py --check`, isolated path checks for all three packages, strict `dist/explainer` lint (0 errors) then render smoke, and `doctor.sh` for the repo plus each package on macOS.

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder.

<a id="en-license"></a>
### License

Apache License 2.0. See `LICENSE` and `NOTICE`.

[↑ Back to top](#top)
