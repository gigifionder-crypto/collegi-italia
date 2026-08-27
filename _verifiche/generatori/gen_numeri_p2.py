# -*- coding: utf-8 -*-
"""I due grafici dell'analisi strutturale dei numeri."""
import importlib.util, os, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
spec = importlib.util.spec_from_file_location('g', os.path.join(SP, 'gen_verifica_p2.py'))
g = importlib.util.module_from_spec(spec)
_out = sys.stdout
sys.stdout = open(os.devnull, 'w')
try:
    spec.loader.exec_module(g)
finally:
    sys.stdout = _out

OUT = g.OUT
NAVY, INK, MUT, ROSSO, GRIGIO = g.NAVY, g.INK, g.MUT, g.ROSSO, g.GRIGIO

D = [('Giudice',1592,504),('Lo Prete',1600,512),('Guglielmi',1602,514),
     ('Miceli',1605,491),('Pelosi',1607,519),('Siracusano',1608,520),
     ('Ortolani',1609,494),('Sindona',1612,501),('Torrisi',1619,531),
     ('Giovannone',1620,532),('Calvi',1624,530),('Grassini',1629,515),
     ('Santovito',1630,527),('Cornacchia',1631,871),('Spagnuolo',1632,543),
     ('Varisco',1633,537),('Gallucci',1634,546),('Viezzer',1635,539),
     ('Malfatti',1636,540),('Semprini',1637,544)]
K = 1088

# ------------------------------------------------ 10. le due numerazioni
def dispersione(out):
    fig, ax = plt.subplots(figsize=(6.8, 4.6), dpi=120)
    g._fondo(fig)
    ax.set_facecolor('none'); ax.patch.set_alpha(0); ax.set_zorder(2)

    xs = np.array([1588, 1641])
    ax.plot(xs, xs - K, color='#8a8375', linewidth=1.3, linestyle=(0, (5, 3)), zorder=3)
    ax.text(1639.5, 1639.5 - K + 6, 'fascicolo = tessera − 1.088',
            fontsize=7.6, color='#6b6455', ha='right', va='bottom')

    # le etichette del gruppo di destra si accavallerebbero: si sfalsano
    SFALSA = {'Spagnuolo': (-1.6, -9), 'Varisco': (-1.0, -20), 'Viezzer': (2.2, -9),
              'Malfatti': (2.6, -20), 'Semprini': (3.0, -31), 'Santovito': (-1.4, -31),
              'Grassini': (-2.0, -42), 'Cornacchia': (-0.6, -11)}
    for n, t, f in D:
        sulla = (t - f) == K
        fuori_scala = f > 600
        y = min(f, 600)
        ax.scatter([t], [y], s=54, zorder=5,
                   color=NAVY if sulla else ROSSO,
                   marker='o' if not fuori_scala else '^',
                   edgecolor='white', linewidth=1.0)
        if not sulla:
            et = f'{n} · {f}' + (' (fuori scala)' if fuori_scala else '')
            dx, dy = SFALSA.get(n, (0, -9))
            ax.annotate(et, xy=(t, y), xytext=(t + dx, y + dy),
                        fontsize=6.8, color=ROSSO, ha='center', va='top',
                        arrowprops=dict(arrowstyle='-', color=ROSSO, linewidth=0.5,
                                        alpha=.55, shrinkA=0, shrinkB=3))

    ax.set_xlim(1588, 1643); ax.set_ylim(462, 612)
    ax.set_xlabel('numero di tessera dichiarato', fontsize=8, color=MUT, labelpad=4)
    ax.set_ylabel('numero di fascicolo dichiarato', fontsize=8, color=MUT, labelpad=4)
    for a in (ax.xaxis, ax.yaxis):
        a.set_major_formatter(mticker.FuncFormatter(lambda v, _: g._it(v)))
    ax.xaxis.grid(True, color='#d9d3c6', linewidth=0.7, zorder=1)
    ax.yaxis.grid(True, color='#d9d3c6', linewidth=0.7, zorder=1)
    ax.set_axisbelow(True)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('bottom', 'left'):
        ax.spines[s].set_color('#c9ccd2'); ax.spines[s].set_linewidth(0.8)
    ax.tick_params(labelsize=7.0, colors=MUT, length=0)
    fig.text(0.012, 0.965, 'Otto coppie su venti stanno sulla stessa retta',
             fontsize=12.2, color=NAVY, fontweight='bold', va='top')
    fig.text(0.012, 0.012, '\n'.join([
      "Ogni punto è una persona: in ascissa la tessera che il testo le attribuisce, in ordinata il fascicolo.",
      "Otto coppie cadono esattamente su fascicolo = tessera − 1.088. Se due numerazioni progressive corrono",
      "in parallelo su un blocco contiguo, ogni altra coppia del blocco deve stare sulla stessa retta: se il",
      "1.602 è il 514 e il 1.607 è il 519, il 1.605 non può che essere il 517 — e il testo lo dà per 491.",
      "Il triangolo è Cornacchia, fascicolo 871: fuori scala di oltre trecento posizioni."]),
      fontsize=6.5, color=MUT, va='bottom')
    fig.subplots_adjust(left=0.10, right=0.985, top=0.885, bottom=0.315)
    fig.savefig(os.path.join(OUT, out)); plt.close(fig)
    print('  ', out)

dispersione('10_le-due-numerazioni-sulla-stessa-retta.png')

# ------------------------------------------------ 11. gli scarti dalla retta
def scarti(out):
    """Barre divergenti dallo zero: i valori negativi hanno un verso, e va mostrato."""
    res = sorted(((n, t, f, f - (t - K)) for n, t, f in D), key=lambda r: r[3])
    n_ = len(res)
    LIM = 34                      # oltre questo si tronca e si dichiara
    fig, ax = plt.subplots(figsize=(6.8, 6.4), dpi=120)
    g._fondo(fig)
    ax.set_facecolor('none'); ax.patch.set_alpha(0); ax.set_zorder(2)
    y = np.arange(n_)[::-1].astype(float)
    for yy, (nome, t, f, d) in zip(y, res):
        v = max(-LIM, min(LIM, d))
        troncato = v != d
        ax.barh(yy, v, height=0.62, color=NAVY if d == 0 else ROSSO,
                edgecolor='white', linewidth=0.6, zorder=3,
                hatch='///' if troncato else None)
        if d == 0:
            ax.text(1.4, yy, 'sulla retta', va='center', ha='left',
                    fontsize=7.2, color=NAVY, zorder=4)
        else:
            et = ('+' if d > 0 else '−') + g._it(abs(d)) + (' (troncato)' if troncato else '')
            ax.text(v + (1.4 if v >= 0 else -1.4), yy, et, va='center',
                    ha='left' if v >= 0 else 'right', fontsize=7.2, color=ROSSO, zorder=4)
    ax.axvline(0, color='#6b6455', linewidth=1.1, zorder=5)
    ax.set_yticks(y)
    ax.set_yticklabels([f'{nome}  ({g._it(t)} · {g._it(f)})' for nome, t, f, _ in res],
                       fontsize=7.6, color=INK)
    ax.set_xlim(-LIM - 12, LIM + 16); ax.set_ylim(-0.8, n_ - 0.2)
    ax.set_xlabel('posizioni di scarto dal valore che la retta predice',
                  fontsize=8, color=MUT, labelpad=4)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(10))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(
        lambda v, _: ('' if abs(v) > LIM else ('+' if v > 0 else '−' if v < 0 else '') + g._it(abs(v)))))
    g._telaio(ax); ax.spines['left'].set_visible(False)
    fig.text(0.012, 0.965, 'Lo scarto di ciascuna coppia dalla retta',
             fontsize=12.2, color=NAVY, fontweight='bold', va='top')
    fig.text(0.012, 0.012, '\n'.join([
      "Zero significa che il fascicolo dichiarato coincide con quello che la retta predice. Otto coppie su",
      "venti sono a zero; le altre dodici deviano, in un verso o nell'altro, da una a trecentoventotto",
      "posizioni. La barra tratteggiata è Cornacchia, +328: troncata perché schiaccerebbe la scala.",
      "Uno scarto costante fra due numerazioni indipendenti ha, su ventitré coppie, una probabilità",
      "dell'ordine di cinque su mille miliardi: significa che una delle due è stata ricavata dall'altra per",
      "sottrazione, non registrata a parte. Le dodici deviazioni restano allora senza spiegazione."]),
      fontsize=6.5, color=MUT, va='bottom')
    fig.subplots_adjust(left=0.30, right=0.985, top=0.905, bottom=0.175)
    fig.savefig(os.path.join(OUT, out)); plt.close(fig)
    print('  ', out)

scarti('11_scarto-dalla-retta.png')
print('fatto.')
