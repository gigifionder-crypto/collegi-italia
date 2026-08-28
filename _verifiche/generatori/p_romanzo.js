const fs=require('fs');
const md=fs.readFileSync('/home/user/collegi-italia/_romanzo/OTTANTA-ANNI-DI-PACE-prima-stesura.md','utf8');
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function inl(t){return esc(t)
  .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
  .replace(/\*([^*]+)\*/g,'<em>$1</em>')
  .replace(/`([^`]+)`/g,'<code>$1</code>');}
const L=md.split('\n'); const out=[]; let buf=[],tbl=[],quote=false;
const fb=()=>{if(!buf.length)return;const t=buf.join(' ').trim();buf=[];
  if(!t)return; out.push(quote?`<blockquote><p>${inl(t)}</p></blockquote>`:`<p>${inl(t)}</p>`);};
const ft=()=>{if(!tbl.length)return;
  const h=tbl[0],b=tbl.slice(1);
  out.push('<div class="tw"><table><thead><tr>'+h.map(c=>`<th>${inl(c)}</th>`).join('')+
    '</tr></thead><tbody>'+b.map(r=>'<tr>'+r.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>').join('')+'</tbody></table></div>');
  tbl=[];};
for(const r of L){
  if(/^\|/.test(r)){fb();const c=r.split('|').slice(1,-1).map(s=>s.trim());
    if(c.every(x=>/^:?-{2,}:?$/.test(x)||x===''))continue; tbl.push(c);continue;}
  ft();
  if(/^# /.test(r)){fb();quote=false;out.push(`<h1>${inl(r.slice(2))}</h1>`);continue;}
  if(/^## /.test(r)){fb();quote=false;out.push(`<h2>${inl(r.slice(3))}</h2>`);continue;}
  if(/^---\s*$/.test(r)){fb();quote=false;continue;}
  if(/^> ?/.test(r)){const c=r.replace(/^> ?/,'');if(!c.trim()){fb();continue;}
    if(!quote){fb();quote=true;} buf.push(c.trim());continue;}
  if(!r.trim()){fb();quote=false;continue;}
  if(quote){fb();quote=false;}
  buf.push(r.trim());
}
fb();ft();
fs.writeFileSync('/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/romanzo-print.html',
`<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>Ottanta anni di Pace</title>

<style>
@page{size:A4;margin:22mm 20mm}
body{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:11.2pt;line-height:1.5;color:#16150f;max-width:none}
h1{font-size:19pt;font-weight:600;page-break-before:always;margin:0 0 14pt;letter-spacing:.01em}
h1:first-of-type{page-break-before:avoid}
h2{font-size:13pt;font-weight:600;margin:18pt 0 7pt;page-break-after:avoid}
p{margin:0 0 8pt;text-align:justify;hyphens:auto}
blockquote{margin:10pt 0;padding:2pt 0 2pt 11pt;border-left:2px solid #9a9a93}
blockquote p{margin:0 0 5pt;font-size:10.6pt}
.tw{page-break-inside:avoid;margin:9pt 0}
table{border-collapse:collapse;width:100%;font-size:10pt;font-variant-numeric:tabular-nums}
th{background:#efefea;text-align:left;font-weight:600}
th,td{border:1px solid #cfcfc7;padding:3pt 6pt;vertical-align:top}
code{font-family:Consolas,monospace;font-size:9.4pt;background:#f2f2ee;padding:0 2px}
</style></head><body>
${out.join('\n')}
</body></html>`);
console.log('html ok');
