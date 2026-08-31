# -*- coding: utf-8 -*-
"""Estrae tutte le note bibliografiche con indirizzo dai 35 capitoli dell'Opera integrale,
numerate dalla prima all'ultima in ordine di apparizione, e scrive l'apparato conclusivo."""
import re, json, os
from collections import Counter, OrderedDict

REPO = '/home/user/collegi-italia'
SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'

# L'ordine dell'opera sta in parti.json, sorgente unica (vedi la nota nel file).
# Qui entra tutto tranne l'apparato bibliografico, che questo script produce.
_PARTI = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'parti.json'), encoding='utf-8'))['parti']
PARTS = [(p['etichetta'], p['breve'], p['file'])
         for p in _PARTI if not p.get('solo_volume')]


TLD = r'(?:gov|it|va|com|org|net|edu|uk|fr|de|eu|int|ch|nl|info)'
RE_MDLINK = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
RE_BAREURL = re.compile(r'https?://[^\s\)\]»«,;]+')
RE_DOMAIN = re.compile(r'(?<![\w/.@-])((?:[a-z0-9-]+\.)+' + TLD + r'(?:/[^\s\)\]»«,;:]*)?)(?![\w-])')

def clean_label(s):
    s = re.sub(r'[*`_]', '', s).strip()
    return s[:110]

def norm(addr):
    a = addr.rstrip('.,;:)»')
    a = re.sub(r'^https?://', '', a)
    a = re.sub(r'^www\.', '', a)
    a = a.rstrip('/')
    return a.lower()

def extract(text):
    """Ritorna occorrenze (pos, label, display_addr, is_link) in ordine di posizione."""
    occ = []
    covered = []
    for m in RE_MDLINK.finditer(text):
        occ.append((m.start(), clean_label(m.group(1)), m.group(2).rstrip('.,;)'), True))
        covered.append((m.start(), m.end()))
    for m in RE_BAREURL.finditer(text):
        if any(s <= m.start() < e for s, e in covered):
            continue
        occ.append((m.start(), '', m.group(0).rstrip('.,;)'), True))
        covered.append((m.start(), m.end()))
    for m in RE_DOMAIN.finditer(text):
        if any(s <= m.start() < e for s, e in covered):
            continue
        d = m.group(1).rstrip('.,;:)')
        if d.count('.') < 1 or len(d) < 6:
            continue
        occ.append((m.start(), '', d, False))
    occ.sort(key=lambda x: x[0])
    return occ

seen = OrderedDict()   # norm -> nota dict
tot_occ = 0
per_part_first = {i: [] for i in range(len(PARTS))}
per_part_occ = [0] * len(PARTS)

for idx, (label, title, path) in enumerate(PARTS):
    text = open(os.path.join(REPO, path), encoding='utf-8').read()
    for pos, lab, addr, is_link in extract(text):
        key = norm(addr)
        tot_occ += 1
        per_part_occ[idx] += 1
        if key in seen:
            seen[key]['occ'] += 1
            continue
        nota = {'label': lab, 'addr': addr, 'is_link': is_link, 'part': idx, 'occ': 1}
        seen[key] = nota
        per_part_first[idx].append(nota)

# numerazione dalla prima all'ultima
for n, nota in enumerate(seen.values(), start=1):
    nota['n'] = n

domains = Counter()
for nota in seen.values():
    d = norm(nota['addr']).split('/')[0]
    domains[d] += 1

out = []
out.append('# Le note bibliografiche')
out.append("## Dalla prima all'ultima: gli indirizzi citati nell'opera, in ordine di apparizione\n")
out.append(f"> **Statuto dell'apparato.** Questo apparato conclusivo raccoglie **tutte le note bibliografiche con indirizzo** dell'opera integrale — {len(seen)} indirizzi distinti per {tot_occ} citazioni complessive — numerate **dalla prima all'ultima nell'ordine di apparizione** lungo i {len(PARTS)} capitoli dell'opera, ciascuna registrata sotto il capitolo della sua prima citazione (le citazioni ripetute sono contate, non duplicate). Vi compaiono sia gli indirizzi in collegamento pieno sia quelli citati in forma d'indirizzo semplice, come l'opera li riporta «per la tracciabilità». L'apparato è generato meccanicamente dai testi e si rigenera con essi: non è una bibliografia selettiva ma il censimento integrale degli indirizzi dell'opera — la sua impronta documentale.\n")

for idx, (label, title, path) in enumerate(PARTS):
    notes = per_part_first[idx]
    out.append(f'### {label} — {title}')
    if not notes:
        if per_part_occ[idx]:
            out.append('*Gli indirizzi citati in questo capitolo compaiono tutti in capitoli precedenti: nessuna nota nuova.*\n')
        else:
            out.append("*Capitolo senza citazioni in forma d'indirizzo: le sue fonti sono richiamate per titolo e rango nei documenti del corpus (si vedano la bibliografia critica e l'apparato dei gradi).*\n")
        continue
    for nota in notes:
        lab = nota['label']
        if nota['is_link']:
            if lab:
                out.append(f"**{nota['n']}.** {lab} — [{nota['addr']}]({nota['addr']})" + (f" *(citato {nota['occ']} volte)*" if nota['occ'] > 1 else ''))
            else:
                short = norm(nota['addr'])
                if len(short) > 72:
                    short = short[:71] + '…'
                out.append(f"**{nota['n']}.** [{short}]({nota['addr']})" + (f" *(citato {nota['occ']} volte)*" if nota['occ'] > 1 else ''))
        else:
            out.append(f"**{nota['n']}.** `{nota['addr']}` *(citato in forma d'indirizzo{', ' + str(nota['occ']) + ' volte' if nota['occ'] > 1 else ''})*")
        out.append('')
    out.append('')

out.append('---\n')
out.append('### Il riepilogo')
top = domains.most_common(10)
out.append(f"L'opera cita {tot_occ} volte {len(seen)} indirizzi distinti su {len(domains)} domini. I domini più citati: " +
           ' · '.join(f'`{d}` ({c})' for d, c in top) + '.')
out.append('')
out.append("*L'apparato conta indirizzi, non gerarchie di verità: il grado di ogni affermazione resta dichiarato nel capitolo che la contiene. Un indirizzo citato è una porta aperta alla verifica — l'opera ne lascia " + str(len(seen)) + '.*')

open(os.path.join(REPO, 'note-bibliografiche-opera-integrale.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

stats = {
 'per_part_occ': per_part_occ,
 'per_part_new': [len(per_part_first[i]) for i in range(len(PARTS))],
 'labels': [p[0] for p in PARTS],
 'top_domains': top,
 'tot_occ': tot_occ, 'distinct': len(seen),
}
json.dump(stats, open(os.path.join(SP, 'note_stats.json'), 'w'), ensure_ascii=False)
print(f'note distinte: {len(seen)} | occorrenze: {tot_occ} | domini: {len(domains)}')
print('top domini:', ', '.join(f'{d}({c})' for d, c in top[:6]))
