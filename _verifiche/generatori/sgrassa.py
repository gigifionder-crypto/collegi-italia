# -*- coding: utf-8 -*-
"""Toglie il grassetto dove è dominante, e solo lì.

Sedici ricognizioni Farnesina e il Libro quindicesimo arrivano dai DOCX con
OGNI paragrafo interamente in grassetto: 198.503 parole, il diciassette per
cento del volume. Un grassetto che sta ovunque non distingue nulla — è rumore
tipografico ereditato dalla conversione, non una scelta d'autore — e nessun
libro si stampa così.

Dove invece il grassetto è occasionale porta un'informazione, e non si tocca.
La soglia è dichiarata e vale per file, non per riga: si interviene solo se più
della metà dei paragrafi è interamente in grassetto.

Nessuna parola viene aggiunta, tolta o riordinata: cadono soltanto i marcatori,
e la funzione `verifica` lo dimostra confrontando i due testi privati di ogni
asterisco."""
import glob, os, re, sys

SOGLIA = 0.5
# un paragrafo interamente in grassetto: comincia per ** e finisce per **,
# e non contiene altre coppie che spezzerebbero la resa
TUTTO = re.compile(r'^\*\*(?!\s)(.+?)\*\*\s*$')

def _paragrafo(r):
    return bool(r.strip()) and not r.startswith(('#', '|', '>', '-', '*   ', '    '))

def quota(testo):
    righe = [r for r in testo.split('\n') if _paragrafo(r)]
    if not righe:
        return 0.0
    return sum(1 for r in righe if TUTTO.match(r)) / len(righe)

def sgrassa(testo):
    fuori = []
    for r in testo.split('\n'):
        m = TUTTO.match(r) if _paragrafo(r) else None
        if m and '**' not in m.group(1):
            fuori.append(m.group(1).rstrip())
        else:
            fuori.append(r)
    return '\n'.join(fuori)

def verifica(prima, dopo):
    """Le due versioni devono coincidere una volta tolti tutti gli asterischi:
    se non coincidono, l'intervento ha toccato il testo e non solo la resa."""
    n = lambda s: re.sub(r'\s+', ' ', s.replace('*', '')).strip()
    return n(prima) == n(dopo)

if __name__ == '__main__':
    scritti = 0
    for p in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else '**/*.md', recursive=True)):
        if '/italia-nera/' in p or p.startswith('italia-nera/'):
            continue
        t = open(p, encoding='utf-8').read()
        q = quota(t)
        if q <= SOGLIA:
            continue
        d = sgrassa(t)
        if not verifica(t, d):
            print(f'  SALTATO (il testo cambierebbe): {p}')
            continue
        open(p, 'w', encoding='utf-8').write(d)
        scritti += 1
        print(f'  {100*q:>3.0f}% -> {100*quota(d):>3.0f}%  {len(t.split()):>7} par  {p}')
    print(f'file sgrassati: {scritti}')
