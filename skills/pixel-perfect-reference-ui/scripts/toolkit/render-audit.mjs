// Opt-in diagnostic installed before navigation. It observes calls, never replays them.
export function installRenderAudit(){
 const contexts=[],textDraws=[],shaders=[],limits={contexts:32,textDraws:100,shaders:64,shaderCharacters:300000};
 let truncated=false,characters=0;
 const ids=new WeakMap();let nextId=0;
 const id=canvas=>{if(!ids.has(canvas))ids.set(canvas,++nextId);return ids.get(canvas);};
 const original=HTMLCanvasElement.prototype.getContext;
 HTMLCanvasElement.prototype.getContext=function(type,...args){
  const result=original.call(this,type,...args);
  if(result&&!contexts.some(c=>c.canvas===this&&c.type===type)){
   if(contexts.length<limits.contexts)contexts.push({canvas:this,type,id:id(this)});else truncated=true;
  }
  return result;
 };
 for(const method of ['fillText','strokeText']){
  const original=CanvasRenderingContext2D.prototype[method];
  CanvasRenderingContext2D.prototype[method]=function(text,...args){
   // Match the native call first: diagnostics must not turn a failed draw into evidence.
   const result=original.call(this,text,...args);
   // Object coercion may be stateful; native drawing already performed it once.
   const textCaptured=text===null||!['object','function'].includes(typeof text);
   const item={canvasId:id(this.canvas),method,font:this.font,text:textCaptured?String(text).slice(0,300):'[non-primitive text: not inspected]',textCaptured};
   if(!textDraws.some(x=>x.canvasId===item.canvasId&&x.font===item.font&&x.text===item.text&&x.method===method)){
    if(textDraws.length<limits.textDraws)textDraws.push(item);else truncated=true;
   }
   return result;
  };
 }
 for(const Type of [window.WebGLRenderingContext,window.WebGL2RenderingContext].filter(Boolean)){
  const original=Type.prototype.shaderSource;
  Type.prototype.shaderSource=function(shader,source){
   const result=original.call(this,shader,source);
   if(typeof source==='string'&&!shaders.some(x=>x.source===source)){
    if(shaders.length<limits.shaders&&characters+source.length<=limits.shaderCharacters){
     characters+=source.length;shaders.push({canvasId:id(this.canvas),stage:this.getShaderParameter(shader,this.SHADER_TYPE)===this.VERTEX_SHADER?'vertex':'fragment',source});
    }else truncated=true;
   }
   return result;
  };
 }
 window.__pixelcloneRenderAudit=()=>({
  contexts:contexts.map(({canvas,type,id})=>({id,type,width:canvas.width,height:canvas.height,connected:canvas.isConnected,rect:canvas.getBoundingClientRect().toJSON()})),
  textDraws,shaders,truncated,limits,isFidelityProof:false,
  coverage:'Main-frame HTML canvas calls, including detached/shadow canvases. Worker/OffscreenCanvas, WebGPU and cross-frame renderers are not covered. Declared canvas font is not proof of the actual glyph face. Shader submission is not proof of successful compilation or visible use.'
 });
}
