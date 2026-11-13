# Motion and 3D / 动效与三维

Pick the least complex renderer that reproduces observed behavior:

| Evidence | Implementation |
|---|---|
| Static render with no motion evidence | Original image/crop |
| Layer tilt, perspective, simple transform | CSS perspective/preserve-3d + WAAPI |
| Coordinated timeline / scroll-linked sequence | Existing animation stack, otherwise GSAP/ScrollTrigger |
| Raster text, displacement maps, masks, RGB split or lens refraction | Canvas/WebGL compositor; preserve the existing Pixi/filter stack when available |
| Actual geometry, lighting, shader or particle system | Existing renderer, otherwise Three.js |
| Original fixed playback clip, no interactive scene | Original video |

Never force Three.js on a CSS effect or rebuild an available illustration as approximate geometry. Use original model/textures when available. Record missing material, geometry, camera or shader information. A guessed shader is an approximation even if visually attractive. If the source is Canvas-based and DOM text has zero bounds, collect the rendered region and explicitly record that DOM measurement does not describe the visible text.

Capture: trigger, start/end, duration or scroll range, easing, direction, transform origin, pointer coordinates, reverse/exit state, mobile behavior and reduced-motion behavior. Check a continuous recording as well as samples at 0/25/50/75/100%; these samples alone can miss incorrect interpolation.

Local test adapter (development/test only):

```js
window.__pixelclone = {
  ready: Promise.resolve(), // replace with assets/fonts/renderer ready promise
  async setState({timeSeconds = 0, progress = 0, pointer = null}) {
    // Set WAAPI currentTime, GSAP timeline time, or Three mixer/camera explicitly.
    // Set any PRNG seed at scene initialization; do not depend on wall-clock time.
  },
  async render() { /* render one fully settled frame */ }
};
```

Implement this interface for the chosen effect; an empty adapter is not completion. `capture` with `state` waits for it and fails if absent. Third-party pages do not automatically expose it: replay supported actions, record timing uncertainty, and do not claim exact dynamic parity. `animationMode: static` only disables CSS/WAAPI screenshot animation; it does not freeze canvas, WebGL, video or arbitrary RAF loops.

Reduced motion must preserve information and usable controls: freeze decorative motion at a representative frame rather than reset layout transforms blindly. Pause offscreen/hidden animations, cap renderer DPR where needed, dispose GPU resources and restore original event handlers. Do not intercept pointer or keyboard interaction with decorative overlays.

## Interactive text and shader effects / 文字形变与着色器

When moving a pointer changes the shapes or language of visible glyphs, read [render-effects.md](render-effects.md) before implementation. A moving overlay and a working event handler only establish input plumbing; compare the affected glyph pixels and the full response over time. WebGL is not evidence of a geometric 3D scene.
