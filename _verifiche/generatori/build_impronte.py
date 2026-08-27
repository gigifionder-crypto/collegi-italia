# -*- coding: utf-8 -*-
"""La pagina del registro delle impronte."""
import json, os

SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
REPO = '/home/user/collegi-italia'
D = json.load(open(os.path.join(SP, 'impronte.json'), encoding='utf-8'))
TXT = open(os.path.join(REPO, 'IMPRONTE-SHA256.txt'), encoding='utf-8').read()

def _n(x):
    return f'{x:,}'.replace(',', '.')

def _peso(b):
    if b >= 1 << 20:
        return f'{b / (1 << 20):.1f}'.replace('.', ',') + ' MB'
    return f'{b / (1 << 10):.0f} kB'

def righe(voci):
    out = []
    for v in voci:
        out.append(
            '<li class="riga">'
            f'<div class="capo"><span class="nome">{v["nome"]}</span>'
            f'<span class="peso">{_n(v["byte"])} byte · {_peso(v["byte"])}</span></div>'
            f'<code class="sha" title="Un clic seleziona l\'impronta intera">{v["sha"]}</code>'
            '</li>')
    return '\n'.join(out)

HTML = f'''<title>Le impronte dei volumi</title>
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
.eyebrow{{
  font-family:var(--cond);text-transform:uppercase;letter-spacing:.16em;
  font-size:.72rem;font-weight:600;color:var(--ink-faint);margin:0 0 1.1rem;
}}
h1{{
  font-family:var(--cond);font-weight:700;font-size:clamp(2.5rem,6.5vw,3.9rem);
  line-height:1.02;letter-spacing:-.01em;margin:0 0 1.1rem;color:var(--navy);text-wrap:balance;
}}
.stand{{font-size:1.14rem;line-height:1.55;color:var(--ink-soft);max-width:38rem;margin:0 0 1.4rem;}}
.stato{{
  font-family:var(--mono);font-size:.82rem;color:var(--ink-soft);
  background:var(--band);border-left:3px solid var(--navy);
  padding:.7rem .9rem;display:inline-block;max-width:100%;overflow-wrap:anywhere;
}}

h2{{
  font-family:var(--cond);font-weight:700;font-size:1.6rem;line-height:1.16;
  margin:3.2rem 0 .5rem;color:var(--navy);text-wrap:balance;
}}
h2 .n{{display:block;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;
  font-weight:600;color:var(--ink-faint);margin-bottom:.5rem;}}
h3{{font-family:var(--cond);font-weight:600;font-size:1.02rem;margin:1.9rem 0 .5rem;color:var(--navy-soft);}}
.lead{{color:var(--ink-soft);}}

pre{{
  font-family:var(--mono);font-size:.82rem;line-height:1.7;
  background:var(--surface);border:1px solid var(--rule-soft);
  padding:.85rem 1rem;margin:.7rem 0 1.2rem;overflow-x:auto;color:var(--ink);
}}
pre .c{{color:var(--ink-faint);}}

.due{{display:grid;gap:1.3rem;margin:1.6rem 0 1.2rem;}}
@media(min-width:44rem){{.due{{grid-template-columns:1fr 1fr;}}}}
.cassa{{background:var(--surface);border:1px solid var(--rule-soft);padding:1.1rem 1.2rem 1.2rem;}}
.cassa.si{{border-top:3px solid var(--navy);}}
.cassa.no{{border-top:3px solid var(--brick);}}
.cassa .k{{
  font-family:var(--cond);font-size:.72rem;font-weight:600;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ink-faint);display:block;margin-bottom:.45rem;
}}
.cassa.no .k{{color:var(--brick);}}
.cassa p{{margin:0;font-size:.98rem;color:var(--ink-soft);}}
.cassa p + p{{margin-top:.7rem;}}

ul.elenco{{list-style:none;margin:1.5rem 0 0;padding:0;border-top:1px solid var(--rule-soft);}}
li.riga{{padding:.8rem 0 .85rem;border-bottom:1px solid var(--rule-soft);}}
.capo{{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:.5rem 1rem;}}
.nome{{font-family:var(--mono);font-size:.86rem;font-weight:500;color:var(--ink);overflow-wrap:anywhere;}}
.peso{{font-family:var(--cond);font-size:.8rem;color:var(--ink-faint);font-variant-numeric:tabular-nums;white-space:nowrap;}}
code.sha{{
  display:block;margin-top:.4rem;
  font-family:var(--mono);font-size:.78rem;line-height:1.55;letter-spacing:.01em;
  color:var(--navy-soft);overflow-wrap:anywhere;user-select:all;cursor:text;
}}

.dlbar{{margin:1.6rem 0 .4rem;display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;}}
button.dl{{
  font-family:var(--cond);font-size:.82rem;font-weight:600;letter-spacing:.03em;
  color:var(--navy);background:var(--surface);border:1px solid var(--rule);border-radius:2px;
  padding:.4rem .8rem;cursor:pointer;display:inline-flex;align-items:center;gap:.5rem;
  transition:background .12s ease,border-color .12s ease;
}}
button.dl:hover{{background:var(--band);border-color:var(--navy-soft);}}
button.dl:focus-visible{{outline:2px solid var(--navy);outline-offset:2px;}}
button.dl[disabled]{{opacity:.55;cursor:default;}}
button.dl .ext{{font-size:.66rem;letter-spacing:.11em;color:var(--ink-faint);}}
button.dl.fatto{{color:#2f6b3a;border-color:#b7ccb8;background:#f2f7f1;}}

.chiusa{{margin-top:3.4rem;padding-top:1.5rem;border-top:1px solid var(--rule);
  font-family:var(--cond);font-size:.83rem;line-height:1.6;color:var(--ink-faint);max-width:40rem;}}
</style>

<div class="wrap">

<header class="top">
  <p class="eyebrow">Ottanta anni senza Pace · registro di integrità · 27 agosto 2026</p>
  <h1>Le impronte dei volumi</h1>
  <p class="stand">Ogni file pubblicato porta qui la propria impronta crittografica.
  Chi riceve un volume — un editore, un archivio, un lettore — può accertare in un
  comando che il file che ha in mano è <strong>bit per bit</strong> quello depositato,
  e non una copia alterata, troncata o rimontata.</p>
  <p class="stato">commit {D['commit']}<br>ramo {D['ramo']}</p>
</header>

<h2><span class="n">I</span>Come si verifica</h2>
<p class="lead">Dalla cartella che contiene il file, un comando solo.</p>

<h3>Linux</h3>
<pre>sha256sum UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf</pre>

<h3>macOS</h3>
<pre>shasum -a 256 UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf</pre>

<h3>Windows, da PowerShell</h3>
<pre>Get-FileHash UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf -Algorithm SHA256</pre>

<p>La stringa che compare va confrontata con quella del registro. Se coincide, il
file è integro. Se differisce anche per un solo carattere <strong>non è lo stesso
file</strong>: non va letto come se lo fosse, e va richiesta una copia nuova.</p>

<h3>Tutti i volumi in un colpo solo</h3>
<pre>sha256sum --check IMPRONTE-SHA256.txt</pre>
<div class="dlbar" hidden id="dlbar">
  <button type="button" class="dl" id="dltxt">Scarica il file delle impronte <span class="ext">TXT</span></button>
</div>

<h2><span class="n">II</span>Che cosa l'impronta certifica, e che cosa no</h2>
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

<p>Chi riceve questi volumi deve poter fare due cose distinte: <strong>accertare</strong>
di averli ricevuti integri — e a questo serve il registro — e <strong>verificare</strong>
ciò che affermano, che è invece il lavoro reso possibile dai gradi dichiarati, dalle sedi
d'archivio nominate e dagli Stati Zero. La prima cosa è meccanica. La seconda no.</p>

<h2><span class="n">III</span>L'opera integrale</h2>
<ul class="elenco">
{righe(D['integrale'])}
</ul>

<h2><span class="n">IV</span>I volumi autonomi</h2>
<p class="lead">Estratti dell'opera integrale, non testi diversi: ciascuno riporta un
tratto del corpus nella stessa composizione tipografica.</p>
<ul class="elenco">
{righe(D['volumi'])}
</ul>

<h2><span class="n">V</span>Il pacchetto dei grafici della verifica</h2>
<ul class="elenco">
{righe(D['grafici'])}
</ul>

<h2><span class="n">VI</span>Il commit, che è un'altra cosa</h2>
<p>L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git.
Sono due garanzie diverse e vanno tenute distinte: il commit fissa <strong>lo stato
del repository</strong> — quali file esistevano e con quale contenuto in quel momento.
L'impronta SHA-256 fissa <strong>il singolo file</strong> anche quando viaggia fuori
dal repository: in allegato a una PEC, su una chiave, dentro un deposito d'archivio.
Un file staccato dal repository perde il commit e conserva l'impronta.</p>
<pre>{D['commit']}</pre>

<p class="chiusa">
Le impronte si ricalcolano a ogni nuova edizione. Un registro che non cambia quando
cambiano i file non certifica nulla: viene rigenerato dal proprio script e ricommesso
insieme ai volumi.<br><br>
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
  const btn = document.getElementById("dltxt");
  if (!barra || !btn) return;
  barra.hidden = false;
  const TESTO = __TXT__;
  btn.addEventListener("click", async () => {
    btn.disabled = true;
    try {
      await dl.save({ filename: "IMPRONTE-SHA256.txt", data: TESTO });
      btn.firstChild.nodeValue = "Salvato ";
      btn.classList.add("fatto");
      btn.querySelector(".ext").hidden = true;
    } catch (e) {
      if ((e && e.code) !== "declined") btn.firstChild.nodeValue = "Salvataggio non disponibile ";
    }
    btn.disabled = false;
  });
})();
</script>
""".replace('__TXT__', json.dumps(TXT))

out = os.path.join(SP, 'impronte.html')
open(out, 'w', encoding='utf-8').write(HTML + SCRIPT)
print(out, os.path.getsize(out) // 1024, 'kB')
