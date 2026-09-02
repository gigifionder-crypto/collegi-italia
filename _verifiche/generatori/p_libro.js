// Compositore di stampa dell'EDIZIONE BREVE (tetto: 250 pagine).
// Legge UN solo markdown assemblato e produce l'HTML di stampa con la
// stessa gabbia tipografica di p_integrale.js, cosi' il conteggio pagine
// e' confrontabile con quello del volume integrale.
// Uso: node p_libro.js <sorgente.md> <uscita.html>
const fs=require('fs');
const SRC=process.argv[2];
const OUT=process.argv[3];
if(!SRC||!OUT){console.error('uso: node p_libro.js <sorgente.md> <uscita.html>');process.exit(1);}

function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
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
  const lines=md.split(/\r?\n/); let out=[],i=0;
  while(i<lines.length){
    let ln=lines[i];
    if(/^\s*$/.test(ln)){i++;continue;}
    let m;
    if((m=ln.match(/^(#{1,6})\s+(.*)$/))){
      const lvl=m[1].length; const txt=stripMd(m[2]);
      // I capitoli del libro stanno a livello h2: pagina nuova per ciascuno.
      if(lvl===2&&/^\d+\.\s/.test(txt)){out.push(`<h2 class="chap">${inline(txt)}</h2>`);i++;continue;}
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

let md=fs.readFileSync(SRC,'utf8');
// Copertina: H1, gli eventuali H2/H3 che lo seguono, l'epigrafe e la
// dichiarazione. La dichiarazione e' il blockquote che si annuncia come tale;
// un blockquote che la precede e' l'epigrafe e va in copertina sopra di essa.
let titolo='Una guerra senza fine — l’edizione breve';
const mT=md.match(/^#\s+(.+)$/m);
if(mT){titolo=stripMd(mT[1]);md=md.replace(mT[0],'');}
let sottotitolo='',occhiello='';
const mS=md.match(/^\s*##\s+(.+)$/m);
if(mS&&md.slice(0,mS.index).trim()===''){sottotitolo=stripMd(mS[1]);md=md.replace(mS[0],'');}
const mO=md.match(/^\s*###\s+(.+)$/m);
if(mO&&md.slice(0,mO.index).replace(/^[\s-]*$/gm,'').trim()===''){occhiello=stripMd(mO[1]);md=md.replace(mO[0],'');}
function prendiCitazione(re){
  const m=md.match(re);
  if(!m)return '';
  md=md.replace(m[0],'');
  return m[0].split('\n').map(l=>l.replace(/^>\s?/,'').replace(/^#{1,6}\s+/,'')).join(' ').replace(/\s+/g,' ').trim();
}
// La dichiarazione si riconosce dal proprio incipit, non dalla posizione.
let epigrafe='';
const iDich=md.search(/^>\s*\*\*Dichiarazione/m);
const mE=md.match(/^(>\s?.*(?:\n>\s?.*)*)/m);
if(mE&&(iDich<0||mE.index<iDich))epigrafe=prendiCitazione(/^(>\s?.*(?:\n>\s?.*)*)/m);
let dichiarazione=prendiCitazione(/^(>\s?.*(?:\n>\s?.*)*)/m);
// Le righe orizzontali rimaste in testa appartenevano al frontespizio.
md=md.replace(/^(\s*---\s*\n)+/,'');

const body=mdToHtml(md);
const html=`<!doctype html><html lang="it"><head><meta charset="utf-8"><title>${esc(titolo)}</title>
<style>
@page{size:A4;margin:22mm 20mm 24mm 20mm;}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:11pt;line-height:1.52;color:#111;margin:0;}
.cover{page-break-after:always;display:flex;flex-direction:column;justify-content:center;min-height:230mm;text-align:center;}
.cover .k{font-size:9pt;letter-spacing:.28em;text-transform:uppercase;color:#555;margin-bottom:14mm;}
.cover h1{font-size:30pt;line-height:1.08;margin:0 0 4mm;font-weight:700;color:#1F3864;letter-spacing:.04em;}
.cover .sub{font-size:16pt;color:#1F3864;font-weight:600;margin:0 0 2mm;}
.cover .subsub{font-size:12.5pt;color:#555;font-style:italic;margin:0 0 6mm;}
.cover .epi{font-size:11.5pt;color:#1F3864;font-style:italic;margin:8mm auto 6mm;max-width:120mm;line-height:1.45;}
.cover .rule{width:42mm;border-top:1.2pt solid #1F3864;margin:0 auto 16mm;}
.cover .disc{margin-top:18mm;font-size:9.2pt;color:#555;text-align:justify;border-left:2.2pt solid #1F3864;padding-left:5mm;line-height:1.6;}
h2.chap{page-break-before:always;font-size:20pt;color:#1F3864;margin:24mm 0 8mm;line-height:1.15;border-bottom:1.2pt solid #1F3864;padding-bottom:4mm;}
h2{font-size:14.5pt;color:#1F3864;margin:9mm 0 3mm;line-height:1.2;page-break-after:avoid;}
h3{font-size:12pt;color:#1F3864;margin:6mm 0 2mm;page-break-after:avoid;}
p{margin:0 0 3.2mm;text-align:justify;}
blockquote{margin:4mm 0;padding:2mm 5mm;border-left:2.2pt solid #8a2d2d;color:#333;font-size:10pt;}
table{border-collapse:collapse;width:100%;margin:4mm 0;font-size:9pt;}
th,td{border:.4pt solid #999;padding:1.4mm 2.2mm;text-align:left;vertical-align:top;}
th{background:#eef1f6;color:#1F3864;}
code{font-family:"Liberation Mono",monospace;font-size:9pt;background:#f3f3f3;padding:0 1mm;}
.url{color:#555;font-size:8.6pt;word-break:break-all;}
.ref{color:#1F3864;}
hr{border:none;border-top:.6pt solid #bbb;margin:6mm 0;}
</style></head><body>
<section class="cover"><div class="k">Il corpus documentale sul caso Moro</div>
<h1>${esc(titolo)}</h1>${sottotitolo?`<div class="sub">${esc(sottotitolo)}</div>`:''}${occhiello?`<div class="subsub">${esc(occhiello)}</div>`:''}<div class="rule"></div>
${epigrafe?`<div class="epi">${inline(epigrafe)}</div>`:''}
<div class="disc">${inline(dichiarazione)}</div></section>
${body}
</body></html>`;
fs.writeFileSync(OUT,html);
console.log('scritto',OUT,html.length,'bytes');
