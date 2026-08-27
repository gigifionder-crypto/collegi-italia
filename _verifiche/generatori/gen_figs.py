# -*- coding: utf-8 -*-
"""Genera l'apparato grafico 3D per l'Opera integrale: >=2 grafici per capitolo, sfondo bianco."""
import os, re, json, glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D  # noqa
import numpy as np

SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
REPO = '/home/user/collegi-italia'
FIGS = os.path.join(SP, 'figs')
os.makedirs(FIGS, exist_ok=True)

for f in glob.glob(os.path.expanduser('~/.fonts/BarlowSemiCondensed-*.ttf')):
    font_manager.fontManager.addfont(f)
plt.rcParams['font.family'] = 'Barlow Semi Condensed'
plt.rcParams['figure.facecolor'] = '#ffffff'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'none'

NAVY = '#1F3864'
CAT = ['#3465C0', '#C24444', '#E07B2E', '#3B9C3B']  # sottoinsieme categoriale della tavolozza
PAL8 = ['#3465C0', '#E07B2E', '#8257C8', '#3B9C3B', '#C7699E', '#C7AB1E', '#2FA0B8', '#C24444']  # blu·arancione·viola·verde·rosa·giallo·teal·rosso — convalidata (ordine fisso)
def pal(n, rot=0):
    return [PAL8[(rot + i) % len(PAL8)] for i in range(n)]
INK = '#222222'; MUT = '#666666'

PARTS = [
 ('Portale', 'aldo-moro-una-guerra-senza-fine-edizione-strutturata.md'),
 ('Libro primo', 'aldo-moro-una-guerra-senza-fine-fase-ottava-il-ritratto.md'),
 ('Libro secondo', 'dal-che-a-moro-una-guerra-senza-fine.md'),
 ('Libro terzo I', 'guevara-origini-esilio-messicano.md'),
 ('Libro terzo II', 'guevara-messico-avana-1954-1965.md'),
 ('Libro terzo III', 'guevara-mosca-bolivia-1964-1966.md'),
 ('Libro terzo IV', 'guevara-campagna-boliviana-1966-1967.md'),
 ('Libro terzo V', 'guevara-bibliografia-critica.md'),
 ('Libro terzo VI', 'triangolazioni-guevara-moro.md'),
 ('Libro quarto', 'dossier-maggiore-una-pace-senza-pace.md'),
 ('Libro quinto I', 'feltrinelli-il-vettore.md'),
 ('Libro quinto II', 'triangolazione-feltrinelli-corpus.md'),
 ('Libro quinto III', 'triangolazione-hyperion-corpus.md'),
 ('Libro quinto IV', 'triangolazione-feltrinelli-hyperion.md'),
 ('Libro quinto V', 'ceppo-simioni-cpm-superclan-hyperion.md'),
 ('Libro sesto I', 'tribunale-speciale-storia-istituzione.md'),
 ('Libro sesto II', 'tribunale-speciale-approfondimento-sottonodi.md'),
 ('Libro sesto III', 'amnistiati-tribunale-speciale.md'),
 ('Libro settimo', 'aldo-moro-una-guerra-senza-fine-parte-terza.md'),
 ('Libro ottavo I', 'aldo-moro-una-guerra-senza-fine-fase-sesta.md'),
 ('Libro ottavo II', 'metodologie-del-dossier-sinaptogenesi-e-strumenti.md'),
 ('Libro nono', 'aldo-moro-una-guerra-senza-fine-fase-settima-registro-giudiziario.md'),
 ('Libro decimo', 'aldo-moro-una-guerra-senza-fine-fase-nona-repertorio-del-caso.md'),
 ('Libro undicesimo I', 'aldo-moro-una-guerra-senza-fine-fase-decima-responsabilita-personali.md'),
 ('Libro undicesimo II', 'triangolazione-condannati-corpus.md'),
 ('Libro dodicesimo I', 'moro-ministro-esteri/README.md'),
 ('Libro dodicesimo II', 'moro-ministro-esteri/originali/ricognizione-ministro-esteri-1969-1974.md'),
 ('Libro dodicesimo III', 'moro-ministro-esteri/originali/germania-opus-dei-1952-1985.md'),
 ('Libro dodicesimo IV', 'moro-ministro-esteri/originali/santa-sede-due-germanie-oder-neisse.md'),
 ('Libro dodicesimo V', 'moro-ministro-esteri/originali/portogallo-opus-dei.md'),
 ('Libro dodicesimo VI', 'moro-ministro-esteri/originali/portogallo-santa-sede-1969-1974.md'),
 ('Libro dodicesimo VII', 'moro-ministro-esteri/originali/grecia-opus-dei-1969-1985.md'),
 ('Libro dodicesimo VIII', 'moro-ministro-esteri/originali/turchia-opus-dei-1969-1975.md'),
 ('Libro dodicesimo IX', 'moro-ministro-esteri/originali/santa-sede-turchia-attentato-giovanni-paolo-ii.md'),
 ('Libro dodicesimo X', 'moro-ministro-esteri/originali/documenti-italiani-spagnoli-opus-dei.md'),
 ('Libro dodicesimo XI', 'moro-ministro-esteri/triangolazione-seconda-campagna.md'),
 ('Libro dodicesimo XII', 'moro-ministro-esteri/documenti-state-dept-1965-1978.md'),
 ('Libro dodicesimo XIII', 'le-pene-oltre-confine-mitterrand-mulinaris.md'),
 ('Libro tredicesimo I', 'programma-investigativo-caso-moro.md'),
 ('Libro tredicesimo II', 'approfondimento-piste-di-testa.md'),
 ('Libro tredicesimo III', 'approfondimento-piste-entita.md'),
 ('Libro tredicesimo IV', 'manuale-investigativo-nuovo-caso-moro.md'),
 ('Libro tredicesimo V', 'agenda-di-ricerca-del-nuovo-caso-moro.md'),
 ('Libro tredicesimo VI', 'nove-cantieri-mille-blocchi.md'),
 ('Libro tredicesimo VII', 'kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md'),
 ('Libro quattordicesimo', 'il-meridiano-e-la-valle-mille-blocchi.md'),
 ('Appendice I', 'aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md'),
 ('Appendice II', 'relazione-stato-lavori-stile-moro.md'),
 ('Appendice III', '_verifiche/verifica-elenco-trentatre-nomi-p2.md'),
 ('Appendice IV.i', 'GUIDA-ALLA-LETTURA.md'),
 ('Appendice IV.ii', 'INDICE-DOCUMENTI-BRANCH.md'),
 ('Appendice IV.iii', '_diffusione-opera/README.md'),
 ('Appendice IV.iv', '_diffusione-opera/scheda-dell-opera.md'),
 ('Appendice IV.v', '_diffusione-opera/capitolo-campione.md'),
 ('Appendice IV.vi', '_diffusione-opera/mappa-dei-destinatari.md'),
 ('Appendice IV.vii', '_diffusione-opera/registro-pec-e-canali.md'),
 ('Appendice IV.viii', '_diffusione-opera/checklist-di-invio.md'),
 ('Appendice IV.ix', '_diffusione-opera/curriculum-modello.md'),
 ('Appendice IV.x', '_diffusione-opera/lettera-fondazione-aldo-moro.md'),
 ('Appendice IV.xi', '_diffusione-opera/pec-archivio-flamigni.md'),
 ('Appendice IV.xii', '_diffusione-opera/relazione-al-centro-flamigni.md'),
 ('Appendice IV.xiii', '_diffusione-opera/proposta-editrice-laterza.md'),
 ('Appendice IV.xiv', '_diffusione-opera/proposte-mulino-carocci-einaudi.md'),
 ('Appendice IV.xv', '_diffusione-opera/proposte-chiarelettere-bompiani.md'),
]

def idx_di(nomefile):
    """Indice in PARTS del documento indicato: calcolato, non fissato a mano."""
    for i, (_lab, _p) in enumerate(PARTS):
        if _p.endswith(nomefile):
            return i
    raise SystemExit('gen_figs: documento non trovato in PARTS: ' + nomefile)

IDX_KISS = idx_di('kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md')
IDX_SA   = idx_di('il-meridiano-e-la-valle-mille-blocchi.md')
IDX_PORTALE  = idx_di('aldo-moro-una-guerra-senza-fine-edizione-strutturata.md')
IDX_METOD    = idx_di('metodologie-del-dossier-sinaptogenesi-e-strumenti.md')
IDX_PROGRAMMA= idx_di('programma-investigativo-caso-moro.md')
IDX_PISTE    = idx_di('approfondimento-piste-di-testa.md')
IDX_ENTITA   = idx_di('approfondimento-piste-entita.md')
IDX_MANUALE  = idx_di('manuale-investigativo-nuovo-caso-moro.md')
IDX_AGENDA   = idx_di('agenda-di-ricerca-del-nuovo-caso-moro.md')
IDX_CANTIERI = idx_di('nove-cantieri-mille-blocchi.md')
IDX_DECIMA   = idx_di('aldo-moro-una-guerra-senza-fine-fase-decima-responsabilita-personali.md')
IDX_APPARATO = len(PARTS)   # l'apparato bibliografico segue l'ultimo documento di PARTS
IDX_DOSSIER  = idx_di('dossier-maggiore-una-pace-senza-pace.md')

def load(p):
    return open(os.path.join(REPO, p), encoding='utf-8').read()

def sections(md, max_n=9):
    """Divide per H2; fallback H3; fallback blocchi di paragrafi."""
    lines = md.split('\n')
    secs, cur_t, cur = [], None, []
    for ln in lines:
        m = re.match(r'^## (.+)$', ln)
        if m:
            if cur_t is not None:
                secs.append((cur_t, '\n'.join(cur)))
            cur_t, cur = m.group(1), []
        else:
            cur.append(ln)
    if cur_t is not None:
        secs.append((cur_t, '\n'.join(cur)))
    if len(secs) < 3:
        secs, cur_t, cur = [], None, []
        for ln in lines:
            m = re.match(r'^### (.+)$', ln)
            if m:
                if cur_t is not None:
                    secs.append((cur_t, '\n'.join(cur)))
                cur_t, cur = m.group(1), []
            else:
                cur.append(ln)
        if cur_t is not None:
            secs.append((cur_t, '\n'.join(cur)))
    if len(secs) < 3:
        paras = [p for p in md.split('\n\n') if p.strip()]
        k = max(3, min(6, len(paras)//8 or 3))
        step = max(1, len(paras)//k)
        secs = [(f'Segmento {i+1}', '\n\n'.join(paras[i*step:(i+1)*step])) for i in range(k)]
    if len(secs) > max_n:
        head = secs[:max_n-1]
        tail = secs[max_n-1:]
        head.append(('Altre sezioni', '\n'.join(t for _, t in tail)))
        secs = head
    return secs

def clean_title(t, n=34):
    t = re.sub(r'[*`_]', '', t)
    t = re.sub(r'\s*[—–-]\s*.*$', '', t) if len(t) > n else t
    t = re.sub(r'\(.*?\)', '', t).strip()
    return (t[:n-1] + '…') if len(t) > n else t

def ramp(vals):
    v = np.asarray(vals, dtype=float)
    if v.max() == v.min():
        t = np.full_like(v, 0.7)
    else:
        t = 0.35 + 0.65 * (v - v.min()) / (v.max() - v.min())
    base = np.array([31, 56, 100]) / 255.0   # navy
    light = np.array([201, 212, 234]) / 255.0
    return [tuple(light + (base - light) * ti) + (1.0,) for ti in t]

def style_ax(ax):
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 1))
        axis._axinfo['grid'].update(color='#DDDDDD', linewidth=0.5)
        axis.line.set_color('#AAAAAA')
    ax.tick_params(colors=INK, labelsize=8)


# Fondo a gradiente — gli stessi tre valori della pagina dell'opera.
from matplotlib.colors import LinearSegmentedColormap
_CREMA = LinearSegmentedColormap.from_list(
    'crema', ['#ffffff', '#fdfaf4', '#f7f1e5', '#f2e8d6', '#eee2cc'])


def _fondo(fig):
    """Il gradiente della pagina, portato sotto il grafico: scende dall'alto,
    con una lieve deriva verso destra come il 168° della pagina."""
    bg = fig.add_axes([0, 0, 1, 1], zorder=-1)
    vert = np.linspace(0, 1, 256).reshape(-1, 1)
    oriz = np.linspace(0, 1, 256).reshape(1, -1)
    g = vert * 0.82 + oriz * 0.18
    bg.imshow(g, aspect='auto', cmap=_CREMA, origin='upper', interpolation='bilinear',
              vmin=0, vmax=1)
    bg.set_axis_off()
    return bg


def _fmt(v, value_fmt):
    return value_fmt.format(v).replace(',', '.')


def bar3d(labels, values, title, zlabel, out, colors=None, legend_lines=None,
          value_fmt='{:,.0f}', elev=None, azim=None, ylabels=None, rows=None, rot=0):
    """Barre orizzontali. Il nome resta per compatibilita' con le chiamate esistenti;
    elev e azim sono ignorati (non c'e' piu' prospettiva da orientare)."""
    if rows is None:
        rows = [('', values)]
    nrows = len(rows)
    n = len(labels)

    # altezza proporzionale al numero di barre, entro limiti tipografici
    h = max(2.5, min(6.4, 0.34 * n * nrows + 1.25 + (0.5 if legend_lines else 0)))
    fig, ax = plt.subplots(figsize=(6.6, h), dpi=118)
    _fondo(fig)
    ax.set_facecolor('none')
    ax.set_zorder(2)
    ax.patch.set_alpha(0)

    allv = [v for _, vv in rows for v in vv] or [0]
    vmax = max(allv) or 1

    ypos = np.arange(n)[::-1].astype(float)      # prima etichetta in alto
    bh = 0.72 / nrows                             # 2px di respiro fra barre adiacenti

    for ri, (rlab, vals) in enumerate(rows):
        off = (ri - (nrows - 1) / 2) * bh
        if colors is not None:
            cs = colors
        elif nrows > 1:
            cs = [PAL8[(rot + ri) % len(PAL8)]] * len(vals)
        else:
            cs = [NAVY] * len(vals)
        ax.barh(ypos + off, vals, height=bh * 0.92, color=cs,
                edgecolor='white', linewidth=0.6, zorder=3,
                label=rlab or None)
        for y, v in zip(ypos + off, vals):
            if v == 0:
                continue
            ax.text(v + vmax * 0.014, y, _fmt(v, value_fmt),
                    va='center', ha='left', fontsize=7.0, color=INK, zorder=4)

    ax.set_yticks(ypos)
    ax.set_yticklabels(labels, fontsize=7.6, color=INK)
    ax.set_xlim(0, vmax * 1.17)
    ax.set_ylim(-0.8, n - 0.2)
    ax.set_xlabel(zlabel, fontsize=8, color=MUT, labelpad=4)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(nbins=6, steps=[1, 2, 2.5, 5, 10]))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(
        lambda v, _: (f'{int(round(v)):,}' if abs(v - round(v)) < 1e-9
                      else f'{v:,.1f}').replace(',', '@').replace('.', ',').replace('@', '.')))
    ax.tick_params(axis='x', labelsize=7.0, colors=MUT, length=0)
    ax.tick_params(axis='y', length=0)
    ax.xaxis.grid(True, color='#d9d3c6', linewidth=0.7, zorder=1)
    ax.set_axisbelow(True)
    for side in ('top', 'right', 'bottom'):
        ax.spines[side].set_visible(False)
    ax.spines['left'].set_color('#c9ccd2')
    ax.spines['left'].set_linewidth(0.8)
    ax.set_title(title, fontsize=11.5, color=NAVY, fontweight='bold', loc='left', pad=9)
    if nrows > 1:
        ax.legend(fontsize=7.0, frameon=False, loc='lower right', labelcolor=INK)
    if legend_lines:
        fig.text(0.012, 0.012, '\n'.join(legend_lines), fontsize=6.4, color=MUT, va='bottom')
        fig.subplots_adjust(left=0.30, right=0.985, top=0.895,
                            bottom=0.10 + 0.030 * len(legend_lines))
    else:
        fig.subplots_adjust(left=0.30, right=0.985, top=0.895, bottom=0.13)
    fig.savefig(os.path.join(FIGS, out))
    plt.close(fig)


manifest = {}

def add(idx, out, caption):
    manifest.setdefault(str(idx), []).append({'file': 'figs/' + out, 'caption': caption})

def wc(t):
    return len(t.split())

def url_count(t):
    return len(re.findall(r'https?://', t))


def _n(x):
    """Numero con il punto come separatore delle migliaia."""
    return f'{x:,}'.replace(',', '.')

def _sez(n):
    return '1 sezione' if n == 1 else f'{n} sezioni'

def _pulisci(t):
    return t.rstrip(' .·—-')

# ---------- grafici strutturali per ogni capitolo ----------
for idx, (label, path) in enumerate(PARTS):
    md = load(path)
    secs = sections(md)
    codes = [_pulisci(clean_title(t, 30)) or f'§{i+1}'
             for i, (t, _) in enumerate(secs)]
    words = [wc(t) for _, t in secs]
    legend = None   # le barre orizzontali portano il nome della sezione: la legenda sarebbe un doppione
    n = (idx, path)
    bar3d(codes, words, f'{label} — Le parole per sezione', 'parole',
          f'fig_{idx:02d}_a.png', legend_lines=legend, rot=idx % 8)
    _tw = sum(words); _ns = len(secs)
    _mi = words.index(max(words)) if words else 0
    _mt = _pulisci(clean_title(secs[_mi][0], 46)) if secs else ''
    add(idx, f'fig_{idx:02d}_a.png',
        f'{label}: {_n(_tw)} parole in {_sez(_ns)}; la più ampia è §{_mi+1} {_mt}, con {_n(max(words))}.')
    urls = [url_count(t) for _, t in secs]
    if sum(urls) >= 5:
        bar3d(codes, urls, f'{label} — I rinvii alle fonti per sezione', 'indirizzi citati',
              f'fig_{idx:02d}_b.png', legend_lines=legend, rot=(idx + 3) % 8)
        _tu = sum(urls); _su = len([u for u in urls if u])
        add(idx, f'fig_{idx:02d}_b.png',
            f'{label}: {_n(_tu)} indirizzi di fonte citati, addensati in {_sez(_su)} su {len(secs)}.')
    else:
        paras = [len([p for p in t.split('\n\n') if p.strip()]) for _, t in secs]
        bar3d(codes, paras, f'{label} — I paragrafi per sezione', 'paragrafi',
              f'fig_{idx:02d}_b.png', legend_lines=legend, rot=(idx + 3) % 8)
        _tp = sum(paras); _av = round(_tp/len(paras)) if paras else 0
        add(idx, f'fig_{idx:02d}_b.png',
            f'{label}: {_n(_tp)} paragrafi in {_sez(len(secs))}, {_av} in media per sezione.')

# ---------- grafici curati sui dati verificati ----------
# Portale (0): la quadriga in blocchi
bar3d(['Manuale', 'Agenda', 'Nove\ncantieri', 'Il codice\n(Kissinger)', 'Il meridiano\ne la valle'], [400, 300, 1000, 1000, 1000],
      'Le opere a blocchi mirati — blocchi per opera', 'blocchi',
      'fig_00_c.png')
add(IDX_PORTALE, 'fig_00_c.png', 'Le cinque opere a blocchi (il programma ne è il telaio): 3.700 blocchi mirati coordinati.')

# Metodologie (19): centralità di intermediazione
bar3d(['BR', 'CPM', 'Simioni', 'Moretti'], [426.7, 241.3, 220.0, 202.9],
      'La rete documentata — centralità di intermediazione (primi 4 nodi)', 'betweenness',
      'fig_19_c.png', value_fmt='{:.1f}')
add(IDX_METOD, 'fig_19_c.png', 'Le metriche calcolate sulla rete dei documenti (39 nodi, 59 archi): misurano documentazione, mai colpe.')

# Programma (27): punteggi piste PN e PE, due grafici
bar3d(['PN-1', 'PN-7', 'PN-4', 'PN-2', 'PN-5', 'PN-3', 'PN-8', 'PN-6'],
      [89.0, 77.5, 74.5, 71.0, 67.5, 67.5, 52.5, 50.5],
      'Le piste operative — graduatoria a punteggio (0,1–100)', 'punteggio MCDA',
      'fig_27_c.png', value_fmt='{:.1f}',
      legend_lines=['PN-1 terze presenze · PN-7 testimoni viventi · PN-4 fonte di «Gradoli» · PN-2 caricatore · PN-5 fondo Renzi · PN-3 seduta · PN-8 archivi · PN-6 vaglio negativo',
                    'Escluso il comparto BR e Superclan. I punteggi ordinano atti istruttori, mai persone.'])
add(IDX_PROGRAMMA, 'fig_27_c.png', 'Il modello MCDA dichiarato (rendimento 30% · diagnosticità 25% · fattibilità 20% · urgenza 15% · indipendenza 10%).')
bar3d(['PE-1', 'PE-3', 'PE-2', 'PE-6', 'PE-5', 'PE-4'],
      [74.5, 74.5, 67.5, 61.0, 59.5, 54.0],
      'Le piste su entità e strutture — graduatoria a punteggio', 'punteggio MCDA',
      'fig_27_d.png', value_fmt='{:.1f}',
      legend_lines=['PE-1 comitati del Viminale · PE-3 i trenta giorni di via Gradoli · PE-2 il condominio · PE-6 registro delle segnalazioni · PE-5 gli alleati · PE-4 la mediazione vaticana'])
add(IDX_PROGRAMMA, 'fig_27_d.png', 'Le sei entità con punteggio: ogni pista ha per esito un documento, non un colpevole.')

# Piste di testa (28): i 91 bossoli
bar3d(['FNAB-43 unico\n(perizia 1978,\nconf. 2015)', 'secondo mitra\n(declassati C\nnel 2015)', 'altre armi'],
      [49, 22, 20], 'I 91 bossoli di via Fani per attribuzione peritale', 'bossoli',
      'fig_28_c.png')
add(IDX_PISTE, 'fig_28_c.png', 'La sequenza peritale 1978–1993–2015: la conferma dei 49, la declassificazione dei 22 a esito non conclusivo.')

# Entita' (29): la macchina delle ricerche — scala lineare, perche' la sproporzione e' il dato
bar3d(['persone controllate', 'veicoli controllati', 'posti di blocco', 'perquisizioni'],
      [6413713, 3383123, 72460, 37702],
      "La macchina delle ricerche dei 55 giorni — l'output documentato", 'atti registrati',
      'fig_29_c.png',
      legend_lines=["Scala lineare: la sproporzione fra i quattro output è essa stessa il dato.",
                    "La colonna d'ingresso — le segnalazioni ricevute — non fu mai prodotta: è il quesito 7 dell'agenda."])
add(IDX_ENTITA, 'fig_29_c.png', "Le quattro colonne d'uscita documentate della macchina; l'ingresso mai misurato (scheda PE-6).")

# Entita': la quota romana dello spiegamento — dove il prigioniero effettivamente era
_SPIEG = [('persone controllate', 6413713, 167409),
          ('autoveicoli ispezionati', 3383123, 96572),
          ('posti di blocco', 72460, 6296),
          ('perquisizioni domiciliari', 37702, 6933)]
bar3d([n for n, _, _ in _SPIEG], [100.0 * r / t for _, t, r in _SPIEG],
      "La quota romana dello spiegamento — percentuale sul totale nazionale", 'per cento del totale',
      'fig_29_d.png', value_fmt='{:.1f}',
      legend_lines=["Roma è la città in cui il prigioniero fu tenuto per l'intera durata del sequestro.",
                    "Su 6.413.713 persone controllate in Italia, 167.409 lo furono a Roma: il 2,6 per cento.",
                    "La ripartizione è un dato ufficiale registrato; la sua interpretazione non è compito di un grafico."])
add(IDX_ENTITA, 'fig_29_d.png',
    "Lo sforzo nazionale e la sua quota romana: le perquisizioni domiciliari sono la sola voce in cui Roma pesa oltre un decimo.")

# Entita': l'intensita' giornaliera sui 55 giorni
bar3d([n for n, _, _ in _SPIEG], [t / 55 for _, t, _ in _SPIEG],
      "L'intensità giornaliera — media sui 55 giorni di prigionia", 'atti al giorno',
      'fig_29_e.png',
      legend_lines=["Media aritmetica sui 55 giorni fra il 16 marzo e il 9 maggio 1978: il ritmo reale variò.",
                    "Centosedicimila persone controllate al giorno, e il covo di via Montalcini non fu individuato."])
add(IDX_ENTITA, 'fig_29_e.png',
    "Lo stesso spiegamento diviso per i giorni che durò: la misura dello sforzo quotidiano, non del suo esito.")

# Manuale (30): blocchi per serie
bar3d(['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV'],
      [20,25,45,50,30,40,25,15,30,20,30,25,20,16,9],
      'Il manuale — blocchi per serie (400 in quindici serie)', 'blocchi',
      'fig_30_c.png',
      legend_lines=['I principi · II architettura · III reperti · IV archivi · V persone · VI ACH · VII registro segnalazioni · VIII internazionale',
                    'IX errori e antidoti · X cronoprogramma · XI cantiere digitale · XII strumenti giuridici · XIII qualità · XIV raccordo · XV contingenze'])
add(IDX_MANUALE, 'fig_30_c.png', 'Le quindici serie della seconda edizione accresciuta: 300 della prima edizione, 100 della seconda.')

# Agenda (31): blocchi per serie
bar3d(['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'],
      [15,30,25,30,25,30,25,30,25,25,20,20],
      "L'agenda — blocchi per serie (300 in dodici serie)", 'blocchi',
      'fig_31_c.png',
      legend_lines=['I quesiti · II Direttiva · III parlamentari · IV reperti · V persone · VI internazionali',
                    'VII carte private · VIII scienze · IX smentite · X cronologie e registri · XI raccordi · XII governo'])
add(IDX_AGENDA, 'fig_31_c.png', 'Le dodici serie dell’agenda: ogni blocco un bersaglio, mai un’affermazione.')

# Cantieri (32): blocchi per Parte
bar3d(['I\nUK-FR-DE','II\nVaticano','III\nfondi','IV\nreperti','V\nmemoriale','VI\naudio-foto','VII\nscienze','VIII\nregistro','IX\nRoma'],
      [120,100,110,130,100,100,130,90,120],
      'I nove cantieri — blocchi per Parte (1.000 in nove Parti)', 'blocchi',
      'fig_32_c.png')
add(IDX_CANTIERI, 'fig_32_c.png', 'I nove fronti dell’opera monumentale, con le due campagne di verifica (V-1…V-12, C-1…C-9).')

# Kissinger (33): blocchi per serie e per statuto del ponte
_kc_path = os.path.join(SP, 'kiss_counts.json')
_KORD = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII']
_KDES = [60, 75, 70, 85, 100, 95, 75, 70, 85, 70, 65, 90, 60]
if os.path.exists(_kc_path):
    _kc = json.load(open(_kc_path))
    _KVAL = [int(_kc.get(k, 0)) for k in _KORD]
else:
    _KVAL = _KDES
bar3d(_KORD, _KVAL,
      "Il codice e la sua trasmissione \u2014 blocchi per serie (%s in tredici serie)" % f'{sum(_KVAL):,}'.replace(',', '.'),
      'blocchi', 'fig_33_c.png', rot=3,
      legend_lines=['I il nome e la mutazione \u00b7 II il genoma dichiarato \u00b7 III l\u2019ereditariet\u00e0 dottrinale \u00b7 IV la trascrizione \u00b7 V l\u2019espressione differenziale',
                    'VI omologia e analogia \u00b7 VII il vettore \u00b7 VIII la mutazione e il falso \u00b7 IX il DNA non codificante \u00b7 X fenotipo e genotipo',
                    'XI l\u2019epigenetica \u00b7 XII la filogenesi del caso Moro \u00b7 XIII il limite della metafora: la colpa non si eredita'])
add(IDX_KISS, 'fig_33_c.png', 'Le tredici serie della triangolazione: ogni blocco un bersaglio d\u2019archivio, mai una sentenza.')

bar3d(['piano 1\nrapporto\ndocumentato', 'piano 2\nconvergenza\nstrutturale', 'piano 3\naffermazione\nterziaria'],
      [1, 2, 3],
      'La regola dei tre piani \u2014 il metro di ogni blocco', 'peso probatorio (ordinale)',
      'fig_33_d.png', colors=[CAT[3], CAT[2], CAT[1]], value_fmt='{:.0f}',
      legend_lines=['Scala ordinale, non quantit\u00e0: un ponte \u00e8 reale solo al piano 1.',
                    'I piani 2 e 3 si registrano come tali e non si promuovono mai a nesso causale.'])
add(IDX_KISS, 'fig_33_d.png', 'Il metro dichiarato in apertura: la contemporaneit\u00e0 non \u00e8 prova di nesso, l\u2019appartenenza non \u00e8 prova di condotta.')

# Kissinger, seconda campagna: i gruppi territoriali e la distribuzione misurata dei piani
_kp = os.path.join(REPO, 'kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md')
if os.path.exists(_kp):
    _kt = open(_kp, encoding='utf-8').read()
    _kb = re.findall(r'^\*\*(\d+) \u00b7 (.+?)\.\*\* (.+)$', _kt, re.M)
    if len(_kb) > 1200:
        _GR = [('I-XIII\nconcettuale', 1, 1000),
               ('XIV-XXVI\nnarrativo', 1001, 2000),
               ('XXVII-XXXIX\nmetodo e\nFarnesina', 2001, 3000),
               ('XL-LII\nquadriga', 3001, 4000),
               ('LIII-LXV\ncerniere e\ncensimenti', 4001, 4999)]
        _gv = [sum(1 for b in _kb if a <= int(b[0]) <= z) for _, a, z in _GR]
        bar3d([g for g, _, _ in _GR], _gv,
              'Il codice e la sua trasmissione \u2014 blocchi per gruppo (%s in sessantacinque serie)'
              % f'{sum(_gv):,}'.replace(',', '.'),
              'blocchi', 'fig_33_e.png', rot=4,
              legend_lines=['Prima campagna concettuale (la lente dichiarata); quattro gruppi territoriali della seconda.',
                            'Ogni serie territoriale triangola il nome contro un documento del corpus, letto prima di scriverne.'])
        add(IDX_KISS, 'fig_33_e.png', 'Le due campagne dell\u2019opera: una lente applicata a un nome, e il nome portato contro ogni territorio del corpus.')

        _mis = [
            ('piano 1', r'piano 1\b|piano uno|primo piano|piano primo'),
            ('piano 2', r'piano 2\b|piano due|secondo piano|piano secondo'),
            ('piano 3', r'piano 3\b|piano tre|terzo piano|piano terzo'),
            ('Stato\nZero', r'Stato Zero'),
            ('silenzio\nd\u2019oggetto', r'silenzio d\u2019oggetto|silenzio del testo|perimetro'),
            ('sede o atto\nnominati', r'archiv|fondo|FRUS|NARA|Ford Library|ACS|segnatur|verbal|fascicol|registro'),
        ]
        _mv = [sum(1 for b in _kb if re.search(rx, b[2], re.I)) for _, rx in _mis]
        bar3d([g for g, _ in _mis], _mv,
              'Che cosa dichiarano i %s blocchi \u2014 misura sul testo' % f'{len(_kb):,}'.replace(',', '.'),
              'blocchi che lo dichiarano', 'fig_33_f.png', rot=7,
              legend_lines=['Conteggio meccanico sul testo pubblicato, non stima. Un blocco puo ricadere in piu colonne.',
                            'Un ponte e reale solo al piano 1: le colonne 2 e 3 non si promuovono mai a nesso causale.'])
        add(IDX_KISS, 'fig_33_f.png', 'La contabilita dichiarata dell\u2019opera: quanti ponti reali, quante convergenze, quanti vuoti verbalizzati.')

# Il meridiano e la valle (34): blocchi per serie e ricognizione meccanica sul corpus
_sc_path = os.path.join(SP, 'sa_counts.json')
_SORD = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII']
_SDES = [50, 85, 90, 80, 85, 80, 70, 70, 85, 85, 75, 75, 70]
if os.path.exists(_sc_path):
    _sc = json.load(open(_sc_path))
    _SVAL = [int(_sc.get(k, 0)) for k in _SORD]
else:
    _SVAL = _SDES
bar3d(_SORD, _SVAL,
      "Il meridiano e la valle \u2014 blocchi per serie (%s in tredici serie)" % f'{sum(_SVAL):,}'.replace(',', '.'),
      'blocchi', 'fig_34_c.png', rot=5,
      legend_lines=['I statuto e metodo \u00b7 II anagrafe \u00b7 III la cornice sudafricana \u00b7 IV i lignaggi \u00b7 V le materie prime',
                    "VI embargo e aggiramenti \u00b7 VII le rotte \u00b7 VIII formazione e coscrizione \u00b7 IX la valle \u00b7 X le dottrine",
                    'XI il denaro \u00b7 XII critica delle fonti \u00b7 XIII il limite: la colpa non si eredita'])
add(IDX_SA, 'fig_34_c.png', 'Le tredici serie del Libro quattordicesimo: ogni blocco un bersaglio d\u2019archivio, e ogni serie i propri bersagli di smentita.')

# ricognizione meccanica: quanto di questo Libro esisteva gia nel resto del corpus
bar3d(['Musk', 'Thiel', 'Botha', 'PayPal', 'Silicon\nValley', 'Namibia', 'Sud\nAfrica', 'apartheid'],
      [0, 0, 0, 0, 0, 0, 0, 2],
      'Quanto di questo Libro esisteva gi\u00e0 nel corpus \u2014 occorrenze negli altri Libri',
      'documenti che contengono il termine', 'fig_34_d.png', rot=1, value_fmt='{:.0f}',
      legend_lines=['Ricognizione meccanica su tutti i documenti del branch, esclusi questo Libro e i file di servizio.',
                    "Unico esito non nullo: \u00abapartheid\u00bb, di cui una occorrenza \u00e8 il nodo consolidato E-16 della",
                    'triangolazione Guevara-Moro \u2014 il discorso alle Nazioni Unite dell\u201911 dicembre 1964.'])
add(IDX_SA, 'fig_34_d.png', 'Lo Stato Zero reso visibile: il Libro quattordicesimo apre un fronte nuovo, e il solo ponte documentato col corpus \u00e8 un atto del 1964.')

# Fase decima (22): stati del registro + decessi cumulati
bar3d(['deceduti', 'viventi\nin Italia', 'oltre\nconfine'], [5, 6, 2],
      'Il registro del giudicato — gli stati documentati dei tredici', 'persone',
      'fig_22_c.png', colors=[CAT[1], CAT[0], CAT[2]],
      legend_lines=['Stati verificati con fonti (campagna C-8): decessi 2001, 2013, 2024, 2025, 2025.'])
add(IDX_DECIMA, 'fig_22_c.png', 'I tredici del registro per stato documentato: il tempo stringe la finestra della parola (priorità biologica).')
bar3d(['2001', '2013', '2024', '2025'], [1, 2, 3, 5],
      'I decessi documentati del registro — cumulato per anno', 'deceduti (cumulato)',
      'fig_22_d.png',
      legend_lines=['2001 Maccari · 2013 Gallinari · 2024 Balzerani · 2025 Morucci e Braghetti.'])
add(IDX_DECIMA, 'fig_22_d.png', 'La curva che si accelera: ogni scheda vivente del registro lavora contro questo grafico.')


# ---------- apparato delle note bibliografiche (parte 35) ----------
_ns_path = os.path.join(SP, 'note_stats.json')
if os.path.exists(_ns_path):
    ns = json.load(open(_ns_path))
    ROM = ['primo','secondo','terzo','quarto','quinto','sesto','settimo','ottavo','nono',
           'decimo','undicesimo','dodicesimo','tredicesimo']
    SIG = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII']
    groups = [('Portale', [i for i,(l,_) in enumerate(PARTS) if l.startswith('Portale')])]
    for r, s in zip(ROM, SIG):
        idxs = [i for i,(l,_) in enumerate(PARTS) if l.startswith('Libro ' + r)]
        if idxs:
            groups.append((s, idxs))
    groups.append(('App.', [i for i,(l,_) in enumerate(PARTS) if l.startswith('Appendice')]))
    gl = [g0 for g0,_ in groups]
    gv = [sum(ns['per_part_new'][i] for i in idxs) for _,idxs in groups]
    bar3d(gl, gv, 'Le note bibliografiche — indirizzi nuovi per Libro', 'indirizzi (prima citazione)',
          'fig_note_a.png', rot=2,
          legend_lines=['Portale e dodici Libri con le Appendici; ogni indirizzo contato nel Libro della sua prima citazione.'])
    add(IDX_APPARATO, 'fig_note_a.png', f"La distribuzione delle {ns['distinct']} note bibliografiche lungo l'opera, per Libro di prima citazione.")
    td = ns['top_domains'][:8]
    bar3d([d.replace('www.','') for d,_ in td], [c for _,c in td],
          'Le note bibliografiche — i domini piu citati', 'indirizzi distinti',
          'fig_note_b.png', rot=6)
    add(IDX_APPARATO, 'fig_note_b.png', f"I domini piu ricorrenti fra i {ns['distinct']} indirizzi citati ({ns['tot_occ']} citazioni complessive).")


# Dossier maggiore: gli elenchi di Castiglion Fibocchi — composizione certificata
bar3d(['nominativi negli elenchi', 'parlamentari in carica',
       'vertici dei servizi informativi', 'ministri in carica'],
      [962, 44, 3, 3],
      'Gli elenchi sequestrati il 17 marzo 1981 — le sole voci quantificate',
      'persone', 'fig_p2_a.png',
      legend_lines=[
        'Le uniche cifre esatte che il corpus registra. Le altre categorie vi compaiono senza numero',
        'e non sono disegnate: ufficiali generali e superiori, magistrati, prefetti, diplomatici,',
        "il comandante generale della Guardia di Finanza, il gruppo dirigente del maggior quotidiano.",
        "L'appartenenza a un elenco non è prova di condotta: è la terza regola dell'opera."])
add(IDX_DOSSIER, 'fig_p2_a.png',
    'La composizione quantificata degli elenchi: 962 nominativi, di cui 44 parlamentari e 3 ministri in carica. Le categorie senza cifra non sono rappresentate.')

# Dossier maggiore: la distanza fra il sequestro Moro e la scoperta degli elenchi
bar3d(['dal sequestro Moro\nagli elenchi', 'dalla morte di Moro\nagli elenchi',
       'durata della prigionia'],
      [1097, 1043, 55],
      'La cronologia, in giorni — la lista è posteriore ai fatti',
      'giorni', 'fig_p2_b.png',
      legend_lines=[
        '16 marzo 1978 via Fani · 9 maggio 1978 la morte · 17 marzo 1981 il sequestro degli elenchi.',
        'Nel 1978 la composizione della loggia non era un oggetto conoscibile: fu rivelata tre anni dopo.',
        'Perciò il corpus non può dire chi vi fosse iscritto durante i 55 giorni, ma solo chi vi risultava nel 1981.'])
add(IDX_DOSSIER, 'fig_p2_b.png',
    'Tre anni e un giorno separano via Fani dal sequestro degli elenchi: la finestra dei 55 giorni non è documentabile con una lista del 1981.')


# Dossier maggiore: dove il corpus ha materia, nella finestra dei sei mesi
_MESI = [('settembre 1977', 3), ('ottobre 1977', 6), ('novembre 1977', 8), ('dicembre 1977', 1),
         ('gennaio 1978', 5), ('febbraio 1978', 7), ('marzo 1978', 63), ('aprile 1978', 48),
         ('maggio 1978', 50), ('giugno 1978', 3), ('luglio 1978', 3), ('agosto 1978', 5),
         ('settembre 1978', 16), ('ottobre 1978', 7), ('novembre 1978', 0)]
bar3d([n for n, _ in _MESI], [v for _, v in _MESI],
      'Dove il corpus ha materia — date documentate per mese',
      'occorrenze datate nel corpus', 'fig_p2_c.png',
      legend_lines=[
        'Conteggio meccanico delle date esplicite nei documenti del corpus, da settembre 1977 a novembre 1978.',
        'Dei 225 riferimenti datati della finestra, 161 — il 72 per cento — cadono nei tre mesi del sequestro.',
        'Misura quanto il corpus parla di ciascun mese, non quanto in quel mese accadde: è una misura',
        "della documentazione disponibile, e il vuoto ai due estremi è esso stesso un dato da registrare."])
add(IDX_DOSSIER, 'fig_p2_c.png',
    'La finestra dei sei mesi, misurata: la documentazione si addensa sui 55 giorni e si dirada prima e dopo. Novembre 1978 non ha una sola data.')


# ---- Appendice III: i nove grafici della verifica, generati a parte ----
# Le immagini nascono da gen_verifica_p2.py, che le compone nello stesso stile.
# Qui vengono soltanto portate in figs/ e iscritte nel manifesto, cosi' che una
# sola sorgente le produca e non esistano due versioni divergenti.
import shutil
IDX_VERIFICA = idx_di('_verifiche/verifica-elenco-trentatre-nomi-p2.md')
_VER = os.path.join(SP, 'grafici-verifica-p2')
_DIDA = [
 ('1_imbuto-della-verificabilita.png',
  "I quattro campi della tabella verificata e quanti nomi reggono in ciascuno: trentatré nomi, trentatré ruoli verificabili, venti appartenenze corroborate, nessun numero di tessera."),
 ('2_tessere-sotto-la-soglia-documentata.png',
  "Quattro dei trentatré valori dichiarati come numero di tessera cadono sotto il 1.600, soglia verbalizzata negli atti della Commissione; un quinto vi si posa esatto."),
 ('3_i-trentatre-per-sede-istituzionale.png',
  "Ripartizione delle trentatré righe per sede istituzionale attribuita nel 1978: quindici nei servizi informativi, ventidue in apparati che rispondono all'esecutivo."),
 ('4_composizione-documentata-dei-962.png',
  "La composizione degli elenchi secondo le fonti sui lavori della Commissione Anselmi, con l'annotazione sulla cifra dei parlamentari registrata nel Libro quarto."),
 ('5_distanza-fra-i-fatti-e-la-prova.png',
  "Quattrocentodiciannove giorni la finestra richiesta, 1.097 dai fatti al sequestro degli elenchi, 2.310 dai fatti al deposito della relazione di maggioranza."),
 ('6_finestra-sei-mesi-materia-disponibile.png',
  "La finestra dei sei mesi misurata sul corpus: la documentazione si addensa sui tre mesi del sequestro e si dirada ai due estremi."),
 ('7_quota-dei-trentatre-sul-totale.png',
  "Le sole percentuali sui 962 che i dati consentano di calcolare: 3,43 per cento i nomi asseriti, 2,08 quelli con appartenenza corroborata, zero quelli con un numero verificato."),
 ('8_date-di-affiliazione-disponibili.png',
  "Il campo che il calcolo per finestra temporale richiederebbe: due righe su trentatré portano una data di affiliazione, una sola è collocabile in un mese preciso."),
 ('9_finestra-e-i-due-dati-datati.png',
  "I quattrocentodiciannove giorni della finestra, con i cinquantacinque della prigionia in evidenza, e i due soli dati datati della tabella verificata."),
]
_mancanti = [n for n, _ in _DIDA if not os.path.exists(os.path.join(_VER, n))]
if _mancanti:
    raise SystemExit('gen_figs: mancano i grafici della verifica: ' + ', '.join(_mancanti))
for _nome, _dida in _DIDA:
    shutil.copyfile(os.path.join(_VER, _nome), os.path.join(FIGS, _nome))
    add(IDX_VERIFICA, _nome, _dida)

json.dump(manifest, open(os.path.join(SP, 'figs_manifest.json'), 'w'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in manifest.values())
print(f'grafici generati: {tot} | capitoli coperti: {len(manifest)} | min per capitolo: {min(len(v) for v in manifest.values())}')
