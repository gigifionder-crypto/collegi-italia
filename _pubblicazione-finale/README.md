# Pubblicazione finale — Lo Psicologo di Base in Puglia

Generata il 2026-07-08, su decisione esplicita dell'autore di procedere
al formato di pubblicazione finale (prompt operativo, riga 155) **prima**
del completamento del criterio 8 di Fase 4 (validazione da parte di tre
lettori-tipo reali) — un'anticipazione consapevole rispetto alla
sequenza descritta dal prompt operativo, non un'esecuzione automatica di
quella sequenza. Il protocollo di validazione
(`_meta/protocollo-validazione-fase4.md`) resta aperto e può essere
condotto anche su questa stessa edizione, quando l'autore lo vorrà.

## Contenuto

Cartella `pdf/`: un PDF navigabile per ciascun prodotto della piramide,
con segnalibri (bookmarks) di navigazione derivati dalla struttura dei
titoli del documento originale, più un indice generale con collegamenti
cliccabili a ciascun prodotto.

| File | Prodotto |
|---|---|
| `00-indice-generale.pdf` | Indice generale, punto d'accesso alla raccolta |
| `livello-1-one-pager.pdf` | Livello 1 — One-pager |
| `livello-2-policy-brief.pdf` | Livello 2 — Policy Brief |
| `livello-3-executive-summary.pdf` | Livello 3 — Executive Summary |
| `livello-4-sintesi-tecnica.pdf` | Livello 4 — Sintesi Tecnica |
| `versione-mmg-pls.pdf` | Prodotto satellite — Versione MMG/PLS |
| `abstract-strutturato.pdf` | Prodotto satellite — Abstract strutturato (CHEERS) |
| `elevator-pitch.pdf` | Prodotto satellite — Elevator Pitch |
| `tomo-1-puglia.pdf` | Livello 5 — Tomo I, corpo integrale Puglia (perimetro validato) |
| `tomo-2-linea-a.pdf` | Livello 5 — Tomo II, Linea A (volumi regionali individuali + UE-27) |
| `tomo-2-linea-b.pdf` | Livello 5 — Tomo II, Linea B (Blocco Regionale) |

I due volumi di Tomo II (Linee A e B) e la sezione UE-27 restano fuori
dal perimetro esteso di validazione, per la stessa decisione dell'autore
già documentata in `_meta/status-tracker.md` per il benchmark di Fase 3
e per il criterio 5 di Fase 4.

## Come è stata generata (nota tecnica)

LibreOffice, disponibile nell'ambiente, si è rivelato non funzionante
per la conversione (fallisce silenziosamente il caricamento di
qualunque file, anche minimale, con l'errore "source file could not be
loaded" — causa non diagnosticata nel tempo disponibile). È stata usata
una pipeline alternativa: **mammoth.js** per convertire ciascun `.docx`
in HTML (preservando titoli, paragrafi, tabelle ed enfasi; alcuni stili
di paragrafo Word non riconosciuti da mammoth sono stati riportati come
paragrafi semplici, senza perdita di testo — si vedano gli avvisi di
conversione, nessuno relativo a perdita di contenuto sostanziale) e
**Chromium headless** (via Playwright, già presente nell'ambiente) per
la stampa in PDF con generazione nativa di segnalibri
(`outline: true`) a partire dai tag di titolo HTML. Verificato a
campione che cifre e intestazioni chiave sopravvivono alla conversione
(es. "775", "40,5 mln€", intestazioni delle Parti).

## Limiti noti

- **I collegamenti dell'indice generale usano percorsi assoluti**
  (`file:///home/user/collegi-italia/_pubblicazione-finale/pdf/...`),
  validi in questo checkout. Se la cartella viene copiata altrove, i
  collegamenti cliccabili dell'indice non punteranno più ai file
  corretti (restano comunque leggibili i nomi dei file in tabella,
  sopra) — limite noto della clonazione dell'ambiente, non del
  contenuto.
- **Nessun identificativo persistente (DOI) è stato depositato**: il
  deposito presso un servizio come Zenodo richiede un account e
  un'azione dell'autore, non simulabile qui. I metadati per il deposito
  sono già preparati in `_meta/metadati-deposito.md`.
- **Il criterio 8 di Fase 4 (validazione dei tre lettori-tipo reali)
  non è stato condotto**: questa pubblicazione anticipa la sequenza
  dichiarata dal prompt operativo, per scelta esplicita dell'autore
  (2026-07-08).
- Le pagine non corrispondono 1:1 all'impaginazione che avrebbe Word:
  font, margini e interruzioni di pagina sono quelli del foglio di
  stile usato per questa conversione, non quelli del documento Word
  originale. Il contenuto testuale e tabellare è invariato.
