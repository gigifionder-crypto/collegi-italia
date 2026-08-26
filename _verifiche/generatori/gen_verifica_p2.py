# -*- coding: utf-8 -*-
"""Infografiche della verifica sull'elenco dei trentatre nomi.
Stile della casa: fondo a gradiente crema, inchiostro blu navy, barre orizzontali."""
import os, glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
OUT = os.path.join(SP, 'grafici-verifica-p2')
os.makedirs(OUT, exist_ok=True)

for f in glob.glob(os.path.expanduser('~/.fonts/BarlowSemiCondensed-*.ttf')):
    font_manager.fontManager.addfont(f)
plt.rcParams['font.family'] = 'Barlow Semi Condensed'
plt.rcParams['figure.facecolor'] = '#ffffff'
plt.rcParams['savefig.facecolor'] = 'none'

NAVY = '#1F3864'
INK  = '#222222'
MUT  = '#666666'
PAL8 = ['#3465C0', '#E07B2E', '#8257C8', '#3B9C3B', '#C7699E', '#C7AB1E', '#2FA0B8', '#C24444']
ROSSO = '#C24444'      # stato "valore impossibile" — sempre accompagnato da etichetta
GRIGIO = '#9AA1AC'

_CREMA = LinearSegmentedColormap.from_list(
    'crema', ['#ffffff', '#fdfaf4', '#f7f1e5', '#f2e8d6', '#eee2cc'])

def _fondo(fig):
    bg = fig.add_axes([0, 0, 1, 1], zorder=-1)
    vert = np.linspace(0, 1, 256).reshape(-1, 1)
    oriz = np.linspace(0, 1, 256).reshape(1, -1)
    bg.imshow(vert * 0.82 + oriz * 0.18, aspect='auto', cmap=_CREMA,
              origin='upper', interpolation='bilinear', vmin=0, vmax=1)
    bg.set_axis_off()

def _it(v):
    return f'{int(round(v)):,}'.replace(',', '.')

def _telaio(ax):
    ax.xaxis.grid(True, color='#d9d3c6', linewidth=0.7, zorder=1)
    ax.set_axisbelow(True)
    for s in ('top', 'right', 'bottom'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_color('#c9ccd2'); ax.spines['left'].set_linewidth(0.8)
    ax.tick_params(axis='x', labelsize=7.0, colors=MUT, length=0)
    ax.tick_params(axis='y', length=0)

def barre(labels, values, title, xlabel, out, colors=None, note=None, valuefmt=_it):
    n = len(labels)
    h = max(2.6, min(7.2, 0.36 * n + 1.5 + (0.10 * len(note or []))))
    fig, ax = plt.subplots(figsize=(6.8, h), dpi=120)
    _fondo(fig)
    ax.set_facecolor('none'); ax.patch.set_alpha(0); ax.set_zorder(2)
    y = np.arange(n)[::-1].astype(float)
    cs = colors or [NAVY] * n
    vmax = max(values) or 1
    ax.barh(y, values, height=0.66, color=cs, edgecolor='white', linewidth=0.6, zorder=3)
    for yy, v in zip(y, values):
        ax.text(v + vmax * 0.015, yy, valuefmt(v), va='center', ha='left',
                fontsize=7.4, color=INK, zorder=4)
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=7.8, color=INK)
    ax.set_xlim(0, vmax * 1.18); ax.set_ylim(-0.8, n - 0.2)
    ax.set_xlabel(xlabel, fontsize=8, color=MUT, labelpad=4)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(nbins=6, steps=[1, 2, 2.5, 5, 10]))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: _it(v)))
    _telaio(ax)
    fig.text(0.012, 0.965, title, fontsize=12.2, color=NAVY, fontweight='bold', va='top')
    # margini in pollici, convertiti: cosi' la nota resta attaccata al grafico anche in figure alte
    if note:
        bassa = 0.30 + 0.115 * len(note)
        fig.text(0.012, (0.10 / h), '\n'.join(note), fontsize=6.5, color=MUT, va='bottom')
    else:
        bassa = 0.42
    fig.subplots_adjust(left=0.34, right=0.985, top=1 - 0.55 / h, bottom=bassa / h)
    fig.savefig(os.path.join(OUT, out)); plt.close(fig)
    print('  ', out)


# ---------------------------------------------------------------- i dati
# Le 33 righe della tabella, nell'ordine in cui il testo le presenta.
# (nome, tessera dichiarata nel post, sede istituzionale, riscontro indipendente)
#   F = appartenenza agli elenchi corroborata da fonti indipendenti dal testo
#   C = persona reale e ruolo 1978 verificabile, appartenenza non corroborata
#   G = posizione contestata e definita in sede giudiziaria
TAB = [
 ('Sergio Di Donato',      158,  'servizi informativi',      'C'),
 ('Giuseppe Santovito',    163,  'servizi informativi', 'F'),
 ('Vincenzo Rizzuti',      811,  'servizi informativi', 'C'),
 ('Raffaele Giudice',      1592, 'finanza (GdF)','F'),
 ('Donato Lo Prete',       1600, 'finanza (GdF)','F'),
 ('Camillo Guglielmi',     1602, 'servizi informativi', 'C'),
 ('Vito Miceli',           1605, 'servizi informativi', 'F'),
 ('Walter Pelosi',         1607, 'servizi informativi', 'F'),
 ('Giuseppe Siracusano',   1608, 'carabinieri',  'C'),
 ('Umberto Ortolani',      1609, 'banche',       'F'),
 ('Michele Sindona',       1612, 'banche',       'F'),
 ('Pietro Musumeci',       1614, 'servizi informativi', 'F'),
 ('Giovanni Torrisi',      1619, 'difesa',       'F'),
 ('Stefano Giovannone',    1620, 'servizi informativi', 'C'),
 ('Antonino Geraci',       1621, 'servizi informativi', 'C'),
 ('Roberto Calvi',         1624, 'banche',       'F'),
 ('Elio Cioppa',           1628, 'polizia',      'F'),
 ('Giulio Grassini',       1629, 'servizi informativi', 'F'),
 ('Mario Salacone',        1630, 'servizi informativi', 'C'),
 ('Antonio Cornacchia',    1631, 'carabinieri',  'F'),
 ('Carmelo Spagnuolo',     1632, 'magistratura', 'F'),
 ('Antonio Varisco',       1633, 'carabinieri',  'F'),
 ('Achille Gallucci',      1634, 'magistratura', 'C'),
 ('Antonio Viezzer',       1635, 'servizi informativi', 'F'),
 ('Francesco Malfatti',    1636, 'diplomazia',   'C'),
 ('Mario Semprini',        1637, 'governo',      'C'),
 ('Antonio Esposito',      1638, 'servizi informativi', 'C'),
 ('Franco Ferracuti',      1639, 'servizi informativi', 'C'),
 ("Federico U. D'Amato",   1643, 'servizi informativi', 'F'),
 ('Mino Pecorelli',        1750, 'stampa e RAI', 'F'),
 ('Gustavo Selva',         1803, 'stampa e RAI', 'G'),
 ('Maurizio Costanzo',     1819, 'stampa e RAI', 'F'),
 ('Franco Di Bella',       1887, 'stampa e RAI', 'F'),
]
SOGLIA = 1600
nF = sum(1 for r in TAB if r[3] == 'F')
nC = sum(1 for r in TAB if r[3] == 'C')
nG = sum(1 for r in TAB if r[3] == 'G')
assert nF + nC + nG == 33, (nF, nC, nG)
print(f'tabella: {len(TAB)} righe — F {nF} · C {nC} · G {nG}')


# ---------------------------------------------------------- 1. l'imbuto
barre(["nomi elencati nella tabella",
       "persone storiche reali,\nruolo del 1978 verificabile",
       "appartenenza agli elenchi\ncorroborata fuori dal testo",
       "posizione definita\nin sede giudiziaria",
       "numero di tessera\ncorroborato fuori dal testo"],
      [33, 33, nF, nG, 0],
      "Che cosa regge, campo per campo",
      "nomi", "1_imbuto-della-verificabilita.png",
      colors=[NAVY, NAVY, PAL8[0], PAL8[1], ROSSO],
      note=["Il campo su cui il testo chiede di costruire il calcolo — il numero di tessera — è l'unico",
            "per cui non ho un solo riscontro indipendente. Dodici nomi restano al grado C: la persona",
            "e il ruolo del 1978 sono verificabili, l'appartenenza no. Il confine fra i due gradi è quello",
            "della mia conoscenza, non quello dell'archivio: solo l'allegato Anselmi può spostarlo."])


# ------------------------------------- 2. le tessere contro la soglia 1600
def soglia_plot(out):
    casi = [(n, t) for n, t, _, _ in TAB if t <= SOGLIA]
    casi.sort(key=lambda r: r[1])
    altri = [t for _, t, _, _ in TAB if t > SOGLIA]
    n = len(casi)
    fig, ax = plt.subplots(figsize=(6.8, 3.5), dpi=120)
    _fondo(fig)
    ax.set_facecolor('none'); ax.patch.set_alpha(0); ax.set_zorder(2)
    y = np.arange(n)[::-1].astype(float)
    cs = [ROSSO if t < SOGLIA else GRIGIO for _, t in casi]
    ax.barh(y, [t for _, t in casi], height=0.62, color=cs,
            edgecolor='white', linewidth=0.6, zorder=3)
    for yy, (nm, t) in zip(y, casi):
        etichetta = _it(t) + ('' if t < SOGLIA else '  (esattamente sulla soglia)')
        if SOGLIA - t < 120:      # eviterebbe la linea tratteggiata: etichetta dentro la barra
            ax.text(t - 30, yy, etichetta, va='center', ha='right',
                    fontsize=7.4, color='white', zorder=4)
        else:
            ax.text(t + 28, yy, etichetta, va='center', ha='left',
                    fontsize=7.4, color=ROSSO if t < SOGLIA else MUT, zorder=4)
    ax.axvline(SOGLIA, color='#6b6455', linewidth=1.3, linestyle=(0, (5, 3)), zorder=5)
    ax.text(SOGLIA - 30, n - 0.42, 'soglia documentata\nnegli atti: 1.600',
            fontsize=7.6, color='#6b6455', ha='right', va='center', linespacing=1.35)
    ax.set_yticks(y)
    ax.set_yticklabels([nm for nm, _ in casi], fontsize=8.0, color=INK)
    ax.set_xlim(0, 1780); ax.set_ylim(-0.7, n - 0.25)
    ax.set_xlabel('numero di tessera dichiarato nel testo', fontsize=8, color=MUT, labelpad=4)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(400))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: _it(v)))
    _telaio(ax)
    fig.text(0.012, 0.965, 'Quattro tessere che la fonte primaria esclude',
             fontsize=12.2, color=NAVY, fontweight='bold', va='top')
    fig.text(0.012, 0.012,
             '\n'.join(["Nelle audizioni della Commissione Anselmi è verbalizzato che la numerazione delle tessere",
                        "sequestrate presenta ampi vuoti e che nessuna tessera aveva numero inferiore al 1.600.",
                        f"Quattro dei trentatré valori del testo cadono sotto quella soglia; un quinto vi si posa esatto.",
                        f"Gli altri {len(altri)} stanno fra {_it(min(altri))} e {_it(max(altri))}, dentro l'intervallo plausibile.",
                        "Non sono numeri sbagliati di poco: sono numeri che quel campo non poteva contenere."]),
             fontsize=6.5, color=MUT, va='bottom')
    fig.subplots_adjust(left=0.26, right=0.985, top=0.86, bottom=0.30)
    fig.savefig(os.path.join(OUT, out)); plt.close(fig)
    print('  ', out)

soglia_plot('2_tessere-sotto-la-soglia-documentata.png')


# --------------------------------------- 3. i trentatré per sede istituzionale
from collections import Counter
_c = Counter(sede for _, _, sede, _ in TAB)
_ord = sorted(_c.items(), key=lambda kv: -kv[1])
barre([k for k, _ in _ord], [v for _, v in _ord],
      "Dove stavano, nella primavera del 1978",
      "nomi della tabella", "3_i-trentatre-per-sede-istituzionale.png",
      note=["Ripartizione delle trentatré righe secondo la sede istituzionale che il testo attribuisce",
            "a ciascuno nel 1978. Quindici su trentatré stanno nei servizi informativi riformati l'anno",
            "prima; ventidue su trentatré in apparati che rispondono all'esecutivo. È la ragione per cui",
            "l'elenco impressiona — e la ragione per cui va verificato prima, non dopo, averlo pubblicato."])


# ------------------------------ 4. la composizione documentata dei 962
_ANS = [('dirigenti di enti pubblici', 128),
        ('ufficiali delle forze armate', 119),
        ('parlamentari', 59),
        ('dirigenti di polizia', 22),
        ('giornalisti', 22),
        ('direttori di giornale', 8),
        ('editori', 4),
        ('giudici costituzionali', 1)]
barre([k for k, _ in _ANS], [v for _, v in _ANS],
      "Che cosa contengono davvero i 962 nominativi",
      "persone", "4_composizione-documentata-dei-962.png",
      note=["Composizione riportata dalle fonti sui lavori della Commissione Anselmi. I 119 ufficiali si",
            "ripartiscono in 50 dell'Esercito, 37 della Guardia di Finanza e 32 dell'Arma dei Carabinieri.",
            "ANNOTAZIONE — Il grafico del Libro quarto registra 44 parlamentari, cifra presa dal corpus.",
            "La cifra documentata è 59. L'errore non viene cancellato là: viene annotato qui accanto,",
            "come vuole la disciplina dell'opera. Resta da dirimere sull'allegato quale delle due regga."])


# ------------------------------------------------ 5. la cronologia della prova
from datetime import date
_seq   = date(1978, 3, 16)     # via Fani
_morte = date(1978, 5, 9)
_fin_a = date(1977, 9, 16)     # sei mesi prima del sequestro
_fin_b = date(1978, 11, 9)     # sei mesi dopo la morte
_elen  = date(1981, 3, 17)     # sequestro degli elenchi a Castiglion Fibocchi
_anse  = date(1984, 7, 12)     # deposito della relazione di maggioranza
_CRO = [("finestra richiesta\n(sei mesi · 55 giorni · sei mesi)", (_fin_b - _fin_a).days),
        ("dai fatti al sequestro\ndegli elenchi", (_elen - _seq).days),
        ("dai fatti al deposito\ndella relazione Anselmi", (_anse - _seq).days)]
barre([k for k, _ in _CRO], [v for _, v in _CRO],
      "La prova è molto più tardi dei fatti",
      "giorni", "5_distanza-fra-i-fatti-e-la-prova.png",
      colors=[PAL8[0], NAVY, NAVY],
      note=["16 settembre 1977 – 9 novembre 1978 la finestra · 17 marzo 1981 gli elenchi a Castiglion",
            "Fibocchi · 12 luglio 1984 il deposito della relazione di maggioranza.",
            "Nel 1978 la composizione della loggia non era un oggetto conoscibile: fu rivelata tre anni dopo",
            "e ordinata sei anni dopo. Una lista del 1981 dice chi vi risultava nel 1981, non chi agì nel 1978."])


# ---------------------------- 6. dove il corpus ha materia, nella finestra
_MESI = [('settembre 1977', 3), ('ottobre 1977', 6), ('novembre 1977', 8), ('dicembre 1977', 1),
         ('gennaio 1978', 5), ('febbraio 1978', 7), ('marzo 1978', 63), ('aprile 1978', 48),
         ('maggio 1978', 50), ('giugno 1978', 3), ('luglio 1978', 3), ('agosto 1978', 5),
         ('settembre 1978', 16), ('ottobre 1978', 7), ('novembre 1978', 0)]
_dentro = {'marzo 1978', 'aprile 1978', 'maggio 1978'}
barre([n for n, _ in _MESI], [v for _, v in _MESI],
      "Dove il corpus ha materia, mese per mese",
      "date esplicite nei documenti del corpus", "6_finestra-sei-mesi-materia-disponibile.png",
      colors=[PAL8[0] if n in _dentro else NAVY for n, _ in _MESI],
      note=["Conteggio meccanico delle date esplicite nei documenti del corpus, da settembre 1977 a",
            "novembre 1978. Dei 225 riferimenti datati della finestra, 161 — il 72 per cento — cadono nei",
            "tre mesi del sequestro (in azzurro). Misura quanto il corpus parla di ciascun mese, non quanto",
            "in quel mese accadde. Novembre 1978 non ha una sola data: il vuoto è esso stesso un dato."])

print('fatto.')
