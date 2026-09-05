// Renderer PDF dell'Opera. Non usa --print-to-pdf da riga di comando perche'
// quella via non sa fare tre cose che a un volume di 250 pagine servono:
//   - PDF TAGGATO (struttura accessibile, lettura assistita)
//   - SEGNALIBRI generati dalla gerarchia dei titoli
//   - NUMERAZIONE delle pagine al piede
// Le fa Playwright, che pilota lo stesso Chromium via protocollo.
//
// Uso: node pdf_opera.js <sorgente.html> <uscita.pdf>
const path = require('path');
const M = '/opt/node22/lib/node_modules/playwright';
const { chromium } = require(M);

const SRC = process.argv[2], OUT = process.argv[3];
if (!SRC || !OUT) { console.error('uso: node pdf_opera.js <sorgente.html> <uscita.pdf>'); process.exit(1); }

const PIEDE = `
<div style="width:100%;font-family:'Barlow Semi Condensed',sans-serif;font-size:7.4pt;
            color:#5B6B8C;padding:0 19mm;-webkit-print-color-adjust:exact;">
  <div style="border-top:.4pt solid #C9D2E2;padding-top:2mm;display:flex;justify-content:space-between;">
    <span style="letter-spacing:.14em;text-transform:uppercase;">Opera Nera · Aldo Moro</span>
    <span style="font-variant-numeric:tabular-nums;"><span class="pageNumber"></span></span>
  </div>
</div>`;

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--font-render-hinting=none'] });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(SRC), { waitUntil: 'load', timeout: 180000 });
  await page.emulateMedia({ media: 'print' });
  // Le facce sono installate localmente: si attende che siano davvero pronte,
  // altrimenti il PDF ripiega su un'altra faccia senza dirlo.
  await page.evaluate(() => document.fonts.ready);
  const usaBarlow = await page.evaluate(() =>
    document.fonts.check('400 11pt "Barlow Semi Condensed"') &&
    document.fonts.check('700 11pt "Barlow Semi Condensed"'));
  if (!usaBarlow) { console.error('ERRORE: Barlow Semi Condensed non risolve. Non compongo un PDF che ripiega in silenzio.'); await browser.close(); process.exit(2); }

  // Nessun elemento puo' essere piu' largo della pagina: se lo e', Chromium
  // rimpicciolisce IN SILENZIO tutto il documento per farcelo stare, e il
  // libro esce di due terzi. Verificato su tre tomi, rimpiccioliti da alcuni
  // indirizzi lunghi dell'apparato bibliografico. Si controlla prima di
  // comporre, perche' dopo il danno non si vede: il PDF sembra a posto.
  const largo = await page.evaluate(() => {
    const L = document.body.clientWidth, fuori = [];
    for (const e of document.querySelectorAll('body *')) {
      const w = Math.max(e.scrollWidth, e.getBoundingClientRect().width);
      if (w > L + 2) fuori.push({ tag: e.tagName, w: Math.round(w),
                                  testo: (e.textContent || '').trim().slice(0, 90) });
    }
    return { L, fuori: fuori.sort((a, b) => b.w - a.w).slice(0, 5), n: fuori.length };
  });
  if (largo.n) {
    console.error(`ERRORE: ${largo.n} elementi sono piu' larghi della pagina (${largo.L}px).`);
    for (const x of largo.fuori) console.error(`  ${x.tag} ${x.w}px  ${JSON.stringify(x.testo)}`);
    console.error("Chromium rimpicciolirebbe in silenzio tutto il documento. Non compongo.");
    await browser.close(); process.exit(3);
  }
  await page.pdf({
    path: OUT, format: 'A4', printBackground: true,
    margin: { top: '15mm', right: '0mm', bottom: '16mm', left: '0mm' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: PIEDE,
    tagged: true,     // struttura accessibile
    outline: true,    // segnalibri dai titoli
    preferCSSPageSize: false,
  });
  await browser.close();
  console.log('reso', OUT, '· Barlow verificata · taggato · segnalibri');
})().catch(e => { console.error(e); process.exit(1); });
