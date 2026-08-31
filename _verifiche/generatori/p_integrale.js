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
// L'ordine dell'opera sta in parti.json, sorgente unica — come in
// b_integrale.js, gen_note.py e gen_figs.py. Il manifesto dei grafici
// (figs_manifest.json) e' indicizzato sulla POSIZIONE in parti.json:
// una lista locale disallineerebbe le figure sui capitoli sbagliati.
const parts=JSON.parse(fs.readFileSync(__dirname+'/parti.json','utf8'))
  .parti.map(p=>({label:p.etichetta, title:p.titolo.replace(/^[^—]+—\s*/,''), file:p.file}));
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
