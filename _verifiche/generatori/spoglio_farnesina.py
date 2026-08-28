#!/usr/bin/env python3
"""Spoglio del Libro dodicesimo: estrae le proposizioni datate con luogo.
Criterio dichiarato: una frase entra se contiene (a) una data risolvibile
almeno al mese, e (b) un toponimo o un'istituzione localizzata. Le frasi
puramente metodologiche sono escluse per parola-spia."""
import re, glob, json, collections

MESI = ('gennaio febbraio marzo aprile maggio giugno luglio agosto settembre '
        'ottobre novembre dicembre').split()
RE_GIORNO = re.compile(r'\b(\d{1,2})\s+(' + '|'.join(MESI) + r')\s+(19\d{2})\b', re.I)
RE_MESE   = re.compile(r'\b(' + '|'.join(MESI) + r')\s+(19\d{2})\b', re.I)
RE_ANNO   = re.compile(r'\b(19[4-8]\d)\b')

LUOGHI = ['Lisbona','Madrid','Atene','Ankara','Istanbul','Bonn','Berlino','Varsavia',
          'Roma','Vaticano','Farnesina','Pretoria','Città del Capo','Windhoek','Tripoli',
          'Bengasi','Nicosia','Cipro','Il Cairo','Tel Aviv','Belgrado','Mosca','Washington',
          'New York','Ginevra','Bruxelles','Parigi','Londra','Helsinki','Lourenço Marques',
          'Luanda','Maputo','Praga','Vienna','Strasburgo','Napoli','Milano','Bari','Torino',
          'Palazzo Chigi','Quirinale','Montecitorio','Palazzo Giustiniani','Nazioni Unite',
          'Santa Sede','Segreteria di Stato','Estado Novo','Aermacchi','Aginter']

SPIA = ('metodo','criterio','grado','livello','stato zero','ricognizione','registro',
        'blocco mirato','falsificatore','ipotesi','congettura','si registra','va registrat',
        'la presente','questo capitolo','la ricerca','fonte','bibliograf')

def frasi(t):
    t = re.sub(r'\s+', ' ', t)
    return re.split(r'(?<=[.;])\s+(?=[A-ZÈÉÀÌÒÙ«])', t)

def data_di(f):
    m = RE_GIORNO.search(f)
    if m: return f"{int(m.group(1)):02d} {m.group(2).lower()} {m.group(3)}", 'giorno', int(m.group(3))
    m = RE_MESE.search(f)
    if m: return f"{m.group(1).lower()} {m.group(2)}", 'mese', int(m.group(2))
    m = RE_ANNO.search(f)
    if m: return m.group(1), 'anno', int(m.group(1))
    return None, None, None

righe = []
for path in sorted(glob.glob('moro-ministro-esteri/**/*.md', recursive=True)):
    testo = open(path, encoding='utf-8').read()
    for f in frasi(testo):
        if len(f) < 60 or len(f) > 700: continue
        b = f.lower()
        if any(s in b for s in SPIA): continue
        d, prec, anno = data_di(f)
        if not d: continue
        lu = [l for l in LUOGHI if l.lower() in b]
        if not lu: continue
        righe.append({'file': path.split('/')[-1], 'data': d, 'precisione': prec,
                      'anno': anno, 'luoghi': lu, 'frase': f.strip()})

# deduplica per (data, primo luogo, incipit)
visti, out = set(), []
for r in righe:
    k = (r['data'], r['luoghi'][0], r['frase'][:80])
    if k in visti: continue
    visti.add(k); out.append(r)

out.sort(key=lambda r: (r['anno'], r['data']))
json.dump(out, open('/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/spoglio.json','w'), ensure_ascii=False, indent=1)

print(f"proposizioni datate e localizzate: {len(out)}")
print("precisione:", collections.Counter(r['precisione'] for r in out))
print("per anno:", dict(sorted(collections.Counter(r['anno'] for r in out).items())))
print("luoghi piu frequenti:", collections.Counter(l for r in out for l in r['luoghi']).most_common(15))
print("\n--- le datate al giorno ---")
for r in out:
    if r['precisione']=='giorno':
        print(f"[{r['data']}] {'/'.join(r['luoghi'][:2])} :: {r['frase'][:230]}")
