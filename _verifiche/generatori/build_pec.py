# -*- coding: utf-8 -*-
"""La pagina della PEC unica, nello stile della casa."""
import importlib.util, os, sys
SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
REPO = '/home/user/collegi-italia'
spec = importlib.util.spec_from_file_location('pd', os.path.join(SP, 'p_dossier.py'))
pd = importlib.util.module_from_spec(spec)
sys.argv = ['p_dossier.py', '--solo-import']
try:
    spec.loader.exec_module(pd)
except SystemExit:
    pass

MD = open(os.path.join(REPO, '_diffusione-opera/pec-unica-formale.md'), encoding='utf-8').read()
# via il titolo e la riga di dichiarazione: la pagina li porta nella testata
righe = MD.split('\n')
i = next(k for k, r in enumerate(righe) if r.startswith('---'))
CORPO = pd.to_html('\n'.join(righe[i + 1:]))

HTML = f'''<title>La PEC unica</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400&family=Spectral:ital,wght@0,300;0,400;0,600;1,400&display=swap">
<style>
:root{{
  --paper:#ffffff; --cream:#f6efe1; --cream-deep:#f0e5d0; --surface:#fffdf8;
  --ink:#1F3864; --ink-soft:#42598a; --ink-faint:#7d8fb2;
  --navy:#1F3864; --navy-soft:#3d5c96; --brick:#8a2d2d;
  --rule:#ddd4c1; --rule-soft:#e9e0ce; --band:#f4ecdb;
  --mono:"IBM Plex Mono","SFMono-Regular",Consolas,monospace;
  --cond:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
}}
*{{box-sizing:border-box;}}
body{{margin:0;background:var(--paper);
  background-image:linear-gradient(168deg,#ffffff 0%,#ffffff 24%,var(--cream) 76%,var(--cream-deep) 100%);
  background-attachment:fixed;min-height:100vh;color:var(--ink);
  font-family:"Spectral",Georgia,"Times New Roman",serif;font-size:17px;line-height:1.62;
  -webkit-font-smoothing:antialiased;}}
.wrap{{max-width:47rem;margin:0 auto;padding:0 1.5rem 5rem;}}
p{{margin:0 0 1.05em;}}
strong{{font-weight:600;}} em{{font-style:italic;}}

header.top{{padding:4rem 0 2rem;border-bottom:1px solid var(--rule);}}
.eyebrow{{font-family:var(--cond);text-transform:uppercase;letter-spacing:.16em;
  font-size:.72rem;font-weight:600;color:var(--ink-faint);margin:0 0 1.1rem;}}
h1{{font-family:var(--cond);font-weight:700;font-size:clamp(2.4rem,6.5vw,3.7rem);
  line-height:1.03;letter-spacing:-.01em;margin:0 0 1rem;color:var(--navy);text-wrap:balance;}}
.stand{{font-size:1.13rem;line-height:1.55;color:var(--ink-soft);margin:0;}}

h2{{font-family:var(--cond);font-weight:700;font-size:1.55rem;line-height:1.16;
  margin:2.9rem 0 .55rem;color:var(--navy);text-wrap:balance;
  padding-top:1.4rem;border-top:1px solid var(--rule-soft);}}
h2:first-of-type{{border-top:none;padding-top:0;}}
h3{{font-family:var(--cond);font-weight:600;font-size:1.06rem;margin:1.9rem 0 .5rem;color:var(--navy-soft);}}

blockquote{{margin:1.2rem 0;padding:.9rem 1.1rem;background:var(--band);
  border-left:3px solid var(--navy);}}
blockquote p{{margin:0;font-family:var(--cond);font-size:1.02rem;line-height:1.45;color:var(--navy);}}
blockquote code{{font-family:var(--mono);font-size:.82rem;overflow-wrap:anywhere;
  user-select:all;color:var(--navy-soft);}}
code{{font-family:var(--mono);font-size:.87em;color:var(--navy-soft);overflow-wrap:anywhere;}}

.tabwrap,table{{max-width:100%;}}
table{{border-collapse:collapse;width:100%;margin:1.3rem 0;font-family:var(--cond);
  font-size:.9rem;background:var(--surface);border:1px solid var(--rule-soft);}}
th{{text-align:left;font-weight:600;font-size:.72rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--ink-faint);padding:.7rem .85rem;border-bottom:1px solid var(--rule);}}
td{{padding:.55rem .85rem;border-bottom:1px solid var(--rule-soft);vertical-align:top;}}
tr:last-child td{{border-bottom:none;}}

ol,ul{{padding-left:1.3rem;margin:0 0 1.1rem;}}
li{{margin-bottom:.4rem;}}
ul li{{list-style:none;position:relative;}}
ul li::before{{content:"—";position:absolute;left:-1.3rem;color:var(--ink-faint);}}
hr{{border:none;border-top:1px solid var(--rule-soft);margin:2.4rem 0;}}

.chiusa{{margin-top:3.2rem;padding-top:1.4rem;border-top:1px solid var(--rule);
  font-family:var(--cond);font-size:.83rem;line-height:1.6;color:var(--ink-faint);}}
</style>

<div class="wrap">
<header class="top">
  <p class="eyebrow">Ottanta anni di Pace · dossier di invio · 27 agosto 2026</p>
  <h1>La PEC unica</h1>
  <p class="stand">Un solo testo formale per tutti i destinatari, unico nel contenuto
  e adattabile nel canale. Con l'avvertenza che lo precede: dei dodici destinatari,
  <strong>uno solo ha davvero un canale PEC</strong>.</p>
</header>

{CORPO}

<p class="chiusa">
Lettera prodotta con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera. I campi fra parentesi
quadre vanno compilati e le parentesi tolte prima dell'invio.
</p>
</div>
'''
out = os.path.join(SP, 'pec.html')
open(out, 'w', encoding='utf-8').write(HTML)
print(out, os.path.getsize(out) // 1024, 'kB')
