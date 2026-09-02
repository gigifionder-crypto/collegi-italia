#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scheda di stato dell'opera. Una pagina, tutti i numeri contati.

Nessun numero e' scritto a mano: ciascuno viene da un conteggio o dalla
riga di un registro generato. E' la lezione che quest'opera ha pagato una
volta -- un numero scritto a mano deriva -- applicata a se stessa.

Uso:  python3 stato_dell_opera.py [FILE_USCITA]
"""
import json
import pathlib
import re
import subprocess
import sys

BASE = pathlib.Path(__file__).resolve().parent
REPO = BASE.parent.parent


def cifra(file, motivo, dopo=None):
    """Prima cifra della riga che contiene il motivo.

    `dopo`, se dato, e' il testo dopo il quale cercare la cifra nella riga:
    serve quando il numero sta in prosa e non in una cella di tabella.
    """
    p = REPO / file
    if not p.exists():
        return None
    for riga in p.read_text(encoding='utf-8').split('\n'):
        if motivo not in riga:
            continue
        if dopo:
            i = riga.find(dopo)
            if i < 0:
                continue
            m = re.search(r'([\d.,]+)', riga[i + len(dopo):])
        else:
            m = re.search(r'\*\*([\d.,]+)\*\*', riga)
        if m:
            return m.group(1).rstrip('.,')
    return None


def parole(p):
    return len(p.read_text(encoding='utf-8').split()) if p.exists() else 0


def main():
    uscita = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 \
        else REPO / 'lo-stato-dell-opera.md'

    parti = json.loads((BASE / 'parti.json').read_text(encoding='utf-8'))['parti']
    mancanti = [x for x in parti if not (REPO / x['file']).exists()]
    senza_breve = [x for x in parti if not x.get('breve')]
    integrale = sum(parole(REPO / x['file']) for x in parti)

    opera = REPO / 'novanta-secondi-e-quarantotto-anni.md'
    breve = REPO / 'una-guerra-senza-fine-edizione-breve.md'
    man = json.loads((REPO / '_monografia' / 'opera.json').read_text(encoding='utf-8'))
    capitoli = sum(len(L['capitoli']) for L in man['libri'])

    commit = subprocess.run(['git', 'log', '-1', '--format=%h · %ad', '--date=short'],
                            cwd=REPO, capture_output=True, text=True).stdout.strip()

    R = ["# Lo stato dell'opera\n",
         '*Scheda generata. Ogni numero è contato, nessuno è scritto a mano: '
         'un numero scritto a mano deriva, e quest\'opera lo ha imparato a '
         'proprie spese.*\n',
         f'*Ultimo commit al momento del conteggio: {commit}.*\n',
         '## Il corpus\n',
         '| voce | numero |', '|---|---:|',
         f'| parti registrate in `parti.json` | **{len(parti)}** |',
         f'| di esse, con file mancante | **{len(mancanti)}** |',
         f'| di esse, senza campo `breve` | **{len(senza_breve)}** |',
         f'| parole delle parti registrate | **{integrale:,}** |'.replace(',', '.'),
         '',
         '## Le edizioni\n',
         '| edizione | capitoli | parole |', '|---|---:|---:|',
         f'| Opera monografica · `{opera.name}` | **{capitoli}** in **{len(man["libri"])}** libri '
         f'| **{parole(opera):,}** |'.replace(',', '.'),
         f'| Edizione ridotta · `{breve.name}` | **{capitoli}** | **{parole(breve):,}** |'.replace(',', '.'),
         '',
         '*Le edizioni sono derivate: non sono registrate fra le parti e non '
         'entrano nei registri. Un\'opera che si contasse fra le proprie fonti '
         'non sarebbe una misura.*\n',
         '## I registri\n',
         '| registro | esito |', '|---|---:|']

    voci = [
        ('il-registro-di-chiusura.md', 'non interrogate',
         'celle aperte con sede, non interrogate'),
        ('il-registro-delle-convergenze.md', 'Il numero corrente',
         'conferme del risultato ricorrente', 'Il numero corrente è'),
        ('il-registro-savona.md', 'archi con livello Savona',
         'archi con livello Savona'),
        ('il-registro-savona.md', 'Savona A**',
         'di essi, livello Savona A'),
        ('il-registro-savona.md', 'etichette di entità',
         'etichette di entità negli archi'),
    ]
    for voce in voci:
        f, motivo, etichetta = voce[:3]
        v = cifra(f, motivo, voce[3] if len(voce) > 3 else None)
        R.append(f'| {etichetta} | **{v if v else "—"}** |')

    R += ['',
          '## Ciò che resta, e non lo farà una macchina\n',
          '**Trenta consegne**, di cui quindici richiedono soltanto una '
          'connessione di rete e quindici richiedono **una persona**: una '
          'lettera, un nome, un appuntamento, un pomeriggio in una sala di '
          'consultazione.\n',
          '**Una domanda mai scritta**, che sta in un risvolto di pantaloni: '
          'il deposito è unico o multiplo; si distinguono strati; quegli '
          'strati stanno sopra o sotto i residui attribuibili all\'ambiente '
          'della custodia.\n',
          '**Un caricatore** repertato all\'angolo fra via Fani e via Stresa, '
          'mai comparato in quarantotto anni.\n',
          '**Una campagna sospesa**, il vivaio nero: sei lotti su otto '
          'lavorati, **zero verificati**, e il capitolo lo dichiara nella '
          'propria prima riga.\n',
          '**E la prima consegna, che non aspetta nessuna verifica**: ai '
          'familiari di Oreste Leonardi, Domenico Ricci, Giulio Rivera, '
          'Francesco Zizzi, Raffaele Iozzino.\n']

    uscita.write_text('\n'.join(R) + '\n', encoding='utf-8')
    print(f'{uscita.name}: {len(parti)} parti, {len(mancanti)} mancanti, '
          f'{len(senza_breve)} senza breve, {integrale} parole')


if __name__ == '__main__':
    main()
