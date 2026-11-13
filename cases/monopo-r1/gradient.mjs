// Local reference-derived gradient. GLSL and provenance live in assets/sources.json.
export async function createGradient(){
 const canvas=document.createElement('canvas');
 const gl=canvas.getContext('webgl2',{alpha:false,preserveDrawingBuffer:true});
 if(!gl)throw Error('WebGL2 is unavailable');
 const program=gl.createProgram();
 for(const [file,type] of [['gradient.vert',gl.VERTEX_SHADER],['gradient.frag',gl.FRAGMENT_SHADER]]){
  const response=await fetch(new URL('assets/'+file,import.meta.url));if(!response.ok)throw Error('Missing '+file);
  const shader=gl.createShader(type);gl.shaderSource(shader,await response.text());gl.compileShader(shader);
  if(!gl.getShaderParameter(shader,gl.COMPILE_STATUS))throw Error(gl.getShaderInfoLog(shader));gl.attachShader(program,shader);gl.deleteShader(shader);
 }
 gl.linkProgram(program);if(!gl.getProgramParameter(program,gl.LINK_STATUS))throw Error(gl.getProgramInfoLog(program));gl.useProgram(program);
 const buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,0,1,-1,0,-1,1,0,-1,1,0,1,-1,0,1,1,0]),gl.STATIC_DRAW);
 const position=gl.getAttribLocation(program,'position');gl.enableVertexAttribArray(position);gl.vertexAttribPointer(position,3,gl.FLOAT,false,0,0);
 const locations=new Map();const set=(name,values)=>{if(!locations.has(name))locations.set(name,gl.getUniformLocation(program,name));const location=locations.get(name);if(Array.isArray(values))gl['uniform'+values.length+'fv'](location,values);else gl.uniform1f(location,values);};
 for(const [name,value] of Object.entries({color1:[22/255,37/255,75/255],color2:[35/255,65/255,138/255],color3:[170/255,223/255,217/255],color4:[230/255,79/255,15/255],colorSize:.75,colorSpacing:.52,colorRotation:-.381592653589793,colorSpread:4.52,colorOffset:[-.7741174697875977,-.20644775390624992],transformPosition:[-.2816110610961914,-.43914794921875],zoom:.72,spacing:4.27,noiseSize:.5,noiseIntensity:.04}))set(name,value);
 return {canvas,resize(width,height){canvas.width=width;canvas.height=height;gl.viewport(0,0,width,height);set('viewportSize',[width,height]);},draw(force,seed){set('displacement',force);set('seed',seed);gl.drawArrays(gl.TRIANGLES,0,6);},destroy(){gl.deleteBuffer(buffer);gl.deleteProgram(program);}};
}
