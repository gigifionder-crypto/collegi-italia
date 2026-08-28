const fs=require('fs');
const REPO='/home/user/collegi-italia';
const OUT='/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/integrale-print.html';
function load(p){return fs.readFileSync(REPO+'/'+p,'utf8');}
const MAN=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/figs_manifest.json','utf8'));

// Il titolo generale dell'opera, ripetuto in testa a certi sorgenti, e' ridondante
// sotto l'occhiello del Libro: si toglie.
const TITOLI_GENERICI=[/^#\s*Aldo Moro\s*$/,/^#\s*Aldo Moro\s+—\s+Una guerra senza fine\s*$/];
function stripGenericTitle(md){
  const lines=md.split('\n');
  for(let i=0;i<lines.length;i++){
    if(!lines[i].trim()) continue;
    if(lines[i].startsWith('# ') && TITOLI_GENERICI.some(r=>r.test(lines[i].trim()))) lines.splice(i,1);
    break;
  }
  return lines.join('\n');
}
function esc2(x){return x;}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
const parts=[
 {label:'Portale', title:"L'edizione strutturata: la mappa dell'opera", file:'aldo-moro-una-guerra-senza-fine-edizione-strutturata.md'},
 {label:'Libro primo', title:"Il ritratto: l'uomo prima del caso", file:'aldo-moro-una-guerra-senza-fine-fase-ottava-il-ritratto.md'},
 {label:'Libro quarto', title:'Il Dossier maggiore: «Una Pace senza Pace · Tutta la verità»', file:'dossier-maggiore-una-pace-senza-pace.md'},
 {label:'Libro quinto · I', title:'Feltrinelli, il vettore', file:'feltrinelli-il-vettore.md'},
 {label:'Libro quinto · II', title:'La triangolazione di Feltrinelli', file:'triangolazione-feltrinelli-corpus.md'},
 {label:'Libro quinto · III', title:'Il nodo Hyperion', file:'triangolazione-hyperion-corpus.md'},
 {label:'Libro quinto · IV', title:"L'incrocio Feltrinelli-Hyperion", file:'triangolazione-feltrinelli-hyperion.md'},
 {label:'Libro quinto · V', title:'Il ceppo Simioni: la terza strada', file:'ceppo-simioni-cpm-superclan-hyperion.md'},
 {label:'Libro sesto · I', title:'Il Tribunale Speciale: l\'istituzione', file:'tribunale-speciale-storia-istituzione.md'},
 {label:'Libro sesto · II', title:'Gli otto sottonodi', file:'tribunale-speciale-approfondimento-sottonodi.md'},
 {label:'Libro sesto · III', title:'Gli amnistiati', file:'amnistiati-tribunale-speciale.md'},
 {label:'Libro settimo', title:'Le questioni aperte: il ritorno del Pollo di Popper', file:'aldo-moro-una-guerra-senza-fine-parte-terza.md'},
 {label:'Libro ottavo · I', title:'Il presidio del garante', file:'aldo-moro-una-guerra-senza-fine-fase-sesta.md'},
 {label:'Libro ottavo · II', title:'Le metodologie del Dossier, calcolate', file:'metodologie-del-dossier-sinaptogenesi-e-strumenti.md'},
 {label:'Libro nono', title:'Il registro giudiziario', file:'aldo-moro-una-guerra-senza-fine-fase-settima-registro-giudiziario.md'},
 {label:'Libro nono · II', title:'Appendice quinta alla Fase settima', file:'appendici-fase-settima/appendice-quinta-fase-settima.md'},
 {label:'Libro nono · III', title:'Appendice sesta alla Fase settima', file:'appendici-fase-settima/appendice-sesta-fase-settima.md'},
 {label:'Libro nono · IV', title:'Appendice settima alla Fase settima', file:'appendici-fase-settima/appendice-settima-fase-settima.md'},
 {label:'Libro nono · V', title:'Appendice ottava alla Fase settima', file:'appendici-fase-settima/appendice-ottava-fase-settima.md'},
 {label:'Libro nono · VI', title:'Appendice nona alla Fase settima', file:'appendici-fase-settima/appendice-nona-fase-settima.md'},
 {label:'Libro nono · VII', title:'Appendice decima alla Fase settima', file:'appendici-fase-settima/appendice-decima-fase-settima.md'},
 {label:'Libro nono · VIII', title:'Appendice undicesima alla Fase settima', file:'appendici-fase-settima/appendice-undicesima-fase-settima.md'},
 {label:'Libro nono · IX', title:'Appendice dodicesima alla Fase settima', file:'appendici-fase-settima/appendice-dodicesima-fase-settima.md'},
 {label:'Libro nono · X', title:'Appendice tredicesima alla Fase settima', file:'appendici-fase-settima/appendice-tredicesima-fase-settima.md'},
 {label:'Libro nono · XI', title:'Appendice quattordicesima alla Fase settima', file:'appendici-fase-settima/appendice-quattordicesima-fase-settima.md'},
 {label:'Libro nono · XII', title:'Appendice quindicesima alla Fase settima', file:'appendici-fase-settima/appendice-quindicesima-fase-settima.md'},
 {label:'Libro decimo', title:'Il repertorio del caso', file:'aldo-moro-una-guerra-senza-fine-fase-nona-repertorio-del-caso.md'},
 {label:'Libro undicesimo · I', title:'Il principio personalistico', file:'aldo-moro-una-guerra-senza-fine-fase-decima-responsabilita-personali.md'},
 {label:'Libro undicesimo · II', title:'La prosopografia dei tredici', file:'triangolazione-condannati-corpus.md'},
 {label:'Libro dodicesimo · I', title:'Moro alla Farnesina (la collazione)', file:'moro-ministro-esteri/README.md'},
 {label:'Libro dodicesimo · II', title:"La ricognizione-madre: Moro ministro degli Esteri 1969-1974", file:'moro-ministro-esteri/originali/ricognizione-ministro-esteri-1969-1974.md'},
 {label:'Libro dodicesimo · III', title:"Germania e Opus Dei 1952-1985", file:'moro-ministro-esteri/originali/germania-opus-dei-1952-1985.md'},
 {label:'Libro dodicesimo · IV', title:"La Santa Sede e le due Germanie: la sequenza Oder-Neisse", file:'moro-ministro-esteri/originali/santa-sede-due-germanie-oder-neisse.md'},
 {label:'Libro dodicesimo · V', title:"Portogallo e Opus Dei", file:'moro-ministro-esteri/originali/portogallo-opus-dei.md'},
 {label:'Libro dodicesimo · VI', title:"Portogallo e Santa Sede 1969-1974", file:'moro-ministro-esteri/originali/portogallo-santa-sede-1969-1974.md'},
 {label:'Libro dodicesimo · VII', title:"Grecia e Opus Dei 1969-1985", file:'moro-ministro-esteri/originali/grecia-opus-dei-1969-1985.md'},
 {label:'Libro dodicesimo · VIII', title:"Turchia e Opus Dei 1969-1975", file:'moro-ministro-esteri/originali/turchia-opus-dei-1969-1975.md'},
 {label:'Libro dodicesimo · IX', title:"La Santa Sede, la Turchia e l’attentato del 1981", file:'moro-ministro-esteri/originali/santa-sede-turchia-attentato-giovanni-paolo-ii.md'},
 {label:'Libro dodicesimo · X', title:"Documenti italiani e spagnoli, e l’Opus Dei", file:'moro-ministro-esteri/originali/documenti-italiani-spagnoli-opus-dei.md'},
 {label:'Libro dodicesimo · XI', title:"La triangolazione della seconda campagna", file:'moro-ministro-esteri/triangolazione-seconda-campagna.md'},
 {label:'Libro dodicesimo · II', title:'I documenti del Dipartimento di Stato', file:'moro-ministro-esteri/documenti-state-dept-1965-1978.md'},
 {label:'Libro dodicesimo · III', title:'Le pene oltre confine', file:'le-pene-oltre-confine-mitterrand-mulinaris.md'},
 {label:'Libro dodicesimo · IV', title:'Aldo Moro Alla Farnesina E L\'Opus Dei', file:'moro-ministro-esteri/terza-campagna/terza-ricognizione-spagna-opus-dei.md'},
 {label:'Libro dodicesimo · V', title:'Aldo Moro Alla Farnesina E Il Portogallo', file:'moro-ministro-esteri/terza-campagna/quarta-ricognizione-portogallo-santa-sede.md'},
 {label:'Libro dodicesimo · VI', title:'Aldo Moro Alla Farnesina, Il Portogallo E La Santa Sede', file:'moro-ministro-esteri/terza-campagna/quinta-ricognizione-portogallo-le-sei-lacune.md'},
 {label:'Libro dodicesimo · VII', title:'Aldo Moro Alla Farnesina, Il Portogallo E L\'Opus Dei', file:'moro-ministro-esteri/terza-campagna/sesta-ricognizione-il-ribaltamento-iberico.md'},
 {label:'Libro dodicesimo · VIII', title:'Aldo Moro Alla Farnesina, La Turchia E La Santa Sede', file:'moro-ministro-esteri/terza-campagna/settima-ricognizione-turchia-e-attentato.md'},
 {label:'Libro dodicesimo · IX', title:'Moro, Il Mediterraneo Orientale E L\'Opus Dei', file:'moro-ministro-esteri/terza-campagna/ottava-ricognizione-mediterraneo-orientale.md'},
 {label:'Libro dodicesimo · X', title:'Moro, Le Due Germanie E La Santa Sede', file:'moro-ministro-esteri/terza-campagna/nona-ricognizione-la-sequenza-oder-neisse.md'},
 {label:'Libro dodicesimo · XI', title:'Moro, La Germania E L\'Opus Dei', file:'moro-ministro-esteri/terza-campagna/decima-ricognizione-revisione-del-modello.md'},
 {label:'Libro dodicesimo · XII', title:'Strauss E Aginter Press', file:'moro-ministro-esteri/terza-campagna/undicesima-ricognizione-strauss-e-aginter.md'},
 {label:'Libro dodicesimo · XIII', title:'I Sette Casi Extraeuropei', file:'moro-ministro-esteri/terza-campagna/dodicesima-ricognizione-sette-casi-extraeuropei.md'},
 {label:'Libro dodicesimo · XIV', title:'Aginter Press E Lo Stato Italiano', file:'moro-ministro-esteri/terza-campagna/tredicesima-ricognizione-aginter-i-due-silenzi.md'},
 {label:'Libro dodicesimo · XV', title:'Il Silenzio Dello Stato: Azione O Archivio', file:'moro-ministro-esteri/terza-campagna/quattordicesima-ricognizione-la-calibrazione-libica.md'},
 {label:'Libro dodicesimo · XVI', title:'L\'Italia, L\'Aermacchi E Il Sudafrica Dell\'Apartheid', file:'moro-ministro-esteri/terza-campagna/quindicesima-ricognizione-aermacchi-e-il-sudafrica.md'},
 {label:'Libro dodicesimo · XVII', title:'Italia E Germania Sul Dossier Namibiano', file:'moro-ministro-esteri/terza-campagna/sedicesima-ricognizione-il-dossier-namibiano.md'},
 {label:'Libro dodicesimo · XVIII', title:'La Santa Sede, La Dc E Il Sudafrica Dell\'Apartheid', file:'moro-ministro-esteri/terza-campagna/diciassettesima-ricognizione-santa-sede-e-sudafrica.md'},
 {label:'Libro dodicesimo · XIX', title:'L\'Italia Alle Nazioni Unite: Embargo, Apartheid, Namibia', file:'moro-ministro-esteri/terza-campagna/diciottesima-ricognizione-nazioni-unite-ed-embargo.md'},
 {label:'Libro dodicesimo · XX', title:'Registro Analitico Dei Nodi E Dei Ponti', file:'moro-ministro-esteri/terza-campagna/registro-dei-nodi-e-dei-ponti-teatro-australe.md'},
 {label:'Libro dodicesimo · XXI', title:'Secondo Registro Analitico Dei Nodi E Dei Ponti', file:'moro-ministro-esteri/terza-campagna/secondo-registro-dei-nodi-e-dei-ponti.md'},
 {label:'Libro dodicesimo · XXII', title:'Terzo Registro Analitico Dei Nodi E Dei Ponti', file:'moro-ministro-esteri/terza-campagna/terzo-registro-dei-nodi-e-dei-ponti.md'},
 {label:'Libro dodicesimo · XXIII', title:'Quarto Registro Analitico', file:'moro-ministro-esteri/terza-campagna/quarto-registro-la-scala-degli-stati-zero.md'},
 {label:'Libro dodicesimo · XXIV', title:'Quinto Registro Analitico', file:'moro-ministro-esteri/terza-campagna/quinto-registro-la-tavola-unica.md'},
 {label:'Libro dodicesimo · XXV', title:'Sesto Registro Analitico', file:'moro-ministro-esteri/terza-campagna/sesto-registro-strumenti-e-volume.md'},
 {label:'Libro dodicesimo · XXVI', title:'Settimo Registro Analitico', file:'moro-ministro-esteri/terza-campagna/settimo-registro-la-riqualificazione.md'},
 {label:'Libro dodicesimo · XXVII', title:'Registro Delle Undici Ricognizioni', file:'moro-ministro-esteri/terza-campagna/registro-delle-undici-ricognizioni.md'},
 {label:'Libro dodicesimo · XXVIII', title:'La triangolazione della terza campagna', file:'moro-ministro-esteri/triangolazione-terza-campagna.md'},
 {label:'Libro tredicesimo · I', title:'Il fascicolo aperto: il programma e le graduatorie', file:'programma-investigativo-caso-moro.md'},
 {label:'Libro tredicesimo · II', title:'Le schede delle piste di testa', file:'approfondimento-piste-di-testa.md'},
 {label:'Libro tredicesimo · III', title:'Le schede delle entità', file:'approfondimento-piste-entita.md'},
 {label:'Libro tredicesimo · IV', title:'Il manuale del nuovo Caso Moro (400 blocchi)', file:'manuale-investigativo-nuovo-caso-moro.md'},
 {label:'Libro tredicesimo · V', title:"L'agenda di ricerca (300 blocchi)", file:'agenda-di-ricerca-del-nuovo-caso-moro.md'},
 {label:'Libro tredicesimo · VI', title:'I nove cantieri (1.000 blocchi)', file:'nove-cantieri-mille-blocchi.md'},
 {label:'Libro tredicesimo · VII', title:'Il codice e la sua trasmissione (4.999 blocchi)', file:'kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md'},
 {label:'Libro quattordicesimo', title:"Il meridiano e la valle: dal Sud Africa dell'apartheid alla PayPal Mafia (1.000 blocchi)", file:'il-meridiano-e-la-valle-mille-blocchi.md'},
 {label:'Libro quindicesimo', title:'Il Registro dei cinquantacinque giorni — opera seconda, in sette Fasi e settanta Capitoli', file:'il-registro-dei-cinquantacinque-giorni-opera-seconda.md'},
 {label:'Appendice I', title:"L'apparato dei gradi", file:'aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md'},
 {label:'Appendice II', title:'Relazione in stile moroteo (pastiche dichiarato)', file:'relazione-stato-lavori-stile-moro.md'},
 {label:'Appendice III', title:'Verifica di un elenco esterno', file:'_verifiche/verifica-elenco-trentatre-nomi-p2.md'},
 {label:'Appendice IV.i', title:'L\'apparato di navigazione — La guida alla lettura', file:'GUIDA-ALLA-LETTURA.md'},
 {label:'Appendice IV.ii', title:'L\'apparato di navigazione — L\'indice dei documenti', file:'INDICE-DOCUMENTI-BRANCH.md'},
 {label:'Appendice IV.iii', title:'Il dossier di invio — La mappa', file:'_diffusione-opera/README.md'},
 {label:'Appendice IV.iv', title:'Il dossier di invio — La scheda dell\'opera', file:'_diffusione-opera/scheda-dell-opera.md'},
 {label:'Appendice IV.v', title:'Il dossier di invio — Il capitolo campione', file:'_diffusione-opera/capitolo-campione.md'},
 {label:'Appendice IV.vi', title:'Il dossier di invio — La mappa dei destinatari', file:'_diffusione-opera/mappa-dei-destinatari.md'},
 {label:'Appendice IV.vii', title:'Il dossier di invio — Il registro dei canali e delle PEC', file:'_diffusione-opera/registro-pec-e-canali.md'},
 {label:'Appendice IV.viii', title:'Il dossier di invio — La checklist di invio', file:'_diffusione-opera/checklist-di-invio.md'},
 {label:'Appendice IV.ix', title:'Il dossier di invio — Il curriculum, modello da compilare', file:'_diffusione-opera/curriculum-modello.md'},
 {label:'Appendice IV.x', title:'Il dossier di invio — Lettera alla Fondazione Aldo Moro', file:'_diffusione-opera/lettera-fondazione-aldo-moro.md'},
 {label:'Appendice IV.xi', title:'Il dossier di invio — PEC all\'Archivio Flamigni', file:'_diffusione-opera/pec-archivio-flamigni.md'},
 {label:'Appendice IV.xii', title:'Il dossier di invio — Relazione al Centro Flamigni', file:'_diffusione-opera/relazione-al-centro-flamigni.md'},
 {label:'Appendice IV.xiii', title:'Il dossier di invio — Proposta all\'editrice Laterza', file:'_diffusione-opera/proposta-editrice-laterza.md'},
 {label:'Appendice IV.xiv', title:'Il dossier di invio — Proposte a il Mulino, Carocci, Einaudi', file:'_diffusione-opera/proposte-mulino-carocci-einaudi.md'},
 {label:'Appendice IV.xv', title:'Il dossier di invio — Proposte a Chiarelettere e Bompiani', file:'_diffusione-opera/proposte-chiarelettere-bompiani.md'},
 {label:'Appendice IV.xvi', title:'Il dossier di invio — Il deposito Zenodo, foglio operativo', file:'_diffusione-opera/deposito-zenodo.md'},
 {label:'Appendice IV.xvii', title:"Il dossier di invio — La richiesta all'Archivio storico della Camera", file:'_diffusione-opera/richiesta-archivio-storico-camera.md'},
 {label:'Appendice IV.xviii', title:'Il dossier di invio — La PEC unica formale', file:'_diffusione-opera/pec-unica-formale.md'},
 {label:'Appendice IV.xix', title:'Il dossier di invio — La PEC di presentazione per le case editrici', file:'_diffusione-opera/pec-presentazione-case-editrici.md'},
 {label:'Appendice V.i', title:'L\'apparato della verifica — La certificazione dei numeri P2', file:'_verifiche/certificazione-numeri-p2.md'},
 {label:'Appendice V.ii', title:'L\'apparato della verifica — La relazione della campagna di ricerca', file:'_verifiche/campagna-ricerca-numeri-p2-relazione.md'},
 {label:'Appendice V.iii', title:'L\'apparato della verifica — Il registro degli ingressi', file:'_verifiche/registro-degli-ingressi.md'},
 {label:'Apparato conclusivo', title:"Le note bibliografiche (dalla prima all'ultima)", file:'note-bibliografiche-opera-integrale.md'},
];
function inline(t){
  t=esc(t);
  t=t.replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g,(m,txt,url)=>`${txt}<span class="url"> (${url})</span>`);
  t=t.replace(/\[([^\]]+)\]\([^)]*\)/g,'<span class="ref">$1</span>');
  t=t.replace(/\*\*(.+?)\*\*/g,(m,x)=>'<strong>'+x.replace(/\*/g,'')+'</strong>');
  t=t.replace(/\*([^*]+)\*/g,'<em>$1</em>');
  t=t.replace(/`([^`]+)`/g,'<code>$1</code>');
  return t;
}
function stripMd(t){return t.replace(/\*\*/g,'').replace(/`/g,'').replace(/^\*|\*$/g,'');}
function renderTable(buf){
  const rows=buf.filter(r=>!/^\s*\|?[\s:|-]+\|?\s*$/.test(r));
  const cells=rows.map(r=>r.replace(/^\s*\|/,'').replace(/\|\s*$/,'').split('|').map(c=>c.trim()));
  let h='<table>';
  cells.forEach((row,ri)=>{h+='<tr>'+row.map(c=>ri===0?`<th>${inline(c)}</th>`:`<td>${inline(c)}</td>`).join('')+'</tr>';});
  return h+'</table>';
}
function mdToHtml(md){
  const lines=md.split(/\r?\n/); let out=[],i=0,first=true;
  while(i<lines.length){
    let ln=lines[i];
    if(/^\s*$/.test(ln)){i++;continue;}
    let m;
    if((m=ln.match(/^(#{1,6})\s+(.*)$/))){
      const lvl=m[1].length; const txt=stripMd(m[2]);
      if(lvl===1&&first){first=false;i++; // drop doc H1 (part page carries it)
        // also drop immediate subtitle h2
        while(i<lines.length&&/^\s*$/.test(lines[i]))i++;
        if(i<lines.length&&/^## /.test(lines[i])){out.push(`<p class="docsub">${inline(stripMd(lines[i].slice(3)))}</p>`);i++;}
        continue;}
      const hl=lvl===1?2:(lvl===2?2:3);
      out.push(`<h${hl}>${inline(txt)}</h${hl}>`);i++;continue;
    }
    if(/^---\s*$/.test(ln)){out.push('<hr>');i++;continue;}
    if(/^>\s?/.test(ln)){
      let buf=[];while(i<lines.length&&/^>\s?/.test(lines[i])){buf.push(lines[i].replace(/^>\s?/,''));i++;}
      out.push(`<blockquote>${inline(buf.join(' ').trim())}</blockquote>`);continue;
    }
    if(/^\s*\|/.test(ln)){let buf=[];while(i<lines.length&&/^\s*\|/.test(lines[i])){buf.push(lines[i]);i++;}out.push(renderTable(buf));continue;}
    if(/^\s*\d+\.\s+/.test(ln)){let buf=[];while(i<lines.length&&/^\s*\d+\.\s+/.test(lines[i])){buf.push(lines[i].replace(/^\s*\d+\.\s+/,''));i++;}
      out.push('<ol>'+buf.map(x=>`<li>${inline(x)}</li>`).join('')+'</ol>');continue;}
    if(/^\s*[-*]\s+/.test(ln)){let buf=[];while(i<lines.length&&/^\s*[-*]\s+/.test(lines[i])){buf.push(lines[i].replace(/^\s*[-*]\s+/,''));i++;}
      out.push('<ul>'+buf.map(x=>`<li>${inline(x)}</li>`).join('')+'</ul>');continue;}
    out.push(`<p>${inline(ln)}</p>`);i++;
  }
  return out.join('\n');
}
let body='';
parts.forEach((p,pi)=>{
  body+=`<section class="partpage"><div class="pl">${esc(p.label)}</div><h1 class="pt">${esc(p.title)}</h1></section>\n`;
  body+=`<section class="content">${mdToHtml(stripGenericTitle(load(p.file)))}</section>\n`;
  const fl=MAN[String(pi)]||[];
  if(fl.length){
    body+=`<section class="figs"><div class="fighead">Apparato grafico — ${esc(p.label)}${p.title?" · "+esc(p.title.slice(0,58)):""}</div><div class="figgrid">`
      +fl.map(f=>`<figure><img src="${f.file}"><figcaption>${esc(f.caption)}</figcaption></figure>`).join('')
      +`</div><p class="fignote">Le metriche dell'apparato contano parole, documenti e atti — mai colpe.</p></section>\n`;
  }
});
const html=`<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Aldo Moro — Ottanta anni di Pace</title>
<style>
@page{size:A4;margin:22mm 20mm 24mm 20mm;}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:11pt;line-height:1.52;color:#111;margin:0;}
.cover{page-break-after:always;display:flex;flex-direction:column;justify-content:center;min-height:230mm;text-align:center;}
.cover .k{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:9pt;letter-spacing:.28em;text-transform:uppercase;color:#555;margin-bottom:14mm;}
.cover h1{font-size:30pt;line-height:1.08;margin:0 0 6mm;font-weight:700;color:#1F3864;}
.cover .sub{font-size:15pt;font-style:italic;color:#333;margin:0 0 16mm;}
.cover .rule{width:42mm;border-top:1.2pt solid #1F3864;margin:0 auto 16mm;}
.cover .imp{font-size:10pt;color:#444;line-height:1.7;}
.cover .disc{margin-top:18mm;font-size:9.2pt;color:#555;text-align:justify;border-left:2.2pt solid #1F3864;padding-left:5mm;line-height:1.6;}
.partpage{page-break-before:always;page-break-after:always;display:flex;flex-direction:column;justify-content:center;min-height:225mm;}
.partpage .pl{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:10pt;letter-spacing:.3em;text-transform:uppercase;color:#8a2d2d;margin-bottom:8mm;}
.partpage .pt{font-size:24pt;color:#1F3864;margin:0;line-height:1.12;border-bottom:1.4pt solid #1F3864;padding-bottom:6mm;max-width:150mm;}
.content{}
.docsub{font-size:13pt;font-style:italic;color:#1F3864;margin:0 0 6mm;}
h2{font-size:14.5pt;color:#1F3864;margin:9mm 0 3mm;line-height:1.2;page-break-after:avoid;}
h3{font-size:11.5pt;color:#333;margin:6mm 0 2mm;font-style:italic;page-break-after:avoid;}
p{margin:0 0 3.2mm;text-align:justify;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:anywhere;}
blockquote{margin:4mm 0;padding:1mm 0 1mm 5mm;border-left:2.4pt solid #1F3864;color:#222;text-align:justify;font-size:10.3pt;line-height:1.55;page-break-inside:avoid;}
ul,ol{margin:0 0 3.2mm;padding-left:7mm;}
li{margin:0 0 1.4mm;text-align:justify;overflow-wrap:anywhere;}
table{border-collapse:collapse;width:100%;margin:4mm 0;font-size:9.3pt;line-height:1.4;page-break-inside:avoid;}
th{background:#1F3864;color:#fff;text-align:left;padding:1.8mm 2.4mm;font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:8.4pt;letter-spacing:.03em;}
td{border-bottom:.5pt solid #bbb;padding:1.6mm 2.4mm;vertical-align:top;text-align:justify;hyphens:auto;-webkit-hyphens:auto;}
tr:nth-child(even) td{background:#f3f5f8;}
code{font-family:"Liberation Mono",monospace;font-size:9pt;background:#eee;padding:0 1mm;overflow-wrap:anywhere;word-break:break-all;}
.ref{font-family:"Liberation Mono",monospace;font-size:9pt;color:#333;}
.url{font-size:8.3pt;color:#666;word-break:break-all;}
hr{border:0;border-top:.6pt solid #999;margin:6mm 0;}
.figs{margin-top:9mm;}
.fighead{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:9pt;letter-spacing:.22em;text-transform:uppercase;color:#8a2d2d;border-top:.9pt solid #1F3864;padding-top:3mm;margin-bottom:3.5mm;}
.figgrid{display:grid;grid-template-columns:1fr 1fr;gap:4mm 5mm;}
.figs figure{margin:0;page-break-inside:avoid;}
.figs img{width:100%;background:#fff;}
.figs figcaption{font-size:8.2pt;color:#555;margin-top:1mm;line-height:1.35;}
.fignote{font-size:8pt;color:#777;margin-top:2.5mm;}
strong{color:#000;}
</style></head><body>
<div class="cover">
  <div class="k">Corpus storico · Branch pubblico · AI generated</div>
  <h1>Aldo Moro</h1>
  <p class="sub">Ottanta anni di Pace</p>
  <p class="sub" style="font-size:11pt;color:#555;">L'opera integrale «Una guerra senza fine» — tredici Libri e cinque Appendici</p>
  <div class="rule"></div>
  <p class="imp">Il ritratto · il Dossier maggiore · il vettore e il ceppo · il filo del 1926<br>le questioni aperte · il metodo · il registro giudiziario · il repertorio · le responsabilità personali<br>la dimensione diplomatica · il fascicolo aperto con la quadriga investigativa<br>(il programma · il manuale in 400 blocchi · l'agenda in 300 · i nove cantieri in 1.000)<br>e la triangolazione di un solo nome col corpus in 1.000 blocchi: Il codice e la sua trasmissione<br><br>Edizione integrale in senso stretto: dei centoundici documenti del perimetro ne entrano centootto<br>Settima edizione — 27 agosto 2026<br><span style="font-size:8.4pt">Priva del Libro secondo e del Libro terzo, rimossi per decisione dell'autore: il saggio-cerniera «Dal Che a Moro» e la parabola di Guevara in sei parti, 17.769 parole. La numerazione dei Libri superstiti non è stata rifatta — dopo il Libro primo viene il Libro quarto — perché rinumerare renderebbe invisibile la rimozione e falsificherebbe ogni citazione anteriore.</span><br><span style="font-size:8.4pt">Restano fuori tre documenti soltanto, e ciascuno per una ragione: il registro delle impronte, che misura questo volume e non può stare dentro ciò che misura; il memorandum operativo, che per statuto proprio non appartiene all'opera; la nota sugli strumenti ricevuti, che riguarda codice e segue i generatori. La quarta edizione è del 26 agosto e portava quattordici Libri e due Appendici: non è ritirata, è superata. Resta fuori, per dichiarazione, l'opera «Italia Nera», che è un lavoro distinto e non una parte di questo.</span></p>
  <p class="disc"><strong>Il titolo.</strong> «Ottanta anni di Pace» è la chiave interpretativa scelta dall'autore per questa edizione, e come ogni chiave del corpus si dichiara e non giudica. La Pace che il titolo conta è quella dei calendari e delle ricorrenze: proclamata nel maggio del 1945 e misurata da allora in anni. L'opera non la nega e non la irride — chiede che cosa quegli anni abbiano contenuto, e trova, nei documenti che raccoglie, che la pace dichiarata e la violenza praticata hanno convissuto a lungo. Il titolo si presta perciò a due letture che l'opera non scioglie: gli ottant'anni dal 1945, e il decennio Ottanta che il 1978 apre e a cui sopravvive. Ciò che dichiara è una continuità, non una responsabilità: è una lente, non una sentenza, e nessuna pagina che segue attribuisce a chicchessia ciò che una lente lascia vedere. L'opera resta, nel suo nome proprio, «Una guerra senza fine», e il Libro quarto porta il proprio: «Una Pace senza Pace».</p>
  <p class="disc"><strong>Disciplina.</strong> In ogni pagina vale la Regola di Ferro: gradi dichiarati (A giudicato · B accertamento · C congettura · F fatto pubblico · Stato Zero), criteri di smentita, esiti negativi come acquisizioni. Nessuna imputazione oltre il giudicato; nessuna graduatoria di persone — con l'unica eccezione, dichiarata in apertura del Libro quarto e valida soltanto entro di esso, della bilancia probabilistica che il Dossier maggiore porta con sé come volume nel volume: essa ordina per plausibilità e non per colpa, lavora per categorie di soggetti e non per nomi individuali, muove dai condannati in via definitiva e rifiuta di nominare un mandante esterno determinato; la colpa non è mai del gruppo ed è sempre della persona; gli assolti restano assolti; le sei vittime stanno in testa, non in fondo. I pastiche sono dichiarati e non sono parole di Aldo Moro. Un'indagine produce atti, non colpevoli.</p>
</div>
${body}
</body></html>`;
fs.writeFileSync(OUT,html);
console.log('scritto',OUT,html.length);
