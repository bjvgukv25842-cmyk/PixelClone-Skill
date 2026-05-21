# PixelClone Skill

PixelClone Skill turns a total web design reference into a real frontend with pixel-level visual fidelity while preserving the existing product behavior.

It is designed for the modern AI UI workflow:

1. Generate or prepare a beautiful full-page web design reference.
2. Give that reference to Codex or another coding agent.
3. Let the agent rebuild the existing frontend by copying the reference, not inventing a new design.

The repository provides two skills:

| User Language | Recommended Skill | Path |
| --- | --- | --- |
| English users | `pixel-perfect-reference-ui` | `skills/pixel-perfect-reference-ui` |
| 中文用户 | `pixel-perfect-reference-ui-zh` | `skills/pixel-perfect-reference-ui-zh` |

If you mainly prompt in Chinese, install the Chinese skill. If you mainly prompt in English, install the English skill. Both versions provide the same workflow and helper scripts.

## What Problem Does It Solve?

AI coding agents are good at building frontends, but they often fail at strict visual replication.

Common problems:

- The agent treats the design as inspiration instead of a strict source of truth.
- It invents new icons, illustrations, gradients, ornaments, or UI language.
- It uses external assets that do not match the reference.
- It changes layout proportions, section heights, page width, or spacing.
- It stretches or clips reference assets.
- It leaves white edges, black edges, dirty backgrounds, or halo artifacts around cropped images.
- It breaks existing routes, API calls, form behavior, buttons, filters, or user flows while restyling.

PixelClone Skill forces a safer workflow:

- The reference design is the only visual source of truth.
- The existing app is the only business behavior source of truth.
- Visual assets must come from the provided reference or user-provided local replacement files.
- Functional UI must remain real HTML/CSS/components, not screenshots.
- Layout must be measured: canvas size, section heights, gutters, columns, text boxes, and asset bounding boxes.
- The final result must be checked in the real browser, at the exact URL and viewport the user sees.

## What Can This Skill Do?

PixelClone Skill helps a coding agent perform:

- Full-page website UI replication from a total design image.
- Existing frontend restyling without changing product behavior.
- Image2-generated web design implementation.
- Screenshot/mockup/Figma export to real frontend conversion.
- Reference-only asset extraction and placement.
- High-precision decorative asset replacement.
- Pixel-level layout blueprint creation.
- Section height, container width, gutter, grid, and hero/media region matching.
- Transparent PNG/WebP asset cleanup.
- White-edge, black-edge, hard-edge, halo, and background-residue fixes.
- Responsive desktop/mobile visual QA.
- Dropdown/modal/z-index regression checks.
- Business flow preservation during frontend redesign.

## What It Does Not Do

PixelClone Skill is intentionally strict.

It should not:

- Redesign freely from taste.
- Invent new decorative elements.
- Download external UI kits, icon packs, stock images, or templates.
- Replace real forms, tables, buttons, filters, or modals with screenshots.
- Change backend APIs, auth, stores, schemas, route logic, validation, or database code.
- Hide existing features to make a design look cleaner.

## Where Can the Total Design Reference Come From?

The reference can come from many sources, as long as the user has the right to use it:

- GPT image generation / image2 output.
- Midjourney, Stable Diffusion, Flux, or other AI-generated UI images.
- Figma, Sketch, Adobe XD, Framer, Webflow, or Penpot export.
- Product screenshots.
- Landing page screenshots.
- Dribbble-style mockups created by your own workflow.
- Local design image folders containing logos, decorations, backgrounds, buttons, icons, and illustrations.
- Hand-composed full-page UI references.

Best results come from high-resolution full-page references with clear layout boundaries and complete visual assets.

## Repository Structure

```text
PixelClone-Skill/
  README.md
  skills/
    pixel-perfect-reference-ui/       # English skill
      SKILL.md
      agents/
      scripts/
        prepare_reference_asset.py
        extract_layout_blueprint.py
    pixel-perfect-reference-ui-zh/    # Chinese skill
      SKILL.md
      scripts/
        prepare_reference_asset.py
        extract_layout_blueprint.py
```

## Installation For Codex

### Option 1: Copy Manually

Clone this repository:

```bash
git clone https://github.com/bjvgukv25842-cmyk/PixelClone-Skill.git
```

Copy the skill you want into your Codex skills directory.

English version:

```bash
mkdir -p ~/.codex/skills
cp -R PixelClone-Skill/skills/pixel-perfect-reference-ui ~/.codex/skills/
```

Chinese version:

```bash
mkdir -p ~/.codex/skills
cp -R PixelClone-Skill/skills/pixel-perfect-reference-ui-zh ~/.codex/skills/
```

On Windows PowerShell, use paths like:

```powershell
Copy-Item -Recurse .\skills\pixel-perfect-reference-ui "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse .\skills\pixel-perfect-reference-ui-zh "$env:USERPROFILE\.codex\skills\"
```

Restart Codex after installing so the skill list refreshes.

### Option 2: Install Both

You may install both skills at the same time. Use the English skill for English prompts and the Chinese skill for Chinese prompts.

## Python Helper Scripts

The skills include two optional helper scripts.

### `prepare_reference_asset.py`

Used for cropping and cleaning assets from the design reference.

It can help with:

- Precise crop output.
- Transparent PNG/WebP preparation.
- Connected near-background removal.
- 1-2px alpha feathering.
- Page-background matte blending.
- Asset inspection report generation.

Example:

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

Used for turning a total design screenshot into a measurable layout blueprint.

It records:

- Reference canvas width and height.
- Target viewport width.
- Section y positions and heights.
- Major region bounding boxes.
- Grid container width, columns, and gutters.
- Optional CSS variable output.

Example:

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

These scripts require Python and Pillow:

```bash
python -m pip install Pillow
```

They are optional, but recommended for serious pixel-level replication.

## How To Use In Codex

### English Prompt

```text
Use $pixel-perfect-reference-ui.
Rebuild this existing frontend page to match the provided total design reference as closely as possible.
Reference path: [path].
Target URL/page: [url/page].
Treat the reference as the only visual source of truth and the current app as the only behavior source of truth.
Preserve APIs, routes, stores, auth, form fields, validation, filters, sorting, pagination, click actions, and user flows.
Extract visual assets only from the provided reference. Do not use external assets or redraw similar visuals.
Build real HTML/CSS/components for functional UI.
Verify desktop/mobile screenshots, layout blueprint proportions, served asset URLs, and build/lint/typecheck if available.
```

### 中文提示词

```text
Use $pixel-perfect-reference-ui-zh。
请将当前已有前端页面按我提供的总设计图尽可能一比一复刻。
参考图路径：[path]。
目标页面/URL：[url/page]。
请把参考图视为唯一视觉来源，把当前应用视为唯一业务行为来源。
必须完整保留业务行为：API、路由、store、auth、表单字段、校验、筛选、排序、分页、点击事件和用户流程都不能改变。
所有视觉素材只能从我提供的参考图中裁切，不得使用外部素材，不得自己重画类似元素。
功能 UI 必须仍然是真实 HTML/CSS/组件。
完成后检查桌面端和移动端截图、布局蓝图比例、实际 served asset URL，以及项目可用的 build/lint/typecheck。
```

## Typical Workflows

### 1. Full Page Replication

Use this when you have a full design image and want the current frontend to match it.

```text
Use $pixel-perfect-reference-ui. Match this page to my total design reference. Do not change business behavior. Extract all visual assets from the reference only.
```

### 2. Single Asset Replacement

Use this when only one button, logo, flower, icon, background, card decoration, or illustration needs replacement.

```text
Use $pixel-perfect-reference-ui. Replace only the hero-right decorative image with the local asset at [path]. Keep the same behavior, position, aspect ratio, and nearby layout. Do not change other components.
```

### 3. Layout Proportion Fix

Use this when the page looks good but does not match the original design's size distribution.

```text
Use $pixel-perfect-reference-ui. The current result looks visually close, but section heights, page width, gutters, and hero media bounding boxes do not match the reference. Build a layout blueprint from the reference and adjust the page to match it at the reference desktop viewport.
```

### 4. Edge Cleanup

Use this when cropped assets have white edges, black edges, dirty backgrounds, or obvious cut marks.

```text
Use $pixel-perfect-reference-ui. Reprocess this asset from the reference image. Remove connected near-background residue, feather the edge by 1-2px, preserve alpha, and verify there is no white/black halo in the browser.
```

## How To Use With Other Coding Agents

PixelClone Skill is written for Codex skills, but the workflow can be used with other coding tools.

### Claude Code / Cursor / Windsurf / Cline / Aider

Use the corresponding `SKILL.md` as a project instruction file or paste it into the agent's custom instructions.

Recommended options:

- Copy `skills/pixel-perfect-reference-ui/SKILL.md` into your project as `PIXELCLONE.md`.
- Copy `skills/pixel-perfect-reference-ui-zh/SKILL.md` into your project as `PIXELCLONE.zh.md`.
- Add a short instruction in your agent prompt: `Before frontend redesign work, read PIXELCLONE.md and follow it strictly.`
- Keep the helper scripts in your repo under `tools/pixelclone/` or similar.

For non-Codex tools, replace `Use $pixel-perfect-reference-ui` with:

```text
Read and strictly follow PIXELCLONE.md before making frontend UI changes.
```

For Chinese users:

```text
请先阅读并严格遵守 PIXELCLONE.zh.md，再进行前端 UI 复刻或素材替换。
```

## Configuration Tips

For best results, provide the agent with:

- The exact project path.
- The exact local URL and port you are viewing.
- The total design reference path.
- The target page or component name.
- The intended desktop viewport width.
- Any current screenshot showing mismatch.
- Whether the task is full-page replication, partial replacement, or correction.
- Whether full background replacement is allowed or only extracted assets may be used.

Recommended reference quality:

- High-resolution image.
- Full-page screenshot or complete artboard.
- Clear section boundaries.
- Complete decorative assets with no pre-existing crop damage.
- Enough resolution for major hero illustrations and logos.

## What Problems Can It Solve?

PixelClone Skill is useful for:

- Vibe coding teams that want AI-generated UI designs to become real websites.
- Founders who generate landing page designs and need fast implementation.
- Designers who want coding agents to follow a design image strictly.
- Developers who need to restyle an existing app without breaking business logic.
- Product teams that need visual consistency across pages.
- UI repair tasks: clipping, overlap, wrong scale, wrong spacing, wrong section height.
- Asset replacement tasks: logos, decorations, buttons, hero art, background images.
- AI-generated design implementation pipelines.

## Core Principle

PixelClone is not a creativity booster. It is a replication discipline.

The skill tells the agent:

> Do not invent. Measure, crop, place, compare, and preserve behavior.

That is how a beautiful AI-generated design becomes a real, usable frontend.

## License

Add your preferred license here.
