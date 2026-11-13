# Monopo development repair — r1

Source-assisted, scoped reconstruction of https://monopo.london/: navigation, hero typography, pointer lens, background, cookies, a touch layout and reduced motion. This is a local development case, not a clean benchmark run. The previous three arms did not receive runtime/source evidence, so this repair cannot establish a causal skill uplift.

`scene.mjs` assembles a new PixiJS 6.2.0 scene and native DOM controls. It does not load the reference site's application bundle. The original fonts, lens, displacement map, mask, logo and gradient/filter shaders are used as authorized local reference inputs. Their source URLs and SHA256 are in `sources.json`. Captured shader debug macros are stripped before passing to Pixi, which adds its own wrappers.

The final runnable copy is in the workspace's `outputs/pixelclone-review/round-1/candidate/`. Serve that folder with an HTTP server; ES modules cannot run from a file URL. Original site resources in `assets/` and the Pixi vendor runtime in `vendor/` remain local and are excluded from the distributable skill and source archive. The archive's case code requires those declared resources; it is not an asset-complete offline case bundle.

From this repository with dependencies and local assets present:

```text
node cases/monopo-r1/verify.mjs
```

The adapter can set a settled pointer or resume live input, toggle displacement/color separation, set entry progress and render an explicit frame. Tests check changed glyph pixels, stable background under effect toggles, reverse/real pointer behavior, reduced motion, touch heading, cookies/menu and back-forward-cache restoration. These mechanical checks are not a visual similarity score.

Remaining scope limits: the page's downstream destination sections are inherited local scaffolds, not the original full site; the entry easing is not frame-calibrated; continuous motion and full acceptance await human review. Boundary states and every critical region remain in the report even if they fail tolerance. Mobile retains a menu control that differs from the sampled original initial viewport. No holdout case was used for this repair.

Technical references: [Pixi displacement](https://pixijs.download/v5.3.12/docs/PIXI.filters.DisplacementFilter.html), [Pixi filters](https://api.pixijs.io/pixi-filters-monorepo.html), [CDP screencast](https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-startScreencast).
