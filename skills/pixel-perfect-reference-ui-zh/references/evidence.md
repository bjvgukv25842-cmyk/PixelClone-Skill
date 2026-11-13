# Reference evidence / 参考证据

Choose the input track before implementation: screenshot-only, website-resources, or video. Keep tracks separate in comparisons. Record viewport, device pixel ratio, reference dimensions, environment, selected states and resource permissions. A screenshot's pixels are not automatically CSS pixels.

Website mode: use `collect --config ...`; the browser collects resource URLs, currentSrc, CSS backgrounds, inline SVG, fonts, canvas/video bounds, selected text boxes and network failures. Discovery does not automatically download or grant redistribution rights. Use original assets only within the authorized task, keep source URL + SHA256 + role, and do not put proprietary fonts in a public skill package. Do not copy the reference site's application bundle as the reconstruction.

Image mode: `collect --type image --src ...` records dimensions/alpha and preserves a canonical PNG without resizing. Mark inferred boxes as inferred. Use the existing crop/blueprint Python commands for measured coordinates. Missing hidden pixels cannot be recovered by cropping. Inspect crops on checkerboard and intended background; threshold removal can erase intentional near-background parts. Use lossless output for typography and sharp edges.

Video mode: `collect --type video --src ... --fps 2` emits frames and a contact sheet. Timestamp basis is the resampled output timeline. Inspect the full clip, select exact key times when 2 fps misses a fast event. Do not infer DOM or font identity from a video. User-provided motion specification is valid evidence; a single static image is not a motion specification.

Source priority: user-specified original -> authorized reference resource -> reference crop -> explicit missing item. No stock/generated substitute without a user instruction. Never silently turn a missing item into a passing requirement.

Readiness: wait for document fonts and visible image decoding; inspect failed fonts/images and console errors. Lazy sections must be scrolled into view and captured individually. Long-page captures with sticky sections or WebGL require viewport state captures, not a stitched screenshot as motion evidence.

For typography use `fonts --src font.woff2 --text "target text"` and browser `fonts --config ...`. Inspect font names, axes and missing codepoints plus actual Chromium platform fonts for selected nodes. CSS fontFamily is only a declaration. Check glyph coverage, actual face/weight, text box, line count, letter spacing, line height, OpenType features (liga/kern), font-kerning and text-rendering. Identical font files can still differ when these settings or text-size-adjust differ. Font loading completion alone is not proof of correct rendering. Screenshot-only identification remains a hypothesis; never stretch text or rasterize functional text to fake a match.

If the visible heading is in Canvas/WebGL while its DOM bounds are empty, CDP's DOM font report does not audit the visible text. Use opt-in `renderAudit: true` and [render-effects.md](render-effects.md) to inspect the text rasterization and compositor. Compare trim, texture resolution, masks, displacement and color separation separately from font identity.

The collection output can include website text, resource URLs and query strings. Inspect before sharing; exclude credentials, personal data and unrelated requests from public reports.
