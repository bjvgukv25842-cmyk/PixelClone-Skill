# Tools / 工具接口

In an installed skill folder: run `npm ci`, `npx playwright install chromium`, and install `requirements.txt` into a project virtual environment. Do not install globally or add runtime libraries to the target frontend unless needed. Node >=20, Python >=3.10. Use `PIXELCLONE_PYTHON` for a virtual-environment interpreter; optional `PIXELCLONE_BROWSER_CHANNEL=msedge` records an explicit system-browser fallback. Never mix browser versions within a scored comparison. FFmpeg is optional (video only); use PIXELCLONE_FFMPEG or the pinned imageio-ffmpeg package.

From the installed skill root:

```text
node scripts/toolkit/pixelclone.mjs collect --type image --src reference.png --out evidence/image
node scripts/toolkit/pixelclone.mjs collect --config reference.json --out evidence/website
node scripts/toolkit/pixelclone.mjs collect --type video --src reference.mp4 --out evidence/video
node scripts/toolkit/pixelclone.mjs fonts --src original.woff2 --text "Target heading" --out evidence/font
node scripts/toolkit/pixelclone.mjs capture --config implementation.json --out evidence/implementation
node scripts/toolkit/pixelclone.mjs compare --reference reference.png --actual actual.png --config compare.json --out evidence/diff
node scripts/toolkit/pixelclone.mjs report --out evidence/diff
python scripts/prepare_reference_asset.py --src reference.png --out crop.png --box 0,0,100,100
python scripts/extract_layout_blueprint.py --src reference.png --out layout.json
```

In the source repository replace `scripts/toolkit/` with `toolkit/`. Exit codes: 0 successful operation (not necessarily task acceptance), 1 input/runtime error, 2 image comparison exceeds tolerance. Errors go to stderr; result JSON goes to stdout. No auto-resizing, credential entry, crawling or resource downloading.

Capture config:

```json
{"url":"http://localhost:3000","viewport":{"width":1440,"height":900},"deviceScaleFactor":1,"locale":"en-GB","timezoneId":"UTC","colorScheme":"light","animationMode":"live","fullPage":false,"regions":[{"name":"title","selector":"h1"}],"actions":[{"type":"hover","selector":".card"}],"state":{"progress":0.5},"recordVideo":false}
```

Omit state for sites without the local adapter. Actions: click(selector), hover(selector), scroll(x,y), pointer(x,y), wait(ms up to 30000), press(key), drag(from,to). Regions are CSS selectors for collection. Compare regions use integer screenshot pixels, not CSS pixels:

```json
{"threshold":0.1,"maxDiffRatio":0.01,"includeAA":false,"regions":[{"name":"title","x":40,"y":120,"width":600,"height":160}]}
```

Capture includes declared and actual fonts, selected text boxes and line counts, viewport/scroll, resources, missing images, runtime errors and bounded console errors (which include non-throwing shader failures), browser/environment and screenshot hash. Layout line counts are diagnostic for complex nested inline markup. Inspect actual text before asserting a line break match. A successful capture does not certify resource or functional correctness.

Set `hasTouch: true` and `isMobile: true` for a touch/mobile reference; a narrow viewport alone remains desktop input. Record DPR separately. Set `renderAudit: true` only for renderer diagnosis: it records bounded main-frame Canvas text/context calls and WebGL shader submissions (including sources and SHA256). See [render effects](render-effects.md) for coverage, timing and redistribution limits. Omit it for the uninstrumented visual baseline.
