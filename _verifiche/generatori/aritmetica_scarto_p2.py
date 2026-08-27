# -*- coding: utf-8 -*-
"""L'aritmetica dello scarto fra numero di tessera e numero di fascicolo P2.

Ricalcola cio' che la quarta annotazione della certificazione afferma, cosi' che
chiunque possa rifarlo e contestarlo. Non richiede rete."""
from math import comb, log, exp

ATTESTATE = [('Berlusconi', 1816, 625), ('Costanzo', 1819, 626)]
OTTO = [('Giudice', 1592, 504), ('Lo Prete', 1600, 512), ('Guglielmi', 1602, 514),
        ('Pelosi', 1607, 519), ('Siracusano', 1608, 520), ('Torrisi', 1619, 531),
        ('Giovannone', 1620, 532), ('Gallucci', 1634, 546)]

def scarti(coppie):
    return [(n, t - f) for n, t, f in coppie]

def p_necessaria(soglia, n=23, k=8):
    """La probabilita' che il valore piu' frequente dovrebbe avere perche' otto
    scarti uguali fra n siano plausibili alla soglia data. Non assume nulla sulla
    forma della distribuzione: e' il maggiorante C(n,k)*p^(k-1)."""
    return exp((log(soglia) - log(comb(n, k))) / (k - 1))

if __name__ == '__main__':
    print('attestate:', scarti(ATTESTATE))
    print('otto del testo pervenuto:', sorted({s for _, s in scarti(OTTO)}))
    for soglia in (0.5, 0.1, 0.05, 0.01, 0.001):
        p = p_necessaria(soglia)
        print(f'  soglia {soglia:>6.3f} -> p necessaria {p:.3f} '
              f'(circa {round(962 * p)} iscritti su 962)')
