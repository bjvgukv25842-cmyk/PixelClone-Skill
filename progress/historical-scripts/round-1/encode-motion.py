from pathlib import Path
import json,subprocess,imageio_ffmpeg
base=Path('../outputs/pixelclone-review/round-1')
for label in ['reference','candidate']:
 folder=base/label/'recording';data=json.loads((folder/'timeline.json').read_text());frames=data['frames'];assert len(frames)>10
 lines=[]
 for i,frame in enumerate(frames):
  duration=frames[i+1]['timestamp']-frame['timestamp'] if i+1<len(frames) else .033
  assert duration>=0
  lines.extend(["file '"+frame['file']+"'",'duration '+str(max(duration,.001))])
 lines.append("file '"+frames[-1]['file']+"'")
 (folder/'frames.ffconcat').write_text('\n'.join(lines)+'\n')
 output=(base/label/'preview.mp4').resolve()
 result=subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-y','-loglevel','error','-f','concat','-safe','0','-i','frames.ffconcat','-fps_mode','vfr','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart',str(output)],cwd=folder,capture_output=True,text=True)
 assert result.returncode==0,result.stderr
 print(label,len(frames),'frames',round(frames[-1]['timestamp']-frames[0]['timestamp'],3),'seconds',output.stat().st_size,'bytes')
