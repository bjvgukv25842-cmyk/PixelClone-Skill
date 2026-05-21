#!/usr/bin/env python3
"""Create a layout blueprint JSON from a total website reference image.

The script intentionally does not pretend to auto-detect design intent. It records
image dimensions and converts manually supplied section/region boxes into both
pixel and percentage data, which is safer for pixel-level UI replication.

Examples:
  python scripts/extract_layout_blueprint.py ^
    --src reference.png --out reference-layout.json ^
    --viewport-width 1440 ^
    --section header:0,0,1920,112 ^
    --section hero:0,112,1920,932 ^
    --region heroText:120,310,540,740 ^
    --region heroMedia:760,250,1650,870:contain ^
    --grid 120,1680,12,24
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc


def parse_named_box(value: str) -> tuple[str, tuple[float, float, float, float], str | None]:
    if ":" not in value:
        raise argparse.ArgumentTypeError("box must be name:x1,y1,x2,y2 or name:x1,y1,x2,y2:fit")
    name, rest = value.split(":", 1)
    fit = None
    if ":" in rest:
        box_part, fit = rest.rsplit(":", 1)
    else:
        box_part = rest
    nums = [float(p.strip()) for p in box_part.split(",")]
    if len(nums) != 4:
        raise argparse.ArgumentTypeError("box must contain x1,y1,x2,y2")
    x1, y1, x2, y2 = nums
    if x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("box must have x2>x1 and y2>y1")
    return name.strip(), (x1, y1, x2, y2), fit.strip() if fit else None


def parse_grid(value: str) -> dict[str, float | int]:
    nums = [float(p.strip()) for p in value.split(",")]
    if len(nums) != 4:
        raise argparse.ArgumentTypeError("grid must be containerX,containerW,columns,gutter")
    container_x, container_w, columns, gutter = nums
    return {
        "containerX": container_x,
        "containerW": container_w,
        "columns": int(columns),
        "gutter": gutter,
    }


def box_record(box: tuple[float, float, float, float], canvas_w: int, canvas_h: int, fit: str | None = None) -> dict[str, object]:
    x1, y1, x2, y2 = box
    w = x2 - x1
    h = y2 - y1
    record: dict[str, object] = {
        "x": round(x1, 3),
        "y": round(y1, 3),
        "w": round(w, 3),
        "h": round(h, 3),
        "xPct": round(x1 / canvas_w, 6),
        "yPct": round(y1 / canvas_h, 6),
        "wPct": round(w / canvas_w, 6),
        "hPct": round(h / canvas_h, 6),
        "aspect": round(w / h, 6),
    }
    if fit:
        record["fit"] = fit
    return record


def css_vars(blueprint: dict[str, object]) -> str:
    canvas = blueprint["referenceCanvas"]
    lines = [":root {"]
    lines.append(f"  --ref-width: {canvas['width']}px;")
    lines.append(f"  --ref-height: {canvas['height']}px;")
    for section in blueprint.get("sections", []):
        key = section["name"].replace("_", "-")
        lines.append(f"  --section-{key}-y: {section['y']}px;")
        lines.append(f"  --section-{key}-h: {section['h']}px;")
    for name, region in blueprint.get("regions", {}).items():
        key = name.replace("_", "-")
        lines.append(f"  --region-{key}-x: {region['x']}px;")
        lines.append(f"  --region-{key}-y: {region['y']}px;")
        lines.append(f"  --region-{key}-w: {region['w']}px;")
        lines.append(f"  --region-{key}-h: {region['h']}px;")
    lines.append("}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="Reference design image")
    parser.add_argument("--out", required=True, help="Output layout blueprint JSON")
    parser.add_argument("--viewport-width", type=float, help="Target browser viewport width for comparison")
    parser.add_argument("--section", action="append", default=[], type=parse_named_box, help="name:x1,y1,x2,y2")
    parser.add_argument("--region", action="append", default=[], type=parse_named_box, help="name:x1,y1,x2,y2 or name:x1,y1,x2,y2:contain")
    parser.add_argument("--grid", type=parse_grid, help="containerX,containerW,columns,gutter")
    parser.add_argument("--css-out", help="Optional CSS variable output path")
    args = parser.parse_args()

    src = Path(args.src)
    with Image.open(src) as img:
        canvas_w, canvas_h = img.size

    scale = args.viewport_width / canvas_w if args.viewport_width else None
    sections = []
    for name, box, fit in args.section:
        rec = box_record(box, canvas_w, canvas_h, fit)
        rec["name"] = name
        sections.append(rec)
    sections.sort(key=lambda item: (item["y"], item["x"]))

    regions = {}
    for name, box, fit in args.region:
        regions[name] = box_record(box, canvas_w, canvas_h, fit)

    blueprint: dict[str, object] = {
        "sourceReference": str(src),
        "referenceCanvas": {"width": canvas_w, "height": canvas_h},
        "targetViewport": {"width": args.viewport_width} if args.viewport_width else None,
        "scale": round(scale, 6) if scale else None,
        "sections": sections,
        "regions": regions,
        "grid": args.grid,
        "notes": [
            "Use section heights and region boxes as the desktop composition baseline.",
            "Prefer percentages for responsive scaling, but preserve these proportions at the reference viewport.",
            "Manually verify fold position and dominant asset bounding boxes with browser screenshots.",
        ],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(blueprint, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.css_out:
        css_path = Path(args.css_out)
        css_path.parent.mkdir(parents=True, exist_ok=True)
        css_path.write_text(css_vars(blueprint), encoding="utf-8")
    print(json.dumps(blueprint, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
