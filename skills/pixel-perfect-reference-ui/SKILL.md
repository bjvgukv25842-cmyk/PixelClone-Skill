---
name: pixel-perfect-reference-ui
description: Use when recreating a website from screenshots, a reference URL, video or local assets, or correcting visual mismatches in layout, typography, assets, 3D or interactive motion.
metadata:
  short-description: Evidence-based website reconstruction and evaluation
---

# PixelClone: evidence-based reconstruction

Reproduce the reference rather than redesign it. Preserve APIs, routes, state, authentication, validation, events, keyboard focus and accessibility. Change presentation only. Keep functional navigation, controls, text and forms as real DOM.

## Inputs and sources

Choose screenshot-only, website-resources or video mode. Record target URL, scope, reference viewport and DPR; image pixels are not necessarily CSS pixels. User originals, reference-site resources authorized for the task, and reference crops are valid sources. Do not compare runs with different input permissions.

Prefer original fonts, SVG, textures and models to redrawing. Do not silently substitute stock/generated art, approximate fonts or guessed models. Record missing evidence. If the user requests approximation, label it as such. A static image does not establish original motion.

## Workflow

1. Verify the actual runtime URL/port, scope and existing behavior.
2. Read [evidence and typography](references/evidence.md). Inventory sources, hashes, resource gaps, layout boxes, fonts and motion evidence.
3. Build a measured blueprint: page/section dimensions, columns, gutters and dominant media first; text and details second. Keep real controls and prevent decoration from occluding menus.
4. Crop/place assets at their original aspect ratio. Inspect alpha edges, resolution, object-fit, served URLs and cache. Separate button artwork from live text; never stretch patterns to fit labels.
5. For motion read [motion and 3D](references/motion.md). Select images, CSS/WAAPI, GSAP, Canvas/WebGL or Three.js from observed behavior, reusing an appropriate existing stack. For distorted text, lenses or color separation, use [render effects](references/render-effects.md) to record layers, filter order, glyph rasterization and pointer response, then verify actual deformation.
6. Use [commands](references/commands.md) to capture and compare, following [frozen-round evaluation](references/evaluation.md). Establish reference stability before grading.
7. Verify desktop, mobile, reduced motion, navigation/forms and existing project checks. Report errors and untested behavior explicitly.

## Evaluation and repair

Freeze skill, tools, inputs, model and budget per round. Do not edit the skill during a scored run. Deliver screenshots/recordings, difference images, font/resource evidence, requirement statuses and a humanReview field that stays null until user feedback.

Exact pixel equality requires raw pixel equality. Tolerance is not perceptual similarity. Static success is not dynamic or functional success. Inspect both global and critical-region errors; unstable references yield diagnostics, not an exact-pass claim.

Repair structure -> assets/fonts -> typography -> spacing -> color/shadows -> motion, at most three rounds by default. Classify source gaps, tool defects, execution mistakes and skill omissions before changing guidance. Only transferable findings enter the next version; keep hold-outs out of tuning.

## Delivery

Report scope, runnable artifact, reference provenance, evidence, remaining differences and user-review items. Missing fonts/assets/motion evidence remain explicit. One successful example does not establish a general success rate.
