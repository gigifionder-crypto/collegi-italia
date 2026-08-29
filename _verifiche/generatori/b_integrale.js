const fs=require('fs');
const SP='/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad';
const D=require(SP+'/node_modules/docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,WidthType,BorderStyle,ShadingType,PageBreak,TableOfContents,ImageRun}=D;
const FONT="Barlow Semi Condensed";
const REPO='/home/user/collegi-italia';
function load(p){return fs.readFileSync(REPO+'/'+p,'utf8');}
const MAN=JSON.parse(fs.readFileSync(SP+'/figs_manifest.json','utf8'));
function delink(md){
  return md
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g,'$1 ($2)')
    .replace(/\[([^\]]+)\]\([^)]*\.(md|html|docx|txt)[^)]*\)/g,'`$1`');
}
const front=`# Aldo Moro

## Ottanta anni di Pace

**L'opera integrale «Una guerra senza fine» — il corpus storico completo del branch, in tredici Libri e cinque Appendici**

> **Il titolo.** «Ottanta anni di Pace» è la chiave interpretativa scelta dall'autore per questa edizione, e come ogni chiave del corpus si dichiara e non giudica. La Pace che il titolo conta è quella dei calendari e delle ricorrenze: proclamata nel maggio del 1945 e misurata da allora in anni. L'opera non la nega e non la irride — chiede che cosa quegli anni abbiano contenuto, e trova, nei documenti che raccoglie, che la pace dichiarata e la violenza praticata hanno convissuto a lungo. Il titolo si presta perciò a due letture che l'opera non scioglie: gli ottant'anni dal 1945, e il decennio Ottanta che il 1978 apre e a cui sopravvive. Ciò che dichiara è una continuità, non una responsabilità: è una lente, non una sentenza, e nessuna pagina che segue attribuisce a chicchessia ciò che una lente lascia vedere. L'opera resta, nel suo nome proprio, «Una guerra senza fine», e il Libro quarto porta il proprio: «Una Pace senza Pace».

---

*Settima edizione integrale rilegata — 28 agosto 2026 · Branch pubblico*

> **La rimozione del 27 agosto 2026, e perché i numeri non si toccano.** Questa
edizione è **priva del Libro secondo e del Libro terzo**, che portavano il
saggio-cerniera «Dal Che a Moro» e la parabola di Ernesto Guevara in sei parti:
sette documenti, 17.769 parole, rimossi per decisione dell'autore insieme al
volume tematico che li rilegava a parte. **La numerazione dei Libri superstiti non
è stata rifatta**: dopo il Libro primo viene il Libro quarto, e il salto è
voluto. Rinumerare avrebbe reso invisibile la rimozione e falsificato ogni
citazione anteriore; il salto la rende leggibile a chiunque apra l'indice. È la
stessa ragione per cui in quest'opera le correzioni si annotano accanto
all'errore e non al suo posto.

> **Le edizioni anteriori.** La quarta è del 26 agosto 2026 e portava quattordici Libri e due Appendici; la terza, del 25 agosto, la precedeva col medesimo impianto. Non sono ritirate né smentite: sono superate dalla crescita del corpus, e chi ne possiede un esemplare ha in mano un'edizione esatta alla propria data. La quinta, del 27 agosto, aggiungeva la terza campagna Farnesina nel Libro dodicesimo, il **Libro quindicesimo** (il Registro dei cinquantacinque giorni, opera seconda), le **undici appendici alla Fase settima** nel Libro nono e le **Appendici terza e quarta**; la sesta rimuoveva il materiale su Guevara. **Questa settima aggiunge il Libro sedicesimo, «Le tavole della custodia»**, in cinque parti: il fascicolo su vita, prigionia, mandanti ed esecutori con le quattordici piste in ordine di priorità istruttoria; le tre matrici delle ipotesi concorrenti — la custodia, via Fani, le omissioni — che il corpus prescriveva in più luoghi e non aveva mai costruito; e il quesito peritale sulla sola cella che quelle matrici dichiarano riempibile. Il loro risultato comune, che si annuncia qui perché muta la lettura di tutto ciò che precede: **in ciascuna delle tre tavole la maggioranza delle evidenze più citate ha diagnosticità nulla** — cinque su undici, tre su undici, sei su nove — e ciò che discrimina è ogni volta poco, tecnico, e ancora da leggere.

> **Ordine dell'opera.** Il volume raccoglie l'intero corpus nell'ordine di lettura: il **Portale** (l'edizione strutturata secondo l'architettura del Dossier maggiore); il **ritratto** dell'uomo; il **Dossier maggiore** dell'autore, «Una Pace senza Pace · Tutta la verità», qui conservato per intero come volume nel volume e con la divergenza di regime dichiarata in sua apertura; **il vettore e il ceppo** (Feltrinelli, Hyperion, la terza strada di Simioni); il **filo del 1926** (il Tribunale Speciale); le **questioni aperte**; il **metodo** (il presidio del garante e le metodologie calcolate); il **registro giudiziario** con le sue **undici appendici**, dalla quinta alla quindicesima; il **repertorio**; le **responsabilità personali** (il principio personalistico e la prosopografia dei tredici); la **dimensione diplomatica** (Moro alla Farnesina in tre campagne — la ricognizione-madre, le nove ricognizioni originali, le sedici della terza campagna coi sette registri analitici — e le pene oltre confine); il **fascicolo aperto** (il programma investigativo con le graduatorie e le schede, la quadriga a blocchi mirati e la triangolazione di un solo nome contro tutto il corpus in 4.999 blocchi: «Il codice e la sua trasmissione»); **il meridiano e la valle** (dal Sud Africa dell'apartheid alle imprese tecnologiche californiane, in mille blocchi); il **Registro dei cinquantacinque giorni**, opera seconda in sette Fasi e settanta Capitoli; e le cinque **Appendici** (l'apparato dei gradi; il pastiche dichiarato; la verifica di un elenco esterno; l'apparato di navigazione col dossier di invio; e l'apparato della verifica, con la certificazione dei numeri P2, la relazione della campagna di ricerca e il registro degli ingressi). **Questa edizione è integrale in senso stretto**, e lo è alla lettera: dei centonove documenti del perimetro moroteano ne entrano centosette, e i due che restano fuori sono nominati qui sotto con la propria ragione. Ne resta fuori, e per dichiarazione, l'opera «Italia Nera», che è un lavoro distinto e non una parte di questo.

> **I due documenti che restano fuori, e perché.** Il **registro delle impronte** non entra, e non può: misura questo volume, e rilegarlo dentro il volume che misura cambierebbe il volume e quindi la misura — è la stessa regola per cui il registro non certifica sé stesso. Il **memorandum operativo sulla riapertura delle verifiche** non entra per statuto proprio: è un documento di lavoro che dichiara da sé di non appartenere all'opera. Tutto il resto del perimetro moroteano è qui. Ne resta fuori per dichiarazione, e non per dimenticanza, anche **il romanzo che dal corpus si ricava**: è opera derivata, ha un proprio manifesto di impronte, e contare dentro l'opera ciò che l'opera ha prodotto sarebbe contarlo due volte.

> **Disciplina.** In ogni pagina vale la Regola di Ferro: gradi dichiarati (A giudicato · B accertamento · C congettura · F fatto pubblico · Stato Zero), criteri di smentita, esiti negativi come acquisizioni. Nessuna imputazione oltre il giudicato; nessuna graduatoria di persone — con l'unica eccezione, dichiarata in apertura del Libro quarto e valida soltanto entro di esso, della bilancia probabilistica che il Dossier maggiore porta con sé come volume nel volume: essa ordina per plausibilità e non per colpa, lavora per categorie di soggetti e non per nomi individuali, muove dai condannati in via definitiva e rifiuta di nominare un mandante esterno determinato; la colpa non è mai del gruppo ed è sempre della persona; gli assolti restano assolti; le sei vittime stanno in testa, non in fondo. I pastiche sono dichiarati e non sono parole di Aldo Moro. Un'indagine produce atti, non colpevoli.

\\newpage
`;
// L'ordine dell'opera sta in parti.json, sorgente unica: lo leggono anche
// gen_note.py e gen_figs.py. Prima esisteva in tre copie, e disallinearle
// produceva un volume incoerente coi propri grafici — errore gia' accaduto.
// Chi aggiunge un documento all'opera tocca parti.json e nient'altro.
const parts=JSON.parse(fs.readFileSync(__dirname+'/parti.json','utf8'))
  .parti.map(p=>({title:p.titolo, file:p.file}));


// Il titolo generale dell'opera, ripetuto in testa a certi sorgenti, e' ridondante
// sotto il titolo del Libro che il compositore ha gia' scritto: si toglie.
const TITOLI_GENERICI=[/^#\s*Aldo Moro\s*$/,/^#\s*Aldo Moro\s+—\s+Una guerra senza fine\s*$/];
function stripGenericTitle(md, hasTitle){
  if(!hasTitle) return md;
  const lines=md.split('\n');
  for(let i=0;i<lines.length;i++){
    if(!lines[i].trim()) continue;
    if(lines[i].startsWith('# ')){
      if(TITOLI_GENERICI.some(r=>r.test(lines[i].trim()))){ lines.splice(i,1); }
    }
    break;
  }
  return lines.join('\n');
}
let vol=front;
parts.forEach((p,idx)=>{
  if(p.title){ vol+='# '+p.title+'\n\n'; }
  vol+=delink(stripGenericTitle(load(p.file), !!p.title));
  vol+='\n\n\\figs:'+idx+'\n';
  vol+= (idx<parts.length-1) ? '\n\\newpage\n\n' : '\n';
});


// Nome breve della parte, per non ripetere la stessa intestazione a ogni capitolo.
function shortLabel(i){
  const t=(parts[Number(i)]||{}).title||'';
  const seg=t.split(' — ');
  if(seg.length>=2){
    const coda=seg[seg.length-1].replace(/^[IVX]+\.\s*/,'');
    return seg[0]+' · '+coda.slice(0,58);
  }
  return t.slice(0,72)||'il capitolo';
}
function runs(text, base={}){
  const out=[]; const re=/(\*\*(.+?)\*\*|\*([^*]+)\*|`([^`]+)`)/g; let last=0,m;
  while((m=re.exec(text))){
    if(m.index>last) out.push(new TextRun({text:text.slice(last,m.index),font:FONT,size:24,...base}));
    if(m[2]!==undefined) out.push(new TextRun({text:m[2].replace(/\*/g,''),font:FONT,size:24,bold:true,...base}));
    else if(m[3]!==undefined) out.push(new TextRun({text:m[3],font:FONT,size:24,italics:true,...base}));
    else if(m[4]!==undefined) out.push(new TextRun({text:m[4],font:FONT,size:24,italics:true,...base}));
    last=re.lastIndex;
  }
  if(last<text.length) out.push(new TextRun({text:text.slice(last),font:FONT,size:24,...base}));
  if(out.length===0) out.push(new TextRun({text:"",font:FONT,size:24,...base}));
  return out;
}
function stripMd(t){return t.replace(/\*\*/g,'').replace(/`/g,'').replace(/^\*|\*$/g,'');}
const lines=vol.split(/\r?\n/);
const children=[];
let i=0;
function tableBlock(rowsRaw){
  const rows=rowsRaw.filter(r=>!/^\s*\|?[\s:|-]+\|?\s*$/.test(r));
  const cells=rows.map(r=>r.replace(/^\s*\|/,'').replace(/\|\s*$/,'').split('|').map(c=>c.trim()));
  const ncol=Math.max(...cells.map(c=>c.length));
  const total=9360; const cw=Math.floor(total/ncol); const colWidths=Array(ncol).fill(cw);
  const trows=cells.map((row,ri)=>new TableRow({children:Array.from({length:ncol},(_,ci)=>{
    const txt=row[ci]||"";
    return new TableCell({width:{size:cw,type:WidthType.DXA},shading:ri===0?{type:ShadingType.CLEAR,fill:"1F3864"}:undefined,
      children:[new Paragraph({alignment:AlignmentType.JUSTIFIED,spacing:{after:20,before:20},
        children:runs(txt, ri===0?{bold:true,color:"FFFFFF",size:20}:{size:20})})]});
  })}));
  return new Table({width:{size:total,type:WidthType.DXA},columnWidths:colWidths,rows:trows});
}
while(i<lines.length){
  let ln=lines[i];
  if(/^\s*$/.test(ln)){i++;continue;}
  if(ln.trim()==='\\newpage'){children.push(new Paragraph({children:[new PageBreak()]}));i++;continue;}
  let fm;
  if((fm=ln.trim().match(/^\\figs:(\d+)$/))){
    const fl=MAN[fm[1]]||[];
    if(fl.length){
      children.push(new Paragraph({heading:HeadingLevel.HEADING_3,spacing:{before:240,after:80},children:runs('Apparato grafico — '+shortLabel(fm[1]))}));
      fl.forEach(f=>{
        const img=fs.readFileSync(SP+'/'+f.file);
        children.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:80,after:20},
          children:[new ImageRun({data:img,type:'png',transformation:{width:560,height:390}})]}));
        children.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:120},
          children:[new TextRun({text:f.caption,font:FONT,size:17,italics:true,color:'555555'})]}));
      });
      children.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:120},
        children:[new TextRun({text:"Le metriche dell'apparato contano parole, documenti e atti — mai colpe.",font:FONT,size:16,color:'777777'})]}));
    }
    i++;continue;
  }

  if(/^# /.test(ln)){children.push(new Paragraph({heading:HeadingLevel.HEADING_1,spacing:{before:240,after:120},children:runs(stripMd(ln.slice(2)))}));i++;continue;}
  if(/^## /.test(ln)){children.push(new Paragraph({heading:HeadingLevel.HEADING_2,spacing:{before:200,after:100},children:runs(stripMd(ln.slice(3)))}));i++;continue;}
  if(/^### /.test(ln)){children.push(new Paragraph({heading:HeadingLevel.HEADING_3,spacing:{before:160,after:80},children:runs(stripMd(ln.slice(4)))}));i++;continue;}
  if(/^---\s*$/.test(ln)){children.push(new Paragraph({border:{bottom:{color:"999999",space:1,style:BorderStyle.SINGLE,size:6}},spacing:{after:80}}));i++;continue;}
  if(/^>\s?/.test(ln)){
    let buf=[];
    while(i<lines.length && /^>\s?/.test(lines[i])){buf.push(lines[i].replace(/^>\s?/,''));i++;}
    const text=buf.join(' ').trim();
    children.push(new Paragraph({alignment:AlignmentType.JUSTIFIED,indent:{left:360,right:360},spacing:{before:80,after:80},
      border:{left:{color:"1F3864",space:8,style:BorderStyle.SINGLE,size:18}},children:runs(text,{italics:false})}));
    continue;
  }
  if(/^\s*\|/.test(ln)){
    let buf=[];while(i<lines.length && /^\s*\|/.test(lines[i])){buf.push(lines[i]);i++;}
    children.push(tableBlock(buf));children.push(new Paragraph({spacing:{after:80}}));continue;
  }
  if(/^\s*\d+\.\s+/.test(ln)){
    const text=ln.replace(/^\s*/,'');
    children.push(new Paragraph({alignment:AlignmentType.JUSTIFIED,indent:{left:360},spacing:{after:40},children:runs(text)}));i++;continue;
  }
  if(/^\s*[-*]\s+/.test(ln)){
    const text=ln.replace(/^\s*[-*]\s+/,'');
    children.push(new Paragraph({bullet:{level:0},alignment:AlignmentType.JUSTIFIED,spacing:{after:40},children:runs(text)}));i++;continue;
  }
  children.push(new Paragraph({alignment:AlignmentType.JUSTIFIED,spacing:{after:120,line:276},children:runs(ln)}));i++;
}
const doc=new Document({hyphenation:{autoHyphenation:true},
  styles:{default:{document:{run:{font:FONT,size:24}}},
    paragraphStyles:[
     {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:FONT,size:32,bold:true,color:"1F3864"},paragraph:{spacing:{before:240,after:120}}},
     {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:FONT,size:28,bold:true,color:"1F3864"},paragraph:{spacing:{before:200,after:100}}},
     {id:"Heading3",name:"Heading 3",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:FONT,size:24,bold:true,italics:true,color:"333333"},paragraph:{spacing:{before:160,after:80}}},
    ]},
  sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1440,bottom:1440,left:1440,right:1440}}},
    children:[new Paragraph({heading:HeadingLevel.HEADING_1,spacing:{after:120},children:[new TextRun({text:"Indice",font:FONT,size:32,bold:true,color:"1F3864"})]}),
      new TableOfContents("Sommario",{hyperlink:true,headingStyleRange:"1-2"}),
      new Paragraph({children:[new PageBreak()]}),
      ...children]}]
});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(REPO+'/UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.docx',b);console.log("scritto, bytes:",b.length);});
