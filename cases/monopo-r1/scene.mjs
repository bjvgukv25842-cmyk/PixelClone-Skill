import {createGradient} from './gradient.mjs';
const P=window.PIXI,hero=document.querySelector('.hero'),canvas=document.querySelector('#field');
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),touch=matchMedia('(pointer:coarse)');
const cookie=document.querySelector('.cookie'),menu=document.querySelector('.menu-toggle'),header=document.querySelector('.header');
try{cookie.hidden=localStorage.getItem('monopo-demo-cookie')==='accepted';}catch{}
document.querySelector('#accept').onclick=()=>{cookie.hidden=true;try{localStorage.setItem('monopo-demo-cookie','accepted');}catch{}};
const closeMenu=()=>{header.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.textContent='MENU';};
const updateClocks=()=>document.querySelectorAll('.clock').forEach((clock,i)=>clock.textContent=new Intl.DateTimeFormat('en-US',{timeZone:['Europe/London','Asia/Tokyo','America/New_York'][i],hour:'2-digit',minute:'2-digit',hour12:true}).format(new Date()));updateClocks();const clockTimer=setInterval(updateClocks,30000);
menu.onclick=()=>{const open=header.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'CLOSE':'MENU';};
document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu();});

let width=0,height=0,app,gradient,gradientTexture,background,scene,english,japanese,fringe;
let lens,circle,inverse,effectMask,displacementMap,displacement,rgb,frame,controlled=false;
let target={x:0,y:0,force:5,seed:.18},smooth={...target},effects=true,colorSplit=true,entry=1,startTime=0;
const groups=[];const sources={english:['We are a brand','of collective','creativity'],japanese:['私たちは','創造性を結集した','ブランド']};
function makeText(lines,family,size,lineHeight){
 const group=new P.Container();const offsets=[0,.1651*width,.10416*width];
 for(const [i,text] of lines.entries()){
  const item=new P.Text(text,{fontFamily:family,fontSize:size+'px',fill:'#FFFFFF',padding:100,trim:true});
  item.position.set(offsets[i],i*lineHeight);group.addChild(item);
 }
 return group;
}
function align(group){group.position.set(width/2-group.width/2,height/2-group.height/2);}
function viewport(){
 width=Math.round(hero.clientWidth);height=Math.round(hero.clientHeight);app.renderer.resize(width,height);gradient.resize(width,height);
 gradientTexture.noFrame=true;gradientTexture.baseTexture.setRealSize(width,height,1);gradientTexture.update();
 background.width=width;background.height=height;
 for(const group of groups.splice(0)){scene.removeChild(group);group.destroy({children:true});}
 english=makeText(sources.english,'Roobert',Math.max(width*.059895833333,47),0);
 const lineHeight=english.children[0].height*1.4;
 english.children.forEach((line,i)=>line.y=i*lineHeight);align(english);scene.addChild(english);groups.push(english);
 const makeFullLayer=()=>{const wrapper=new P.Container();const spacer=new P.Graphics();spacer.beginFill(0xff0000).drawRect(0,0,width,height).endFill();spacer.alpha=0;wrapper.addChild(spacer);const text=makeText(sources.japanese,'Noto Sans CJK JP',Math.max(width*.05,39),lineHeight);align(text);wrapper.addChild(text);scene.addChild(wrapper);groups.push(wrapper);return {wrapper,text};};
 japanese=makeFullLayer();fringe=makeFullLayer();
 english.mask=inverse;japanese.wrapper.mask=circle;fringe.wrapper.mask=effectMask;
 japanese.wrapper.filters=[displacement];fringe.wrapper.filters=[displacement,rgb];
 target={x:width/2,y:height/2,force:touch.matches?4.66:5,seed:touch.matches?-.06:.18};smooth={...target};
 hero.classList.toggle('gpu-ready',!touch.matches);scene.visible=!touch.matches;render();
}
function placeMasks(){
 const {x,y}=smooth;
 lens.position.set(x,y);effectMask.position.set(x,y);displacementMap.position.set(x,y);
 circle.clear().beginFill(0xffffff).drawCircle(x,y,125).endFill();
 inverse.clear().beginFill(0xffffff).drawRect(0,0,width,height).beginHole().drawCircle(x,y,125).endHole().endFill();
}
function animateText(){
 const t=1-entry,offsets=[0,.1651*width,.10416*width];
 for(const group of [english,japanese.text,fringe.text])for(const [i,line] of group.children.entries()){
  line.x=offsets[i]+(i===1?1:-1)*width*.1*t;line.alpha=entry;
 }
}
function render(){
 if(!app||!english)return;
 gradient.draw(smooth.force,smooth.seed);gradientTexture.update();placeMasks();animateText();
 displacement.scale.set(effects?20:0);rgb.enabled=effects&&colorSplit;
 scene.visible=!touch.matches;app.renderer.render(app.stage);
}
function pointer(e){
 if(reduced.matches||touch.matches||controlled)return;
 const rect=hero.getBoundingClientRect();const x=e.clientX-rect.left,y=e.clientY-rect.top;
 if(y<0||y>height)return;target={x,y,force:x/width*5,seed:y/height*2-1};
}
hero.addEventListener('pointermove',pointer);
// Reference freezes its last valid position outside the hero; keep that exit behavior.
function tick(now){
 frame=requestAnimationFrame(tick);if(document.hidden||controlled||!app)return;
 if(!reduced.matches){for(const key of Object.keys(smooth))smooth[key]+=.1*(target[key]-smooth[key]);entry=1-Math.pow(1-Math.min(1,Math.max(0,(now-startTime-400)/1200)),3);}
 render();
}
function onReduced(){if(reduced.matches){target={x:width/2,y:height/2,force:touch.matches?4.66:5,seed:touch.matches?-.06:.18};smooth={...target};entry=1;render();}}
reduced.addEventListener('change',onReduced);
async function init(){
 await Promise.all([document.fonts.load('86px Roobert'),document.fonts.load('72px "Noto Sans CJK JP"'),document.fonts.ready]);
 if(!P)throw Error('Local PixiJS runtime is missing');gradient=await createGradient();
 P.settings.FILTER_RESOLUTION=Math.min(devicePixelRatio,2);
 app=new P.Application({view:canvas,width:1440,height:900,resolution:Math.min(devicePixelRatio,2),autoDensity:true,autoStart:false,backgroundColor:0,preserveDrawingBuffer:true});app.stop();
 app.renderer.plugins.interaction.destroy();
 gradientTexture=P.Texture.from(gradient.canvas);background=new P.Sprite(gradientTexture);app.stage.addChild(background);
 scene=new P.Container();app.stage.addChild(scene);
 const textures=await Promise.all(['lense.png','mask.png','displace.png'].map(file=>new Promise((resolve,reject)=>{const texture=P.Texture.from('assets/'+file);if(texture.baseTexture.valid)resolve(texture);else{texture.baseTexture.once('loaded',()=>resolve(texture));texture.baseTexture.once('error',()=>reject(Error('Missing '+file)));}})));
 lens=new P.Sprite(textures[0]);lens.anchor.set(.5);scene.addChild(lens);
 effectMask=new P.Sprite(textures[1]);effectMask.anchor.set(.5);scene.addChild(effectMask);
 circle=new P.Graphics();inverse=new P.Graphics();scene.addChild(circle,inverse);
 displacementMap=new P.Sprite(textures[2]);displacementMap.anchor.set(.5);scene.addChild(displacementMap);displacement=new P.filters.DisplacementFilter(displacementMap);displacement.scale.set(20);
 // Captured shaders include the previous runtime's debug macro. Pixi adds its own.
 const shader=await Promise.all(['rgb.vert','rgb.frag'].map(async file=>{const response=await fetch('assets/'+file);if(!response.ok)throw Error('Missing '+file);return (await response.text()).replace(/^\s*#define SHADER_NAME.*$/gm,'');}));
 rgb=new P.Filter(shader[0],shader[1],{red:[-2,2],green:[1,1],blue:[2,-2]});
 viewport();onReduced();startTime=performance.now();frame=requestAnimationFrame(tick);addEventListener('resize',viewport);touch.addEventListener('change',viewport);
 return true;
}
// Adapter controls the actual rendering graph; normal pointer events remain the live path.
window.__pixelclone={
 ready:init(),
 async setState(state={}){
  await this.ready;controlled=state.live!==true;
  if(state.initial){target={x:width/2,y:height/2,force:touch.matches?4.66:5,seed:touch.matches?-.06:.18};smooth={...target};}
  if(state.pointer&&!reduced.matches&&!touch.matches){const {x,y}=state.pointer;target={x,y,force:x/width*5,seed:y/height*2-1};smooth={...target};}
  effects=state.effects??true;colorSplit=state.colorSplit??true;entry=reduced.matches?1:(state.progress??1);render();
 },async render(){await this.ready;render();}
};
window.__pixelclone.ready.catch(error=>{
 hero.classList.remove('gpu-ready');const message=document.createElement('p');message.className='render-error';message.textContent='Interactive render unavailable: '+error.message;hero.append(message);console.error(error);
});
addEventListener('pagehide',event=>{if(event.persisted)return;cancelAnimationFrame(frame);clearInterval(clockTimer);gradient?.destroy();app?.destroy(false,{children:true,texture:true,baseTexture:true});});
