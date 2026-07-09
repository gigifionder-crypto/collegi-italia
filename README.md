# Studio Integrale Puglia / Psicologo di Base — Ristrutturazione a piramide

Questo repository ospita la ristrutturazione a piramide dell'opera "Studio
Integrale Puglia / Psicologo di Base" (Tomo I Puglia, Tomo II Nazionale,
sezione UE-27) secondo il prompt operativo concordato con l'autore.

## Stato attuale

**Corpus ricevuto (2026-07-06).** Il testo sorgente è caricato e
organizzato per tomo (si vedano i README di ciascuna cartella per la
provenienza esatta dei file e le decisioni di canonicità prese con
l'autore). È stata rilevata e documentata in `_meta/status-tracker.md` una
discrepanza tra il numero di parti dichiarato nel prompt operativo (13) e
quello effettivo nell'indice interno del Tomo I (15, di cui le ultime due
non ancora integrate nel file) — da chiarire prima di procedere oltre la
Fase 1. Il lavoro di costruzione della piramide di prodotti derivati e di
messa in conformità agli standard internazionali è in corso.

## Struttura

- `tomo-1-puglia/` — corpo integrale, Tomo I (Puglia). File canonico:
  `opera-integrale-puglia.docx`; versioni precedenti in
  `versioni-precedenti/`.
- `tomo-2-nazionale/` — corpo integrale, Tomo II (20 regioni italiane) e
  sezione UE-27. File canonico: `opera-unificata-nazionale-e-ue27.docx`.
- `ue-27/` — sezione UE-27 (collegamento allo stesso file del Tomo II).
- `_livelli-piramide/` — prodotti derivati (Livello 1 one-pager, Livello 2
  policy brief, Livello 3 executive summary, Livello 4 sintesi tecnica) e
  prodotti satellite (versione MMG/PLS, slide deck, tabella comparativa,
  FAQ, elevator pitch).
- `_meta/` — tracker di stato per parte, parking lot list, cut/darlings,
  changelog, checklist di conformità (CHEERS 2022, EUnetHTA, GRADE EtD,
  ecc.).

Il prompt operativo integrale di riferimento è conservato in
`_meta/prompt-operativo.md`.

## Nuova collana: «Le Professioni di Base»

- `professioni-di-base/` — collana di Volumi-figura che applicano il metodo
  di valutazione dello Psicologo di Base alle altre figure medico-sanitarie
  del Censimento Integrale. Si veda `professioni-di-base/README.md` per lo
  stato di avanzamento e la nota sulla differenza rispetto all'opera madre.
