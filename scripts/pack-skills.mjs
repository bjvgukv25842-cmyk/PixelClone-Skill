import fs from 'node:fs/promises';
import path from 'node:path';
const check=process.argv.includes('--check');
const root=path.resolve(import.meta.dirname,'..');
const source=path.join(root,'toolkit');
async function files(dir){const result=[];for(const e of await fs.readdir(dir,{withFileTypes:true})){if(e.name==='__pycache__')continue;const p=path.join(dir,e.name);if(e.isDirectory())result.push(...await files(p));else result.push(p);}return result;}
let errors=[];
for(const skill of ['pixel-perfect-reference-ui','pixel-perfect-reference-ui-zh']){
 const base=path.join(root,'skills',skill);
 const mappings=(await files(source)).map(f=>{const rel=path.relative(source,f);return [f,path.join(base,rel.startsWith('references'+path.sep)?rel:path.join('scripts','toolkit',rel))];});
 for(const legacy of ['prepare_reference_asset.py','extract_layout_blueprint.py'])mappings.push([path.join(source,'python',legacy),path.join(base,'scripts',legacy)]);
 for(const f of ['package.json','package-lock.json','requirements.txt'])mappings.push([path.join(root,f),path.join(base,f)]);
 for(const [src,dst] of mappings){const data=await fs.readFile(src);if(check){let target;try{target=await fs.readFile(dst);}catch{}if(!target||!target.equals(data))errors.push(path.relative(root,dst));}else{await fs.mkdir(path.dirname(dst),{recursive:true});await fs.writeFile(dst,data);}}
}
if(errors.length){console.error('Stale/missing packaged files:\n'+errors.join('\n'));process.exitCode=1;}else console.log(check?'Skill packages match canonical sources':'Both standalone skills packaged');
