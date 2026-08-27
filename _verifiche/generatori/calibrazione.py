# -*- coding: utf-8 -*-
"""Il controllo di calibrazione: due coppie attestate contro le coppie del testo.
Se un archivio reale accoppia tessera e fascicolo, lo scarto DEVE derivare,
perche' le due numerazioni hanno vuoti diversi. Uno scarto congelato non e
un archivio: e una sottrazione."""

# Coppie riferite dalla ricerca come attestate in fonti pubblicate.
# Grado C: la ricerca le riporta, io non ho potuto aprirle.
ATTESTATE = [
    ('Silvio Berlusconi', 1816, 625),
    ('Maurizio Costanzo', 1819, 626),
]

# Le coppie che il testo esaminato dichiara.
TESTO = [
 ('Giudice',1592,504),('Lo Prete',1600,512),('Guglielmi',1602,514),
 ('Miceli',1605,491),('Pelosi',1607,519),('Siracusano',1608,520),
 ('Ortolani',1609,494),('Sindona',1612,501),('Torrisi',1619,531),
 ('Giovannone',1620,532),('Calvi',1624,530),('Grassini',1629,515),
 ('Santovito',1630,527),('Cornacchia',1631,871),('Spagnuolo',1632,543),
 ('Varisco',1633,537),('Gallucci',1634,546),('Viezzer',1635,539),
 ('Malfatti',1636,540),('Semprini',1637,544),
]

print('COPPIE ATTESTATE — lo scarto deriva')
print('-' * 58)
for n, t, f in ATTESTATE:
    print(f'  {n:<20} {t} − {f} = {t-f}')
d = abs((ATTESTATE[1][1]-ATTESTATE[1][2]) - (ATTESTATE[0][1]-ATTESTATE[0][2]))
print(f'\n  Due tessere distanti 3 posizioni ({ATTESTATE[0][1]}→{ATTESTATE[1][1]}) hanno fascicoli')
print(f'  distanti 1 ({ATTESTATE[0][2]}→{ATTESTATE[1][2]}). Lo scarto cambia di {d} in tre posizioni:')
print('  le due numerazioni corrono a passo diverso, perche hanno vuoti diversi.')
print('  E cosi che si comporta un archivio con due registri.')

print()
print('COPPIE DEL TESTO — lo scarto si congela')
print('-' * 58)
from collections import Counter
sc = Counter(t - f for _, t, f in TESTO)
comune, quante = sc.most_common(1)[0]
print(f'  scarto piu frequente: {comune}, su {quante} coppie di {len(TESTO)}')
blocco = [(n, t, f) for n, t, f in TESTO if t - f == comune]
print(f'  tessere interessate: {", ".join(str(t) for _, t, _ in blocco)}')
print(f'  vanno da {min(t for _, t, _ in blocco)} a {max(t for _, t, _ in blocco)}:')
print(f'  {max(t for _,t,_ in blocco) - min(t for _,t,_ in blocco)} posizioni con scarto invariato.')
print()
print('  Nelle due coppie attestate lo scarto cambia di 2 in 3 posizioni.')
print(f'  Nelle otto coppie del testo non cambia di 1 in {max(t for _,t,_ in blocco) - min(t for _,t,_ in blocco)}.')

print()
print('LA SERIE CONTINUA')
print('-' * 58)
SERIE = [('Salacone',1630),('Cornacchia',1631),('Spagnuolo',1632),('Varisco',1633),
         ('Gallucci',1634),('Viezzer',1635),('Malfatti',1636),('Semprini',1637),
         ('Esposito',1638),('Ferracuti',1639)]
print(f'  Il testo assegna {len(SERIE)} interi consecutivi a {len(SERIE)} persone diverse:')
for n, t in SERIE:
    print(f'    {t}  {n}')
print()
print('  Una corsa ininterrotta di dieci e incompatibile con la numerazione')
print('  "ad ampi e ingiustificati vuoti" che gli atti descrivono. In un elenco')
print('  di 962 nomi sparsi su un intervallo di circa 1.600 valori, la densita')
print(f'  media e di {962/1600:.2f} nomi per posizione: la probabilita di dieci')
print(f'  consecutivi in un punto qualsiasi e dell ordine di {(962/1600)**10:.1e}.')
