# -*- coding: utf-8 -*-
"""Estrae tutte le note bibliografiche con indirizzo dai 35 capitoli dell'Opera integrale,
numerate dalla prima all'ultima in ordine di apparizione, e scrive l'apparato conclusivo."""
import re, json, os
from collections import Counter, OrderedDict

REPO = '/home/user/collegi-italia'
SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'

PARTS = [
 ('Portale', "L'edizione strutturata", 'aldo-moro-una-guerra-senza-fine-edizione-strutturata.md'),
 ('Libro primo', 'Il ritratto', 'aldo-moro-una-guerra-senza-fine-fase-ottava-il-ritratto.md'),
 ('Libro secondo', 'Dal Che a Moro', 'dal-che-a-moro-una-guerra-senza-fine.md'),
 ('Libro terzo · I', 'Origini ed esilio', 'guevara-origini-esilio-messicano.md'),
 ('Libro terzo · II', "Dal Messico all'Avana", 'guevara-messico-avana-1954-1965.md'),
 ('Libro terzo · III', 'Da Mosca alla Bolivia', 'guevara-mosca-bolivia-1964-1966.md'),
 ('Libro terzo · IV', 'La campagna boliviana', 'guevara-campagna-boliviana-1966-1967.md'),
 ('Libro terzo · V', 'Bibliografia critica', 'guevara-bibliografia-critica.md'),
 ('Libro terzo · VI', 'Le triangolazioni Guevara-Moro', 'triangolazioni-guevara-moro.md'),
 ('Libro quarto', 'Il Dossier maggiore', 'dossier-maggiore-una-pace-senza-pace.md'),
 ('Libro quinto · I', 'Feltrinelli, il vettore', 'feltrinelli-il-vettore.md'),
 ('Libro quinto · II', 'La triangolazione di Feltrinelli', 'triangolazione-feltrinelli-corpus.md'),
 ('Libro quinto · III', 'Il nodo Hyperion', 'triangolazione-hyperion-corpus.md'),
 ('Libro quinto · IV', "L'incrocio Feltrinelli-Hyperion", 'triangolazione-feltrinelli-hyperion.md'),
 ('Libro quinto · V', 'Il ceppo Simioni', 'ceppo-simioni-cpm-superclan-hyperion.md'),
 ('Libro sesto · I', 'Il Tribunale Speciale', 'tribunale-speciale-storia-istituzione.md'),
 ('Libro sesto · II', 'Gli otto sottonodi', 'tribunale-speciale-approfondimento-sottonodi.md'),
 ('Libro sesto · III', 'Gli amnistiati', 'amnistiati-tribunale-speciale.md'),
 ('Libro settimo', 'Le questioni aperte', 'aldo-moro-una-guerra-senza-fine-parte-terza.md'),
 ('Libro ottavo · I', 'Il presidio del garante', 'aldo-moro-una-guerra-senza-fine-fase-sesta.md'),
 ('Libro ottavo · II', 'Le metodologie calcolate', 'metodologie-del-dossier-sinaptogenesi-e-strumenti.md'),
 ('Libro nono', 'Il registro giudiziario', 'aldo-moro-una-guerra-senza-fine-fase-settima-registro-giudiziario.md'),
 ('Libro decimo', 'Il repertorio del caso', 'aldo-moro-una-guerra-senza-fine-fase-nona-repertorio-del-caso.md'),
 ('Libro undicesimo · I', 'Il principio personalistico', 'aldo-moro-una-guerra-senza-fine-fase-decima-responsabilita-personali.md'),
 ('Libro undicesimo · II', 'La prosopografia dei tredici', 'triangolazione-condannati-corpus.md'),
 ('Libro dodicesimo · I', 'Moro alla Farnesina', 'moro-ministro-esteri/README.md'),
 ('Libro dodicesimo · II', "La ricognizione-madre: Moro ministro degli Esteri 1969-1974", 'moro-ministro-esteri/originali/ricognizione-ministro-esteri-1969-1974.md'),
 ('Libro dodicesimo · III', "Germania e Opus Dei 1952-1985", 'moro-ministro-esteri/originali/germania-opus-dei-1952-1985.md'),
 ('Libro dodicesimo · IV', "La Santa Sede e le due Germanie: la sequenza Oder-Neisse", 'moro-ministro-esteri/originali/santa-sede-due-germanie-oder-neisse.md'),
 ('Libro dodicesimo · V', "Portogallo e Opus Dei", 'moro-ministro-esteri/originali/portogallo-opus-dei.md'),
 ('Libro dodicesimo · VI', "Portogallo e Santa Sede 1969-1974", 'moro-ministro-esteri/originali/portogallo-santa-sede-1969-1974.md'),
 ('Libro dodicesimo · VII', "Grecia e Opus Dei 1969-1985", 'moro-ministro-esteri/originali/grecia-opus-dei-1969-1985.md'),
 ('Libro dodicesimo · VIII', "Turchia e Opus Dei 1969-1975", 'moro-ministro-esteri/originali/turchia-opus-dei-1969-1975.md'),
 ('Libro dodicesimo · IX', "La Santa Sede, la Turchia e l’attentato del 1981", 'moro-ministro-esteri/originali/santa-sede-turchia-attentato-giovanni-paolo-ii.md'),
 ('Libro dodicesimo · X', "Documenti italiani e spagnoli, e l’Opus Dei", 'moro-ministro-esteri/originali/documenti-italiani-spagnoli-opus-dei.md'),
 ('Libro dodicesimo · XI', "La triangolazione della seconda campagna", 'moro-ministro-esteri/triangolazione-seconda-campagna.md'),
 ('Libro dodicesimo · II', 'I documenti del Dipartimento di Stato', 'moro-ministro-esteri/documenti-state-dept-1965-1978.md'),
 ('Libro dodicesimo · III', 'Le pene oltre confine', 'le-pene-oltre-confine-mitterrand-mulinaris.md'),
 ('Libro tredicesimo · I', 'Il programma e le graduatorie', 'programma-investigativo-caso-moro.md'),
 ('Libro tredicesimo · II', 'Le schede delle piste di testa', 'approfondimento-piste-di-testa.md'),
 ('Libro tredicesimo · III', 'Le schede delle entità', 'approfondimento-piste-entita.md'),
 ('Libro tredicesimo · IV', 'Il manuale (400 blocchi)', 'manuale-investigativo-nuovo-caso-moro.md'),
 ('Libro tredicesimo · V', "L'agenda di ricerca (300 blocchi)", 'agenda-di-ricerca-del-nuovo-caso-moro.md'),
 ('Libro tredicesimo · VI', 'I nove cantieri (1.000 blocchi)', 'nove-cantieri-mille-blocchi.md'),
 ('Libro tredicesimo · VII', 'Il codice e la sua trasmissione (4.999 blocchi)', 'kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md'),
 ('Libro quattordicesimo', "Il meridiano e la valle (1.000 blocchi)", 'il-meridiano-e-la-valle-mille-blocchi.md'),
 ('Appendice I', "L'apparato dei gradi", 'aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md'),
 ('Appendice II', 'Il pastiche dichiarato', 'relazione-stato-lavori-stile-moro.md'),
 ('Appendice III', 'Verifica di un elenco esterno', '_verifiche/verifica-elenco-trentatre-nomi-p2.md'),
]

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
out.append(f"> **Statuto dell'apparato.** Questo apparato conclusivo raccoglie **tutte le note bibliografiche con indirizzo** dell'opera integrale — {len(seen)} indirizzi distinti per {tot_occ} citazioni complessive — numerate **dalla prima all'ultima nell'ordine di apparizione** lungo i trentacinque capitoli, ciascuna registrata sotto il capitolo della sua prima citazione (le citazioni ripetute sono contate, non duplicate). Vi compaiono sia gli indirizzi in collegamento pieno sia quelli citati in forma d'indirizzo semplice, come l'opera li riporta «per la tracciabilità». L'apparato è generato meccanicamente dai testi e si rigenera con essi: non è una bibliografia selettiva ma il censimento integrale degli indirizzi dell'opera — la sua impronta documentale.\n")

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
