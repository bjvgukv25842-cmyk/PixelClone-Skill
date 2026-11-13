# Rendered typography and pointer effects / 渲染文字与指针效果

Use for lens refraction, text distortion, displacement, RGB split or apparently three-dimensional screen effects. First distinguish geometry/camera/light changes from image-space filters. A matching font file solves glyph identity, not the compositor that changes its appearance.

## Evidence contract

Before building the effect, save a case-specific `render-contract.json` with:

- `inputTrack`: screenshot-only, website-resources, or video. For website inputs add `sourceAccess`: assets-only or runtime-and-published-source. Record newly granted or newly used inputs; expanded inputs invalidate direct comparison with an earlier arm.
- `layers`: for each visible layer, its role, renderer, source URL/hash, text or asset, measured bounds, blend/mask/filter order, and evidence. Mark unknown fields explicitly.
- `typography`: actual font resource and glyph coverage, canvas/DOM text ownership, raster resolution/DPR, padding/trim, line origin and baseline, and post-processing. Keep the meaningful heading in accessible DOM when the visual copy is GPU-rendered.
- `response`: trigger, pointer coordinate space, target mapping, smoothing/inertia, displaced layer, filter strength/radius, entry/exit/reverse behavior and reduced motion. Distinguish observed values from inferred ones.
- `checks`: requirements with evidence paths and `pass`, `fail` or `unverified`; font availability, pointer delivery and visual deformation are separate requirements.

For a URL, `renderAudit: true` in a capture config records bounded canvas context, text-draw and submitted shader evidence. This opt-in probe runs before navigation and may perturb timing: pair it with an uninstrumented visual capture. Canvas text draws record the **declared** font; validate actual glyph appearance separately. The probe does not cover workers/OffscreenCanvas, WebGPU or other frames and does not establish that a shader compiled or affected visible pixels. Preserve these limits in the report. Keep captured shader sources out of public skill packages unless redistribution is permitted.

If source inspection is permitted, use it to resolve the rendering graph, texture roles and coordinate mappings. Implement the scoped scene independently; do not load the original application bundle as the replica. Otherwise derive measurements from recordings and report unresolved rendering details. A missing rendering mechanism is an unmet requirement under a faithful-source brief, even if a decorative substitute looks plausible.

## Build and check the causal chain

1. Render the unfiltered text at the measured bounds after fonts load. Compare its line breaks and glyph edges before tuning an effect.
2. Recreate the layer order. Displacement before a circular mask, displacement after a mask and a translated DOM layer yield different edge pixels. Test the order at a lens boundary.
3. Feed pointer coordinates through the observed mapping and smoothing into the renderer. Keep pointer position distinct from its smoothed state. For an adapter, set **both** and render a settled frame; for live playback, preserve the transient.
4. Replay a path across a glyph, a blank area, then the same glyph in reverse. Sample start, 25%, 50%, 75%, end, post-stop settling and exit. Store intended pointer positions and actual elapsed capture times. Watch the continuous result as well.
5. At the same endpoint, approach from opposite directions and compare settling. Change viewport/DPR and test touch and reduced motion using the reference's observed behavior. Touch behavior need not reproduce a desktop cursor lens.

Check both page exceptions and captured console errors: a GPU compile failure may only be logged. Submitted shader source can contain renderer-injected defines/version headers; when adapting permitted source, preserve provenance and let the target renderer supply its own wrappers.

Inspect a tight glyph region to ensure it warps/refracts rather than only translating, clipping or revealing baked pixels. A pixel change proves a response exists; it does **not** prove the reference response matches. Compare corresponding reference frames and have the user judge the motion; if reference time cannot be controlled, label numerical scores diagnostic.

Keep a case-specific executable regression for the observed mechanism: e.g. disabling the displacement filter at a fixed pointer must change the glyph region, while the background remains stable. This detects a renderer accidentally becoming a mock. Never put the case's filter constants, colors or coordinates into generic skill rules.
