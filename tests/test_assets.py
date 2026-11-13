import json, subprocess, tempfile, unittest
from pathlib import Path
from PIL import Image
import sys
ROOT=Path(__file__).resolve().parents[1]
class Assets(unittest.TestCase):
 def test_blueprint_rejects_invalid_grid_and_viewport(self):
  with tempfile.TemporaryDirectory() as d:
   src=Path(d)/'source.png';Image.new('RGB',(8,8)).save(src)
   for args in [('--grid','0,8,0,2'),('--viewport-width','nan'),('--region','box:0,0,9,9')]:
    r=subprocess.run([sys.executable,str(ROOT/'toolkit/python/extract_layout_blueprint.py'),'--src',str(src),'--out',str(Path(d)/'out.json'),*args],capture_output=True)
    self.assertNotEqual(r.returncode,0,args)
 def run_asset(self,*args):
  return subprocess.run([sys.executable,str(ROOT/'toolkit/python/prepare_reference_asset.py'),*args],capture_output=True,text=True)
 def test_rejects_crop_outside_source(self):
  with tempfile.TemporaryDirectory() as d:
   src=Path(d)/'source.png';Image.new('RGB',(8,8),'white').save(src)
   r=self.run_asset('--src',str(src),'--out',str(Path(d)/'out.png'),'--box','0,0,9,9')
   self.assertNotEqual(r.returncode,0)
 def test_nested_report_and_transparency(self):
  with tempfile.TemporaryDirectory() as d:
   src=Path(d)/'source.png';im=Image.new('RGB',(8,8),'white');im.putpixel((4,4),(255,0,0));im.save(src)
   out=Path(d)/'out.png';report=Path(d)/'reports'/'asset.json'
   r=self.run_asset('--src',str(src),'--out',str(out),'--transparent-edge','#fff','--report',str(report))
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertEqual(Image.open(out).getpixel((0,0))[3],0)
   self.assertEqual(Image.open(out).getpixel((4,4))[3],255)
   self.assertIn('sha256',json.loads(report.read_text())['source'])
if __name__=='__main__':unittest.main()
