// Compositore di stampa dell'OPERA MONOGRAFICA.
// Distinto da p_libro.js, che compone l'edizione ridotta e non si tocca:
// l'Opera ha una struttura propria -- libri, raccordi, referti, versi -- e
// una propria identita' tipografica.
//
// Tipografia: Barlow Semi Condensed (sei tagli, installati in locale).
// Carta: bianco con gradiente di crema al 5%, dipinto da uno strato fisso
//        cosi' che OGNI pagina porti lo stesso gradiente e non una sua fetta.
// Inchiostro: blu navy con gradiente di nero al 5%.
//
// Uso: node p_opera.js <sorgente.md> <uscita.html>
const fs = require('fs');
const SRC = process.argv[2], OUT = process.argv[3];
if (!SRC || !OUT) { console.error('uso: node p_opera.js <sorgente.md> <uscita.html>'); process.exit(1); }

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const stripMd = t => t.replace(/\*\*/g, '').replace(/`/g, '').replace(/^\*|\*$/g, '');

function inline(t) {
  t = esc(t);
  t = t.replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, (m, txt, url) => `${txt}<span class="url"> (${url})</span>`);
  t = t.replace(/\[([^\]]+)\]\([^)]*\)/g, '<span class="ref">$1</span>');
  t = t.replace(/\*\*(.+?)\*\*/g, (m, x) => '<strong>' + x.replace(/\*/g, '') + '</strong>');
  t = t.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  t = t.replace(/`([^`]+)`/g, '<code>$1</code>');
  t = t.replace(/(\d)-(\d)/g, '$1‑$2');           // intervalli numerici non si spezzano
  return t;
}

// Ancora stabile e leggibile: serve ai collegamenti del sommario e ai segnalibri.
const slug = t => stripMd(t).toLowerCase()
  .normalize('NFD').replace(/[̀-ͯ]/g, '')
  .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 72);


// ---------------------------------------------------------------------------
// Sillabazione italiana.
// Chromium in questo ambiente NON ha il dizionario: `hyphens:auto` non fa
// nulla, e lo si e' verificato invece di darlo per buono. Su 236 pagine
// giustificate l'assenza si vede, percio' i punti di rottura si calcolano qui
// e si inseriscono come trattini molli (U+00AD).
//
// Le regole sono quelle dell'italiano, applicate in modo CONSERVATIVO: dove il
// caso e' dubbio non si rompe. Una sillabazione sbagliata e' peggio di una
// sillabazione mancante, perche' la mancante produce una riga larga e la
// sbagliata produce una parola falsa.
const VOC = new Set('aeiouàèéìíîòóùúï'.split(''));
const MUTA = 'bcdfgptv', LIQUIDA = 'lr';

function digramma(w, i) {           // coppia che non si separa mai
  const a = w[i], b = w[i + 1];
  if (!b) return false;
  if (a === 'c' && b === 'h') return true;
  if (a === 'g' && b === 'h') return true;
  if (a === 'g' && b === 'n') return true;
  if (a === 'g' && b === 'l' && w[i + 2] === 'i') return true;
  if (a === 's' && b === 'c' && 'ei'.includes(w[i + 2])) return true;
  if (a === 'q' && b === 'u') return true;
  return false;
}
const onsetValido = (a, b) => a === 's' || (MUTA.includes(a) && LIQUIDA.includes(b));

function puntiRottura(w) {
  const n = w.length, br = [];
  const V = i => VOC.has(w[i]);
  for (let i = 1; i < n; i++) {
    if (digramma(w, i - 1)) continue;              // mai dentro un digramma
    if (V(i - 1) && V(i)) continue;                // mai fra due vocali
    if (V(i - 1) && !V(i)) {                       // V | C…
      let j = i; while (j < n && !V(j)) j++;
      const cons = w.slice(i, j);
      if (cons.length === 1) br.push(i);
      else if (cons.length === 2 && (onsetValido(cons[0], cons[1]) || digramma(w, i))) br.push(i);
      continue;                                    // tre consonanti: si rompe piu' avanti
    }
    if (!V(i - 1) && !V(i)) {                      // C | C
      if (digramma(w, i)) { if ('lmnr'.includes(w[i - 1])) br.push(i); continue; }
      if (!onsetValido(w[i - 1], w[i]) || 'lmnr'.includes(w[i - 1])) br.push(i);
    }
    // C | V non si rompe mai: la consonante appartiene alla vocale che segue.
  }
  return br;
}

const SHY = '­';
function sillabaParola(w) {
  if (w.length < 8) return w;                      // parole corte: non conviene
  const br = puntiRottura(w).filter(i => i >= 3 && w.length - i >= 3);
  if (!br.length) return w;
  let out = '', prev = 0;
  for (const i of br) { out += w.slice(prev, i) + SHY; prev = i; }
  return out + w.slice(prev);
}

// Si opera solo sul testo fuori dai tag, e solo su parole tutte minuscole:
// i nomi propri e le sigle si lasciano interi.
function sillabaHtml(html) {
  // Si salta l'interno dei titoli e del codice: il testo dei titoli diventa il
  // testo dei segnalibri del PDF, e un trattino molle dentro un segnalibro e'
  // spazzatura che si vede.
  const SALTA = /^(h[1-6]|code|title)$/;
  const re = /<\/?([a-z0-9]+)[^>]*>/gi;
  let out = '', ultimo = 0, dentro = 0, m;
  while ((m = re.exec(html)) !== null) {
    const testo = html.slice(ultimo, m.index);
    out += dentro ? testo : sillabaTesto(testo);
    out += m[0];
    const tag = m[1].toLowerCase(), chiude = m[0][1] === '/';
    if (SALTA.test(tag)) dentro = Math.max(0, dentro + (chiude ? -1 : 1));
    ultimo = re.lastIndex;
  }
  const coda = html.slice(ultimo);
  return out + (dentro ? coda : sillabaTesto(coda));
}
function sillabaTesto(s) {
  return s.replace(/[a-zàèéìíîòóùúï]{8,}/g, m => sillabaParola(m));
}

function renderTable(buf) {
  const rows = buf.filter(r => !/^\s*\|?[\s:|-]+\|?\s*$/.test(r));
  const cells = rows.map(r => r.replace(/^\s*\|/, '').replace(/\|\s*$/, '').split('|').map(c => c.trim()));
  let h = '<table>';
  cells.forEach((row, ri) => {
    h += '<tr>' + row.map(c => ri === 0 ? `<th>${inline(c)}</th>` : `<td>${inline(c)}</td>`).join('') + '</tr>';
  });
  return h + '</table>';
}

// Un verso e' una riga interamente in corsivo. I versi non si giustificano e
// non si sillabano: si spezzano dove l'autore li ha spezzati.
const isVerso = ln => /^\*[^*].*[^*]\*$/.test(ln.trim()) && !/\*\*/.test(ln);

// Righe che aprono un blocco proprio e percio' chiudono il paragrafo in corso.
const nuovoBlocco = ln =>
  /^#{1,6}\s/.test(ln) || /^---\s*$/.test(ln) || /^>\s?/.test(ln) ||
  /^\s*\|/.test(ln) || /^\s*\d+\.\s+/.test(ln) || /^\s*[-*]\s+/.test(ln) || isVerso(ln);

function mdToHtml(md, ancore, raccogliAncore) {
  const lines = md.split(/\r?\n/); const out = []; let i = 0;
  while (i < lines.length) {
    const ln = lines[i];
    if (/^\s*$/.test(ln)) { i++; continue; }
    let m;
    if ((m = ln.match(/^(#{1,6})\s+(.*)$/))) {
      const lvl = m[1].length, txt = stripMd(m[2]);
      const numerato = txt.match(/^([0-9]+|[IVXLC]+)\.\s+(.*)$/);
      const id = slug(lvl === 2 && numerato ? numerato[2] : txt);
      if (raccogliAncore) { ancore.add(id); i++; continue; }
      if (lvl === 1) {
        // Libro, Congedo, Quadro sinottico, Apparati: pagina d'occhiello.
        // L'occhiello sta DENTRO l'h1, non accanto: il segnalibro del PDF
        // prende il testo dell'intestazione, e un albero di segnalibri che
        // recita «I, II, III» senza dire di quale Libro non e' navigabile.
        // Visivamente non cambia nulla: lo span e' di blocco e porta lo stile
        // dell'occhiello.
        const p = txt.split(' · ');
        out.push(`<section class="parte" id="${id}"><h1>` +
                 (p.length > 1 ? `<span class="parte-k">${inline(p[0])}<i class="giunt">\u00A0</i></span>${inline(p.slice(1).join(' · '))}`
                               : `${inline(txt)}`) +
                 `</h1><div class="parte-rule"></div></section>`);
        i++; continue;
      }
      if (lvl === 2 && numerato) {
        const n = numerato;
        // L'ancora porta il titolo senza il numero: il sommario elenca i titoli,
        // e un'ancora che il sommario non sa nominare non serve a nulla.
        out.push(`<h2 class="cap" id="${slug(n[2])}"><span class="cap-n">${n[1]}</span>${inline(n[2])}</h2>`);
        i++; continue;
      }
      if (lvl === 2) {
        let cls = 'sez';
        if (/^Referto\b/i.test(txt)) cls = 'sez referto';
        else if (/^I documenti di questo libro$/i.test(txt)) cls = 'sez raccordo';
        out.push(`<h2 class="${cls}" id="${id}">${inline(txt)}</h2>`); i++; continue;
      }
      // Nell'edizione integrale le parti sono declassate di due livelli: la
      // gerarchia arriva percio' al quarto e al quinto grado, e appiattirla
      // renderebbe illeggibile la struttura interna dei documenti.
      const g = Math.min(lvl, 5);
      out.push(`<h${g} id="${id}">${inline(txt)}</h${g}>`); i++; continue;
    }
    if (/^---\s*$/.test(ln)) { out.push('<hr>'); i++; continue; }
    if (/^>\s?/.test(ln)) {
      const buf = []; while (i < lines.length && /^>\s?/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, '')); i++; }
      out.push(`<blockquote>${inline(buf.join(' ').trim())}</blockquote>`); continue;
    }
    if (/^\s*\|/.test(ln)) { const buf = []; while (i < lines.length && /^\s*\|/.test(lines[i])) { buf.push(lines[i]); i++; } out.push(renderTable(buf)); continue; }
    if (isVerso(ln)) {
      const buf = []; while (i < lines.length && isVerso(lines[i])) { buf.push(lines[i].trim().replace(/^\*|\*$/g, '')); i++; }
      // Un verso e' breve e sta in compagnia. Un corsivo lungo e solitario e'
      // un attacco in prosa, e giustificarlo e sillabarlo e' giusto.
      if (buf.length >= 2 && buf.every(x => x.length <= 120))
        out.push('<div class="verso">' + buf.map(x => `<span>${inline(x)}</span>`).join('') + '</div>');
      else
        out.push(buf.map(x => `<p class="incipit"><em>${inline(x)}</em></p>`).join(''));
      continue;
    }
    if (/^\s*\d+\.\s+/.test(ln)) { const buf = []; while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) { buf.push(lines[i].replace(/^\s*\d+\.\s+/, '')); i++; } out.push('<ol>' + buf.map(x => `<li>${inline(x)}</li>`).join('') + '</ol>'); continue; }
    if (/^\s*[-*]\s+/.test(ln)) { const buf = []; while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) { buf.push(lines[i].replace(/^\s*[-*]\s+/, '')); i++; } out.push('<ul>' + buf.map(x => `<li>${inline(x)}</li>`).join('') + '</ul>'); continue; }
    // Un paragrafo a capo fisso e' UN paragrafo: si uniscono le righe fino
    // alla riga vuota o al blocco successivo. Senza questo, un grassetto che
    // attraversa due righe non si chiude mai e stampa i propri asterischi.
    {
      const buf = [];
      while (i < lines.length && !/^\s*$/.test(lines[i]) && !nuovoBlocco(lines[i])) { buf.push(lines[i].trim()); i++; }
      out.push(`<p>${inline(buf.join(' '))}</p>`);
    }
  }
  return out.join('\n');
}

let md = fs.readFileSync(SRC, 'utf8');
const shaFonte = require('crypto').createHash('sha256').update(md).digest('hex');

let titolo = 'Opera monografica';
const mT = md.match(/^#\s+(.+)$/m); if (mT) { titolo = stripMd(mT[1]); md = md.replace(mT[0], ''); }
let sottotitolo = '', occhiello = '';
const mS = md.match(/^\s*##\s+(.+)$/m);
if (mS && md.slice(0, mS.index).trim() === '') { sottotitolo = stripMd(mS[1]); md = md.replace(mS[0], ''); }
const mO = md.match(/^\s*###\s+(.+)$/m);
if (mO && md.slice(0, mO.index).replace(/^[\s-]*$/gm, '').trim() === '') { occhiello = stripMd(mO[1]); md = md.replace(mO[0], ''); }
// Il frontespizio porta cinque righe: nome dell'opera, titolo, proposizione,
// argomento e collocazione del tomo. Le ultime due sono facoltative --
// l'edizione ridotta non ha tomi -- e restano vuote se il sorgente non le da'.
let argomento = '', collocazione = '';
const mA = md.match(/^\s*####\s+(.+)$/m);
if (mA && md.slice(0, mA.index).replace(/^[\s-]*$/gm, '').trim() === '') { argomento = stripMd(mA[1]); md = md.replace(mA[0], ''); }
const mC = md.match(/^\s*#####\s+(.+)$/m);
if (mC && md.slice(0, mC.index).replace(/^[\s-]*$/gm, '').trim() === '') { collocazione = stripMd(mC[1]); md = md.replace(mC[0], ''); }

function prendiCitazione(re) {
  const m = md.match(re); if (!m) return '';
  md = md.replace(m[0], '');
  return m[0].split('\n').map(l => l.replace(/^>\s?/, '').replace(/^#{1,6}\s+/, '')).join(' ').replace(/\s+/g, ' ').trim();
}
let epigrafe = '';
const iDich = md.search(/^>\s*\*\*Dichiarazione/m);
const mE = md.match(/^(>\s?.*(?:\n>\s?.*)*)/m);
if (mE && (iDich < 0 || mE.index < iDich)) epigrafe = prendiCitazione(/^(>\s?.*(?:\n>\s?.*)*)/m);
const dichiarazione = prendiCitazione(/^(>\s?.*(?:\n>\s?.*)*)/m);
md = md.replace(/^(\s*---\s*\n)+/, '');

// Due passate: la prima raccoglie le ancore, la seconda compone. Cosi' il
// sommario puo' collegarsi a titoli che vengono dopo di lui.
const ancore = new Set();
mdToHtml(md, ancore, true);
let body = mdToHtml(md, ancore, false);

// Il sommario diventa navigabile: ogni voce che corrisponda a un titolo
// dell'opera si collega ad esso. Le voci senza corrispondenza restano testo.
let collegate = 0;
body = body.replace(/(<h2 class="sez" id="sommario[^"]*">[\s\S]*?)(?=<h2 |<section class="parte")/,
  blocco => blocco.replace(/<(li|p)>((?:(?!<\/\1>).)*)<\/\1>/g, (tutto, tag, dentro) => {
    const id = slug(dentro.replace(/<[^>]+>/g, ''));
    if (!ancore.has(id)) return tutto;
    collegate++;
    return `<${tag}><a href="#${id}">${dentro}</a></${tag}>`;
  }));

let sillabate = 0;
body = sillabaHtml(body);
sillabate = (body.match(/\u00AD/g) || []).length;

// La citazione e la sua attribuzione si separano prima della composizione:
// dividere dopo aver sfuggito i caratteri stamperebbe i tag invece di usarli.
const pezziEpi = epigrafe.split(/\s+—\s+/);
const epiHtml = epigrafe
  ? `<div class="epi"><span>${inline(pezziEpi[0])}</span>` +
    (pezziEpi[1] ? `<span class="epi-a">${inline(pezziEpi.slice(1).join(' — '))}</span>` : '') + '</div>'
  : '';

const CSS = `
:root{
  --carta-alta:#FFFFFF; --carta-bassa:#FAF6EA;      /* bianco -> crema 5% */
  --navy:#1F3864; --inchiostro:#1D355F;              /* navy -> nero 5%  */
  --navy-fondo:#16294A; --navy-tenue:#5B6B8C; --filo:#C9D2E2;
}
/* I margini li governa il renderer, perche' e' lui a riservare lo spazio
   al piede con la numerazione. */
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{
  font-family:"Barlow Semi Condensed","Barlow SemiCondensed","Liberation Sans",sans-serif;
  font-size:10.9pt; line-height:1.50; color:var(--inchiostro);
  margin:0; padding:0 19mm;
  font-variant-numeric:oldstyle-nums proportional-nums;
  hyphens:auto; -webkit-hyphens:auto;
}
/* Lo strato della carta e' fisso: Chromium lo ripete su ogni pagina, cosi'
   ciascuna porta il gradiente intero e non una sua fetta. */
.carta{position:fixed;inset:0;z-index:-1;
  background:linear-gradient(168deg,var(--carta-alta) 0%,#FDFBF4 58%,var(--carta-bassa) 100%);}

p{margin:0 0 2.9mm;text-align:justify;text-justify:inter-word;orphans:3;widows:3;}
strong{font-weight:600;color:var(--navy-fondo);}
em{font-style:italic;}

/* ---- copertina ---- */
.cover{page-break-after:always;display:flex;flex-direction:column;justify-content:center;
  min-height:238mm;text-align:center;}
.cover .k{font-size:8.4pt;letter-spacing:.34em;text-transform:uppercase;color:var(--navy-tenue);margin-bottom:16mm;font-weight:500;}
.cover h1{font-size:44pt;line-height:1;margin:0 0 5mm;font-weight:700;letter-spacing:.06em;
  color:var(--navy-fondo);}
.cover .sub{font-size:19pt;color:var(--navy);font-weight:600;margin:0 0 2mm;letter-spacing:.01em;}
.cover .subsub{font-size:12.4pt;color:var(--navy-tenue);font-style:italic;font-weight:400;margin:0 0 5mm;}
.cover .arg{font-size:9.6pt;color:var(--navy-tenue);font-weight:400;line-height:1.5;
  max-width:118mm;margin:0 auto 9mm;text-wrap:balance;hyphens:none;}
.cover .coll{margin-top:14mm;font-size:8.2pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--navy-tenue);font-weight:600;hyphens:none;line-height:1.7;max-width:152mm;
  margin-left:auto;margin-right:auto;}
.cover .rule{width:38mm;height:1.6pt;margin:0 auto 12mm;
  background:linear-gradient(90deg,transparent,var(--navy),transparent);}
.cover .epi{margin:0 auto;max-width:122mm;}
.cover .epi>span{display:block;font-size:14pt;color:var(--navy);font-style:italic;font-weight:500;line-height:1.4;}
.cover .epi .epi-a{margin-top:5mm;font-size:10.4pt;font-style:normal;font-weight:600;
  letter-spacing:.2em;text-transform:uppercase;color:var(--navy-tenue);}

/* ---- pagina della dichiarazione ---- */
.dich{page-break-after:always;min-height:232mm;display:flex;flex-direction:column;justify-content:center;}
.dich .disc{font-size:10pt;color:var(--inchiostro);text-align:justify;line-height:1.62;
  border-left:2pt solid var(--navy);padding-left:6mm;max-width:132mm;margin:0 auto;}

/* ---- occhiello di libro: pagina intera ---- */
.parte{page-break-before:always;page-break-after:avoid;min-height:150mm;
  display:flex;flex-direction:column;justify-content:flex-end;text-align:left;}
.parte h1 .giunt{letter-spacing:0;}
.parte h1 .parte-k{display:block;font-size:9pt;letter-spacing:.3em;text-transform:uppercase;color:var(--navy-tenue);
  font-weight:600;margin-bottom:5mm;}
.parte h1{font-size:27pt;line-height:1.1;margin:0;font-weight:700;color:var(--navy);letter-spacing:.005em;}
.parte-rule{width:100%;height:1.4pt;margin-top:8mm;
  background:linear-gradient(90deg,var(--navy) 0%,var(--navy) 22%,var(--filo) 22%,var(--filo) 100%);}

/* ---- capitolo ---- */
h2.cap{page-break-before:always;page-break-after:avoid;font-size:17.5pt;color:var(--navy);
  font-weight:600;line-height:1.16;margin:6mm 0 7mm;padding-bottom:3.5mm;
  border-bottom:.8pt solid var(--filo);}
h2.cap .cap-n{display:block;font-size:9pt;letter-spacing:.28em;color:var(--navy-tenue);
  font-weight:600;margin-bottom:2.5mm;}
h2.sez{font-size:13.4pt;color:var(--navy);margin:8mm 0 2.6mm;line-height:1.22;font-weight:600;page-break-after:avoid;}
h2.raccordo{color:var(--navy-tenue);font-style:italic;font-weight:500;font-size:12.4pt;}
h2.referto{border-top:1.1pt solid var(--navy);padding-top:3.5mm;margin-top:9mm;}
h3{font-size:11.4pt;color:var(--navy-fondo);margin:5.5mm 0 1.8mm;font-weight:600;page-break-after:avoid;}
h4{font-size:10.6pt;color:var(--navy);margin:4.5mm 0 1.4mm;font-weight:600;page-break-after:avoid;}
h5{font-size:10pt;color:var(--navy-tenue);margin:4mm 0 1.2mm;font-weight:600;
   letter-spacing:.05em;text-transform:uppercase;page-break-after:avoid;}

/* ---- versi ---- */
.incipit{color:var(--navy-tenue);font-size:10.4pt;margin-bottom:3.4mm;}
.verso{margin:4mm 0 5mm;padding-left:4mm;border-left:.8pt solid var(--filo);
  page-break-inside:avoid;}
.verso span{display:block;font-style:italic;color:var(--navy);font-size:10.6pt;
  line-height:1.44;text-align:left;hyphens:none;}

blockquote{margin:3.5mm 0;padding:1mm 0 1mm 5mm;border-left:2pt solid var(--filo);
  color:var(--navy-fondo);font-size:10.2pt;text-align:justify;}
ul,ol{margin:0 0 3mm;padding-left:6.5mm;}
li{margin-bottom:1.1mm;text-align:justify;}

table{border-collapse:collapse;width:100%;margin:3.5mm 0 4.5mm;font-size:9.1pt;
  page-break-inside:avoid;}
th,td{padding:1.5mm 2.4mm;text-align:left;vertical-align:top;border:none;
  border-bottom:.4pt solid var(--filo);}
th{color:var(--navy);font-weight:600;border-bottom:.9pt solid var(--navy);
  text-transform:uppercase;letter-spacing:.06em;font-size:8.4pt;}
tr:last-child td{border-bottom:.9pt solid var(--filo);}

code{font-family:"Liberation Mono",monospace;font-size:8.8pt;color:var(--navy-fondo);}

/* ---- niente straripa dalla pagina ----------------------------------------
   Un solo elemento piu' largo della pagina fa restringere IN SILENZIO l'intero
   documento: Chromium applica il suo «adatta alla larghezza» a tutta la stampa,
   e il libro esce di due terzi -- o di meta'. E' successo davvero: gli indirizzi
   lunghi dell'apparato bibliografico avevano rimpicciolito tre tomi su undici.
   Un indirizzo che va a capo e' brutto; un libro rimpicciolito e' un altro
   libro. Percio' qui i gettoni lunghi si spezzano, e la verifica in
   pdf_opera.js si rifiuta di comporre se qualcosa straripa ancora. */
code, a, .url{overflow-wrap:anywhere;word-break:break-word;}
p, li, td, th, dd, blockquote{overflow-wrap:break-word;}
pre{white-space:pre-wrap;overflow-wrap:anywhere;}
table{max-width:100%;}
.url{color:var(--navy-tenue);font-size:8.4pt;word-break:break-all;}
.ref{color:var(--navy);}
a{color:inherit;text-decoration:none;}
hr{border:none;height:.6pt;margin:5mm 0;
  background:linear-gradient(90deg,var(--filo),transparent);}

/* ---- colophon ---- */
.colophon{page-break-before:always;font-size:9pt;color:var(--navy-tenue);
  border-top:1.1pt solid var(--navy);padding-top:5mm;margin-top:14mm;line-height:1.6;}
.colophon .sha{font-family:"Liberation Mono",monospace;font-size:8pt;word-break:break-all;color:var(--navy-fondo);}
`;

const html = `<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>${esc(titolo)}</title>
<meta name="author" content="Generato da un'intelligenza artificiale su richiesta del titolare del repository">
<meta name="description" content="${esc(sottotitolo)} — ${esc(occhiello)}">
<style>${CSS}</style></head><body>
<div class="carta"></div>
<section class="cover">
<div class="k">Aldo Moro · Ottanta anni senza pace</div>
<h1>${esc(titolo)}</h1>${sottotitolo ? `<div class="sub">${esc(sottotitolo)}</div>` : ''}${occhiello ? `<div class="subsub">${esc(occhiello)}</div>` : ''}${argomento ? `<div class="arg">${esc(argomento)}</div>` : ''}
<div class="rule"></div>
${epiHtml}
${collocazione ? `<div class="coll">${esc(collocazione)}</div>` : ''}
</section>
<section class="dich"><div class="disc">${inline(dichiarazione)}</div></section>
${body}
<section class="colophon">
<p><strong>Colophon.</strong> Composto in <strong>Barlow Semi Condensed</strong>. Carta bianca con gradiente di crema al cinque per cento; inchiostro blu navy con gradiente di nero al cinque per cento. Testo giustificato, sillabazione italiana; i versi non si giustificano e non si sillabano.</p>
<p><strong>Impronta della sorgente.</strong> Il markdown assemblato da cui questo volume è composto ha impronta SHA-256:</p>
<p class="sha">${shaFonte}</p>
<p>L'impronta si riproduce da chiunque abbia il repository: <code>python3 _monografia/assembla_opera.py</code> e poi <code>sha256sum</code> sul file prodotto. <strong>Un'impronta che non si può ricalcolare non certifica nulla.</strong></p>
</section>
</body></html>`;

fs.writeFileSync(OUT, html);
console.log(`scritto ${OUT} — ${html.length} byte · ${ancore.size} ancore · ${collegate} voci di sommario collegate · ${sillabate} punti di sillabazione · sha256(sorgente) ${shaFonte.slice(0, 16)}…`);
