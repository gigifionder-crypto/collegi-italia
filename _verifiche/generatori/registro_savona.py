#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estrae dal corpus tutti gli archi che portano un livello della Scala Savona.

Il livello Savona si attribuisce a un ARCO -- una connessione documentata fra
due entita' -- e mai a una persona. Questo generatore percio' produce due
elenchi distinti e non li confonde: gli archi con il loro livello, e l'indice
delle entita' che vi compaiono, senza livello, perche' un'entita' non ha un
livello Savona e attribuirglielo sarebbe un errore di categoria.

Le edizioni derivate sono escluse: ripetono archi gia' contati.

Uso:  python3 registro_savona.py [FILE_USCITA]
"""
import collections
import glob
import os
import re
import sys
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
REPO = BASE.parent.parent

RE_ARCO = re.compile(r'^#{1,6}\s*(.+?)\[Savona ([ABC])\]', re.M)

# Escluse per costruzione, con la ragione accanto a ciascuna.
ESCLUSI = [
    ('_monografia/', 'sorgenti di questa edizione'),
    ('novanta-secondi-e-quarantotto-anni.md', 'Opera assemblata: ripete archi contati'),
    ('una-guerra-senza-fine-edizione', 'edizione breve assemblata'),
    ('il-registro-savona.md', 'questo registro: si conterebbe da sé'),
]

# Titoli di connettivo che non sono entita'.
NON_ENTITA = re.compile(
    r'^(?:pattern|filiazione|isomorfismo|riemergenza|convergenza|eredit|arco|'
    r'globale|globali|moderna|inverso|hub|mercati globali)', re.I)


def escluso(rel):
    return any(p in rel for p, _ in ESCLUSI)


def pulisci(t):
    t = re.sub(r'[\\*◈›#]+', ' ', t)
    return re.sub(r'\s+', ' ', t).strip(' —-–·')


def entita(titolo):
    """Estrae le entita' nominate in un titolo d'arco."""
    corpo = re.sub(r'^Arco\s*#?\s*\d+\s*[—–-]\s*', '', titolo)
    corpo = re.sub(r'\([^)]*\)', '', corpo)          # via la qualifica finale
    fuori = []
    # Si spezza SOLO sulle frecce e sulle virgole. Mai sul trattino: dentro
    # un'etichetta il trattino tiene insieme nomi propri ('Stay-Behind',
    # 'Bankman-Fried', 'Stato-Mafia'), e spezzarlo fabbrica nomi che nessuna
    # fonte ha scritto. Le etichette composte restano come il corpus le
    # scrisse, e la ragione e' dichiarata nel registro.
    for e in re.split(r'\s*(?:→|->|>)\s*|\s*,\s*', corpo):
        e = e.strip(' .·—–-')
        if len(e) > 2 and not NON_ENTITA.match(e):
            fuori.append(e)
    return fuori


def main():
    uscita = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 \
        else REPO / 'il-registro-savona.md'

    archi = {}
    for f in glob.glob(str(REPO / '**' / '*.md'), recursive=True):
        rel = os.path.relpath(f, REPO)
        if escluso(rel):
            continue
        for m in RE_ARCO.finditer(open(f, encoding='utf-8', errors='ignore').read()):
            t = pulisci(m.group(1))
            if not t:
                continue
            v = archi.setdefault(t, {'liv': set(), 'file': set()})
            v['liv'].add(m.group(2))
            v['file'].add(rel)

    def chiave(t):
        m = re.search(r'Arco\s*#?\s*(\d+)', t)
        return (0, int(m.group(1))) if m else (1, 0)

    ordinati = sorted(archi.items(), key=lambda kv: chiave(kv[0]))
    conta = collections.Counter(
        l for v in archi.values() for l in v['liv'])

    ind = collections.defaultdict(lambda: {'liv': set(), 'n': 0})
    for t, v in archi.items():
        for e in entita(t):
            ind[e]['liv'] |= v['liv']
            ind[e]['n'] += 1

    R = []
    R.append('# Il registro Savona\n')
    R.append('*Documento generato. Non scritto a mano, e ricontato a ogni '
             'assemblaggio: un elenco che si aggiorna da sé non deriva.*\n')
    R.append('**Il livello Savona si attribuisce a un arco — una connessione '
             'documentata fra due entità — e mai a una persona.** Le due '
             'liste che seguono sono perciò distinte, e la seconda non porta '
             'livelli: attribuire un livello a un\'entità sarebbe un errore '
             'di categoria, e questo registro non lo commette.\n')
    R.append(f'| voce | numero |\n|---|---:|')
    R.append(f'| archi con livello Savona | **{len(archi)}** |')
    for l in 'ABC':
        if conta[l]:
            R.append(f'| di essi, livello **Savona {l}** | **{conta[l]}** |')
    R.append(f'| etichette di entità nominate negli archi | **{len(ind)}** |\n')

    R.append('## Gli archi, con il loro livello\n')
    R.append('| # | arco | livello |\n|---:|---|:-:|')
    for i, (t, v) in enumerate(ordinati, 1):
        R.append(f'| {i} | {t} | **{"/".join(sorted(v["liv"]))}** |')

    R.append('\n## Le entità nominate negli archi\n')
    R.append('*Senza livello, per la ragione detta sopra. Il numero è quello '
             'degli archi in cui l\'etichetta compare: **misura la ricorrenza, '
             'non la responsabilità**.*\n')
    R.append('*Le etichette sono riprodotte come il corpus le scrisse, '
             'composte incluse. Non si spezzano sul trattino: dentro '
             'un\'etichetta il trattino tiene insieme nomi propri, e '
             'spezzarlo fabbricherebbe nomi che nessuna fonte ha scritto.*\n')
    R.append('| etichetta | archi |\n|---|---:|')
    for e, v in sorted(ind.items(), key=lambda kv: (-kv[1]['n'], kv[0])):
        R.append(f'| {e} | {v["n"]} |')

    R.append('\n## Le esclusioni, con la ragione accanto\n')
    for p, ragione in ESCLUSI:
        R.append(f'- `{p}` — {ragione}')

    uscita.write_text('\n'.join(R) + '\n', encoding='utf-8')
    print(f'{uscita.name}: {len(archi)} archi '
          f'({dict(conta)}), {len(ind)} etichette')


if __name__ == '__main__':
    main()
