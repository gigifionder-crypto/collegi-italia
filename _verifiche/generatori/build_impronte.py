# -*- coding: utf-8 -*-
"""La pagina del registro delle impronte di tutta l'opera."""
import json, os

SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
REPO = '/home/user/collegi-italia'
D = json.load(open(os.path.join(SP, 'impronte.json'), encoding='utf-8'))
TXT = open(os.path.join(REPO, 'IMPRONTE-SHA256.txt'), encoding='utf-8').read()
TXT_OPERA = open(os.path.join(REPO, 'IMPRONTE-OPERA-MORO.txt'), encoding='utf-8').read()

def _n(x):
    return f'{x:,}'.replace(',', '.')

def _peso(b):
    if b >= 1 << 20:
        return f'{b / (1 << 20):.1f}'.replace('.', ',') + ' MB'
    if b >= 1 << 10:
        return f'{b / (1 << 10):.0f} kB'
    return f'{b} B'

def righe(voci):
    return '\n'.join(
        '<li class="riga">'
        f'<div class="capo"><span class="nome">{v["nome"]}</span>'
        f'<span class="peso">{_n(v["byte"])} byte · {_peso(v["byte"])}</span></div>'
        f'<code class="sha">{v["sha"]}</code></li>'
        for v in voci)

def sezione(s, aperta):
    n = len(s['voci'])
    b = sum(v['byte'] for v in s['voci'])
    return (f'<details class="sez"{" open" if aperta else ""}>\n'
            f'<summary><span class="t">{s["titolo"]}</span>'
            f'<span class="c">{n} file · {_peso(b)}</span></summary>\n'
            f'<p class="nota">{s["nota"]}</p>\n'
            f'<ul class="elenco">\n{righe(s["voci"])}\n</ul>\n</details>')

SEZIONI = '\n'.join(sezione(s, s['chiave'] in ('volumi', 'grafici'))
                    for s in D['sezioni'])

SOMMARIO = '\n'.join(
    f'<tr><td>{s["titolo"]}</td><td class="num">{len(s["voci"])}</td>'
    f'<td class="num">{_n(sum(v["byte"] for v in s["voci"]))}</td></tr>'
    for s in D['sezioni'])

HTML = f'''<title>Le impronte dell'opera</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&family=Spectral:ital,wght@0,300;0,400;0,600;1,400&display=swap">
<style>
:root{{
  --paper:#ffffff; --cream:#f6efe1; --cream-deep:#f0e5d0; --surface:#fffdf8;
  --ink:#1F3864; --ink-soft:#42598a; --ink-faint:#7d8fb2;
  --navy:#1F3864; --navy-soft:#3d5c96; --brick:#8a2d2d;
  --rule:#ddd4c1; --rule-soft:#e9e0ce; --band:#f4ecdb;
  --mono:"IBM Plex Mono","SFMono-Regular",Consolas,"Liberation Mono",monospace;
  --cond:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
}}
*{{box-sizing:border-box;}}
body{{
  margin:0; background:var(--paper);
  background-image:linear-gradient(168deg,#ffffff 0%,#ffffff 24%,var(--cream) 76%,var(--cream-deep) 100%);
  background-attachment:fixed; min-height:100vh; color:var(--ink);
  font-family:"Spectral",Georgia,"Times New Roman",serif;
  font-size:17px; line-height:1.62; -webkit-font-smoothing:antialiased;
}}
.wrap{{max-width:53rem;margin:0 auto;padding:0 1.5rem 5rem;}}
p{{margin:0 0 1.05em;max-width:38rem;}}
strong{{font-weight:600;}}

header.top{{padding:4rem 0 2.2rem;border-bottom:1px solid var(--rule);}}
.eyebrow{{font-family:var(--cond);text-transform:uppercase;letter-spacing:.16em;
  font-size:.72rem;font-weight:600;color:var(--ink-faint);margin:0 0 1.1rem;}}
h1{{font-family:var(--cond);font-weight:700;font-size:clamp(2.5rem,6.5vw,3.9rem);
  line-height:1.02;letter-spacing:-.01em;margin:0 0 1.1rem;color:var(--navy);text-wrap:balance;}}
.stand{{font-size:1.14rem;line-height:1.55;color:var(--ink-soft);max-width:38rem;margin:0 0 1.4rem;}}
.stato{{font-family:var(--mono);font-size:.82rem;color:var(--ink-soft);
  background:var(--band);border-left:3px solid var(--navy);
  padding:.7rem .9rem;display:inline-block;max-width:100%;overflow-wrap:anywhere;}}

h2{{font-family:var(--cond);font-weight:700;font-size:1.6rem;line-height:1.16;
  margin:3.2rem 0 .5rem;color:var(--navy);text-wrap:balance;}}
h2 .n{{display:block;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;
  font-weight:600;color:var(--ink-faint);margin-bottom:.5rem;}}
h3{{font-family:var(--cond);font-weight:600;font-size:1.02rem;margin:1.9rem 0 .5rem;color:var(--navy-soft);}}
.lead{{color:var(--ink-soft);}}

pre{{font-family:var(--mono);font-size:.82rem;line-height:1.7;
  background:var(--surface);border:1px solid var(--rule-soft);
  padding:.85rem 1rem;margin:.7rem 0 1.2rem;overflow-x:auto;color:var(--ink);}}
pre.grande{{font-size:.86rem;border-left:3px solid var(--navy);
  overflow-wrap:anywhere;white-space:pre-wrap;user-select:all;}}

.due{{display:grid;gap:1.3rem;margin:1.6rem 0 1.2rem;}}
@media(min-width:44rem){{.due{{grid-template-columns:1fr 1fr;}}}}
.cassa{{background:var(--surface);border:1px solid var(--rule-soft);padding:1.1rem 1.2rem 1.2rem;}}
.cassa.si{{border-top:3px solid var(--navy);}}
.cassa.no{{border-top:3px solid var(--brick);}}
.cassa .k{{font-family:var(--cond);font-size:.72rem;font-weight:600;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ink-faint);display:block;margin-bottom:.45rem;}}
.cassa.no .k{{color:var(--brick);}}
.cassa p{{margin:0;font-size:.98rem;color:var(--ink-soft);}}

.tabwrap{{overflow-x:auto;margin:1.6rem 0 1rem;border:1px solid var(--rule-soft);background:var(--surface);}}
table{{border-collapse:collapse;width:100%;min-width:26rem;font-family:var(--cond);font-size:.9rem;}}
thead th{{text-align:left;font-weight:600;font-size:.72rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--ink-faint);padding:.75rem .9rem;border-bottom:1px solid var(--rule);}}
thead th.num,td.num{{text-align:right;}}
td{{padding:.55rem .9rem;border-bottom:1px solid var(--rule-soft);color:var(--ink);}}
td.num{{font-variant-numeric:tabular-nums;color:var(--ink-soft);white-space:nowrap;}}
tbody tr:last-child td{{border-bottom:none;font-weight:600;}}
tbody tr:last-child td.num{{color:var(--ink);}}

details.sez{{margin:.7rem 0;background:var(--surface);border:1px solid var(--rule-soft);}}
details.sez summary{{
  cursor:pointer;list-style:none;padding:.75rem 1rem;
  display:flex;flex-wrap:wrap;gap:.4rem 1rem;align-items:baseline;justify-content:space-between;
  font-family:var(--cond);
}}
details.sez summary::-webkit-details-marker{{display:none;}}
details.sez summary::before{{
  content:"+";font-family:var(--mono);color:var(--ink-faint);
  margin-right:.55rem;font-size:.9rem;
}}
details.sez[open] summary::before{{content:"–";}}
details.sez summary .t{{font-weight:600;font-size:1rem;color:var(--navy);flex:1 1 auto;}}
details.sez summary .c{{font-size:.8rem;color:var(--ink-faint);font-variant-numeric:tabular-nums;white-space:nowrap;}}
details.sez summary:focus-visible{{outline:2px solid var(--navy);outline-offset:-2px;}}
details.sez .nota{{font-family:var(--cond);font-size:.87rem;color:var(--ink-soft);
  margin:0;padding:0 1rem .3rem;max-width:42rem;}}

ul.elenco{{list-style:none;margin:.6rem 0 0;padding:0 1rem 1rem;}}
li.riga{{padding:.72rem 0 .78rem;border-top:1px solid var(--rule-soft);}}
.capo{{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:.4rem 1rem;}}
.nome{{font-family:var(--mono);font-size:.84rem;font-weight:500;color:var(--ink);overflow-wrap:anywhere;}}
.peso{{font-family:var(--cond);font-size:.78rem;color:var(--ink-faint);font-variant-numeric:tabular-nums;white-space:nowrap;}}
code.sha{{display:block;margin-top:.35rem;font-family:var(--mono);font-size:.76rem;
  line-height:1.55;color:var(--navy-soft);overflow-wrap:anywhere;user-select:all;cursor:text;}}

.dlbar{{margin:1.6rem 0 .4rem;display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;}}
button.dl{{font-family:var(--cond);font-size:.82rem;font-weight:600;letter-spacing:.03em;
  color:var(--navy);background:var(--surface);border:1px solid var(--rule);border-radius:2px;
  padding:.4rem .8rem;cursor:pointer;display:inline-flex;align-items:center;gap:.5rem;
  transition:background .12s ease,border-color .12s ease;}}
button.dl:hover{{background:var(--band);border-color:var(--navy-soft);}}
button.dl:focus-visible{{outline:2px solid var(--navy);outline-offset:2px;}}
button.dl[disabled]{{opacity:.55;cursor:default;}}
button.dl .ext{{font-size:.66rem;letter-spacing:.11em;color:var(--ink-faint);}}
button.dl.fatto{{color:#2f6b3a;border-color:#b7ccb8;background:#f2f7f1;}}

code.inline{{font-family:var(--mono);font-size:.86em;color:var(--navy-soft);overflow-wrap:anywhere;}}
.chiusa{{margin-top:3.4rem;padding-top:1.5rem;border-top:1px solid var(--rule);
  font-family:var(--cond);font-size:.83rem;line-height:1.6;color:var(--ink-faint);max-width:40rem;}}
</style>

<div class="wrap">

<header class="top">
  <p class="eyebrow">Ottanta anni di Pace · registro di integrità · 27 agosto 2026</p>
  <h1>Le impronte dell'opera</h1>
  <p class="stand">Ogni file porta qui la propria impronta crittografica. Chi ne
  riceve uno può accertare in un comando che è <strong>bit per bit</strong> quello
  depositato, e non una copia alterata, troncata o rimontata.</p>
  <p class="stato">commit {D['commit']}<br>ramo {D['ramo']}</p>
</header>

<h2><span class="n">I</span>Due lavori, non uno</h2>
<p class="lead">Il repository ospita <strong>due opere distinte</strong>, e vanno tenute
separate anche qui. Il corpus lo dichiara già per conto proprio: <code
class="inline">INDICE-DOCUMENTI-BRANCH.md</code> scrive alla terza riga che i documenti
del caso Moro sono «estranei al progetto principale del repository (Studio Integrale
Puglia)».</p>

<div class="tabwrap">
<table>
<thead><tr><th>Opera</th><th class="num">File</th><th class="num">Byte</th></tr></thead>
<tbody>
<tr><td><strong>L'opera — il caso Moro</strong></td><td class="num">{_n(D['file_opera'])}</td><td class="num">{_n(D['byte_opera'])}</td></tr>
<tr><td>Altro lavoro — Studio Integrale Puglia</td><td class="num">{_n(D['tot_file'] - D['file_opera'])}</td><td class="num">{_n(D['tot_byte'] - D['byte_opera'])}</td></tr>
<tr><td>Totale nel repository</td><td class="num">{_n(D['tot_file'])}</td><td class="num">{_n(D['tot_byte'])}</td></tr>
</tbody>
</table>
</div>

<p>Le impronte valgono per entrambi, perché entrambi stanno nel repository e chiunque
li riceva ha diritto di verificarli. <strong>L'attribuzione no</strong>: contarli insieme
sotto un'unica intestazione sarebbe un errore di descrizione, e in un'opera che misura
la distanza fra un fatto e la sua attribuzione sarebbe l'errore peggiore da commettere.</p>

<div class="cassa no" style="max-width:38rem">
  <span class="k">Annotazione</span>
  <p>La prima stesura di questo registro, del 27 agosto 2026, presentava i 209 file
  come se fossero un'opera sola. La cifra era esatta, la descrizione no. L'errore è
  corretto qui e <strong>annotato, non cancellato</strong>: le impronte di allora
  restano valide, l'intestazione che le raccoglieva era sbagliata.</p>
</div>

<h2><span class="n">II</span>L'impronta dell'opera</h2>
<p class="lead">Una stringa sola per il caso Moro. È l'impronta del manifesto
dell'opera, cioè del file che elenca i {_n(D['n_opera'])} file versionati che le
appartengono.</p>

<pre class="grande">{D['opera']}</pre>
<pre>sha256sum IMPRONTE-OPERA-MORO.txt</pre>

<h3>L'impronta dell'insieme versionato</h3>
<p>La stessa cosa per tutti i {_n(D['n_manifesto'])} file versionati del repository,
le due opere insieme.</p>
<pre class="grande">{D['insieme']}</pre>
<pre>sha256sum IMPRONTE-SHA256.txt</pre>

<p>Se una di queste stringhe coincide, <strong>l'insieme che copre è quello
depositato</strong>: non un file di meno, non un file di più, nessun file diverso.
Se differisce, il confronto riga per riga dice quale.</p>

<h3>I tre file che restano fuori, e perché</h3>
<p>I manifesti elencano ogni file versionato <strong>tranne tre</strong>: i due manifesti
stessi e questo registro. Non è una svista, ed è l'unica esclusione. Un registro non può
certificare sé stesso: i suoi file cambiano a ogni rigenerazione, e l'impronta che vi si
scrivesse dentro sarebbe falsa nell'istante in cui viene scritta.</p>
<p>La catena si chiude comunque, e senza circoli: i file sono certificati dal manifesto,
il manifesto è certificato dalla stringa qui sopra, e questo registro non ha bisogno di
esserlo perché <strong>è interamente ricavabile dal manifesto</strong> — chi vuole
controllarlo lo rigenera.</p>

<h2><span class="n">III</span>Come si verifica</h2>
<p class="lead">Tutti i file versionati in un colpo solo, dalla radice del repository.</p>
<pre>sha256sum --check IMPRONTE-OPERA-MORO.txt  <span class="c"># il solo caso Moro</span>
sha256sum --check IMPRONTE-SHA256.txt      <span class="c"># le due opere</span></pre>
<div class="dlbar" hidden id="dlbar">
  <button type="button" class="dl" id="dlopera">Manifesto dell'opera <span class="ext">TXT</span></button>
  <button type="button" class="dl" id="dltxt">Manifesto dell'insieme <span class="ext">TXT</span></button>
</div>

<h3>Un file solo</h3>
<pre>sha256sum UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf     <span class="c"># Linux</span>
shasum -a 256 UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf <span class="c"># macOS</span></pre>

<h3>Su Windows, da PowerShell</h3>
<pre>Get-FileHash UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf -Algorithm SHA256</pre>

<p>La stringa che compare va confrontata con quella del registro. Se coincide, il
file è integro. Se differisce anche per un solo carattere <strong>non è lo stesso
file</strong>: non va letto come se lo fosse, e va richiesta una copia nuova.</p>

<h2><span class="n">IV</span>Che cosa l'impronta certifica, e che cosa no</h2>
<p class="lead">Va detto con precisione, perché è esattamente il genere di distinzione
su cui quest'opera è costruita.</p>

<div class="due">
  <div class="cassa si">
    <span class="k">Certifica</span>
    <p>Che il file ricevuto è identico a quello depositato. È una garanzia
    sull'<strong>integrità del supporto</strong>: nessuno ha cambiato una cifra,
    tolto una pagina, sostituito un allegato.</p>
  </div>
  <div class="cassa no">
    <span class="k">Non certifica</span>
    <p>Che ciò che il file contiene sia vero. Un documento falso conserva la propria
    impronta con la stessa fedeltà di un documento esatto. L'integrità è una proprietà
    del contenitore, non del contenuto.</p>
  </div>
</div>

<p>Chi riceve quest'opera deve poter fare due cose distinte: <strong>accertare</strong>
di averla ricevuta integra — e a questo serve il registro — e <strong>verificare</strong>
ciò che afferma, che è invece il lavoro reso possibile dai gradi dichiarati, dalle sedi
d'archivio nominate e dagli Stati Zero. La prima cosa è meccanica. La seconda no.</p>

<h2><span class="n">V</span>Il sommario</h2>
<div class="tabwrap">
<table>
<thead><tr><th>Sezione</th><th class="num">File</th><th class="num">Byte</th></tr></thead>
<tbody>
{SOMMARIO}
<tr><td>Totale</td><td class="num">{_n(D['tot_file'])}</td><td class="num">{_n(D['tot_byte'])}</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">VI</span>Le impronte, sezione per sezione</h2>
<p class="lead">Ogni sezione si apre con un clic. Un clic sull'impronta la seleziona
per intero.</p>

{SEZIONI}

<h2><span class="n">VII</span>Il commit, che è un'altra cosa</h2>
<p>L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git.
Sono due garanzie diverse e vanno tenute distinte: il commit fissa <strong>lo stato
del repository</strong> — quali file esistevano e con quale contenuto in quel momento.
L'impronta SHA-256 fissa <strong>il singolo file</strong> anche quando viaggia fuori
dal repository: in allegato a una PEC, su una chiave, dentro un deposito d'archivio.
Un file staccato dal repository perde il commit e conserva l'impronta.</p>
<p>Il pacchetto dei grafici lo mostra bene: non è versionato, quindi non ha commit —
e ha comunque un'impronta.</p>
<pre>{D['commit']}</pre>

<p class="chiusa">
Le impronte si ricalcolano a ogni nuova edizione. Un registro che non cambia quando
cambiano i file non certifica nulla: viene rigenerato dal proprio script e ricommesso
insieme all'opera.<br><br>
Registro prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.
</p>

</div>
'''

SCRIPT = """
<script>
(async () => {
  // Il bottone compare solo se il visore serve davvero il salvataggio.
  const dl = window.claude && await window.claude.use("downloads");
  if (!dl) return;
  const barra = document.getElementById("dlbar");
  if (!barra) return;
  barra.hidden = false;
  const FILE = [
    ["dlopera", "IMPRONTE-OPERA-MORO.txt", __TXT_OPERA__],
    ["dltxt",   "IMPRONTE-SHA256.txt",     __TXT__],
  ];
  for (const [id, filename, testo] of FILE) {
    const btn = document.getElementById(id);
    if (!btn) continue;
    btn.addEventListener("click", async () => {
      btn.disabled = true;
      try {
        await dl.save({ filename, data: testo });
        btn.firstChild.nodeValue = "Salvato ";
        btn.classList.add("fatto");
        btn.querySelector(".ext").hidden = true;
      } catch (e) {
        if ((e && e.code) !== "declined") btn.firstChild.nodeValue = "Salvataggio non disponibile ";
      }
      btn.disabled = false;
    });
  }
})();
</script>
""".replace('__TXT__', json.dumps(TXT)).replace('__TXT_OPERA__', json.dumps(TXT_OPERA))

out = os.path.join(SP, 'impronte.html')
open(out, 'w', encoding='utf-8').write(HTML + SCRIPT)
print(out, os.path.getsize(out) // 1024, 'kB')
