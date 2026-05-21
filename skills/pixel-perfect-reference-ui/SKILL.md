---
name: pixel-perfect-reference-ui
description: Use when Codex must rebuild or restyle an existing website/frontend from a total visual reference such as an image2 output, screenshot, mockup, Figma export, or local reference image set. This skill enforces pixel-level replication, reference-only asset extraction, strict business behavior preservation, no invented visuals, no external assets, and visual QA for clipping, white/black edges, overlap, z-index, responsiveness, and UI regressions.
metadata:
  short-description: Pixel-level website replication from a total design reference
---

# Pixel Perfect Reference UI

## Mission

Use this skill when the user gives a total website design image, screenshot, image2 output, Figma export, or local reference-image folder and wants an existing frontend to match it.

The mental model is strict:

- The reference image is the single visual source of truth.
- The existing app is the single behavior source of truth.
- Your job is copying and implementing, not creative redesign.
- Do not be "inspired by" the reference. Replicate its layout, assets, spacing, colors, proportions, and visual language as closely as the target app and source quality allow.

This skill is general. Do not bake in project names, brand names, colors, routes, or decorative motifs unless they come from the current user's reference.

## Absolute Business Contract

Before editing code, identify the behavior boundary and keep it intact:

- Do not modify backend, API clients, services, stores, auth, permissions, schemas, validation, database, middleware, or business route logic.
- Do not delete, rename, hide, disable, screenshot, or fake any real button, form, table, filter, modal, menu, navigation item, or user action.
- Do not change data structures, request parameters, state transitions, form fields, validation behavior, sorting, filtering, pagination, login/logout, or permissions.
- Do not remove existing functionality, entries, steps, or keyboard/focus access.
- Only change presentation: CSS, theme tokens, layout wrappers, class names, decorative nodes, responsive styling, animation, and static reference-derived assets.
- If component structure must change, preserve props, event handlers, refs, accessibility semantics, and behavior.
- For partial replacements, change only the requested page/region/component. Avoid global style edits unless the user asked for a global redesign.

Functional UI must remain real HTML/CSS/components. Never turn a form, table, filter, dialog, navigation, or button flow into a screenshot.

## Visual Source Contract

Reference replication is asset discipline:

- Use only user-provided reference images or local user-provided replacement assets.
- Do not use stock images, icon packs, generated substitute art, downloaded decorations, external templates, or a different design system.
- Do not redraw a "similar" flower, character, logo, icon, background, sticker, button, avatar, mascot, or illustration.
- Do not create new decorative language. If the reference has no such element, do not add it.
- Cropped assets are placed as img, picture, CSS background-image, sprites, masks, or decoration layers. They are not recreated by hand unless they are plain geometric UI that is better built in CSS.
- Do not use the full reference as a page screenshot background when real UI must remain interactive. Exception: if the user explicitly asks to replace an entire non-interactive background with the supplied image, use it as a background while keeping foreground UI real.

## Required Inputs

If missing, infer only when safe; otherwise ask once:

- Project path and exact target URL/route/port the user is viewing.
- Reference image, screenshot, design export, or local reference-asset folder.
- Target page/region/component and whether this is full-page replication, a single asset replacement, or correction of a previous pass.
- Screenshots showing mismatch if the user says the result is wrong.

Always inspect actual filenames, dimensions, and served URLs before assuming an asset name or that the dev server is showing your latest file.

## Workflow

### 1. Verify the Runtime Target

Before changing visuals, confirm the page the user actually sees:

- Note the exact URL and port from the user/browser context.
- If multiple dev servers exist, validate the one in the browser, not the one you happened to start.
- Inspect route/component mapping for that exact page.
- After asset changes, verify the actual served asset URL returns the image file and correct content type, not an HTML fallback or cached old file.
- If hot reload/cache hides a change, use a new hashed filename or update the import path, then recheck in browser.

### 2. Map Behavior Before Visual Work

Read the target page and nearby shared components. Identify:

- Page component, layout shell, shared nav/header/sidebar, buttons, cards, inputs, modals.
- Existing API calls, stores, route links, click handlers, submit handlers, and permissions.
- CSS system: CSS Modules, SCSS, Tailwind, styled-components, global CSS, UI library, etc.
- Which elements are real controls and which are purely decorative.

Write down what must not be touched. Prefer presentation-only wrappers over refactors.

### 3. Audit the Reference as a Spec

Measure and inventory the reference, preferably with scripts or image tools:

### 3A. Build a Layout Blueprint Before Styling

Pixel-level replication fails when the page looks visually similar but the reference's size distribution is ignored. Before writing CSS, convert the total design into a measurable layout blueprint:

- Record the reference canvas width and height, target viewport width, and screenshot scale ratio.
- Identify every horizontal section from top to bottom: header, hero, feature band, product grid, footer, etc. Measure each section's y-start, height, and percentage of the full page.
- Identify the global page container: full-bleed width, centered max-width, side gutters, and whether the design uses a fixed artboard width.
- Measure primary layout columns: left text block, right media block, center divider, card grid columns, gaps, and edge offsets. Store both pixel values and percentages.
- Measure vertical anchors: logo/nav baseline, hero title top, hero media top/bottom, CTA baseline, section transition lines, card top lines, footer baseline.
- Measure dominant asset bounding boxes: x, y, width, height, aspect ratio, and whether the asset is intentionally cropped or must remain complete.
- Measure text blocks by bounding box, not only font size. Match line breaks, block width, and vertical rhythm before tuning font.
- Derive CSS variables from the blueprint, for example --ref-width, --section-hero-h, --hero-left-x, --hero-media-w, --grid-gap.

Use this hierarchy when CSS disagrees with the reference:

1. Overall canvas/page width and side gutters.
2. Section heights and y positions.
3. Major column widths and x positions.
4. Asset bounding boxes and crop policy.
5. Text block widths and line breaks.
6. Font, shadow, color, and micro-details.

Do not let responsive convenience rewrite the desktop composition. At the reference desktop viewport, the implementation should preserve the same section proportions and object bounding boxes unless current business content makes that impossible.

Suggested blueprint artifact:

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

This skill includes scripts/extract_layout_blueprint.py as a starter helper. It records image size and optional manually supplied section/region boxes into a JSON artifact. Use manual boxes from screenshot inspection when automated detection would be unreliable.

- Canvas size and intended viewport.
- Layout grid, margins, gutters, major region sizes, alignments, and whitespace.
- Typography scale, line height, weight, letter spacing, title wrapping, button text fit.
- Radius, border opacity, shadow color/spread, blur/glass effects.
- Sampled palette from pixels, not memory: background, surfaces, primary, accent, text, muted text, border, shadow.
- Asset inventory: logo, marks, icons, product screenshots, cards, media, stickers, lines, arrows, background patches, flowers/leaves/characters/objects, avatars, button backgrounds.
- For each asset: semantic content or decorative. Decorative assets must be non-interactive and usually aria-hidden.

Create tokens from sampled values, not guessed colors:

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

### 4. Extract Assets With High Precision

Place extracted assets in one clear directory such as:

~~~text
public/assets/reference-style/
src/assets/reference-style/
~~~

Keep a manifest so replacements remain traceable:

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

Use scripts or image tools for precise crops. This skill includes scripts/prepare_reference_asset.py for deterministic crop/alpha/edge cleanup when Python and Pillow are available.

Strict crop rules:

1. Crop only from the reference image or user-provided replacement asset. No external downloads.
2. Output PNG or WebP. Assets needing transparency must have an alpha channel.
3. Do not preserve white rectangular backgrounds, black borders, hard crop edges, dirty residue, or obvious matte boxes unless the reference intentionally contains them.
4. If an asset has white edge, black edge, jaggies, halo, or background residue, fix in this order:
   - Re-crop with a slightly larger or cleaner source box.
   - Remove connected pure-white/near-white/near-background fields conservatively.
   - Feather the alpha edge by 1-2px.
   - Matte against the actual page background if transparency creates a halo.
   - Lightly adjust brightness, saturation, or temperature only to integrate the original source asset with the sampled page background.
   - If still bad, replace with a cleaner same-type asset from the same provided reference set.
   - If none works, report the limitation. Do not draw or generate a substitute.
5. Do not place blurry, low-resolution, partially cut-off, or edge-damaged crops in major visual positions.
6. Do not over-enlarge crops. If the target display size exceeds the crop's useful resolution, re-crop from a larger source region or use a cleaner source asset.
7. Transparent assets must be checked by alpha/pixel data. A transparent PNG may look black in some viewers; do not "fix" a black-looking preview until pixel inspection confirms black pixels are real.

Minimum asset QA:

- Inspect dimensions and aspect ratio.
- Check alpha exists where expected.
- Check edge pixels for white/black halos.
- Open the final asset in the browser via its served URL.
- Confirm it is not an HTML fallback and not stale cache.

### 5. Implement Layout From the Reference

Work large to small:

- Page background and global frame.
- Header/nav/sidebar geometry.
- Hero or primary region.
- Cards, tables, forms, modals, lists, dashboards.
- Real controls and state visuals.
- Decorative overlays.
- Hover/focus/active/loading/empty/error states.
- Responsive breakpoints.

Use stable CSS constraints instead of fragile magic numbers:

- max-width, grid tracks, aspect-ratio, clamp(), min(), max().
- object-fit: contain for illustrations that must never clip.
- background-size: contain when the complete source image must remain visible.
- background-size: cover only when cropping is intentional and acceptable.
- overflow: visible only for decorative wrappers where needed.
- overflow: hidden only when the reference visibly clips content or the asset sits safely inside padding.

Decoration layer rule:

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

For JSX/HTML:

~~~tsx
<img
  className="reference-decor"
  src="/assets/reference-style/decorative-asset.png"
  alt=""
  aria-hidden="true"
  draggable={false}
/>
~~~

Place decorative layers below popovers, dropdowns, modals, and functional panels. If a menu or UI panel is covered, fix z-index/layering without lowering accessibility or hiding the menu.

### 6. Replace Image-Like Buttons Without Losing Behavior

If the reference button is an image-like shape but the app button is functional, keep the original button and event handler. Replace only its visual layer.

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

Use the exported asset's true aspect ratio. Do not stretch or crop the button background. If text differs per button, preserve text as live DOM above the image.

### 7. Partial Replacement Rules

When the user asks to replace a specific asset:

- Find the exact existing node/class/asset currently used at that position.
- Replace the source or local visual layer at the same position unless the user asks to move it.
- Keep approximate existing size and layout first; tune only enough to avoid clipping, overlap, or poor alignment.
- Do not add a duplicate asset elsewhere.
- Do not change global styles or other pages.
- After replacement, search for leftover old decoration layers in that region.
- If the user says "remove your previous change," revert only your previous modification for that region. Do not reset unrelated accepted work.

## Visual QA Checklist

Compare reference and implementation at the same viewport size:

- Header/nav: position, logo size, active state, button shape, spacing.
- Main layout: region widths, vertical rhythm, text wrapping, card alignment, whitespace.
- Layout blueprint: page width, side gutters, section heights, y-starts, column ratios, and dominant asset bounding boxes match the reference at the reference viewport.
- Section distribution: no section is visually compressed or expanded compared with the reference unless required by real content.
- Fold position: the first viewport exposes the same amount of the next section as the reference when applicable.
- Images/decorations: complete asset visible, no missing corners, no unwanted clipping, no duplicate overlap.
- Edges: no white border, black rim, hard rectangle, dirty background, jaggy halo, or obvious matte mismatch.
- Scale: no blurry over-enlargement, no timid undersized asset when the reference is large.
- Text: no icon/text overlap, no hidden first characters, no overflow out of buttons/cards, no clipped long labels.
- Functional layers: dropdowns, panels, popovers, drawers, toasts, and modals appear above backgrounds and nav as intended.
- Forms: labels, placeholders, errors, focus rings, disabled/loading states remain visible.
- Lists/tables: filters, sorting, pagination, hover, empty states remain functional.
- Visual language: no unrelated default Material/Bootstrap/Ant look, no arbitrary gradients/orbs/icons unless the reference contains them.

When the user provides a screenshot or says "still wrong," treat that screenshot as authoritative. Fix the exact mismatch; do not broaden into a redesign.

## Responsive QA

Validate at least the reference desktop width plus common breakpoints:

- 1440px or design desktop width.
- 1200px.
- 1024px.
- 768px.
- 390px/375px.

Mobile must not:

- Lose navigation entries or real actions.
- Clip forms/cards/buttons.
- Let decorative assets cover buttons, text, inputs, or menus.
- Force horizontal scrolling for forms.
- Hide focus states.

Decorative assets may shrink, move, or disappear on small screens if that preserves functionality and matches the spirit of the reference.

## Motion

Replicate motion only if visible or requested. Otherwise use restrained CSS motion that does not introduce a new design language:

- Page/card enter: fade + translateY(8-14px), 240-700ms.
- Hover: translateY(-2px to -4px), slightly softer/stronger shadow.
- Decorative idle only when consistent: tiny float/sway/opacity, 4-8s.
- No dramatic bounce, spin, neon glow, parallax, or animation library unless the reference/app already uses it.

Always support reduced motion:

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

## Verification Commands

Run the project's available checks after implementation:

- Build/typecheck/lint/test when present.
- Browser visual checks with screenshots on the exact user URL and port.
- Open the served asset URLs directly.
- Click modified buttons and major nav entries.
- Open/close modified menus, dropdowns, panels, modals, drawers, and toasts.
- Test search/filter/sort/pagination if present in the touched page.
- Inspect console for runtime errors.

Do not enter credentials unless the user explicitly authorizes it.

## Common Failure Modes to Avoid

- Designing from taste instead of copying the reference.
- Inventing new icons, flowers, mascots, logos, gradients, backgrounds, or decorative elements.
- Using external assets because they look close.
- Cropping a button/decor and stretching it to fit text.
- Moving an asset when the user asked for same position, source replacement only.
- Fixing overlap by making the asset too small and unlike the reference.
- Leaving old duplicate decorations under the new one.
- Using cover where the user needs the whole image visible.
- Treating transparent preview black as real black without alpha inspection.
- Editing the wrong localhost port or stale build.
- Matching colors/assets while ignoring the reference's page-width, section-height, and column-size distribution.
- Letting content-driven auto layout stretch a section that should have a fixed reference proportion at desktop size.
- Using arbitrary max-width or padding values from common UI habits instead of measuring the design image.
- Letting decoration layers cover menus or functional panels.
- Screenshotting real UI to fake visual fidelity.

## Reusable Prompt Templates

Full page replication:

~~~text
Use $pixel-perfect-reference-ui. Rebuild/restyle this existing frontend page to match the provided total design reference as closely as possible. Reference path: [path]. Target URL/page: [url/page]. Treat the reference as the only visual source of truth and the current app as the only behavior source of truth. Preserve all business behavior exactly: APIs, routes, stores, auth, form fields, validation, filters, sorting, pagination, click actions, and user flows must not change. Extract visual assets only from the provided reference; do not use external assets or redraw similar visuals. Build real HTML/CSS/components for functional UI. Verify desktop/mobile screenshots, layout blueprint proportions, served asset URLs, and build/lint/typecheck if available. Report changed files, added assets, commands run, regression results, and any fidelity gaps.
~~~

Single asset replacement:

~~~text
Use $pixel-perfect-reference-ui. Replace only the [current asset/button/decoration] in [page/region/component] with the local asset/reference element at [path/name]. Keep the existing behavior, click events, route, form logic, state, and nearby layout. Preserve the new asset's original aspect ratio; do not stretch, crop, or over-enlarge it. Keep the same position unless I explicitly ask to move it. Remove white/black edges by re-cropping, transparency cleanup, 1-2px feathering, or matte blending. Do not change other pages/components. Verify no clipping, overlap, stale asset, or UI regression.
~~~

Position/size correction:

~~~text
Use $pixel-perfect-reference-ui. Adjust only [asset/component] on [page/url]. Current issue: [too small/clipped/overlapping/edge defect/wrong alignment]. Keep its source and overall design language. Modify only size, position, z-index, object-fit/background-size, or wrapper overflow enough to make it complete, aligned, and non-overlapping. Do not touch business logic or unrelated assets. Verify desktop and mobile.
~~~

Undo a mistaken visual pass:

~~~text
Use $pixel-perfect-reference-ui. Remove only your previous changes related to [asset/region/component]. Do not reset the repository or remove other accepted UI work. Restore the prior source/position/style for that specific region and verify there are no leftover duplicate assets, classes, or decorations.
~~~
