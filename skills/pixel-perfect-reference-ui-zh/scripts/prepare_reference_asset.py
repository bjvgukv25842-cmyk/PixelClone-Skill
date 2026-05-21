#!/usr/bin/env python3
"""Prepare a cropped reference asset for pixel-perfect UI replication.

This script crops from a user-provided reference image, optionally removes
near-background pixels connected to the image edges, feathers alpha edges,
mattes against a page background color, and writes a PNG/WebP asset plus a
JSON report.

Example:
  python scripts/prepare_reference_asset.py ^
    --src reference.png --out public/assets/reference-style/flower.png ^
    --box 120,80,480,620 --transparent-edge #fbfaf4 --threshold 26 --feather 1.5
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError as exc:
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = [int(round(float(p.strip()))) for p in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("--box must be x1,y1,x2,y2")
    x1, y1, x2, y2 = parts
    if x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("--box must have x2>x1 and y2>y1")
    return x1, y1, x2, y2


def parse_color(value: str) -> tuple[int, int, int]:
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if len(v) != 6:
        raise argparse.ArgumentTypeError("color must be #rgb or #rrggbb")
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def near(rgb: tuple[int, int, int], target: tuple[int, int, int], threshold: int) -> bool:
    return sum((int(rgb[i]) - int(target[i])) ** 2 for i in range(3)) ** 0.5 <= threshold


def remove_connected_edge_background(img: Image.Image, bg: tuple[int, int, int], threshold: int) -> Image.Image:
    rgba = img.convert("RGBA")
    px = rgba.load()
    w, h = rgba.size
    visited: set[tuple[int, int]] = set()
    q: deque[tuple[int, int]] = deque()

    def seed(x: int, y: int) -> None:
        if (x, y) not in visited and near(px[x, y][:3], bg, threshold):
            visited.add((x, y))
            q.append((x, y))

    for x in range(w):
        seed(x, 0)
        seed(x, h - 1)
    for y in range(h):
        seed(0, y)
        seed(w - 1, y)

    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                if near(px[nx, ny][:3], bg, threshold):
                    visited.add((nx, ny))
                    q.append((nx, ny))

    for x, y in visited:
        r, g, b, _ = px[x, y]
        px[x, y] = (r, g, b, 0)
    return rgba


def feather_alpha(img: Image.Image, radius: float) -> Image.Image:
    if radius <= 0:
        return img.convert("RGBA")
    rgba = img.convert("RGBA")
    r, g, b, a = rgba.split()
    alpha = a.filter(ImageFilter.GaussianBlur(radius=radius))
    return Image.merge("RGBA", (r, g, b, alpha))


def matte(img: Image.Image, bg: tuple[int, int, int]) -> Image.Image:
    rgba = img.convert("RGBA")
    background = Image.new("RGBA", rgba.size, (*bg, 255))
    return Image.alpha_composite(background, rgba).convert("RGB")


def alpha_edge_report(img: Image.Image) -> dict[str, object]:
    rgba = img.convert("RGBA")
    w, h = rgba.size
    alpha = rgba.getchannel("A")
    bbox = alpha.getbbox()
    edge_pixels = []
    px = rgba.load()
    for x in range(w):
        edge_pixels.append(px[x, 0])
        edge_pixels.append(px[x, h - 1])
    for y in range(h):
        edge_pixels.append(px[0, y])
        edge_pixels.append(px[w - 1, y])
    opaque_edges = sum(1 for p in edge_pixels if p[3] > 8)
    return {
        "size": [w, h],
        "alpha_bbox": list(bbox) if bbox else None,
        "opaque_edge_pixel_count": opaque_edges,
        "opaque_edge_pixel_ratio": round(opaque_edges / max(1, len(edge_pixels)), 4),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="Source reference image")
    parser.add_argument("--out", required=True, help="Output PNG/WebP path")
    parser.add_argument("--box", type=parse_box, help="Crop box x1,y1,x2,y2")
    parser.add_argument("--transparent-edge", type=parse_color, help="Remove connected edge background near this color")
    parser.add_argument("--threshold", type=int, default=24, help="Color distance threshold for background removal")
    parser.add_argument("--feather", type=float, default=0.0, help="Alpha feather radius in px, usually 1-2")
    parser.add_argument("--matte", type=parse_color, help="Flatten against page background color after alpha cleanup")
    parser.add_argument("--brightness", type=float, default=1.0)
    parser.add_argument("--saturation", type=float, default=1.0)
    parser.add_argument("--report", help="Optional JSON report path")
    args = parser.parse_args()

    src = Path(args.src)
    out = Path(args.out)
    img = Image.open(src).convert("RGBA")
    source_size = img.size
    if args.box:
        img = img.crop(args.box)

    if args.transparent_edge:
        img = remove_connected_edge_background(img, args.transparent_edge, args.threshold)
    if args.feather:
        img = feather_alpha(img, args.feather)
    if args.brightness != 1.0:
        img = ImageEnhance.Brightness(img).enhance(args.brightness)
    if args.saturation != 1.0:
        img = ImageEnhance.Color(img).enhance(args.saturation)
    if args.matte:
        img = matte(img, args.matte)

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)

    report = {
        "src": str(src),
        "out": str(out),
        "source_size": list(source_size),
        "crop_box": list(args.box) if args.box else None,
        "transparent_edge": args.transparent_edge,
        "threshold": args.threshold,
        "feather": args.feather,
        "matte": args.matte,
        "brightness": args.brightness,
        "saturation": args.saturation,
        "output": alpha_edge_report(img),
    }
    report_path = Path(args.report) if args.report else out.with_suffix(out.suffix + ".json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
