import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[1]


class Media(unittest.TestCase):
    def inspect(self, mode, src, out, *args):
        result = subprocess.run([sys.executable, str(ROOT/'toolkit/python/inspect_reference.py'), mode,
                                 '--src', str(src), '--out', str(out), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_font_missing_glyph_is_reported(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d)/'test.ttf'; builder = FontBuilder(1000, isTTF=True)
            builder.setupGlyphOrder(['.notdef', 'A']); builder.setupCharacterMap({65:'A'})
            builder.setupGlyf({g:TTGlyphPen(None).glyph() for g in ['.notdef','A']})
            builder.setupHorizontalMetrics({g:(500,0) for g in ['.notdef','A']})
            builder.setupHorizontalHeader(ascent=800, descent=-200)
            builder.setupNameTable({'familyName':'Fixture','styleName':'Regular'})
            builder.setupOS2(); builder.setupPost(); builder.setupMaxp(); builder.save(src)
            report = self.inspect('fonts', src, Path(d)/'out', '--text', 'AB')
            self.assertEqual(report['missingCharacters'], ['B'])
            self.assertEqual(report['names']['1'], 'Fixture')

    def test_image_preserves_size_and_alpha(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d)/'in.png'; Image.new('RGBA',(7,9),(0,0,0,0)).save(src)
            r = self.inspect('image', src, Path(d)/'out')
            self.assertEqual((r['width'],r['height']),(7,9)); self.assertEqual(r['alphaExtrema'],[0,0])

    def test_video_extracts_frames_with_timestamps(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d)/'test.mp4'
            subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-nostdin','-y','-f','lavfi','-i',
                            'color=c=red:s=64x64:d=1:r=10','-pix_fmt','yuv420p',str(src)],check=True,capture_output=True)
            r = self.inspect('video',src,Path(d)/'out')
            self.assertEqual(len(r['frames']),2)
            self.assertEqual([f['timeSeconds'] for f in r['frames']],[0,0.5])
            self.assertTrue((Path(d)/'out/contact-sheet.png').is_file())

if __name__ == '__main__': unittest.main()
