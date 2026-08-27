// Compone in DOCX gli allegati del dossier di invio. Un file per allegato,
// perche' vanno spediti separatamente.
const fs=require('fs');
const SP='/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad';
const D=require(SP+'/node_modules/docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,WidthType,BorderStyle,ShadingType,PageBreak}=D;
const FONT="Barlow Semi Condensed";
const REPO='/home/user/collegi-italia';
const NEWPAGE='\\'+'newpage';   // mai in un template literal: diventerebbe \n + "ewpage"

function delink(md){
  return md
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g,'$1 ($2)')
    .replace(/\[([^\]]+)\]\([^)]*\.(md|html|docx|txt|pdf)[^)]*\)/g,'$1');
}
function runs(text, base={}){
  const out=[]; const re=/(\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`)/g; let last=0,m;
  while((m=re.exec(text))){
    if(m.index>last) out.push(new TextRun({text:text.slice(last,m.index),font:FONT,size:24,...base}));
    if(m[2]!==undefined) out.push(new TextRun({text:m[2],font:FONT,size:24,bold:true,...base}));
    else if(m[3]!==undefined) out.push(new TextRun({text:m[3],font:FONT,size:24,italics:true,...base}));
    else if(m[4]!==undefined) out.push(new TextRun({text:m[4],font:FONT,size:24,italics:true,...base}));
    last=re.lastIndex;
  }
  if(last<text.length) out.push(new TextRun({text:text.slice(last),font:FONT,size:24,...base}));
  if(out.length===0) out.push(new TextRun({text:"",font:FONT,size:24,...base}));
  return out;
}
const stripMd=t=>t.replace(/\*\*/g,'').replace(/`/g,'').replace(/^\*|\*$/g,'');
function tableBlock(rowsRaw){
  const rows=rowsRaw.filter(r=>!/^\s*\|?[\s:|]*-[\s:|-]*\|?\s*$/.test(r));
  const cells=rows.map(r=>r.replace(/^\s*\|/,'').replace(/\|\s*$/,'').split('|').map(c=>c.trim()));
  // intestazione dichiarata vuota — «| | |»: si toglie, non si stampa in bianco
  const vuota=cells.length>0 && cells[0].every(c=>!c);
  if(vuota) cells.shift();
  if(cells.length===0) return null;
  const ncol=Math.max(...cells.map(c=>c.length));
  const total=9360, cw=Math.floor(total/ncol);
  const trows=cells.map((row,ri)=>new TableRow({children:Array.from({length:ncol},(_,ci)=>{
    const head = ri===0 && !vuota;
    return new TableCell({width:{size:cw,type:WidthType.DXA},
      shading:head?{type:ShadingType.CLEAR,fill:"1F3864"}:undefined,
      children:[new Paragraph({alignment:AlignmentType.JUSTIFIED,spacing:{after:20,before:20},
        children:runs(row[ci]||"", head?{bold:true,color:"FFFFFF",size:20}:{size:20})})]});
  })}));
  return new Table({width:{size:total,type:WidthType.DXA},columnWidths:Array(ncol).fill(cw),rows:trows});
}
// I sorgenti sono impaginati a capo morbido intorno agli 80 caratteri: un
// paragrafo occupa piu' righe. Vanno ricongiunte prima di interpretare i
// marcatori, altrimenti un corsivo che scavalca il capoverso resta aperto e
// l'asterisco finisce stampato nel testo.
function ricongiungi(md){
  const src=md.split(/\r?\n/), out=[];
  const elenco=l=>/^\s*([-*]\s|\d{1,2}\.\s)/.test(l);
  const stacco=l=>/^\s*$/.test(l) || /^(#{1,6} |>|\s*\||---\s*$)/.test(l) || l.trim()===NEWPAGE;
  const speciale=l=>stacco(l) || elenco(l);
  for(let i=0;i<src.length;i++){
    if(stacco(src[i])){ out.push(src[i]); continue; }
    // una voce d'elenco assorbe le proprie righe di continuazione, che sono
    // rientrate e non aprono a loro volta un elenco
    let buf=src[i];
    while(i+1<src.length && !speciale(src[i+1])) buf+=' '+src[++i].trim();
    out.push(buf);
  }
  return out.join('\n');
}
function corpo(md){
  const lines=ricongiungi(md).split(/\r?\n/); const children=[]; let i=0;
  while(i<lines.length){
    const ln=lines[i];
    if(/^\s*$/.test(ln)){i++;continue;}
    if(ln.trim()===NEWPAGE){children.push(new Paragraph({children:[new PageBreak()]}));i++;continue;}
    if(/^# /.test(ln)){children.push(new Paragraph({heading:HeadingLevel.HEADING_1,spacing:{before:240,after:120},children:runs(stripMd(ln.slice(2)))}));i++;continue;}
    if(/^## /.test(ln)){children.push(new Paragraph({heading:HeadingLevel.HEADING_2,spacing:{before:200,after:100},children:runs(stripMd(ln.slice(3)))}));i++;continue;}
    if(/^### /.test(ln)){children.push(new Paragraph({heading:HeadingLevel.HEADING_3,spacing:{before:160,after:80},children:runs(stripMd(ln.slice(4)))}));i++;continue;}
    if(/^---\s*$/.test(ln)){children.push(new Paragraph({border:{bottom:{color:"999999",space:1,style:BorderStyle.SINGLE,size:6}},spacing:{after:80}}));i++;continue;}
    if(/^>\s?/.test(ln)){
      let buf=[]; while(i<lines.length && /^>\s?/.test(lines[i])){buf.push(lines[i].replace(/^>\s?/,''));i++;}
      children.push(new Paragraph({alignment:AlignmentType.JUSTIFIED,indent:{left:360,right:360},spacing:{before:80,after:80},
        border:{left:{color:"1F3864",space:8,style:BorderStyle.SINGLE,size:18}},children:runs(buf.join(' ').trim())}));
      continue;
    }
    if(/^\s*\|/.test(ln)){
      let buf=[]; while(i<lines.length && /^\s*\|/.test(lines[i])){buf.push(lines[i]);i++;}
      const tb=tableBlock(buf);
      if(tb){ children.push(tb); children.push(new Paragraph({spacing:{after:80}})); }
      continue;
    }
    if(/^\s*\d{1,2}\.\s+/.test(ln)){
      children.push(new Paragraph({alignment:AlignmentType.JUSTIFIED,indent:{left:360},spacing:{after:40},children:runs(ln.replace(/^\s*/,''))}));i++;continue;
    }
    if(/^\s*[-*]\s+/.test(ln)){
      const grezzo=ln.replace(/^\s*[-*]\s+/,'');
      const casella=/^\[ \]\s*/.test(grezzo);
      const t=grezzo.replace(/^\[ \]\s*/,'☐ ');
      // una voce da spuntare porta gia il proprio segno: il punto elenco la raddoppierebbe
      children.push(new Paragraph(casella
        ? {alignment:AlignmentType.JUSTIFIED,indent:{left:180},spacing:{after:40},children:runs(t)}
        : {bullet:{level:0},alignment:AlignmentType.JUSTIFIED,spacing:{after:40},children:runs(t)}));
      i++;continue;
    }
    children.push(new Paragraph({alignment:AlignmentType.JUSTIFIED,spacing:{after:120,line:276},children:runs(ln)}));i++;
  }
  return children;
}
function componi(sorgente, destinazione){
  const md=delink(fs.readFileSync(REPO+'/'+sorgente,'utf8'));
  const doc=new Document({hyphenation:{autoHyphenation:true},
    styles:{default:{document:{run:{font:FONT,size:24}}},
      paragraphStyles:[
       {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:FONT,size:32,bold:true,color:"1F3864"},paragraph:{spacing:{before:240,after:120}}},
       {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:FONT,size:28,bold:true,color:"1F3864"},paragraph:{spacing:{before:200,after:100}}},
       {id:"Heading3",name:"Heading 3",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:FONT,size:24,bold:true,italics:true,color:"333333"},paragraph:{spacing:{before:160,after:80}}},
      ]},
    sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1440,bottom:1440,left:1440,right:1440}}},
      children:corpo(md)}]});
  return Packer.toBuffer(doc).then(b=>{fs.writeFileSync(REPO+'/'+destinazione,b);console.log('  %s  ->  %s  (%d byte)',sorgente,destinazione,b.length);});
}
const LAVORI=[
 ['_diffusione-opera/pec-unica-formale.md','_diffusione-opera/PEC_UNICA_FORMALE.docx'],
 ['_diffusione-opera/capitolo-campione.md','_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.docx'],
 ['_diffusione-opera/scheda-dell-opera.md','_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.docx'],
 ['_diffusione-opera/curriculum-modello.md','_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.docx'],
 ['_diffusione-opera/checklist-di-invio.md','_diffusione-opera/CHECKLIST_DI_INVIO.docx'],
 ['_diffusione-opera/relazione-al-centro-flamigni.md','_diffusione-opera/RELAZIONE_SUL_PROGETTO.docx'],
 ['_diffusione-opera/lettera-fondazione-aldo-moro.md','_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.docx'],
 ['_diffusione-opera/proposte-chiarelettere-bompiani.md','_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.docx'],
 ['_diffusione-opera/richiesta-archivio-storico-camera.md','_diffusione-opera/RICHIESTA_ARCHIVIO_CAMERA.docx'],
 ['_diffusione-opera/deposito-zenodo.md','_diffusione-opera/DEPOSITO_ZENODO.docx'],
 ['_diffusione-opera/pec-presentazione-case-editrici.md','_diffusione-opera/PEC_PRESENTAZIONE_CASE_EDITRICI.docx'],
];
(async()=>{ for(const [a,b] of LAVORI) await componi(a,b); console.log('allegati composti:',LAVORI.length); })();
