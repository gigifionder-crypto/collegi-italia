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
 ('Libro nono · II', "Appendice quinta alla Fase settima", 'appendici-fase-settima/appendice-quinta-fase-settima.md'),
 ('Libro nono · III', "Appendice sesta alla Fase settima", 'appendici-fase-settima/appendice-sesta-fase-settima.md'),
 ('Libro nono · IV', "Appendice settima alla Fase settima", 'appendici-fase-settima/appendice-settima-fase-settima.md'),
 ('Libro nono · V', "Appendice ottava alla Fase settima", 'appendici-fase-settima/appendice-ottava-fase-settima.md'),
 ('Libro nono · VI', "Appendice nona alla Fase settima", 'appendici-fase-settima/appendice-nona-fase-settima.md'),
 ('Libro nono · VII', "Appendice decima alla Fase settima", 'appendici-fase-settima/appendice-decima-fase-settima.md'),
 ('Libro nono · VIII', "Appendice undicesima alla Fase settima", 'appendici-fase-settima/appendice-undicesima-fase-settima.md'),
 ('Libro nono · IX', "Appendice dodicesima alla Fase settima", 'appendici-fase-settima/appendice-dodicesima-fase-settima.md'),
 ('Libro nono · X', "Appendice tredicesima alla Fase settima", 'appendici-fase-settima/appendice-tredicesima-fase-settima.md'),
 ('Libro nono · XI', "Appendice quattordicesima alla Fase settima", 'appendici-fase-settima/appendice-quattordicesima-fase-settima.md'),
 ('Libro nono · XII', "Appendice quindicesima alla Fase settima", 'appendici-fase-settima/appendice-quindicesima-fase-settima.md'),
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
 ('Libro dodicesimo · IV', "Aldo Moro Alla Farnesina E L'Opus Dei", 'moro-ministro-esteri/terza-campagna/terza-ricognizione-spagna-opus-dei.md'),
 ('Libro dodicesimo · V', "Aldo Moro Alla Farnesina E Il Portogallo", 'moro-ministro-esteri/terza-campagna/quarta-ricognizione-portogallo-santa-sede.md'),
 ('Libro dodicesimo · VI', "Aldo Moro Alla Farnesina, Il Portogallo E La Santa Sede", 'moro-ministro-esteri/terza-campagna/quinta-ricognizione-portogallo-le-sei-lacune.md'),
 ('Libro dodicesimo · VII', "Aldo Moro Alla Farnesina, Il Portogallo E L'Opus Dei", 'moro-ministro-esteri/terza-campagna/sesta-ricognizione-il-ribaltamento-iberico.md'),
 ('Libro dodicesimo · VIII', "Aldo Moro Alla Farnesina, La Turchia E La Santa Sede", 'moro-ministro-esteri/terza-campagna/settima-ricognizione-turchia-e-attentato.md'),
 ('Libro dodicesimo · IX', "Moro, Il Mediterraneo Orientale E L'Opus Dei", 'moro-ministro-esteri/terza-campagna/ottava-ricognizione-mediterraneo-orientale.md'),
 ('Libro dodicesimo · X', "Moro, Le Due Germanie E La Santa Sede", 'moro-ministro-esteri/terza-campagna/nona-ricognizione-la-sequenza-oder-neisse.md'),
 ('Libro dodicesimo · XI', "Moro, La Germania E L'Opus Dei", 'moro-ministro-esteri/terza-campagna/decima-ricognizione-revisione-del-modello.md'),
 ('Libro dodicesimo · XII', "Strauss E Aginter Press", 'moro-ministro-esteri/terza-campagna/undicesima-ricognizione-strauss-e-aginter.md'),
 ('Libro dodicesimo · XIII', "I Sette Casi Extraeuropei", 'moro-ministro-esteri/terza-campagna/dodicesima-ricognizione-sette-casi-extraeuropei.md'),
 ('Libro dodicesimo · XIV', "Aginter Press E Lo Stato Italiano", 'moro-ministro-esteri/terza-campagna/tredicesima-ricognizione-aginter-i-due-silenzi.md'),
 ('Libro dodicesimo · XV', "Il Silenzio Dello Stato: Azione O Archivio", 'moro-ministro-esteri/terza-campagna/quattordicesima-ricognizione-la-calibrazione-libica.md'),
 ('Libro dodicesimo · XVI', "L'Italia, L'Aermacchi E Il Sudafrica Dell'Apartheid", 'moro-ministro-esteri/terza-campagna/quindicesima-ricognizione-aermacchi-e-il-sudafrica.md'),
 ('Libro dodicesimo · XVII', "Italia E Germania Sul Dossier Namibiano", 'moro-ministro-esteri/terza-campagna/sedicesima-ricognizione-il-dossier-namibiano.md'),
 ('Libro dodicesimo · XVIII', "La Santa Sede, La Dc E Il Sudafrica Dell'Apartheid", 'moro-ministro-esteri/terza-campagna/diciassettesima-ricognizione-santa-sede-e-sudafrica.md'),
 ('Libro dodicesimo · XIX', "L'Italia Alle Nazioni Unite: Embargo, Apartheid, Namibia", 'moro-ministro-esteri/terza-campagna/diciottesima-ricognizione-nazioni-unite-ed-embargo.md'),
 ('Libro dodicesimo · XX', "Registro Analitico Dei Nodi E Dei Ponti", 'moro-ministro-esteri/terza-campagna/registro-dei-nodi-e-dei-ponti-teatro-australe.md'),
 ('Libro dodicesimo · XXI', "Secondo Registro Analitico Dei Nodi E Dei Ponti", 'moro-ministro-esteri/terza-campagna/secondo-registro-dei-nodi-e-dei-ponti.md'),
 ('Libro dodicesimo · XXII', "Terzo Registro Analitico Dei Nodi E Dei Ponti", 'moro-ministro-esteri/terza-campagna/terzo-registro-dei-nodi-e-dei-ponti.md'),
 ('Libro dodicesimo · XXIII', "Quarto Registro Analitico", 'moro-ministro-esteri/terza-campagna/quarto-registro-la-scala-degli-stati-zero.md'),
 ('Libro dodicesimo · XXIV', "Quinto Registro Analitico", 'moro-ministro-esteri/terza-campagna/quinto-registro-la-tavola-unica.md'),
 ('Libro dodicesimo · XXV', "Sesto Registro Analitico", 'moro-ministro-esteri/terza-campagna/sesto-registro-strumenti-e-volume.md'),
 ('Libro dodicesimo · XXVI', "Settimo Registro Analitico", 'moro-ministro-esteri/terza-campagna/settimo-registro-la-riqualificazione.md'),
 ('Libro dodicesimo · XXVII', "Registro Delle Undici Ricognizioni", 'moro-ministro-esteri/terza-campagna/registro-delle-undici-ricognizioni.md'),
 ('Libro dodicesimo · XXVIII', "La triangolazione della terza campagna", 'moro-ministro-esteri/triangolazione-terza-campagna.md'),
 ('Libro tredicesimo · I', 'Il programma e le graduatorie', 'programma-investigativo-caso-moro.md'),
 ('Libro tredicesimo · II', 'Le schede delle piste di testa', 'approfondimento-piste-di-testa.md'),
 ('Libro tredicesimo · III', 'Le schede delle entità', 'approfondimento-piste-entita.md'),
 ('Libro tredicesimo · IV', 'Il manuale (400 blocchi)', 'manuale-investigativo-nuovo-caso-moro.md'),
 ('Libro tredicesimo · V', "L'agenda di ricerca (300 blocchi)", 'agenda-di-ricerca-del-nuovo-caso-moro.md'),
 ('Libro tredicesimo · VI', 'I nove cantieri (1.000 blocchi)', 'nove-cantieri-mille-blocchi.md'),
 ('Libro tredicesimo · VII', 'Il codice e la sua trasmissione (4.999 blocchi)', 'kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md'),
 ('Libro quattordicesimo', "Il meridiano e la valle (1.000 blocchi)", 'il-meridiano-e-la-valle-mille-blocchi.md'),
 ('Libro quindicesimo', "Il Registro dei cinquantacinque giorni", 'il-registro-dei-cinquantacinque-giorni-opera-seconda.md'),
 ('Libro sedicesimo · I', 'Il fascicolo della custodia', 'il-fascicolo-della-custodia.md'),
 ('Libro sedicesimo · II', 'La matrice della custodia', 'la-matrice-della-custodia.md'),
 ('Libro sedicesimo · III', 'Il quesito della sabbia', 'il-quesito-della-sabbia.md'),
 ('Libro sedicesimo · IV', 'La matrice di via Fani', 'la-matrice-di-via-fani.md'),
 ('Libro sedicesimo · V', 'La matrice delle omissioni', 'la-matrice-delle-omissioni.md'),
 ('Appendice I', "L'apparato dei gradi", 'aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md'),
 ('Appendice II', 'Il pastiche dichiarato', 'relazione-stato-lavori-stile-moro.md'),
 ('Appendice III', 'Verifica di un elenco esterno', '_verifiche/verifica-elenco-trentatre-nomi-p2.md'),
 ('Appendice IV.i', "L'apparato di navigazione — La guida alla lettura", 'GUIDA-ALLA-LETTURA.md'),
 ('Appendice IV.ii', "L'apparato di navigazione — L'indice dei documenti", 'INDICE-DOCUMENTI-BRANCH.md'),
 ('Appendice IV.iii', "Il dossier di invio — La mappa", '_diffusione-opera/README.md'),
 ('Appendice IV.iv', "Il dossier di invio — La scheda dell'opera", '_diffusione-opera/scheda-dell-opera.md'),
 ('Appendice IV.v', "Il dossier di invio — Il capitolo campione", '_diffusione-opera/capitolo-campione.md'),
 ('Appendice IV.vi', "Il dossier di invio — La mappa dei destinatari", '_diffusione-opera/mappa-dei-destinatari.md'),
 ('Appendice IV.vii', "Il dossier di invio — Il registro dei canali e delle PEC", '_diffusione-opera/registro-pec-e-canali.md'),
 ('Appendice IV.viii', "Il dossier di invio — La checklist di invio", '_diffusione-opera/checklist-di-invio.md'),
 ('Appendice IV.ix', "Il dossier di invio — Il curriculum, modello da compilare", '_diffusione-opera/curriculum-modello.md'),
 ('Appendice IV.x', "Il dossier di invio — Lettera alla Fondazione Aldo Moro", '_diffusione-opera/lettera-fondazione-aldo-moro.md'),
 ('Appendice IV.xi', "Il dossier di invio — PEC all'Archivio Flamigni", '_diffusione-opera/pec-archivio-flamigni.md'),
 ('Appendice IV.xii', "Il dossier di invio — Relazione al Centro Flamigni", '_diffusione-opera/relazione-al-centro-flamigni.md'),
 ('Appendice IV.xiii', "Il dossier di invio — Proposta all'editrice Laterza", '_diffusione-opera/proposta-editrice-laterza.md'),
 ('Appendice IV.xiv', "Il dossier di invio — Proposte a il Mulino, Carocci, Einaudi", '_diffusione-opera/proposte-mulino-carocci-einaudi.md'),
 ('Appendice IV.xv', "Il dossier di invio — Proposte a Chiarelettere e Bompiani", '_diffusione-opera/proposte-chiarelettere-bompiani.md'),
 ('Appendice IV.xvi', "Il dossier di invio — Il deposito Zenodo, foglio operativo", '_diffusione-opera/deposito-zenodo.md'),
 ('Appendice IV.xvii', "Il dossier di invio — La richiesta all'Archivio storico della Camera", '_diffusione-opera/richiesta-archivio-storico-camera.md'),
 ('Appendice IV.xviii', "Il dossier di invio — La PEC unica formale", '_diffusione-opera/pec-unica-formale.md'),
 ('Appendice IV.xix', "Il dossier di invio — La PEC di presentazione per le case editrici", '_diffusione-opera/pec-presentazione-case-editrici.md'),
 ('Appendice V.i', "L'apparato della verifica — La certificazione dei numeri P2", '_verifiche/certificazione-numeri-p2.md'),
 ('Appendice V.ii', "L'apparato della verifica — La relazione della campagna", '_verifiche/campagna-ricerca-numeri-p2-relazione.md'),
 ('Appendice V.iii', "L'apparato della verifica — Il registro degli ingressi", '_verifiche/registro-degli-ingressi.md'),
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
