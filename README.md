# PixelClone Skill｜像素级网页复刻 Skill

## 先看这里：如何部署这个 Skill

本仓库提供两款 skill：

| 使用者 | 推荐安装 | 路径 |
| --- | --- | --- |
| 中文用户 | `pixel-perfect-reference-ui-zh` | `skills/pixel-perfect-reference-ui-zh` |
| 英文用户 | `pixel-perfect-reference-ui` | `skills/pixel-perfect-reference-ui` |

如果你主要用中文提示 Codex，请安装中文版；如果你主要用英文提示 Codex，请安装英文版。两款 skill 的能力一致，只是语言不同。

### 1. 克隆仓库

```bash
git clone https://github.com/bjvgukv25842-cmyk/PixelClone-Skill.git
cd PixelClone-Skill
```

### 2. 安装到 Codex

Windows PowerShell：

```powershell
# 中文用户安装这一款
Copy-Item -Recurse .\skills\pixel-perfect-reference-ui-zh "$env:USERPROFILE\.codex\skills\"

# 英文用户安装这一款
Copy-Item -Recurse .\skills\pixel-perfect-reference-ui "$env:USERPROFILE\.codex\skills\"
```

macOS / Linux：

```bash
mkdir -p ~/.codex/skills

# 中文用户安装这一款
cp -R ./skills/pixel-perfect-reference-ui-zh ~/.codex/skills/

# 英文用户安装这一款
cp -R ./skills/pixel-perfect-reference-ui ~/.codex/skills/
```

安装后重启 Codex，让 skill 列表刷新。

### 3. 在 Codex 中调用

中文用户：

```text
Use $pixel-perfect-reference-ui-zh。
请基于我提供的总设计图，对当前网页进行像素级一比一复刻。
参考图路径：[path]
目标页面：[url/page]
```

英文用户：

```text
Use $pixel-perfect-reference-ui.
Rebuild this frontend page from my total design reference with pixel-level fidelity.
Reference path: [path]
Target page: [url/page]
```

---

## PixelClone 是什么？

PixelClone Skill 是一套面向 Codex 和其他 coding agent 的网页视觉复刻工作流。

它的目标很直接：

> 把一张 AI 生成的网页总设计图、Figma 导出图、截图或 Mockup，尽可能像素级一比一复刻成真实可运行的前端页面，同时不破坏现有业务功能。

它不是让 AI “参考风格重新设计”，而是让 AI 按总设计图复制：

- 复制页面宽度和整体布局。
- 复制 section 高度和上下分布。
- 复制左右栏比例、卡片网格、留白和对齐。
- 从参考图中裁切 logo、图标、按钮背景、装饰贴图和插画。
- 保留现有页面的 API、路由、表单、按钮、状态管理和用户流程。

## 它解决了什么问题？

很多 vibe coder 会用 GPT image、image2、Midjourney、Figma 或其他工具先生成漂亮网页设计图，然后让 Codex、Claude Code、Cursor 等工具实现。

但常见问题是：

- Coding agent 把设计图当成“灵感”，而不是“唯一视觉来源”。
- 它会自己创造新图标、新插画、新装饰和新布局。
- 它会使用外部素材，导致风格不统一。
- 它会把页面宽度、section 高度、主视觉比例、卡片间距做错。
- 它会裁切素材时留下白边、黑边、脏边或硬矩形背景。
- 它可能为了视觉改版误改业务逻辑、按钮行为、路由或表单流程。

PixelClone 的核心约束是：

- 参考图是唯一视觉真相。
- 当前应用是唯一业务行为真相。
- Codex 的任务是复制，不是再设计。
- 所有装饰素材只能来自参考图或用户提供的本地素材。
- 真实功能区域必须仍然是 HTML/CSS/组件，不能截图化。
- 修改后必须用真实浏览器截图、布局蓝图和项目检查命令验证。

## 这个 Skill 能做什么？

PixelClone 可以帮助 coding agent 完成：

- 基于网页总设计图的一比一前端复刻。
- 基于 image2 / GPT image 生成网页图的真实前端落地。
- 现有项目的 UI 视觉重构，且不改变业务功能。
- 局部素材替换，例如 logo、按钮、花朵、贴图、插画、背景、卡片装饰。
- 从参考图中裁切素材，并清理白边、黑边、锯齿和背景残留。
- 建立布局蓝图，测量画布宽高、section 高度、左右 gutter、主视觉包围盒和卡片网格。
- 修复视觉问题，例如素材截断、组件重叠、按钮文字溢出、布局比例不准、移动端错位。
- 检查下拉菜单、弹窗、抽屉、Toast、功能面板是否被装饰层遮挡。
- 在保留 API、路由、状态管理、表单校验、筛选排序分页的前提下做 UI 改版。

## 它不能做什么？

PixelClone 是一个“复刻纪律”，不是自由设计工具。

它不应该：

- 凭审美重新设计页面。
- 自己创造参考图里不存在的花、叶子、机器人、图标、背景、按钮或插画。
- 下载外部 UI 模板、图标包、图库图或贴纸。
- 把真实表单、表格、筛选器、弹窗、导航截图化。
- 修改后端接口、权限、数据库、schema、validation、store 或业务路由逻辑。
- 为了视觉效果隐藏已有功能或删除用户可执行操作。

## 总设计图可以来自哪里？

只要你拥有使用权，总设计图可以来自：

- GPT image / image2 生成的网页设计图。
- Midjourney、Stable Diffusion、Flux 等 AI 生成图。
- Figma、Sketch、Adobe XD、Framer、Webflow、Penpot 导出图。
- 产品截图或竞品截图。
- Landing page 长截图。
- 你自己整理的 Dribbble 风格 Mockup。
- 本地参考图文件夹，例如 logo、装饰、按钮、图标、插画、背景等。
- 手动拼合的完整网页视觉参考图。

推荐使用高清、完整、边界清楚的总设计图。图越清晰，复刻越接近像素级。

## 仓库结构

```text
PixelClone-Skill/
  README.md
  skills/
    pixel-perfect-reference-ui/       # 英文版 skill
      SKILL.md
      agents/
      scripts/
        prepare_reference_asset.py
        extract_layout_blueprint.py
    pixel-perfect-reference-ui-zh/    # 中文版 skill
      SKILL.md
      scripts/
        prepare_reference_asset.py
        extract_layout_blueprint.py
```

## 两个辅助脚本

Skill 内置两个可选 Python 脚本，用于更稳定地完成像素级复刻。

使用前安装 Pillow：

```bash
python -m pip install Pillow
```

### `prepare_reference_asset.py`

用于从参考图裁切并清理素材。

它可以处理：

- 精确裁切。
- 输出 PNG / WebP。
- 透明背景 alpha 处理。
- 移除连接到边缘的近背景色。
- 1px 到 2px 边缘羽化。
- 使用页面背景色做 matte 融合。
- 生成素材检查报告。

示例：

```bash
python scripts/prepare_reference_asset.py \
  --src reference.png \
  --out public/assets/reference-style/flower.png \
  --box 120,80,480,620 \
  --transparent-edge "#fbfaf4" \
  --threshold 26 \
  --feather 1.5
```

### `extract_layout_blueprint.py`

用于把总设计图转成可测量的布局蓝图。

它会记录：

- 参考图画布宽高。
- 目标浏览器视口宽度。
- section 的 y 起点和高度。
- 主要区域的包围盒。
- 页面容器宽度、列数、gutter。
- 可选 CSS 变量输出。

示例：

```bash
python scripts/extract_layout_blueprint.py \
  --src reference.png \
  --out reference-layout.json \
  --viewport-width 1440 \
  --section header:0,0,1920,112 \
  --section hero:0,112,1920,932 \
  --region heroText:120,310,540,740 \
  --region heroMedia:760,250,1650,870:contain \
  --grid 120,1680,12,24
```

## Codex 使用示例

### 整页复刻

```text
Use $pixel-perfect-reference-ui-zh。
请将当前已有前端页面按我提供的总设计图尽可能一比一复刻。
参考图路径：[path]
目标页面/URL：[url/page]
请把参考图视为唯一视觉来源，把当前应用视为唯一业务行为来源。
API、路由、store、auth、表单字段、校验、筛选、排序、分页、点击事件和用户流程都不能改变。
所有视觉素材只能从我提供的参考图中裁切，不得使用外部素材，不得自己重画类似元素。
功能 UI 必须仍然是真实 HTML/CSS/组件。
完成后检查桌面端和移动端截图、布局蓝图比例、实际 served asset URL，以及项目可用的 build/lint/typecheck。
```

### 单个素材替换

```text
Use $pixel-perfect-reference-ui-zh。
请只替换 [页面/区域/组件] 中的 [当前素材/按钮/装饰]，新素材来自 [path/name]。
保留原有行为、点击事件、路由、表单逻辑、状态和附近布局。
新素材必须按原始比例显示，不能拉伸、裁切或过度放大。
除非我明确要求移动，否则保持原位置。
若有白边/黑边，按重新裁切、透明处理、1-2px 羽化、matte 融合的顺序处理。
不要改其他页面或组件。
完成后验证没有截断、重叠、旧缓存或 UI 回归。
```

### 布局比例修正

```text
Use $pixel-perfect-reference-ui-zh。
现在页面视觉已经接近参考图，但页面宽度、section 高度、左右 gutter、主视觉包围盒和卡片网格比例还不准确。
请先基于参考图建立布局蓝图，再调整页面，使它在参考图对应的桌面视口下尽可能一比一匹配。
不要改业务逻辑，不要替换无关素材。
```

### 素材边缘清理

```text
Use $pixel-perfect-reference-ui-zh。
请重新处理这个素材。它来自参考图，但现在有明显白边/黑边/脏边。
请重新裁切，移除连接到边缘的近背景色，做 1-2px 羽化，保留 alpha，并在浏览器里验证没有明显光晕。
禁止自己绘制或生成替代素材。
```

## 如何用于 Codex 之外的 coding 软件？

虽然这个仓库按 Codex skill 格式组织，但其中的工作流也可以用于其他 coding agent。

适用工具包括：

- Claude Code
- Cursor
- Windsurf
- Cline
- Aider
- 其他支持项目规则或自定义提示词的 coding agent

推荐做法：

1. 把 `skills/pixel-perfect-reference-ui-zh/SKILL.md` 复制到你的项目根目录，命名为 `PIXELCLONE.zh.md`。
2. 如果你使用英文，把 `skills/pixel-perfect-reference-ui/SKILL.md` 复制到项目根目录，命名为 `PIXELCLONE.md`。
3. 把 `scripts/` 目录复制到项目里的 `tools/pixelclone/`。
4. 在你的 coding agent 提示词里写：

中文：

```text
请先阅读并严格遵守 PIXELCLONE.zh.md，再进行前端 UI 复刻、视觉重构或素材替换。
```

英文：

```text
Read and strictly follow PIXELCLONE.md before making frontend UI replication or visual redesign changes.
```

## 推荐给 agent 的配置信息

为了获得更好的复刻效果，请在任务开始时提供：

- 当前项目路径。
- 你正在查看的本地 URL 和端口。
- 总设计图或参考素材文件夹路径。
- 目标页面、区域或组件名称。
- 希望匹配的桌面视口宽度。
- 当前页面截图，尤其是你认为“不像”的地方。
- 任务类型：整页复刻、局部替换、布局修正、素材清理。
- 是否允许整张背景图铺满，还是只能从参考图裁切局部素材。

## 面向哪些问题？

PixelClone 适合解决：

- AI 生成网页设计图无法落地成真实前端。
- Codex / Claude Code / Cursor 复刻设计图时喜欢自由发挥。
- image2 生成的网页图和最终页面不够像。
- 现有项目想换 UI，但不能破坏业务逻辑。
- 页面整体格局不像参考图：宽度、section 高度、左右比例、留白不准。
- 裁切素材有白边、黑边、脏边、截断或模糊。
- UI 组件、贴图、按钮、背景、插画需要按参考图替换。
- 弹窗、下拉菜单、功能面板被装饰层遮挡。
- 移动端布局错位、素材重叠或文字溢出。

## 核心原则

PixelClone 不是让 AI 更会自由设计，而是让 AI 学会克制地复刻。

它告诉 coding agent：

> 不要发明。先测量，再裁切，再摆放，再对照截图，最后保留业务行为。

这就是把一张漂亮的 AI 网页设计图，真正落地成可运行前端的关键。

## License

你可以根据自己的发布需求补充许可证。
