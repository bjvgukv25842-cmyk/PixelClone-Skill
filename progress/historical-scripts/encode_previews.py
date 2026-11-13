from pathlib import Path
import subprocess,imageio_ffmpeg
base=Path('../outputs/pixelclone-review')
for arm in ['reference','control','old','candidate']:
 folder=base/arm/('motion' if arm=='reference' else 'recording')
 frames=list(folder.glob('frame-*.png'))
 if len(frames)==30:
  r=subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-nostdin','-y','-framerate','10','-i',str(folder/'frame-%03d.png'),'-c:v','libx264','-pix_fmt','yuv420p',str(base/arm/'preview.mp4')],capture_output=True)
  print(arm,len(frames),r.returncode)
 else: print(arm,'incomplete frames',len(frames))
