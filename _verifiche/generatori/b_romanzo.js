const fs=require('fs');
const SP='/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad';
const D=require(SP+'/node_modules/docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,WidthType,BorderStyle,ShadingType,PageBreak}=D;
const FONT="Barlow Semi Condensed";
const md=fs.readFileSync('/home/user/collegi-italia/_romanzo/OTTANTA-ANNI-DI-PACE-prima-stesura.md','utf8');

function runs(t,{it=false,sz=21}={}){
  const out=[]; const re=/(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g; let last=0,m;
  while((m=re.exec(t))!==null){
    if(m.index>last) out.push(new TextRun({text:t.slice(last,m.index),font:FONT,size:sz,italics:it}));
    const s=m[0];
    if(s.startsWith('**')) out.push(new TextRun({text:s.slice(2,-2),font:FONT,size:sz,bold:true,italics:it}));
    else if(s.startsWith('`')) out.push(new TextRun({text:s.slice(1,-1),font:"Consolas",size:sz-2,italics:it}));
    else out.push(new TextRun({text:s.slice(1,-1),font:FONT,size:sz,italics:true}));
    last=re.lastIndex;
  }
  if(last<t.length) out.push(new TextRun({text:t.slice(last),font:FONT,size:sz,italics:it}));
  return out.length?out:[new TextRun({text:t,font:FONT,size:sz,italics:it})];
}
const cellP=(t,b)=>new Paragraph({children:runs(t.replace(/\*\*/g,''),{sz:19}).map(r=>{r.options&&(r.options.bold=b);return r;}),spacing:{before:40,after:40}});
function tabella(rows){
  const cols=rows[0].length, W=9000, cw=Math.floor(W/cols);
  return new Table({columnWidths:Array(cols).fill(cw),width:{size:W,type:WidthType.DXA},
    rows:rows.map((r,i)=>new TableRow({children:r.map(c=>new TableCell({
      width:{size:cw,type:WidthType.DXA},
      shading:i===0?{type:ShadingType.CLEAR,fill:"EFEFEA"}:undefined,
      children:[cellP(c,i===0)]}))}))});
}
const kids=[]; const L=md.split('\n');
let i=0, buf=[], tbl=[];
const flushBuf=()=>{ if(!buf.length) return; const t=buf.join(' ').trim(); buf=[];
  if(!t) return;
  const quote=t.startsWith('> ');
  const body=quote?t.replace(/^> ?/,'').replace(/\s*> ?/g,' '):t;
  const ital=/^\*[^*]/.test(body)&&body.trim().endsWith('*');
  kids.push(new Paragraph({children:runs(ital?body.replace(/^\*|\*$/g,''):body,{it:ital}),
    alignment:AlignmentType.JUSTIFIED,
    indent:quote?{left:340,right:340}:undefined,
    spacing:{after:quote?140:120,line:290},
    border:quote?{left:{style:BorderStyle.SINGLE,size:8,color:"9A9A93",space:10}}:undefined}));};
const flushTbl=()=>{ if(tbl.length){kids.push(tabella(tbl));kids.push(new Paragraph({text:"",spacing:{after:140}}));tbl=[];}};
for(;i<L.length;i++){
  const r=L[i];
  if(/^\|/.test(r)){ flushBuf();
    const cells=r.split('|').slice(1,-1).map(s=>s.trim());
    if(cells.every(c=>/^:?-{2,}:?$/.test(c)||c==='')) continue;
    tbl.push(cells); continue; }
  flushTbl();
  if(/^# /.test(r)){ flushBuf();
    if(kids.length) kids.push(new Paragraph({children:[new PageBreak()]}));
    kids.push(new Paragraph({children:runs(r.slice(2),{sz:32}),heading:HeadingLevel.HEADING_1,spacing:{before:200,after:200}})); continue; }
  if(/^## /.test(r)){ flushBuf();
    kids.push(new Paragraph({children:runs(r.slice(3),{sz:25}),heading:HeadingLevel.HEADING_2,spacing:{before:260,after:120}})); continue; }
  if(/^---\s*$/.test(r)){ flushBuf(); continue; }
  if(!r.trim()){ flushBuf(); continue; }
  buf.push(r.trim());
}
flushBuf(); flushTbl();
const doc=new Document({styles:{default:{document:{run:{font:FONT,size:21}}}},
  sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1400,bottom:1400,left:1400,right:1400}}},children:kids}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('/home/user/collegi-italia/_romanzo/OTTANTA-ANNI-DI-PACE-prima-stesura.docx',b);console.log('docx ok',b.length);});
