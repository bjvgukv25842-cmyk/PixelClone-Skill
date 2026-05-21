---
name: pixel-perfect-reference-ui-zh
description: 当 Codex 需要基于一张网页总设计图、image2 生成图、截图、Mockup、Figma 导出图或本地参考图集，对现有网站前端进行像素级复刻或视觉重构时使用。本 skill 强制遵守：总设计图是唯一视觉来源、只从参考图裁切素材、不自创设计元素、不使用外部素材、严格保留业务功能，并通过截图、素材边缘、遮挡、响应式、z-index 与回归检查确保网页尽量一比一复刻。
metadata:
  short-description: 基于总设计图的像素级网页复刻
---

# 总设计图像素级网页复刻

## 使命

当用户提供一张网页总设计图、image2 生成图、截图、Mockup、Figma 导出图或本地参考图文件夹，并要求把现有前端改成同款视觉效果时，使用本 skill。

核心心智模型必须非常明确：

- 参考图是唯一视觉真相。
- 当前应用是唯一业务行为真相。
- 你的任务是复制和实现，不是重新设计。
- 不要做“参考灵感风格”。要尽可能复刻参考图中的布局、素材、间距、颜色、比例和视觉语言。

本 skill 必须通用于不同项目。不要把某个具体项目名、品牌名、颜色、路由或装饰元素写死，除非它们来自当前用户给出的参考图。

## 绝对业务契约

改代码前，先识别业务边界，并全程保持不变：

- 不修改后端、API client、services、store、auth、permission、schema、validation、database、middleware 或业务路由逻辑。
- 不删除、不重命名、不隐藏、不禁用、不截图化、不伪造任何真实按钮、表单、表格、筛选器、弹窗、菜单、导航项或用户可执行操作。
- 不改变数据结构、请求参数、状态流转、表单字段、校验逻辑、排序、筛选、分页、登录退出或权限控制。
- 不减少已有功能、入口、步骤、键盘焦点和可访问性能力。
- 只修改展示层：CSS、主题 token、布局 wrapper、className、装饰节点、响应式样式、动效和来自参考图的静态素材。
- 如果必须调整组件结构，要保留 props、事件处理、ref、可访问语义和原有行为。
- 如果用户只要求局部替换，只改指定页面、区域或组件。除非用户要求全站改版，不要动全局样式。

真实功能 UI 必须仍然是 HTML/CSS/组件。不能把表单、表格、筛选器、弹窗、导航或按钮流程变成截图。

## 视觉来源契约

总设计图复刻的关键是素材纪律：

- 只使用用户提供的参考图，或用户提供的本地替换素材。
- 不使用图库、图标包、AI 生成替代图、外部下载装饰、外部模板或另一套设计系统。
- 不重画一个“差不多”的花、角色、logo、图标、背景、贴纸、按钮、头像或插画。
- 不新增参考图中不存在的装饰语言。
- 从参考图裁切出的素材可以作为 img、picture、CSS background-image、sprite、mask 或装饰层放入页面。除非是纯几何 UI 且更适合用 CSS 实现，否则不要手工重绘参考图里的视觉元素。
- 真实可交互 UI 不能直接把整张参考图当截图背景。例外：如果用户明确要求把整张图作为非交互背景铺满，可以把它作为背景，同时保留上层真实 UI。

## 必要输入

如果缺失，只有在安全时才推断；否则只问一次：

- 项目路径，以及用户正在查看的精确 URL、路由和端口。
- 参考图、截图、设计导出文件或本地参考素材文件夹。
- 目标页面、区域、组件，以及任务类型：整页复刻、单素材替换，还是修正上一轮问题。
- 如果用户说效果不对，需要用户当前看到的截图或浏览器上下文。

用户提供本地参考文件夹时，必须先检查真实文件名、尺寸和路径，不要凭记忆假设素材名称。

## 工作流

### 1. 确认运行目标

动手前，先确认用户实际看到的是哪个页面：

- 记录用户或浏览器上下文里的精确 URL 与端口。
- 如果同时存在多个 dev server，验证用户浏览器里的那个，不要只验证自己随手启动的端口。
- 找到该路由对应的页面组件和样式文件。
- 修改素材后，直接打开素材的实际 served URL，确认返回的是图片文件和正确 content-type，而不是 HTML fallback 或旧缓存。
- 如果热更新或缓存导致看不到新图，使用带 hash 的新文件名或更新 import 路径，然后重新在浏览器里检查。

### 2. 先划清业务边界

阅读目标页面和附近共享组件，识别：

- 页面组件、布局壳、共享导航、侧栏、按钮、卡片、输入框、弹窗。
- API 调用、store、路由链接、点击事件、提交事件和权限逻辑。
- 样式体系：CSS Modules、SCSS、Tailwind、styled-components、全局 CSS、UI 库等。
- 哪些元素是真实功能控件，哪些只是装饰。

明确哪些文件和逻辑不能碰。优先用展示层 wrapper 解决视觉问题，避免业务重构。

### 3. 把参考图当规格书审图

用视觉检查和脚本测量参考图：

### 3A. 先建立布局格局蓝图

像素级复刻最容易失败的地方，不是颜色和素材，而是页面看着相似，但没有遵守总设计图的大小格局分布。写 CSS 前，必须把总设计图转成可测量的布局蓝图：

- 记录参考图画布宽高、目标视口宽度，以及截图缩放比例。
- 从上到下识别所有横向 section：header、hero、功能区、产品网格、footer 等。测量每个 section 的 y 起点、高度，以及占整页高度的百分比。
- 识别全局页面容器：是否全宽、是否居中 max-width、左右 gutter、是否使用固定设计稿宽度。
- 测量主要布局列：左侧文字块、右侧媒体块、中间分割、卡片网格列数、gap、左右边距。像素值和百分比都要记录。
- 测量纵向锚点：logo/nav 基线、hero 标题顶部、hero 主视觉顶部和底部、CTA 基线、section 交界线、卡片顶线、footer 基线。
- 测量主要素材包围盒：x、y、宽、高、宽高比，以及该素材是设计图中有意裁切，还是必须完整显示。
- 测量文字块包围盒，而不是只看字号。先匹配换行、文本块宽度和垂直节奏，再微调字体。
- 从蓝图派生 CSS 变量，例如 --ref-width、--section-hero-h、--hero-left-x、--hero-media-w、--grid-gap。

当 CSS 实现和参考图冲突时，按这个优先级修正：

1. 整体画布/页面宽度与左右 gutter。
2. section 高度和 y 位置。
3. 主要列宽与 x 位置。
4. 素材包围盒和裁切策略。
5. 文本块宽度和换行。
6. 字体、阴影、颜色和微细节。

不要让响应式便利性改写桌面端构图。在参考图对应的桌面视口下，页面应保持相同的 section 占比和对象包围盒，除非真实业务内容导致无法做到。

建议生成蓝图文件：

~~~json
{
  "referenceCanvas": { "width": 1920, "height": 2880 },
  "targetViewport": { "width": 1440 },
  "scale": 0.75,
  "sections": [
    { "name": "header", "y": 0, "height": 112, "heightPct": 0.039 },
    { "name": "hero", "y": 112, "height": 820, "heightPct": 0.285 },
    { "name": "feature-band", "y": 932, "height": 520, "heightPct": 0.181 }
  ],
  "regions": {
    "heroText": { "x": 120, "y": 310, "w": 420, "h": 430 },
    "heroMedia": { "x": 760, "y": 250, "w": 890, "h": 620, "fit": "contain" }
  },
  "grid": { "containerX": 120, "containerW": 1680, "columns": 12, "gutter": 24 }
}
~~~

本 skill 提供 scripts/extract_layout_blueprint.py 作为起始辅助脚本。它会记录图片尺寸，并把手动传入的 section/region 包围盒写成 JSON。自动检测不可靠时，以人工截图测量的包围盒为准。

- 画布尺寸与目标视口。
- 布局网格、页边距、栏宽、间距、主区域大小、对齐关系和留白。
- 字体层级、行高、字重、字距、标题换行、按钮文字容纳情况。
- 圆角、边框透明度、阴影颜色与扩散、模糊和玻璃感。
- 从像素采样颜色，不凭感觉选色：背景、表面、主色、强调色、正文、弱文字、边框、阴影。
- 素材清单：logo、标记、图标、产品截图、卡片、媒体图、贴纸、线条、箭头、背景块、花叶/角色/物件、头像、按钮背景。
- 为每个素材标注语义：是有意义内容，还是纯装饰。纯装饰通常要 aria-hidden 且不影响交互。

根据采样值建立 token，不要凭空造色：

~~~css
:root {
  --color-bg: ...;
  --color-surface: ...;
  --color-primary: ...;
  --color-primary-strong: ...;
  --color-accent: ...;
  --color-text-main: ...;
  --color-text-muted: ...;
  --color-border: ...;
  --shadow-card: ...;
  --motion-fast: 140ms;
  --motion-normal: 240ms;
  --motion-slow: 600ms;
  --ease-soft: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-gentle: cubic-bezier(0.16, 1, 0.3, 1);
}
~~~

### 4. 高精度裁切素材

把裁切素材统一放到清晰目录，例如：

~~~text
public/assets/reference-style/
src/assets/reference-style/
~~~

建立 manifest，保证每个素材可追溯：

~~~json
{
  "sourceReference": "absolute/or/user/provided/path.png",
  "assets": {
    "logo-main": {
      "file": "/assets/reference-style/logo-main.png",
      "sourceBox": [120, 44, 268, 92],
      "role": "semantic"
    },
    "hero-flower-01": {
      "file": "/assets/reference-style/hero-flower-01.png",
      "sourceBox": [1460, 80, 1840, 620],
      "role": "decorative"
    }
  }
}
~~~

优先使用脚本或图像工具做精确裁切。本 skill 提供 scripts/prepare_reference_asset.py，可在 Python 和 Pillow 可用时，用于裁切、透明处理、边缘羽化和生成检查报告。

严格裁切规则：

1. 只从参考图或用户提供的本地替换素材裁切。禁止外部下载。
2. 输出 PNG 或 WebP。需要透明背景的素材必须带 alpha 通道。
3. 不保留白色矩形底、黑边、硬边、脏边、明显背景残留或错误 matte，除非参考图本身就是这个效果。
4. 如果素材有白边、黑边、锯齿、光晕或背景残留，按顺序处理：
   - 重新裁切，选择更完整或更干净的区域。
   - 保守地移除连接到边缘的纯白、近白或近背景色区域。
   - 对 alpha 边缘做 1px 到 2px 柔和羽化。
   - 如果透明处理产生光晕，用页面真实背景色做 matte 融合。
   - 只允许轻微调整亮度、饱和度或色温，让原始素材融入采样背景。
   - 仍然无法解决时，从同一参考图集里换一个更干净的同类素材。
   - 如果没有可用替代，说明限制。禁止自己画或生成替代素材。
5. 不要把模糊、低清、被裁断或边缘损坏的素材放在主要视觉位置。
6. 不要过度放大裁切素材。如果目标展示尺寸超过素材可用分辨率，重新从更大区域裁切或选更干净的源素材。
7. 透明 PNG 在某些查看器里可能显示黑底。必须检查 alpha 和像素数据，不要在确认前误以为它真的有黑底。

素材最低 QA：

- 检查尺寸和宽高比。
- 检查需要透明的地方是否真的有 alpha。
- 检查边缘像素是否有白边、黑边或光晕。
- 通过浏览器打开最终素材的 served URL。
- 确认不是 HTML fallback，也不是旧缓存。

### 5. 按参考图实现布局

从大到小实现：

- 页面背景和整体框架。
- Header、导航、侧栏几何结构。
- Hero 或首屏主区域。
- 卡片、表格、表单、弹窗、列表、Dashboard。
- 真实控件与不同状态的视觉。
- 装饰层。
- hover、focus、active、loading、empty、error 状态。
- 响应式断点。

用稳定 CSS 约束，不要堆脆弱魔法数：

- max-width、grid tracks、aspect-ratio、clamp()、min()、max()。
- 对必须完整显示的插图使用 object-fit: contain。
- 对必须完整显示的背景图使用 background-size: contain。
- 只有当裁切是参考图本身要求或用户明确接受时，才使用 background-size: cover。
- 只有装饰 wrapper 需要时才使用 overflow: visible。
- 只有参考图里确实有裁切效果，或素材安全处于内边距中时，才使用 overflow: hidden。

装饰层规则：

~~~css
.reference-decor {
  pointer-events: none;
  user-select: none;
  -webkit-user-drag: none;
  object-fit: contain;
  max-width: 100%;
  height: auto;
}
~~~

JSX/HTML 示例：

~~~tsx
<img
  className="reference-decor"
  src="/assets/reference-style/decorative-asset.png"
  alt=""
  aria-hidden="true"
  draggable={false}
/>
~~~

装饰层必须低于 popover、dropdown、modal、drawer、toast 和真实功能面板。如果菜单或功能 UI 被覆盖，修 z-index 和层级，不要通过隐藏菜单或降低可访问性来解决。

### 6. 替换图片式按钮时保留功能

如果参考图中的按钮像一张图片，但当前按钮是功能控件，必须保留原 button 和事件，只替换视觉层。

~~~tsx
<button type="button" className="ref-image-button" onClick={onClick} aria-label={label}>
  <img src="/assets/reference-style/button-bg.png" alt="" aria-hidden="true" draggable={false} />
  <span className="ref-image-button__text">{label}</span>
</button>
~~~

~~~css
.ref-image-button {
  --button-aspect: 3.2 / 1;
  position: relative;
  width: clamp(144px, 14vw, 220px);
  aspect-ratio: var(--button-aspect);
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
  display: inline-grid;
  place-items: center;
  overflow: visible;
}
.ref-image-button > img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  pointer-events: none;
  user-select: none;
  -webkit-user-drag: none;
}
.ref-image-button__text {
  position: relative;
  z-index: 1;
  max-width: 78%;
  overflow-wrap: anywhere;
}
~~~

使用导出素材真实宽高比。不要拉伸或裁切按钮背景。如果每个按钮文字不同，文字必须作为真实 DOM 覆盖在图片上。

### 7. 局部替换规则

当用户要求替换某个具体素材：

- 找到该位置当前真实使用的节点、class 或资源文件。
- 除非用户要求移动，否则在同一位置替换 source 或视觉层。
- 先保持原有位置和大致尺寸，再只做必要微调以避免裁切、重叠或对齐问题。
- 不要在其他地方新增一个重复素材。
- 不要改全局样式或其他页面。
- 替换后检查该区域是否还残留旧装饰层。
- 如果用户要求“去除上一步修改”，只撤销你上一轮针对该区域的改动。不要 reset 仓库，也不要移除已被用户接受的其他 UI 工作。

## 视觉 QA 清单

在相同视口尺寸下对照参考图检查：

- Header/nav：位置、logo 尺寸、激活态、按钮形状、间距。
- 主布局：区域宽度、垂直节奏、标题换行、卡片对齐、留白。
- 布局蓝图：页面宽度、左右 gutter、section 高度、y 起点、列比例和主素材包围盒在参考视口下匹配参考图。
- 区块分布：section 不应比参考图明显压缩或拉长，除非真实业务内容必须如此。
- 首屏折线：如果参考图首屏露出下一段内容，实现页在同视口下也应露出相近比例。
- 图片/装饰：素材完整可见，没有缺角、意外裁切或重复覆盖。
- 边缘：没有白边、黑边、硬矩形、脏背景、锯齿光晕或明显 matte 不匹配。
- 缩放：没有模糊放大；参考图里很大的素材不能被缩得过小。
- 文字：没有图标压字、首字被遮挡、按钮/卡片文字溢出或长文本被裁掉。
- 功能层级：dropdown、popover、panel、drawer、toast、modal 应位于背景和装饰层之上。
- 表单：label、placeholder、错误提示、focus ring、disabled/loading 状态仍可见。
- 列表/表格：筛选、排序、分页、hover、空状态仍正常。
- 视觉语言：不要混入无关的默认 Material、Bootstrap、Ant Design 风格；不要出现参考图没有的随意渐变、光斑或图标。

当用户提供截图或说“还是不对”时，用户截图是最高优先级事实。修复具体错位区域，不要扩展成大改版。

## 响应式 QA

至少验证参考图桌面宽度和常见断点：

- 1440px 或设计稿桌面宽度。
- 1200px。
- 1024px。
- 768px。
- 390px/375px。

移动端禁止：

- 丢失导航入口或真实操作。
- 裁切表单、卡片、按钮。
- 让装饰素材遮挡按钮、文字、输入框或菜单。
- 表单产生横向滚动。
- 隐藏 focus 状态。

如果能保持功能完整且符合参考图气质，装饰素材可以在小屏缩小、移动或隐藏。

## 动效

只有当参考图、用户或现有应用要求动效时才复刻动效。否则使用克制 CSS 动效，不引入新的设计语言：

- 页面/卡片进入：fade + translateY(8-14px)，240-700ms。
- hover：translateY(-2px 到 -4px)，阴影轻微变化。
- 装饰 idle：仅当参考风格允许，使用很小的 float、sway 或 opacity 变化，周期 4-8s。
- 不使用剧烈弹跳、旋转、霓虹光效、强视差或新的动画库，除非参考图和现有应用本身就是这样。

必须支持减少动态偏好：

~~~css
@media (prefers-reduced-motion: reduce) {
  .reference-decor,
  .card-enter {
    animation: none !important;
    transition-duration: 0.01ms !important;
    transform: none !important;
  }
}
~~~

## 验证命令

实现后运行项目可用检查：

- 项目已有的 build、typecheck、lint、test。
- 在用户实际 URL 和端口上做浏览器截图检查。
- 直接打开 served asset URL。
- 点击被修改按钮和主要导航项。
- 打开和关闭被影响的 menu、dropdown、panel、modal、drawer、toast。
- 如果触及页面里有搜索、筛选、排序、分页，也要验证它们。
- 检查浏览器 console 是否有运行时错误。

除非用户明确授权，不要输入账号密码。

## 常见失败模式

必须避免：

- 根据审美重新设计，而不是复制参考图。
- 自己创造新图标、花朵、角色、logo、渐变、背景或装饰元素。
- 因为“看起来相似”就使用外部素材。
- 裁切按钮或装饰后强行拉伸适配文字。
- 用户要求“原位置替换”，却把素材移动到了别的位置。
- 为了解决重叠把素材缩得过小，导致不像参考图。
- 新旧装饰重复叠在一起。
- 用户需要整图完整显示时误用 cover。
- 没检查 alpha，就把透明预览黑底当成真实黑边。
- 改了错误的 localhost 端口或 stale build。
- 只匹配颜色和素材，却忽略参考图的页面宽度、section 高度和列宽分布。
- 让内容自适应布局把桌面端本该固定比例的 section 拉长或压扁。
- 使用常见 UI 习惯里的 max-width、padding、gap，而不是从设计图测量。
- 装饰层盖住菜单、按钮或功能面板。
- 为了视觉一致把真实 UI 截图化。

## 可复用提示词模板

整页复刻：

~~~text
Use $pixel-perfect-reference-ui-zh。请将当前已有前端页面按我提供的总设计图尽可能一比一复刻。参考图路径：[path]。目标页面/URL：[url/page]。请把参考图视为唯一视觉来源，把当前应用视为唯一业务行为来源。必须完整保留业务行为：API、路由、store、auth、表单字段、校验、筛选、排序、分页、点击事件和用户流程都不能改变。所有视觉素材只能从我提供的参考图中裁切，不得使用外部素材，不得自己重画类似元素。功能 UI 必须仍然是真实 HTML/CSS/组件。完成后检查桌面端和移动端截图、布局蓝图比例、实际 served asset URL，以及项目可用的 build/lint/typecheck。最后报告修改文件、新增素材、检查命令、回归结果和无法完全复刻的原因。
~~~

单素材替换：

~~~text
Use $pixel-perfect-reference-ui-zh。请只替换 [页面/区域/组件] 中的 [当前素材/按钮/装饰]，新素材来自 [path/name]。保留原有行为、点击事件、路由、表单逻辑、状态和附近布局。新素材必须按原始比例显示，不能拉伸、裁切或过度放大。除非我明确要求移动，否则保持原位置。若有白边/黑边，按重新裁切、透明处理、1-2px 羽化、matte 融合的顺序处理。不要改其他页面或组件。完成后验证没有截断、重叠、旧缓存或 UI 回归。
~~~

位置/大小修正：

~~~text
Use $pixel-perfect-reference-ui-zh。请只调整 [页面/url] 上的 [素材/组件]。当前问题是：[太小/被裁切/重叠/边缘异常/对齐不准]。保持素材来源和整体视觉语言不变。只允许改尺寸、位置、z-index、object-fit/background-size 或 wrapper overflow，让它完整、对齐且不遮挡其他 UI。不要触碰业务逻辑或无关素材。请验证桌面端和移动端。
~~~

撤销错误视觉修改：

~~~text
Use $pixel-perfect-reference-ui-zh。请只撤销你上一步针对 [素材/区域/组件] 的修改。不要 reset 仓库，不要移除其他已经被接受的 UI 工作。恢复该区域之前的素材来源、位置或样式，并确认没有残留重复素材、class 或装饰层。
~~~
