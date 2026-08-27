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

**L'opera integrale «Una guerra senza fine» — il corpus storico completo del branch, in quattordici libri e due appendici**

> **Il titolo.** «Ottanta anni di Pace» è la chiave interpretativa scelta dall'autore per questa edizione, e come ogni chiave del corpus si dichiara e non giudica. La Pace che il titolo conta è quella dei calendari e delle ricorrenze: proclamata nel maggio del 1945 e misurata da allora in anni. L'opera non la nega e non la irride — chiede che cosa quegli anni abbiano contenuto, e trova, nei documenti che raccoglie, che la pace dichiarata e la violenza praticata hanno convissuto a lungo. Il titolo si presta perciò a due letture che l'opera non scioglie: gli ottant'anni dal 1945, e il decennio Ottanta che il 1978 apre e a cui sopravvive. Ciò che dichiara è una continuità, non una responsabilità: è una lente, non una sentenza, e nessuna pagina che segue attribuisce a chicchessia ciò che una lente lascia vedere. L'opera resta, nel suo nome proprio, «Una guerra senza fine», e il Libro quarto porta il proprio: «Una Pace senza Pace».

---

*Edizione integrale rilegata — 25 agosto 2026 · Branch pubblico*

> **Ordine dell'opera.** Il volume raccoglie l'intero corpus nell'ordine di lettura: il **Portale** (l'edizione strutturata secondo l'architettura del Dossier maggiore); il **ritratto** dell'uomo; il **saggio-cerniera** Dal Che a Moro; la **parabola di Guevara** in sei studi; il **Dossier maggiore** dell'autore, «Una Pace senza Pace · Tutta la verità», qui conservato per intero come volume nel volume e con la divergenza di regime dichiarata in sua apertura; **il vettore e il ceppo** (Feltrinelli, Hyperion, la terza strada di Simioni); il **filo del 1926** (il Tribunale Speciale); le **questioni aperte**; il **metodo** (il presidio del garante e le metodologie calcolate); il **registro giudiziario**; il **repertorio**; le **responsabilità personali** (il principio personalistico e la prosopografia dei tredici); la **dimensione diplomatica** (Moro alla Farnesina e le pene oltre confine); il **fascicolo aperto** (il programma investigativo con le graduatorie e le schede, la quadriga a blocchi mirati e, in chiusura, la triangolazione di un solo nome contro tutto il corpus in mille blocchi: «Il codice e la sua trasmissione»); e le **appendici** (l'apparato dei gradi; il pastiche dichiarato). **Questa edizione è integrale in senso stretto**: le nove ricognizioni originali della cartella Farnesina e la triangolazione della seconda campagna, che le edizioni precedenti rappresentavano soltanto con la loro collazione, vi compaiono per esteso nel Libro dodicesimo. Nessun documento del corpus moroteano resta fuori.

> **Disciplina.** In ogni pagina vale la Regola di Ferro: gradi dichiarati (A giudicato · B accertamento · C congettura · F fatto pubblico · Stato Zero), criteri di smentita, esiti negativi come acquisizioni. Nessuna imputazione oltre il giudicato; nessuna graduatoria di persone — con l'unica eccezione, dichiarata in apertura del Libro quarto e valida soltanto entro di esso, della bilancia probabilistica che il Dossier maggiore porta con sé come volume nel volume: essa ordina per plausibilità e non per colpa, lavora per categorie di soggetti e non per nomi individuali, muove dai condannati in via definitiva e rifiuta di nominare un mandante esterno determinato; la colpa non è mai del gruppo ed è sempre della persona; gli assolti restano assolti; le sei vittime stanno in testa, non in fondo. I pastiche sono dichiarati e non sono parole di Aldo Moro. Un'indagine produce atti, non colpevoli.

\\newpage
`;
const parts=[
 {title:'Portale — L\'edizione strutturata: la mappa dell\'opera', file:'aldo-moro-una-guerra-senza-fine-edizione-strutturata.md'},
 {title:'Libro primo — Il ritratto: l\'uomo prima del caso', file:'aldo-moro-una-guerra-senza-fine-fase-ottava-il-ritratto.md'},
 {title:'Libro secondo — Dal Che a Moro: il saggio-cerniera', file:'dal-che-a-moro-una-guerra-senza-fine.md'},
 {title:'Libro terzo — La parabola di Guevara — I. Origini ed esilio', file:'guevara-origini-esilio-messicano.md'},
 {title:'Libro terzo — La parabola di Guevara — II. Dal Messico all\'Avana', file:'guevara-messico-avana-1954-1965.md'},
 {title:'Libro terzo — La parabola di Guevara — III. Da Mosca alla Bolivia', file:'guevara-mosca-bolivia-1964-1966.md'},
 {title:'Libro terzo — La parabola di Guevara — IV. La campagna boliviana', file:'guevara-campagna-boliviana-1966-1967.md'},
 {title:'Libro terzo — La parabola di Guevara — V. Bibliografia critica', file:'guevara-bibliografia-critica.md'},
 {title:'Libro terzo — La parabola di Guevara — VI. Le triangolazioni Guevara-Moro', file:'triangolazioni-guevara-moro.md'},
 {title:'Libro quarto — Il Dossier maggiore: «Una Pace senza Pace · Tutta la verità»', file:'dossier-maggiore-una-pace-senza-pace.md'},
 {title:'Libro quinto — Il vettore e il ceppo — I. Feltrinelli, il vettore', file:'feltrinelli-il-vettore.md'},
 {title:'Libro quinto — Il vettore e il ceppo — II. La triangolazione di Feltrinelli', file:'triangolazione-feltrinelli-corpus.md'},
 {title:'Libro quinto — Il vettore e il ceppo — III. Il nodo Hyperion', file:'triangolazione-hyperion-corpus.md'},
 {title:'Libro quinto — Il vettore e il ceppo — IV. L\'incrocio Feltrinelli-Hyperion', file:'triangolazione-feltrinelli-hyperion.md'},
 {title:'Libro quinto — Il vettore e il ceppo — V. Il ceppo Simioni: la terza strada', file:'ceppo-simioni-cpm-superclan-hyperion.md'},
 {title:'Libro sesto — Il filo del 1926 — I. Il Tribunale Speciale: l\'istituzione', file:'tribunale-speciale-storia-istituzione.md'},
 {title:'Libro sesto — Il filo del 1926 — II. Gli otto sottonodi', file:'tribunale-speciale-approfondimento-sottonodi.md'},
 {title:'Libro sesto — Il filo del 1926 — III. Gli amnistiati', file:'amnistiati-tribunale-speciale.md'},
 {title:'Libro settimo — Le questioni aperte: il ritorno del Pollo di Popper', file:'aldo-moro-una-guerra-senza-fine-parte-terza.md'},
 {title:'Libro ottavo — Il metodo — I. Il presidio del garante', file:'aldo-moro-una-guerra-senza-fine-fase-sesta.md'},
 {title:'Libro ottavo — Il metodo — II. Le metodologie del Dossier, calcolate', file:'metodologie-del-dossier-sinaptogenesi-e-strumenti.md'},
 {title:'Libro nono — Il registro giudiziario', file:'aldo-moro-una-guerra-senza-fine-fase-settima-registro-giudiziario.md'},
 {title:'Libro decimo — Il repertorio del caso', file:'aldo-moro-una-guerra-senza-fine-fase-nona-repertorio-del-caso.md'},
 {title:'Libro undicesimo — Le responsabilità personali — I. Il principio personalistico', file:'aldo-moro-una-guerra-senza-fine-fase-decima-responsabilita-personali.md'},
 {title:'Libro undicesimo — Le responsabilità personali — II. La prosopografia dei tredici', file:'triangolazione-condannati-corpus.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — I. Moro alla Farnesina (collazione)', file:'moro-ministro-esteri/README.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — II. La ricognizione-madre: Moro ministro degli Esteri 1969-1974', file:'moro-ministro-esteri/originali/ricognizione-ministro-esteri-1969-1974.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — III. Germania e Opus Dei 1952-1985', file:'moro-ministro-esteri/originali/germania-opus-dei-1952-1985.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — IV. La Santa Sede e le due Germanie: la sequenza Oder-Neisse', file:'moro-ministro-esteri/originali/santa-sede-due-germanie-oder-neisse.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — V. Portogallo e Opus Dei', file:'moro-ministro-esteri/originali/portogallo-opus-dei.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — VI. Portogallo e Santa Sede 1969-1974', file:'moro-ministro-esteri/originali/portogallo-santa-sede-1969-1974.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — VII. Grecia e Opus Dei 1969-1985', file:'moro-ministro-esteri/originali/grecia-opus-dei-1969-1985.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — VIII. Turchia e Opus Dei 1969-1975', file:'moro-ministro-esteri/originali/turchia-opus-dei-1969-1975.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — IX. La Santa Sede, la Turchia e l’attentato del 1981', file:'moro-ministro-esteri/originali/santa-sede-turchia-attentato-giovanni-paolo-ii.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — X. Documenti italiani e spagnoli, e l’Opus Dei', file:'moro-ministro-esteri/originali/documenti-italiani-spagnoli-opus-dei.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — XI. La triangolazione della seconda campagna', file:'moro-ministro-esteri/triangolazione-seconda-campagna.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — XII. I documenti del Dipartimento di Stato', file:'moro-ministro-esteri/documenti-state-dept-1965-1978.md'},
 {title:'Libro dodicesimo — La dimensione diplomatica — XIII. Le pene oltre confine', file:'le-pene-oltre-confine-mitterrand-mulinaris.md'},
 {title:'Libro tredicesimo — Il fascicolo aperto — I. Il programma e le graduatorie', file:'programma-investigativo-caso-moro.md'},
 {title:'Libro tredicesimo — Il fascicolo aperto — II. Le schede delle piste di testa', file:'approfondimento-piste-di-testa.md'},
 {title:'Libro tredicesimo — Il fascicolo aperto — III. Le schede delle entità', file:'approfondimento-piste-entita.md'},
 {title:'Libro tredicesimo — Il fascicolo aperto — IV. Il manuale del nuovo Caso Moro (400 blocchi)', file:'manuale-investigativo-nuovo-caso-moro.md'},
 {title:"Libro tredicesimo — Il fascicolo aperto — V. L'agenda di ricerca (300 blocchi)", file:'agenda-di-ricerca-del-nuovo-caso-moro.md'},
 {title:'Libro tredicesimo — Il fascicolo aperto — VI. I nove cantieri (1.000 blocchi)', file:'nove-cantieri-mille-blocchi.md'},
 {title:'Libro tredicesimo — Il fascicolo aperto — VII. Il codice e la sua trasmissione (4.999 blocchi)', file:'kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md'},
 {title:'Libro quattordicesimo — Il meridiano e la valle: dal Sud Africa dell\'apartheid alla PayPal Mafia (1.000 blocchi)', file:'il-meridiano-e-la-valle-mille-blocchi.md'},
 {title:'Appendici — I. L\'apparato dei gradi (indice analitico)', file:'aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md'},
 {title:'Appendici — II. Relazione sui lavori in stile moroteo (pastiche dichiarato)', file:'relazione-stato-lavori-stile-moro.md'},
 {title:'Appendici — III. Verifica di un elenco esterno (i trentatré nomi)', file:'_verifiche/verifica-elenco-trentatre-nomi-p2.md'},
 {title:'Appendici — IV. i. La guida alla lettura', file:'GUIDA-ALLA-LETTURA.md'},
 {title:'Appendici — IV. ii. L\'indice dei documenti', file:'INDICE-DOCUMENTI-BRANCH.md'},
 {title:'Appendici — IV. iii. Il dossier di invio — la mappa', file:'_diffusione-opera/README.md'},
 {title:'Appendici — IV. iv. La scheda dell\'opera', file:'_diffusione-opera/scheda-dell-opera.md'},
 {title:'Appendici — IV. v. Il capitolo campione', file:'_diffusione-opera/capitolo-campione.md'},
 {title:'Appendici — IV. vi. La mappa dei destinatari', file:'_diffusione-opera/mappa-dei-destinatari.md'},
 {title:'Appendici — IV. vii. Il registro dei canali PEC', file:'_diffusione-opera/registro-pec-e-canali.md'},
 {title:'Appendici — IV. viii. La checklist di invio', file:'_diffusione-opera/checklist-di-invio.md'},
 {title:'Appendici — IV. ix. Il curriculum, modello', file:'_diffusione-opera/curriculum-modello.md'},
 {title:'Appendici — IV. x. Alla Fondazione Aldo Moro', file:'_diffusione-opera/lettera-fondazione-aldo-moro.md'},
 {title:'Appendici — IV. xi. All\'Archivio Flamigni', file:'_diffusione-opera/pec-archivio-flamigni.md'},
 {title:'Appendici — IV. xii. Al Centro Flamigni', file:'_diffusione-opera/relazione-al-centro-flamigni.md'},
 {title:'Appendici — IV. xiii. A Laterza', file:'_diffusione-opera/proposta-editrice-laterza.md'},
 {title:'Appendici — IV. xiv. A il Mulino, Carocci, Einaudi', file:'_diffusione-opera/proposte-mulino-carocci-einaudi.md'},
 {title:'Appendici — IV. xv. A Chiarelettere e Bompiani', file:'_diffusione-opera/proposte-chiarelettere-bompiani.md'},
 {title:"Apparato conclusivo — Le note bibliografiche (dalla prima all'ultima)", file:'note-bibliografiche-opera-integrale.md'},
];

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
