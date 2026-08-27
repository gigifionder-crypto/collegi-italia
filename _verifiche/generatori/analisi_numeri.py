# -*- coding: utf-8 -*-
"""Analisi strutturale dei numeri di tessera e fascicolo asseriti dal testo.
Nessuna fonte esterna: si controlla il testo contro se stesso e contro
l'aritmetica. Cio' che si trova qui non dipende da alcun archivio."""
from collections import Counter

# (nome, tessera asserita, fascicolo asserito)  None = il testo non lo da'
D = [
 ('Sergio Di Donato',        158, 158),
 ('Giuseppe Santovito',     1630, 527),   # il testo corregge 163 -> 1630
 ('Vincenzo Rizzuti',        811, 811),
 ('Raffaele Giudice',       1592, 504),
 ('Donato Lo Prete',        1600, 512),
 ('Camillo Guglielmi',      1602, 514),
 ('Vito Miceli',            1605, 491),
 ('Walter Pelosi',          1607, 519),
 ('Giuseppe Siracusano',    1608, 520),
 ('Umberto Ortolani',       1609, 494),
 ('Michele Sindona',        1612, 501),
 ('Pietro Musumeci',        1614, None),
 ('Giovanni Torrisi',       1619, 531),
 ('Stefano Giovannone',     1620, 532),
 ('Antonino Geraci',        1621, None),
 ('Roberto Calvi',          1624, 530),   # 519 in un altro punto del testo
 ('Elio Cioppa',            1628, None),
 ('Giulio Grassini',        1629, 515),
 ('Mario Salacone',          163, None),  # il testo corregge 1630 -> 163
 ('Antonio Cornacchia',     1631, 871),
 ('Carmelo Spagnuolo',      1632, 543),
 ('Antonio Varisco',        1633, 537),
 ('Achille Gallucci',       1634, 546),
 ('Antonio Viezzer',        1635, 539),
 ('Francesco Malfatti',     1636, 540),
 ('Mario Semprini',         1637, 544),
 ('Antonio Esposito',       1638, None),
 ('Franco Ferracuti',       1639, None),
 ("Federico U. D'Amato",    1643, None),
 ('Mino Pecorelli',         1750, None),
 ('Gustavo Selva',          1814, None),  # il testo corregge 1803 -> 1814
 ('Maurizio Costanzo',      1819, 626),
 ('Franco Di Bella',        1887, None),
]

coppie = [(n, t, f) for n, t, f in D if f is not None]
print(f'righe: {len(D)} · con entrambi i numeri: {len(coppie)}')
print()

# ---------------------------------------------------------------- lo scarto
print('LO SCARTO FRA TESSERA E FASCICOLO')
print('-' * 62)
scarti = Counter()
for n, t, f in sorted(coppie, key=lambda r: r[1]):
    s = t - f
    scarti[s] += 1
    print(f'  {n:<24} {t:>5} − {f:>4} = {s:>5}')
print()
print('distribuzione degli scarti:')
for s, c in scarti.most_common():
    barra = '█' * c
    print(f'  scarto {s:>5} : {c:>2} volte  {barra}')

print()
print('=' * 62)
print("LA RETTA CHE OTTO COPPIE DEFINISCONO")
print('=' * 62)
print("""
Otto coppie stanno esattamente su fascicolo = tessera − 1088. Se due
numerazioni progressive corrono in parallelo su un blocco contiguo, ogni
altra coppia dentro quel blocco deve stare sulla stessa retta: se il 1602
e' il 514 e il 1607 e' il 519, allora il 1605 non puo' che essere il 517.
Ecco che cosa la retta predice, e che cosa il testo dichiara.
""")
BLOCCO = [(n, t, f) for n, t, f in coppie if 1592 <= t <= 1637]
print(f'  {"nome":<24} {"tessera":>7} {"predetto":>9} {"dichiarato":>11} {"scarto":>8}')
print('  ' + '-' * 62)
sulla, fuori = [], []
for n, t, f in sorted(BLOCCO, key=lambda r: r[1]):
    pred = t - 1088
    d = f - pred
    (sulla if d == 0 else fuori).append((n, t, f, pred, d))
    segno = '' if d == 0 else ('+%d' % d if d > 0 else str(d))
    print(f'  {n:<24} {t:>7} {pred:>9} {f:>11} {segno:>8}')
print()
print(f'  sulla retta : {len(sulla)} su {len(BLOCCO)}')
print(f'  fuori retta : {len(fuori)} su {len(BLOCCO)}')

print()
print('=' * 62)
print('QUANTO E IMPROBABILE')
print('=' * 62)
# I fascicoli dichiarati stanno fra 491 e 871: un intervallo di 381 valori.
# Se i due numeri fossero registri indipendenti, lo scarto sarebbe sparso.
import itertools, math
lo, hi = min(f for _, _, f in coppie), max(f for _, _, f in coppie)
amp = hi - lo + 1
n = len(coppie)
p_singolo = 1.0 / amp
# Probabilita' che almeno 8 delle 23 coppie condividano lo stesso scarto,
# stimata con la coda binomiale sul valore piu' probabile: e' una stima
# generosa verso l'ipotesi del caso, e resta comunque schiacciante.
def coda(k, n, p):
    return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(k, n+1))
p = coda(8, n, p_singolo) * amp   # correzione per il numero di scarti possibili
print(f'  ampiezza dei fascicoli dichiarati : {lo}–{hi}  ({amp} valori)')
print(f'  coppie                            : {n}')
print(f'  coppie con scarto identico        : 8')
print(f'  probabilita\' se fossero indipendenti : {p:.3e}')
print()
print('  Uno scarto costante fra due numerazioni significa che una e stata')
print('  ricavata dall\'altra per sottrazione, non registrata a parte.')

print()
print('=' * 62)
print('COLLISIONI E VALORI IMPOSSIBILI')
print('=' * 62)

# Collisioni fra i fascicoli dichiarati nella tabella
c = Counter(f for _, _, f in coppie)
dupl = [(f, [n for n, _, ff in coppie if ff == f]) for f, k in c.items() if k > 1]
print('\n  fascicoli assegnati due volte dentro la tabella:')
print('    nessuno' if not dupl else '')
for f, nomi in dupl:
    print(f'    {f}: ' + ' · '.join(nomi))

# Il testo assegna altrove numeri agli stessi nomi: sono i doppioni gia' noti
ALTROVE = [
 ('Roberto Calvi',   'fascicolo', 530, 519, 'scheda di apertura / riga della tabella'),
 ('Walter Pelosi',   'fascicolo', 519, 519, 'lo stesso 519 e anche di Calvi'),
 ('Licio Gelli',     'numero',   1612, 1711, 'tabella dei protagonisti / sezione sulla Commissione'),
 ('Michele Sindona', 'numero',   1612,  501, 'tessera 1612 — la stessa cifra data a Gelli'),
 ('Giuseppe Santovito','numero',  527,  527, '527 dato sia come fascicolo sia come tessera'),
]
print('\n  numeri che il testo assegna due volte, in punti diversi:')
for n, tipo, a, b, dove in ALTROVE:
    print(f'    {n:<20} {tipo} {a} / {b}   ({dove})')

SOGLIA = 1600
sotto = [(n, t) for n, t, _ in D if t < SOGLIA]
print(f'\n  tessere dichiarate sotto la soglia documentata del {SOGLIA}:')
for n, t in sorted(sotto, key=lambda r: r[1]):
    print(f'    {n:<24} {t}')
print(f'    → {len(sotto)} su {len(D)}')

fuori_962 = [(n, f) for n, _, f in coppie if f > 962]
print(f'\n  fascicoli oltre i 962 nominativi dell elenco: {len(fuori_962) or "nessuno"}')
for n, f in fuori_962:
    print(f'    {n:<24} {f}')
