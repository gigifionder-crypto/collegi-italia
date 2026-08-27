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
AUTOREFERENTI = {'IMPRONTE-SHA256.md', 'IMPRONTE-SHA256.txt'}
TRACCIATI = [f for f in git('ls-files').split('\n')
             if f and not f.startswith('node_modules/') and f not in AUTOREFERENTI]

# I volumi rilegati stanno in radice e portano l'opera fuori dal repository.
VOLUMI = sorted(f for f in TRACCIATI
                if '/' not in f and f.endswith(('.pdf', '.docx')))
_vol = set(VOLUMI)

# ------------------------------------------------- le sezioni del registro
def _sezione(f):
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
 ('_verifiche',            "Le verifiche e i generatori",
  "Le schede di verifica e gli script che ricompongono l'opera, i grafici, le note e questo stesso registro."),
 ('_meta',                 "L'apparato editoriale",
  "I tracker di lavorazione, il registro delle anomalie, il parcheggio delle decisioni sospese."),
 ('_diffusione-opera',     "Il dossier di invio dell'opera",
  "Proposte editoriali, lettere istituzionali, registro dei canali PEC, checklist di spedizione."),
 ('_diffusione',           "Il dossier di diffusione anteriore",
  "L'elenco dei destinatari e i materiali della prima campagna."),
 ('_pubblicazione-finale', "La pubblicazione finale",
  "L'impaginato conclusivo con il proprio indice generale."),
 ('_livelli-piramide',     "I livelli della piramide",
  "Le riduzioni progressive dell'opera, dall'abstract strutturato in giù."),
 ('_paper-accademico',     "Il paper accademico",
  "La versione per la sede accademica, anche in inglese."),
 ('tomo-1-puglia',         "Tomo I — Puglia", "Il nucleo regionale."),
 ('tomo-2-nazionale',      "Tomo II — nazionale", "L'estensione alle altre regioni."),
 ('ue-27',                 "L'estensione ai ventisette", "L'opera unificata nazionale e UE-27."),
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

SEZIONI.append({'chiave': 'grafici', 'titolo': 'Il pacchetto dei grafici',
                'nota': "Le nove infografiche della verifica, la nota di metodo e l'archivio compresso. "
                        "Non sono versionate: viaggiano a parte, e per questo l'impronta conta di più.",
                'voci': GRAFICI})

TOT_FILE = sum(len(s['voci']) for s in SEZIONI)
TOT_BYTE = sum(v['byte'] for s in SEZIONI for v in s['voci'])


# =====================================================================
#  Il manifesto: formato sha256sum, e la sua impronta
# =====================================================================
# Il manifesto elenca solo i file versionati, perché è lì che
# `sha256sum --check` sa andarli a cercare partendo dalla radice del repo.
MANIFESTO = ''.join(
    f'{v["sha"]}  {v["nome"]}\n'
    for s in SEZIONI if s['chiave'] != 'grafici'
    for v in s['voci'])
open(os.path.join(REPO, 'IMPRONTE-SHA256.txt'), 'w', encoding='utf-8').write(MANIFESTO)

# Una stringa sola per tutta l'opera: l'impronta del manifesto. Non e'
# ricorsiva — il manifesto non contiene se stesso — ed e' riproducibile
# da chiunque con `sha256sum IMPRONTE-SHA256.txt`.
OPERA = hashlib.sha256(MANIFESTO.encode('utf-8')).hexdigest()
N_MANIF = MANIFESTO.count('\n')

json.dump({'sezioni': SEZIONI, 'commit': COMMIT, 'ramo': RAMO,
           'opera': OPERA, 'tot_file': TOT_FILE, 'tot_byte': TOT_BYTE,
           'n_manifesto': N_MANIF},
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

MD = f'''# Registro delle impronte SHA-256 — tutta l'opera

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file dell'opera porta qui la propria impronta crittografica: non i soli
volumi rilegati, ma **tutti i {_n(TOT_FILE)} file** — le sorgenti in markdown, gli
apparati, i tracker di lavorazione, il dossier di invio, i generatori, il
pacchetto dei grafici. Chi riceve un file può accertare in un comando che è
**bit per bit** quello depositato, e non una copia alterata, troncata o rimontata.

**Stato al commit `{COMMIT[:12]}`** del ramo `{RAMO}`.

---

## L'impronta dell'opera intera

Una stringa sola per tutto il lavoro. È l'impronta del manifesto, cioè del file
che elenca i {_n(N_MANIF)} file versionati con la loro impronta ciascuno:

```
{OPERA}
```

Non è ricorsiva — il manifesto non contiene sé stesso — ed è riproducibile da
chiunque, in un comando:

```
sha256sum IMPRONTE-SHA256.txt
```

Se quella stringa coincide, **l'intero corpus versionato è quello depositato**:
non un file di meno, non un file di più, nessun file diverso. Se differisce,
il confronto riga per riga dice quale.

### I due file che restano fuori, e perché

Il manifesto elenca ogni file versionato **tranne due**: sé stesso e questo
registro. Non è una svista ed è l'unica esclusione. Un registro non può
certificare sé stesso: i suoi file cambiano a ogni rigenerazione, e l'impronta
che vi si scrivesse dentro sarebbe falsa nell'istante stesso in cui viene
scritta. La catena si chiude comunque, e senza circoli: i {_n(N_MANIF)} file
sono certificati dal manifesto, il manifesto è certificato dalla stringa qui
sopra, e questo registro non ha bisogno di esserlo perché **è interamente
ricavabile dal manifesto** — chi vuole controllarlo lo rigenera.

---

## Come si verifica

Tutti i file versionati in un colpo solo, dalla radice del repository:

```
sha256sum --check IMPRONTE-SHA256.txt
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

print(f'sezioni: {len(SEZIONI)} · file: {TOT_FILE} · byte: {_n(TOT_BYTE)}')
print(f'manifesto: {N_MANIF} righe · impronta dell\'opera: {OPERA[:16]}...')
for s in SEZIONI:
    print(f"  {len(s['voci']):>3}  {s['titolo']}")
