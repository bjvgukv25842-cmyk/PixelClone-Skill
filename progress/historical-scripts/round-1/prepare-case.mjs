import fs from 'node:fs/promises';import crypto from 'node:crypto';
const root='cases/monopo-r1';await fs.mkdir(root+'/assets',{recursive:true});await fs.mkdir(root+'/vendor',{recursive:true});
const manifest=[];
for(const [file,url] of [
 ['assets/Roobert-Regular.woff2','https://monopo.london/fonts/Roobert-Regular.woff2'],
 ['assets/Roobert-Bold.woff2','https://monopo.london/fonts/Roobert-Bold.woff2'],
 ['assets/NotoSansCJKjp-Regular.woff2','https://monopo.london/fonts/NotoSansCJKjp-Regular.woff2'],
 ...['lense.png','displace.png','mask.png','footer-circles.svg','arrow_scroll.png'].map(x=>['assets/'+x,'https://monopo.london/'+x]),
 ['vendor/pixi.min.js','https://pixijs.download/v6.2.0/pixi.min.js']]){
 const r=await fetch(url);if(!r.ok)throw Error(url+' '+r.status);const b=Buffer.from(await r.arrayBuffer());await fs.writeFile(root+'/'+file,b);manifest.push({file,url,sha256:crypto.createHash('sha256').update(b).digest('hex'),scope:'local development evaluation; not bundled in the reusable skill'});
}
const probe=JSON.parse(await fs.readFile('work/round-1/source/probe.json'));
for(const [i,name] of [[0,'gradient.vert'],[1,'gradient.frag'],[11,'rgb.vert'],[12,'rgb.frag']]){
 const s=probe.shaders[i].source;await fs.writeFile(root+'/assets/'+name,s);manifest.push({file:'assets/'+name,url:'https://monopo.london/',evidence:'submitted WebGL shader, captured 2026-11-05',sha256:crypto.createHash('sha256').update(s).digest('hex'),scope:'source-assisted local diagnostic; excluded from skill/source ZIP'});
}
await fs.writeFile(root+'/sources.json',JSON.stringify(manifest,null,2));
let html=await fs.readFile('work/candidate/index.html','utf8');html=html.slice(0,html.indexOf('<script>'))+'<script src="vendor/pixi.min.js"></script><script type="module" src="scene.mjs"></script></body></html>';
html=html.replace('<title>monopo london — reference reconstruction</title>','<title>Monopo · round 1 render reconstruction</title>');
html=html.replace('<div class="noise"></div>','').replace(/<div class="lens" aria-hidden="true">.*?<\/div><\/div>/,'');
html=html.replace('</style>',`\n#field{z-index:-2}.hero.gpu-ready .headline{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);font-size:1px}.scroll img{width:17px;height:53px}.render-error{position:absolute;top:95px;left:24px;background:#111;padding:12px;max-width:420px;font-size:14px;z-index:25}\n</style>`);
html=html.replace('aria-label="Explore recent work">↓','aria-label="Explore recent work"><img src="assets/arrow_scroll.png" alt="">');
await fs.writeFile(root+'/index.html',html);
console.log('Prepared scoped case with '+manifest.length+' provenance entries');
