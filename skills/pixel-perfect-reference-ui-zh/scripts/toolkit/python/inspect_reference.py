"""Local image, font and video evidence. Never infer font identity from pixels."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess


def inspect_font(src, text):
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        raise SystemExit('Install fonttools and brotli: python -m pip install fonttools brotli')
    with TTFont(src) as font:
        cmap = font.getBestCmap() or {}
        return {'names': {str(i): font['name'].getDebugName(i) for i in (1, 2, 6)},
                'missingCharacters': sorted(set(c for c in text if not c.isspace() and ord(c) not in cmap)),
                'axes': [{'tag': a.axisTag, 'min': a.minValue, 'default': a.defaultValue, 'max': a.maxValue}
                         for a in font['fvar'].axes] if 'fvar' in font else [],
                'glyphCoverageCount': len(cmap)}


def inspect_image(src, out):
    try:
        from PIL import Image
    except ImportError:
        raise SystemExit('Install Pillow: python -m pip install Pillow')
    with Image.open(src) as im:
        rgba = im.convert('RGBA')
        rgba.save(out / 'reference.png')
        return {'width': im.width, 'height': im.height, 'mode': im.mode,
                'alphaExtrema': list(rgba.getchannel('A').getextrema()),
                'cssPixelScale': None, 'note': 'Set reference CSS viewport/DPR explicitly; no resizing performed.'}


def extract_video(src, out, fps):
    if not math.isfinite(fps) or fps <= 0 or fps > 60:
        raise ValueError('fps must be finite in (0, 60]')
    executable = os.environ.get('PIXELCLONE_FFMPEG') or shutil.which('ffmpeg')
    if not executable:
        try:
            import imageio_ffmpeg
            executable = imageio_ffmpeg.get_ffmpeg_exe()
        except ImportError:
            raise SystemExit('Install FFmpeg or imageio-ffmpeg; alternatively set PIXELCLONE_FFMPEG.')
    # showinfo follows fps: timestamps describe the output sampling timeline, not inferred source-frame PTS.
    r = subprocess.run([executable, '-nostdin', '-n', '-i', str(src), '-vf', f'fps={fps},showinfo',
                        str(out / 'frame-%06d.png')], capture_output=True, text=True, timeout=300)
    if r.returncode:
        raise RuntimeError(r.stderr[-3000:])
    times = re.findall(r'\bn:\s*\d+.*?pts_time:([\d.\-]+)', r.stderr)
    files = sorted(out.glob('frame-*.png'))
    if not files or len(times) != len(files):
        raise RuntimeError('Could not match extracted frames to output timestamps')
    from PIL import Image, ImageDraw
    thumb_w, thumb_h = 240, 160
    # Bound contact-sheet size; every frame remains in manifest even if omitted from preview.
    selected = list(range(len(files)))[::max(1, math.ceil(len(files) / 100))]
    sheet = Image.new('RGB', (4 * thumb_w, math.ceil(len(selected) / 4) * thumb_h), '#222222')
    draw = ImageDraw.Draw(sheet)
    for n, i in enumerate(selected):
        with Image.open(files[i]) as frame:
            frame.thumbnail((thumb_w, thumb_h - 24)); x, y = (n % 4) * thumb_w, (n // 4) * thumb_h
            sheet.paste(frame, (x, y)); draw.text((x + 4, y + thumb_h - 20), f'{float(times[i]):.3f}s', fill='white')
    sheet.save(out / 'contact-sheet.png')
    return {'fps': fps, 'timestampBasis': 'resampled output timeline',
            'frames': [{'file': f.name, 'timeSeconds': float(t)} for f, t in zip(files, times)]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=['image', 'video', 'fonts'])
    p.add_argument('--src', required=True); p.add_argument('--out', required=True)
    p.add_argument('--text', default=''); p.add_argument('--fps', type=float, default=2)
    a = p.parse_args(); src = Path(a.src); out = Path(a.out)
    if not src.is_file(): p.error('Source file does not exist')
    out.mkdir(parents=True, exist_ok=True)
    if src.resolve() in ((out / 'reference.png').resolve(), (out / 'manifest.json').resolve()):
        p.error('Source must be outside generated output paths')
    result = {'schemaVersion': 1, 'source': str(src.resolve()), 'sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'type': a.mode}
    if a.mode == 'image': result.update(inspect_image(src, out))
    elif a.mode == 'fonts': result.update(inspect_font(src, a.text))
    else: result.update(extract_video(src, out, a.fps))
    (out / 'manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=True))


if __name__ == '__main__':
    main()
