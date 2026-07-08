# Paper accademico — versioni per pubblicazione su rivista indicizzata

Creati il 2026-07-08, su richiesta esplicita dell'autore. **Non previsti
dalla piramide originale del prompt operativo** (Livelli 1-5 + prodotti
satellite) — un nuovo tipo di prodotto derivato, aggiunto in coda al
lavoro di ristrutturazione, non una modifica al corpo integrale.

## Contenuto

| File | Descrizione |
|---|---|
| `paper-italiano-crusca.md` | Paper in italiano, registro formale conforme all'uso raccomandato dall'Accademia della Crusca |
| `paper-english-oxford.md` | Stessa struttura e stessi dati, in inglese accademico britannico (registro "Oxford") |
| `pdf/paper-italiano-crusca.pdf`, `pdf/paper-english-oxford.pdf` | Versioni PDF navigabili con segnalibri |
| `docx/paper-italiano-crusca.docx`, `docx/paper-english-oxford.docx` | Versioni Word, per la sottomissione a piattaforme editoriali che richiedono `.docx` (es. Research Connections) — sezioni numerate come stili "Titolo 1"/"Titolo 2" nativi di Word, dichiarazioni con etichetta in grassetto, bibliografia come elenco numerato |

Entrambi seguono la struttura standard di un paper di valutazione
economica per riviste di Health Technology Assessment indicizzate su
PubMed (riassunto strutturato, introduzione, metodi, risultati,
discussione, conclusioni, dichiarazioni — finanziamento, conflitti di
interesse, approvazione etica, coinvolgimento di pazienti,
disponibilità dei dati, contributo dell'autore — bibliografia).

I file `.docx` sono generati con python-docx (non LibreOffice, non
funzionante in questo ambiente) a partire dai file `.md` sorgente,
mappando titoli e sottotitoli numerati agli stili nativi "Titolo 1"/
"Titolo 2" di Word: non verificati contro un template o una "Guide for
Authors" specifica di Research Connections, di cui non conosco i
requisiti esatti — solo la richiesta generica di ".docx con sezioni
numerate". Se la piattaforma richiede un template proprio (intestazioni
specifiche, ordine diverso delle sezioni, campi metadati aggiuntivi),
fornirlo per un adattamento puntuale.

## Base contenutistica e perimetro

Nessun dato nuovo: entrambi i paper sono costruiti a partire
esclusivamente da `_livelli-piramide/abstract-strutturato.md`,
`livello-3-executive-summary.md`, `livello-4-sintesi-tecnica.md` e
`_meta/checklist-conformita.md` (per le dichiarazioni). Circa
4.500-5.500 parole ciascuno, per uso in una rivista che accetti un
research article di lunghezza standard — non una riscrittura in stile
rivista dell'intero Tomo I.

## Nota su "per PubMed"

PubMed non accetta sottomissioni dirette: indicizza articoli già
pubblicati in riviste indicizzate nel suo database (MEDLINE). Questi
due file sono scritti nello **stile e nella struttura** attesi da una
rivista di economia sanitaria/HTA indicizzata (es. *Value in Health*,
*PharmacoEconomics*, *Cost Effectiveness and Resource Allocation*), pronti
per un'eventuale sottomissione a una di queste sedi — la sottomissione
stessa, la scelta della rivista e l'eventuale revisione tra pari restano
azioni dell'autore.

## Voci da verificare prima di un'eventuale sottomissione

- Il riferimento bibliografico completo di Unützer et al. (citato nel
  corpo integrale solo come "Unützer et al., 2008") è stato integrato
  con gli estremi standard della pubblicazione più plausibile
  corrispondente; da verificare dall'autore contro la fonte originale
  usata in fase di stesura del Tomo I.
- L'affiliazione istituzionale dell'autore non è dicharata nel corpo
  integrale: i due paper riportano solo il nome, da integrare se
  richiesto dalla rivista di destinazione.
- La licenza di pubblicazione e gli eventuali diritti d'autore da
  cedere alla rivista non sono trattati qui: restano una scelta
  dell'autore al momento della sottomissione.
