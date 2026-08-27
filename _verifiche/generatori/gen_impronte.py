# -*- coding: utf-8 -*-
"""Registro delle impronte SHA-256 di tutta l'opera: ogni file versionato,
piu' il pacchetto dei grafici che vive fuori dal repository."""
import hashlib, json, os, subprocess

REPO = '/home/user/collegi-italia'
SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
GRAF = os.path.join(SP, 'grafici-verifica-p2')

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for blocco in iter(lambda: f.read(1 << 20), b''):
            h.update(blocco)
    return h.hexdigest()

def _n(x):
    return f'{x:,}'.replace(',', '.')

def _peso(b):
    if b >= 1 << 20:
        return f'{b / (1 << 20):.1f}'.replace('.', ',') + ' MB'
    if b >= 1 << 10:
        return f'{b / (1 << 10):.0f} kB'
    return f'{b} B'

def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True).stdout

COMMIT = git('rev-parse', 'HEAD').strip()
RAMO = git('rev-parse', '--abbrev-ref', 'HEAD').strip()

# Ogni file versionato, escluse le dipendenze di terze parti: non sono opera.
# Il registro non può certificare sé stesso: i suoi due file cambiano a ogni
# rigenerazione, e la loro impronta sarebbe falsa nell'istante in cui è scritta.
# Restano fuori dal manifesto, ed e' dichiarato nel registro.
AUTOREFERENTI = {'IMPRONTE-SHA256.md', 'IMPRONTE-SHA256.txt',
                 'IMPRONTE-OPERA-MORO.txt', 'IMPRONTE-ITALIA-NERA.txt'}
TRACCIATI = [f for f in git('ls-files').split('\n')
             if f and not f.startswith('node_modules/') and f not in AUTOREFERENTI]

# I volumi rilegati stanno in radice e portano l'opera fuori dal repository.
VOLUMI = sorted(f for f in TRACCIATI
                if '/' not in f and f.endswith(('.pdf', '.docx')))
_vol = set(VOLUMI)

# --------------------------------------------------------- il perimetro
# Il repository ospita due lavori distinti, e il corpus lo dichiara da sé:
# INDICE-DOCUMENTI-BRANCH lo scrive alla terza riga — i documenti del caso Moro
# sono «estranei al progetto principale del repository (Studio Integrale
# Puglia)». Le impronte valgono per entrambi; l'attribuzione no, e tenerle
# insieme sotto un'unica intestazione sarebbe un errore di descrizione.
ALTRA_OPERA_DIR = ('_meta/', '_diffusione/', '_pubblicazione-finale/',
                   '_livelli-piramide/', '_paper-accademico/',
                   'tomo-1-puglia/', 'tomo-2-nazionale/', 'ue-27/')
ALTRA_OPERA_FILE = {'README.md', '.gitignore'}

# La terza opera: Italia Nera. Non e' una parte dell'opera su Moro e non e' lo
# Studio Puglia. Il legame col caso Moro e' genealogico e non testuale — misurato
# agli 8-grammi, il corpus moroteano tocca il Registro V77 per lo 0,77 per cento —
# e contarla dentro l'opera ripeterebbe, alla lettera, l'errore di attribuzione
# corretto il 27 agosto: cifre esatte sotto un'intestazione sbagliata.
TERZA_OPERA_DIR = ('italia-nera/',)

def _altra(f):
    return f.startswith(ALTRA_OPERA_DIR) or f in ALTRA_OPERA_FILE

def _terza(f):
    return f.startswith(TERZA_OPERA_DIR)

# ------------------------------------------------- le sezioni del registro
def _sezione(f):
    if _terza(f):
        return 'terza:italia-nera'
    if _altra(f):
        return 'altra:' + (f.split('/', 1)[0] if '/' in f else '(radice)')
    if f in _vol:
        return 'volumi'
    if '/' not in f:
        return 'corpus'
    return f.split('/', 1)[0]

ETICHETTE = [
 ('volumi',                "I volumi rilegati",
  "Le edizioni tipografiche in DOCX e PDF: è la forma in cui l'opera viaggia fuori dal repository."),
 ('corpus',                "I documenti del corpus",
  "Le sorgenti in markdown del Portale, dei quattordici Libri e delle tre Appendici, con gli indici e gli apparati."),
 ('moro-ministro-esteri',  "Il Libro dodicesimo e i suoi originali",
  "La dimensione diplomatica: le ricognizioni Farnesina per esteso, i documenti State Dept, l'edizione HTML navigabile."),
 ('appendici-fase-settima', "Le appendici alla Fase settima",
  "Le undici appendici al Libro nono, dalla quinta alla quindicesima: la serie chiusa."),
 ('_verifiche',            "Le verifiche e i generatori",
  "Le schede di verifica e gli script che ricompongono l'opera, i grafici, le note e questo stesso registro."),
 ('_meta',                 "L'apparato editoriale",
  "I tracker di lavorazione, il registro delle anomalie, il parcheggio delle decisioni sospese."),
 ('_diffusione-opera',     "Il dossier di invio dell'opera",
  "Proposte editoriali, lettere istituzionali, registro dei canali PEC, checklist di spedizione."),
 ('terza:italia-nera',    "Terza opera — Italia Nera",
  "Il Registro V77 e i suoi otto documenti compagni: opera autonoma, imparentata con quella su Moro ma non contenuta in essa."),
 ('altra:(radice)',        "Altro lavoro — la radice",
  "Il README del repository e la configurazione: appartengono allo Studio Integrale Puglia, non all'opera."),
 ('altra:_meta',           "Altro lavoro — apparato e modelli",
  "Tracker di lavorazione, registri di verifica numerica e modelli di analisi economica dello Studio Puglia."),
 ('altra:_diffusione',     "Altro lavoro — diffusione",
  "Destinatari e lettere della campagna dello Studio Puglia."),
 ('altra:_pubblicazione-finale', "Altro lavoro — pubblicazione finale",
  "L'impaginato conclusivo dello Studio Puglia, col proprio indice generale."),
 ('altra:_livelli-piramide', "Altro lavoro — livelli della piramide",
  "Le riduzioni progressive dello Studio Puglia."),
 ('altra:_paper-accademico', "Altro lavoro — paper accademico",
  "La versione accademica dello Studio Puglia, anche in inglese."),
 ('altra:tomo-1-puglia',   "Altro lavoro — Tomo I, Puglia", "Il nucleo regionale dello Studio Puglia."),
 ('altra:tomo-2-nazionale', "Altro lavoro — Tomo II, nazionale", "L'estensione nazionale dello Studio Puglia."),
 ('altra:ue-27',           "Altro lavoro — estensione ai ventisette", "Lo Studio Puglia esteso all'UE-27."),
]

voci = {}
for f in TRACCIATI:
    p = os.path.join(REPO, f)
    if not os.path.exists(p):
        continue
    voci.setdefault(_sezione(f), []).append(
        {'nome': f, 'byte': os.path.getsize(p), 'sha': sha(p)})

# Il pacchetto dei grafici non è versionato: vive nella cartella di lavoro
# e viaggia come zip. Va nel registro lo stesso, perché è materiale pubblicato.
GRAFICI = [{'nome': n, 'byte': os.path.getsize(os.path.join(GRAF, n)),
            'sha': sha(os.path.join(GRAF, n))} for n in sorted(os.listdir(GRAF))]
GRAFICI.append({'nome': 'GRAFICI_VERIFICA_P2.zip',
                'byte': os.path.getsize(os.path.join(SP, 'GRAFICI_VERIFICA_P2.zip')),
                'sha': sha(os.path.join(SP, 'GRAFICI_VERIFICA_P2.zip'))})

SEZIONI = []
for chiave, titolo, riga in ETICHETTE:
    v = sorted(voci.get(chiave, []), key=lambda x: x['nome'])
    if v:
        SEZIONI.append({'chiave': chiave, 'titolo': titolo, 'nota': riga, 'voci': v})
mancanti = set(voci) - {c for c, _, _ in ETICHETTE}
if mancanti:
    raise SystemExit('gen_impronte: sezioni senza etichetta: ' + ', '.join(sorted(mancanti)))

# L'archivio dell'opera intera: e' il pacchetto che si consegna, e non sta nel
# repository perche' duplicherebbe cio' che il repository gia' contiene.
_ARCHIVI = ['OTTANTA_ANNI_SENZA_PACE_OPERA_OMNICOMPRENSIVA.zip',
            'OPERA_INTERA_CASO_MORO.zip',
            'OPERA_INTERA_1-di-2_IL_VOLUME.zip',
            'OPERA_INTERA_2-di-2_TUTTO_IL_RESTO.zip']
_voci_zip = [{'nome': n, 'byte': os.path.getsize(os.path.join(SP, n)),
              'sha': sha(os.path.join(SP, n))}
             for n in _ARCHIVI if os.path.exists(os.path.join(SP, n))]
if _voci_zip:
    SEZIONI.append({'chiave': 'archivio', 'titolo': "Gli archivi dell'opera intera",
                    'nota': "I pacchetti che si consegnano interi. Non sono versionati: duplicherebbero "
                            "cio' che il repository gia' contiene, e non entrano nei totali perche' "
                            "sommarli conterebbe due volte gli stessi file. Sono elencati qui quelli "
                            "che esistono al momento della rigenerazione: un archivio costruito su una "
                            "edizione anteriore non viene ridichiarato, perche' la sua impronta "
                            "resterebbe esatta mentre la descrizione che l'accompagna sarebbe scaduta.",
                    'voci': _voci_zip})

# Le tre parti in cui il volume si divide per passare dal canale di consegna:
# 2.425 pagine pesano 37,5 MiB e il canale ne accetta 30. Le parti non si
# sovrappongono, portano ciascuna la copertina e insieme fanno il volume.
_PARTI = ['OPERA_INTEGRALE_1-di-3_LIBRI_I-XII.pdf',
          'OPERA_INTEGRALE_2-di-3_LIBRI_XIII-XIV.pdf',
          'OPERA_INTEGRALE_3-di-3_LIBRO_XV_E_APPENDICI.pdf']
_voci_parti = [{'nome': n, 'byte': os.path.getsize(os.path.join(SP, n)),
                'sha': sha(os.path.join(SP, n))}
               for n in _PARTI if os.path.exists(os.path.join(SP, n))]
if _voci_parti:
    SEZIONI.append({'chiave': 'parti', 'titolo': "Il volume diviso in tre parti",
                    'nota': "Le 2.425 pagine dell'edizione integrale pesano 37,5 MiB e il canale di "
                            "consegna ne accetta 30: il volume viaggia in tre parti, tagliate su "
                            "confini di Libro e non a caso. La prima porta dal Portale al Libro "
                            "dodicesimo, la seconda i Libri tredicesimo e quattordicesimo, la terza il "
                            "Libro quindicesimo con le quattro Appendici e l'Apparato conclusivo. Ogni "
                            "parte ripete la copertina, cosi' che nessuna arrivi anonima; a parte "
                            "quelle due pagine le tre non si sovrappongono, e la numerazione del "
                            "volume intero e' dichiarata nelle proprieta' di ciascun file. Non entrano "
                            "nei totali: sono lo stesso volume, tagliato.",
                    'voci': _voci_parti})

SEZIONI.append({'chiave': 'grafici', 'titolo': 'Il pacchetto dei grafici',
                'nota': "Le nove infografiche della verifica, la nota di metodo e l'archivio compresso. "
                        "Non sono versionate: viaggiano a parte, e per questo l'impronta conta di più.",
                'voci': GRAFICI})

_conta = [s for s in SEZIONI if s['chiave'] not in ('archivio', 'parti')]
TOT_FILE = sum(len(s['voci']) for s in _conta)
TOT_BYTE = sum(v['byte'] for s in _conta for v in s['voci'])


# =====================================================================
#  Il manifesto: formato sha256sum, e la sua impronta
# =====================================================================
# Il manifesto elenca solo i file versionati, perché è lì che
# `sha256sum --check` sa andarli a cercare partendo dalla radice del repo.
def _manifesto(sezioni):
    return ''.join(f'{v["sha"]}  {v["nome"]}\n'
                   for s in sezioni if s['chiave'] not in ('grafici', 'archivio', 'parti')
                   for v in s['voci'])

# Due manifesti, perche' i lavori sono due e vanno certificati separatamente.
MANIFESTO = _manifesto(SEZIONI)
MAN_OPERA = _manifesto([s for s in SEZIONI
                        if not s['chiave'].startswith(('altra:', 'terza:'))])
MAN_TERZA = _manifesto([s for s in SEZIONI if s['chiave'].startswith('terza:')])
open(os.path.join(REPO, 'IMPRONTE-SHA256.txt'), 'w', encoding='utf-8').write(MANIFESTO)
open(os.path.join(REPO, 'IMPRONTE-OPERA-MORO.txt'), 'w', encoding='utf-8').write(MAN_OPERA)
open(os.path.join(REPO, 'IMPRONTE-ITALIA-NERA.txt'), 'w', encoding='utf-8').write(MAN_TERZA)

# Una stringa sola per tutta l'opera: l'impronta del manifesto. Non e'
# ricorsiva — il manifesto non contiene se stesso — ed e' riproducibile
# da chiunque con `sha256sum IMPRONTE-SHA256.txt`.
OPERA = hashlib.sha256(MAN_OPERA.encode('utf-8')).hexdigest()
TERZA = hashlib.sha256(MAN_TERZA.encode('utf-8')).hexdigest()
INSIEME = hashlib.sha256(MANIFESTO.encode('utf-8')).hexdigest()
N_MANIF = MANIFESTO.count('\n')
N_OPERA = MAN_OPERA.count('\n')
N_TERZA = MAN_TERZA.count('\n')
SEZ_OPERA = [s for s in SEZIONI
              if not s['chiave'].startswith(('altra:', 'terza:'))
              and s['chiave'] not in ('archivio', 'parti')]
FILE_OPERA = sum(len(s['voci']) for s in SEZ_OPERA)
BYTE_OPERA = sum(v['byte'] for s in SEZ_OPERA for v in s['voci'])
SEZ_TERZA = [s for s in SEZIONI if s['chiave'].startswith('terza:')]
FILE_TERZA = sum(len(s['voci']) for s in SEZ_TERZA)
BYTE_TERZA = sum(v['byte'] for s in SEZ_TERZA for v in s['voci'])

json.dump({'sezioni': SEZIONI, 'commit': COMMIT, 'ramo': RAMO,
           'opera': OPERA, 'insieme': INSIEME, 'terza': TERZA,
           'tot_file': TOT_FILE, 'tot_byte': TOT_BYTE,
           'file_opera': FILE_OPERA, 'byte_opera': BYTE_OPERA,
           'file_terza': FILE_TERZA, 'byte_terza': BYTE_TERZA,
           'n_manifesto': N_MANIF, 'n_opera': N_OPERA, 'n_terza': N_TERZA},
          open(os.path.join(SP, 'impronte.json'), 'w'), ensure_ascii=False, indent=1)


# =====================================================================
#  Il registro in markdown
# =====================================================================
def righe_md(voci):
    return '\n'.join(f'| `{v["nome"]}` | {_n(v["byte"])} | `{v["sha"]}` |' for v in voci)

TESTA = '| File | Byte | SHA-256 |\n|---|---:|---|'

corpo = '\n\n'.join(
    f"### {s['titolo']}\n\n*{s['nota']}*\n\n"
    f"{len(s['voci'])} file · {_n(sum(v['byte'] for v in s['voci']))} byte\n\n"
    f"{TESTA}\n{righe_md(s['voci'])}"
    for s in SEZIONI)

sommario = '\n'.join(
    f"| {s['titolo']} | {len(s['voci'])} | {_n(sum(v['byte'] for v in s['voci']))} |"
    for s in SEZIONI)

MD = f'''# Registro delle impronte SHA-256

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file porta qui la propria impronta crittografica. Chi ne riceve uno può
accertare in un comando che è **bit per bit** quello depositato, e non una copia
alterata, troncata o rimontata.

**Stato al commit `{COMMIT[:12]}`** del ramo `{RAMO}`.

---

## Tre lavori, non uno

Il repository ospita **tre opere distinte**, e vanno tenute separate anche qui.
Il corpus lo dichiara già per conto proprio: `INDICE-DOCUMENTI-BRANCH.md` scrive
alla terza riga che i documenti del caso Moro sono «estranei al progetto
principale del repository (Studio Integrale Puglia)».

| | file | byte |
|---|---:|---:|
| **L'opera — il caso Moro** | {_n(FILE_OPERA)} | {_n(BYTE_OPERA)} |
| Terza opera — Italia Nera | {_n(FILE_TERZA)} | {_n(BYTE_TERZA)} |
| Altro lavoro — Studio Integrale Puglia | {_n(TOT_FILE - FILE_OPERA - FILE_TERZA)} | {_n(TOT_BYTE - BYTE_OPERA - BYTE_TERZA)} |
| **Totale nel repository** | {_n(TOT_FILE)} | {_n(TOT_BYTE)} |

Le impronte valgono per tutte e tre, perché tutte e tre stanno nel repository e
chiunque le riceva ha diritto di verificarle. **L'attribuzione no**: contarle
insieme sotto un'unica intestazione sarebbe un errore di descrizione, e in
un'opera che misura la distanza fra un fatto e la sua attribuzione sarebbe
l'errore peggiore da commettere.

*Annotazione — La prima stesura di questo registro, del 27 agosto 2026,
presentava i 209 file come se fossero un'opera sola. La cifra era esatta, la
descrizione no. L'errore è corretto qui e annotato, non cancellato: le impronte
di allora restano valide, l'intestazione che le raccoglieva era sbagliata.*

*Seconda annotazione, stessa data — La correzione parlava di **due** lavori. Con
l'archiviazione di Italia Nera i lavori sono diventati **tre**, e questa
intestazione è stata estesa di conseguenza. Non è una smentita della prima
annotazione: è lo stesso criterio applicato a un perimetro che si è allargato.
Il legame fra Italia Nera e l'opera su Moro è dichiarato dalla parte
moroteana — «Questa opera nasce dal Registro V77 e ne è la seconda figlia» — ed
è **genealogico, non testuale**: misurato agli 8-grammi, l'opera seconda sui
cinquantacinque giorni sta dentro il V77 per lo **0,5 per cento**, e il V77 tocca
l'intero corpus moroteano per lo **0,77**. Una parentela non è un'appartenenza,
e qui la differenza si conta.*

---

## L'impronta dell'opera

Una stringa sola per il caso Moro. È l'impronta del manifesto dell'opera, cioè
del file che elenca i {_n(N_OPERA)} file versionati che le appartengono:

```
{OPERA}
```

Riproducibile da chiunque, in un comando:

```
sha256sum IMPRONTE-OPERA-MORO.txt
```

## L'impronta della terza opera

La stessa cosa per Italia Nera e i suoi {_n(N_TERZA)} file:

```
{TERZA}
```

```
sha256sum IMPRONTE-ITALIA-NERA.txt
```

## L'impronta dell'insieme versionato

La stessa cosa per tutti i {_n(N_MANIF)} file versionati del repository, le tre
opere insieme:

```
{INSIEME}
```

```
sha256sum IMPRONTE-SHA256.txt
```

Se una di queste stringhe coincide, **l'insieme che copre è quello depositato**:
non un file di meno, non un file di più, nessun file diverso. Se differisce, il
confronto riga per riga dice quale.

### I file che restano fuori, e perché

I manifesti elencano ogni file versionato **tranne i manifesti stessi e questo
registro**. Non è una svista, ed è l'unica esclusione. Un registro non può
certificare sé stesso: i suoi file cambiano a ogni rigenerazione, e l'impronta
che vi si scrivesse dentro sarebbe falsa nell'istante in cui viene scritta. La
catena si chiude comunque, e senza circoli: i file sono certificati dal
manifesto, il manifesto è certificato dalla stringa qui sopra, e questo registro
non ha bisogno di esserlo perché **è interamente ricavabile dal manifesto** —
chi vuole controllarlo lo rigenera.

---

## Come si verifica

Tutti i file versionati in un colpo solo, dalla radice del repository:

```
sha256sum --check IMPRONTE-SHA256.txt       # le tre opere
sha256sum --check IMPRONTE-OPERA-MORO.txt   # il solo caso Moro
sha256sum --check IMPRONTE-ITALIA-NERA.txt  # la sola Italia Nera
```

Un file solo, dalla cartella che lo contiene:

```
sha256sum UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf     # Linux
shasum -a 256 UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf # macOS
```

Su Windows, da PowerShell:

```
Get-FileHash UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf -Algorithm SHA256
```

La stringa che compare va confrontata con quella di questo registro. Se coincide,
il file è integro. Se differisce anche per un solo carattere, **non è lo stesso
file**: non va letto come se lo fosse, e va richiesta una copia nuova.

---

## Che cosa l'impronta certifica, e che cosa no

Va detto con precisione, perché è esattamente il genere di distinzione su cui
quest'opera è costruita.

**L'impronta certifica** che il file ricevuto è identico a quello depositato. È una
garanzia sull'**integrità del supporto**: nessuno ha cambiato una cifra, tolto una
pagina, sostituito un allegato.

**L'impronta non certifica** che ciò che il file contiene sia vero. Un documento
falso conserva la propria impronta con la stessa fedeltà di un documento esatto.
L'integrità è una proprietà del contenitore, non del contenuto.

Chi riceve quest'opera deve poter fare due cose distinte: **accertare** di averla
ricevuta integra — e a questo serve il registro — e **verificare** ciò che afferma,
che è invece il lavoro reso possibile dai gradi dichiarati, dalle sedi d'archivio
nominate e dagli Stati Zero. La prima cosa è meccanica. La seconda no.

---

## Il sommario

| Sezione | File | Byte |
|---|---:|---:|
{sommario}
| **Totale** | **{_n(TOT_FILE)}** | **{_n(TOT_BYTE)}** |

---

## Le impronte, sezione per sezione

{corpo}

---

## Il commit, che è un'altra cosa

L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git:

```
{COMMIT}
```

Sono due garanzie diverse e vanno tenute distinte. Il commit fissa **lo stato del
repository** — quali file esistevano e con quale contenuto in quel momento.
L'impronta SHA-256 fissa **il singolo file** anche quando viaggia fuori dal
repository: in allegato a una PEC, su una chiave, dentro un deposito d'archivio.
Un file staccato dal repository perde il commit e conserva l'impronta.

Il pacchetto dei grafici lo mostra bene: non è versionato, quindi non ha commit —
e ha comunque un'impronta.

---

*Le impronte si ricalcolano a ogni nuova edizione. Un registro che non cambia
quando cambiano i file non certifica nulla: va rigenerato con*
`python3 _verifiche/generatori/gen_impronte.py` *e ricommesso insieme all'opera.*
'''

open(os.path.join(REPO, 'IMPRONTE-SHA256.md'), 'w', encoding='utf-8').write(MD)

print(f'sezioni: {len(SEZIONI)} · file totali: {TOT_FILE} · byte: {_n(TOT_BYTE)}')
print(f"  l'opera del caso Moro: {FILE_OPERA} file · {_n(BYTE_OPERA)} byte")
print(f'  Italia Nera: {FILE_TERZA} file · {_n(BYTE_TERZA)} byte · impronta {TERZA[:16]}...')
print(f'  manifesto opera: {N_OPERA} righe · impronta {OPERA[:16]}...')
print(f'  manifesto intero: {N_MANIF} righe · impronta {INSIEME[:16]}...')
for s in SEZIONI:
    print(f"  {len(s['voci']):>3}  {s['titolo']}")
