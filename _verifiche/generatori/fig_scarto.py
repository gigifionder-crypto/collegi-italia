# -*- coding: utf-8 -*-
"""Il grafico dello scarto: otto coppie congelate a 1088 contro due attestate."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

BLU, ROSSO, GRIGIO = '#1F3864', '#8a2d2d', '#5b5b5b'
try:
    plt.rcParams['font.family'] = 'Barlow Semi Condensed'
except Exception:
    pass

OTTO = [('Giudice', 1592, 504), ('Lo Prete', 1600, 512), ('Guglielmi', 1602, 514),
        ('Pelosi', 1607, 519), ('Siracusano', 1608, 520), ('Torrisi', 1619, 531),
        ('Giovannone', 1620, 532), ('Gallucci', 1634, 546)]
ATT = [('Berlusconi', 1816, 625), ('Costanzo', 1819, 626)]

def disegna(dst):
    fig, ax = plt.subplots(figsize=(9.6, 5.4))
    xs = [t for _, t, _ in OTTO]; ys = [t - f for _, t, f in OTTO]
    ax.plot(xs, ys, 'o-', color=ROSSO, lw=1.6, ms=7, zorder=3,
            label='le otto coppie del testo pervenuto')
    xa = [t for _, t, _ in ATT]; ya = [t - f for _, t, f in ATT]
    ax.plot(xa, ya, 's-', color=BLU, lw=1.6, ms=8, zorder=3,
            label='le due coppie attestate da fonti indipendenti')
    # Le etichette si accavallano se poste tutte allo stesso livello: si sfalsano
    # su quattro quote e si collegano al punto con una guida sottile.
    QUOTE = [-26, -44, -62, -80]
    for i, (n, t, f) in enumerate(OTTO):
        dy = QUOTE[i % len(QUOTE)]
        ax.annotate(n, (t, t - f), textcoords='offset points', xytext=(0, dy),
                    ha='center', fontsize=8.2, color=GRIGIO,
                    arrowprops=dict(arrowstyle='-', color='#c9c9c9', lw=0.7,
                                    shrinkA=0, shrinkB=3))
    for (n, t, f), dx in zip(ATT, (-58, 58)):
        ax.annotate(f'{n}\nscarto {t - f}', (t, t - f), textcoords='offset points',
                    xytext=(dx, 26), ha='center', fontsize=8.8, color=BLU,
                    arrowprops=dict(arrowstyle='-', color='#a9b4cc', lw=0.7,
                                    shrinkA=0, shrinkB=4))
    ax.annotate('1088 · identico su quarantadue posizioni di tessera',
                (xs[3], 1088), textcoords='offset points', xytext=(30, 26),
                ha='left', fontsize=9.4, color=ROSSO,
                arrowprops=dict(arrowstyle='-', color=ROSSO, lw=0.7,
                                shrinkA=0, shrinkB=4))
    ax.set_xlabel('numero di tessera dichiarato')
    ax.set_ylabel('scarto  (tessera − fascicolo)')
    ax.set_title("Uno scarto che non si muove, e due che si muovono",
                 color=BLU, fontsize=13, pad=14)
    ax.set_ylim(1005, 1265)
    ax.grid(axis='y', color='#e3e3e3', lw=0.8)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=8.6, loc='lower right')
    fig.text(0.5, 0.015,
             "Le metriche contano numeri, mai colpe. Nessuna riga di questo grafico "
             "attribuisce condotte ad alcuno.",
             ha='center', fontsize=7.4, color=GRIGIO, style='italic')
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(dst, dpi=200)
    plt.close(fig)
    return dst

if __name__ == '__main__':
    import sys
    print(disegna(sys.argv[1] if len(sys.argv) > 1 else 'scarto.png'))
