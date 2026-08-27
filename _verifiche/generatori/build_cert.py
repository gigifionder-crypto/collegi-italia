# -*- coding: utf-8 -*-
"""La pagina della certificazione, coi tre grafici incorporati."""
import base64, importlib.util, os, re, sys
SP='/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
REPO='/home/user/collegi-italia'; G=os.path.join(SP,'grafici-verifica-p2')
spec=importlib.util.spec_from_file_location('pd', os.path.join(SP,'p_dossier.py'))
pd=importlib.util.module_from_spec(spec); sys.argv=['x','--i']
try: spec.loader.exec_module(pd)
except SystemExit: pass

def fig(nome, dida):
    b=base64.b64encode(open(os.path.join(G,nome),'rb').read()).decode()
    return (f'<figure class="g" data-file="{nome}">\n<img src="data:image/png;base64,{b}" alt="{dida}">\n'
            f'<figcaption>{dida}</figcaption>\n<div class="dlbar" hidden>'
            f'<button type="button" class="dl">Scarica il grafico <span class="ext">PNG</span></button></div>\n</figure>')

MD=open(os.path.join(REPO,'_verifiche/certificazione-numeri-p2.md'),encoding='utf-8').read()
righe=MD.split('\n'); i=next(k for k,r in enumerate(righe) if r.startswith('---'))
CORPO=pd.to_html('\n'.join(righe[i+1:]))

# i grafici entrano dove il discorso li chiama
CORPO=CORPO.replace('<h2>3. L&#x27;aritmetica',
  fig('10_le-due-numerazioni-sulla-stessa-retta.png',
      "Ogni punto è una persona: in ascissa la tessera che il testo le attribuisce, in ordinata il fascicolo. Otto coppie cadono esattamente sulla retta fascicolo = tessera − 1.088.")
  + '\n<h2>3. L&#x27;aritmetica',1)
CORPO=CORPO.replace('<h2>4. Che cosa ritiro',
  fig('11_scarto-dalla-retta.png', "Lo scarto di ciascuna coppia dal valore che la retta predice: otto a zero, dodici in deviazione da una a trecentoventotto posizioni.")
  + '\n' + fig('12_un-archivio-deriva.png', "Il controllo di calibrazione: nelle due coppie attestate lo scarto deriva, nelle otto del testo resta congelato per quarantadue posizioni.")
  + '\n<h2>4. Che cosa ritiro',1)

STILE=open(os.path.join(SP,'pec.html'),encoding='utf-8').read()
STILE=STILE[STILE.index('<style>'):STILE.index('</style>')+8]
STILE=STILE.replace('.wrap{max-width:47rem','.wrap{max-width:50rem').replace('</style>','''
figure.g{margin:1.8rem 0 2.1rem;padding:0;}
figure.g img{display:block;width:100%;height:auto;border:1px solid var(--rule-soft);background:var(--surface);}
figure.g figcaption{font-family:var(--cond);font-size:.86rem;line-height:1.45;color:var(--ink-soft);margin-top:.55rem;}
.dlbar{margin-top:.5rem;}
button.dl{font-family:var(--cond);font-size:.82rem;font-weight:600;color:var(--navy);background:var(--surface);
  border:1px solid var(--rule);border-radius:2px;padding:.38rem .78rem;cursor:pointer;
  display:inline-flex;align-items:center;gap:.5rem;}
button.dl:hover{background:var(--band);border-color:var(--navy-soft);}
button.dl:focus-visible{outline:2px solid var(--navy);outline-offset:2px;}
button.dl .ext{font-size:.66rem;letter-spacing:.11em;color:var(--ink-faint);}
button.dl.fatto{color:#2f6b3a;border-color:#b7ccb8;background:#f2f7f1;}
</style>''')

HTML=f'''<title>Numero non accertato</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400&family=Spectral:ital,wght@0,300;0,400;0,600;1,400&display=swap">
{STILE}
<div class="wrap">
<header class="top">
  <p class="eyebrow">Ottanta anni di Pace · certificazione · 27 agosto 2026</p>
  <h1>Numero non accertato</h1>
  <p class="stand">Mi è stato chiesto di certificare i numeri di tessera e di
  fascicolo di trentatré persone. <strong>Nessuno dei trentatré è
  certificabile.</strong> Ma la verifica ha trovato che cosa quei numeri sono
  davvero — e l'aritmetica del testo, contro sé stessa, dice il resto.</p>
</header>
{CORPO}
<p class="chiusa">
Verifica condotta con diciassette agenti di ricerca indipendenti e con
un'analisi aritmetica deterministica e riproducibile. Prodotta con sistemi di
intelligenza artificiale sotto direzione e responsabilità umana. I limiti della
ricerca sono dichiarati in apertura e non in calce.
</p>
</div>
<script>
(async () => {{
  const dl = window.claude && await window.claude.use("downloads");
  if (!dl) return;
  const byte = (src) => {{
    const bin = atob(src.slice(src.indexOf(",") + 1));
    const b = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) b[i] = bin.charCodeAt(i);
    return b;
  }};
  document.querySelectorAll("figure.g").forEach((f) => {{
    const barra = f.querySelector(".dlbar"), btn = f.querySelector("button.dl");
    if (!barra || !btn) return;
    barra.hidden = false;
    btn.addEventListener("click", async () => {{
      btn.disabled = true;
      try {{
        await dl.save({{ filename: f.dataset.file, data: byte(f.querySelector("img").src) }});
        btn.firstChild.nodeValue = "Salvato ";
        btn.classList.add("fatto");
        btn.querySelector(".ext").hidden = true;
      }} catch (e) {{
        if ((e && e.code) !== "declined") btn.firstChild.nodeValue = "Non disponibile ";
      }}
      btn.disabled = false;
    }});
  }});
}})();
</script>
'''
out=os.path.join(SP,'certificazione.html')
open(out,'w',encoding='utf-8').write(HTML)
print(out, os.path.getsize(out)//1024, 'kB')
