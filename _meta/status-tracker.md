# Tracker di stato

Stato di avanzamento per ciascuna parte dell'opera e per ciascun prodotto
della piramide. Stati ammessi: `draft` / `rivisto` / `validato` / `chiuso`.
Una parte in stato `validato` non viene riaperta per limatura stilistica
(vincolo §2.4 del prompt operativo) — solo correzioni di errore materiale.

## ATTENZIONE — discrepanza rilevata rispetto al prompt operativo (RISOLTA il 2026-07-06)

Il prompt operativo (§0) dichiara un'opera "strutturata in 13 parti". L'indice
interno del file canonico del Tomo I elencava invece **15 parti** (Parte
I–XV), con le Parti XIV e XV inizialmente assenti ("da integrare al
conferimento del file definitivo").

**Risoluzione:** l'autore ha caricato `opera-integrale-puglia_RIORDINATO...docx`,
che conteneva il testo reale di Parte XIV e XV (ripreso dal telaio "Five Case
Model" A–M usato nelle appendici, con nota redazionale esplicita sulla
provenienza). Il 2026-07-06 questo testo è stato integrato chirurgicamente
nel file canonico (inserimento degli elementi XML — 97 paragrafi, 10
tabelle — tra la chiusura di Parte XIII e il "Quadro Conclusivo... del
volume", con rimappatura degli ID di note a piè pagina e segnalibri per
evitare collisioni: +51 note, ora 3.942 totali; +10 tabelle, ora 1.059
totali). Verificato che il documento risultante è integro (nessuna
collisione di ID, tutte le tabelle accessibili). Il file precedente
l'integrazione è conservato in
`tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_pre-integrazione-parte-XIV-XV.docx`.

Il Tomo I risulta quindi ora effettivamente completo in 15 parti (non 13):
la cifra "13 parti" nel prompt operativo era stale rispetto allo stato
reale dell'opera.

## Corpo integrale — Tomo I Puglia (15 parti dichiarate nell'indice interno)

| # | Parte | Stato | Ultimo aggiornamento | Note |
|---|-------|-------|----------------------|------|
| I | Quadro, mandato, metodo e perimetro integrale | rivisto | 2026-07-06 | Contenuto presente nel file canonico. |
| II | Il bisogno e il contesto multidimensionale in Puglia | rivisto | 2026-07-06 | Contenuto presente. |
| III | L'architettura delle figure a cascata gerarchica piramidale | rivisto | 2026-07-06 | Contenuto presente. |
| IV | Il modello organizzativo integrato e le leve abilitanti | rivisto | 2026-07-06 | Contenuto presente. |
| V | La formazione del personale: le quattro modalità, singole e congiunte | rivisto | 2026-07-06 | Contenuto presente (5.1–5.8). |
| VI | Efficacia, evidenza e meccanismi di impatto | rivisto | 2026-07-06 | Contenuto presente (6.1 e segg.). |
| VII | Costi diretti (rinegoziazione integrale) | rivisto | 2026-07-06 | Contenuto presente. |
| VIII | Benefici e risparmi diretti (rinegoziazione integrale) | rivisto | 2026-07-06 | Contenuto presente (8.1–8.6). |
| IX | Costi e benefici indiretti: il perimetro multidisciplinare integrale | rivisto | 2026-07-06 | Contenuto presente (9.1–9.16, 16 domini). |
| X | Valutazione economica integrata e saldo consolidato | rivisto | 2026-07-06 | Contenuto presente (10.1–10.5). |
| XI | Modellazione, incertezza e previsione falsificabile | rivisto | 2026-07-06 | Contenuto presente (11.1–11.7, modello di Markov). |
| XII | Equità e impatto distributivo | rivisto | 2026-07-06 | Contenuto presente (12.1–12.4). |
| XIII | Profili etico-giuridico-organizzativi | rivisto | 2026-07-06 | Contenuto presente (13.1–13.5). |
| XIV | Attuazione, fattibilità e sostenibilità | rivisto | 2026-07-06 | Integrata nel file canonico (fonte: file RIORDINATO); nota redazionale di provenienza mantenuta nel testo. |
| XV | Monitoraggio, valutazione ex-post e sintesi multidimensionale | rivisto | 2026-07-06 | Come sopra. |

Oltre alle 15 Parti, il file canonico contiene 33 Appendici Integrative
(Appendice I–XXXIII), ciascuna delle quali ripete internamente uno schema
a 11 sezioni (Parte A–M: Quadro/quesito/metodo, Problema di salute,
Intervento e modello, Efficacia, Valutazione economica, Modellazione e
incertezza, Equità, Profili etico-giuridico-organizzativi, Attuazione,
Monitoraggio, Sintesi) — coerente con il "Five Case Model"/telaio HTA
citato nell'Appendice XVI. Non ancora verificato nel dettaglio se anche le
Appendici presentino sezioni analogamente "da integrare".

## Corpo integrale — Tomo II Nazionale e UE-27 (due linee editoriali, entrambe mantenute)

**Linea A — 20 volumi regionali individuali:** fonte
`tomo-2-nazionale/opera-unificata-nazionale-e-ue27.docx`. Struttura a 23
Volumi (0.A, 0.B, 1, 2–21 regionali, 22 UE-27); ciascun volume regionale
segue lo schema Premessa/Introduzione/Cruscotto/Sintesi per il
decisore/5 risultati chiave/Raccomandazioni/Capitoli 1–9/Appendici/Quadro
Conclusivo/Conclusione/Note. Stato non ancora verificato volume per
volume — da fare in Fase 1.

**Linea B — 4 Blocchi Regionali macro-territoriali:** fonte
`tomo-2-nazionale/blocco-regionale/tomo-ii-blocco-regionale.docx`
(caricata 2026-07-06, sostituisce come versione più sviluppata il
placeholder "Blocco Regionale" in coda al file del Tomo I). ~305.000
parole, 631 tabelle, 13 Heading 1: Sezione Nazionale, telaio integrato,
impatto nazionale, 4 Blocchi Regionali (Nord/Centro/Sud/Isole), Quadro
Conclusivo, Conclusione. Non ancora chiaro a quale livello della piramide
(Livello 4 o 5) questa linea sia destinata rispetto alla Linea A — da
chiarire in Fase 1.

## Materiale tecnico di supporto (ISPOR-SMDM Task Force-7)

`_meta/modelli-tecnici/` — 12 workbook Excel (tornado diagram, BIA, CEA,
CUA, sensitivity analysis, Monte Carlo, produttività iCBT vs Collaborative
Care) più una guida metodologica, caricati 2026-07-06. Costituiscono la
documentazione tecnica riproducibile del modello richiesta da ISPOR-SMDM
TF-7 (§4.6 del prompt operativo). Non ancora mappati singolarmente alle
appendici del Tomo I che dovrebbero referenziarli — da fare in Fase 2.

## ATTENZIONE — ancoraggio economico corretto a OCSE 2026 (2026-07-06)

I Livelli 1–3, scritti inizialmente sulla base del verdetto tripartito di
Parte X (ancoraggio Chisholm 2016), sono stati corretti dopo aver
verificato che il Tomo I contiene una sezione di governo metodologico
("Revisione metodologica di governo — Il passaggio all'ancoraggio OCSE
2026", paragrafi 147–187) che dichiara: "ovunque il corpo del volume e il
quadro OCSE 2026 divergano, prevale il secondo". Su decisione dell'autore
(2026-07-06), i prodotti della piramide ora usano le cifre OCSE 2026come
autorevoli: scenario intermedio (775 psicologi) — costo 40,5 mln€,
risparmi diretti 47,0 mln€, benefici indiretti 27,0 mln€, ROI lordo 1:6,6,
costo/QALY ~9.800€, break-even 2,3 anni.

**Discrepanza residua non risolta:** la sezione di revisione (§IV.4)
dichiara esplicitamente di aggiornare solo Parte I, II e III; le Parti
VII–X (il calcolo dettagliato di costi/risparmi/ICER/ritorno sociale, da
cui è tratto il "verdetto tripartito" di Parte X) restano espresse
nell'ancoraggio Chisholm 2016 e non sono state riconciliate. Inoltre, la
tabella IV.3 riporta un costo di regime fisso di 40,5 mln€ per tutti e tre
gli scenari "Base/Intermedio/Ottimale", mentre altre sezioni del Tomo I
(Quadro Conclusivo di Parte X) indicano un costo crescente con la
copertura (43–47 mln€ secondo lo scenario 620/775/900): non è chiaro se
"Base/Intermedio/Ottimale" della Parte IV corrispondano esattamente a
620/775/900, o siano un asse di scenario diverso (ipotesi di
risparmio/efficacia a parità di organico). Questo va chiarito con l'autore
prima della Fase 3 (editing per passate tematiche), quando andrà comunque
riconciliato l'intero corpo integrale con l'ancoraggio OCSE 2026. Nel
frattempo i prodotti della piramide usano solo la cifra di costo
pienamente confermata (40,5 mln€, scenario intermedio raccomandato).

## Livelli della piramide

Base: Tomo I Puglia (Parti I–XV, verdetto tripartito in Parte X, revisione
OCSE 2026 in Parte IV/"Revisione metodologica di governo"). Il Livello 4 e
i satelliti dovranno inoltre coprire Tomo II e UE-27 (le due linee) e la
mappatura di conformità — non ancora fatto.

| Livello | Prodotto | Stato | Ultimo aggiornamento | Note |
|---------|----------|-------|----------------------|------|
| 1 | One-pager | rivisto | 2026-07-06 | `_livelli-piramide/livello-1-one-pager.md`. Corretto con cifre OCSE 2026 (scenario intermedio). |
| 2 | Policy brief | rivisto | 2026-07-06 | `_livelli-piramide/livello-2-policy-brief.md`. Opzioni confrontate: status quo + i 3 scenari di copertura reali dello studio (620/775/900) con cifre OCSE 2026; nota metodologica sulla discrepanza di costo per scenario. |
| 3 | Executive summary (1:3:25) | rivisto | 2026-07-06 | `_livelli-piramide/livello-3-executive-summary.md` (~1.600 parole). Corretto con cifre OCSE 2026; limiti dichiarati aggiornati con la nota sulla riconciliazione Chisholm/OCSE ancora da fare. |
| 4 | Sintesi tecnica (25-40 pag.) | rivisto | 2026-07-06 | `_livelli-piramide/livello-4-sintesi-tecnica.md` (~2.750 parole, ~10 pagine): sotto il target di 25-40 pagine dichiarato dal prompt operativo (§3.4). Copre telaio metodologico (4 cornici), mappatura ai 9 domini EUnetHTA, modello a cascata, metodologia economica e versioning OCSE 2026/Chisholm 2016, protocollo dell'incertezza (Parte XI), attuazione/equità/profili etico-giuridici, limiti, mappa dei rimandi. Da espandere con maggior dettaglio granulare (es. i 16 domini di Parte IX uno per uno, checklist CHEERS inline) se si vuole raggiungere il target di lunghezza pieno. |
| 5 | Corpo integrale (riclassificazione) | rivisto (parziale) | 2026-07-06 | Livello tomo: fatto per tutti e 3 i file canonici (Tomo I, Tomo II Linea A, Tomo II Linea B), ciascuno con "Come leggere questo Tomo" + tabella "Mappa dei destinatari". Livello parte: fatto per le Parti III–XV del Tomo I (12 parti — si veda sezione dedicata sotto); **Parte I e Parte II escluse per la duplicazione non dichiarata scoperta il 2026-07-06** (si veda `_meta/anomalie-corpus.md`); non fatto per i volumi di Tomo II (portata maggiore, da pianificare a parte). |

## Livello 5 — Riassunto e messaggi chiave per parte (Tomo I, Parti III–XV)

Eseguito il 2026-07-06 tramite manipolazione diretta dell'XML: per ciascuna
delle 12 Parti da III a XV, un blocco "Riassunto e messaggi chiave"
(intestazione di Livello 3, un paragrafo di sintesi fedele estratto dalla
sezione "Quadro conclusivo"/"Conclusione" della parte stessa, e 3-4
messaggi chiave in forma di elenco puntato manuale) è stato inserito subito
dopo l'intestazione di apertura della parte (o subito prima della prima
sottosezione numerata, per le parti prive di una propria intestazione di
Livello 1). Verificato: +91 paragrafi (13 blocchi × 7 elementi, da 11.124 a
11.215), tabelle invariate (1.060), nessun errore di accesso alle tabelle.

**Parte I e Parte II escluse** da questo passo per la duplicazione non
dichiarata scoperta durante la pianificazione (si veda
`_meta/anomalie-corpus.md`): in attesa di istruzioni dell'autore su come
trattarla prima di scrivere un riassunto che dovrebbe coprire due versioni
diverse dello stesso contenuto.

I riferimenti a paragrafi nel Livello 4 (`_livelli-piramide/livello-4-sintesi-tecnica.md`),
resi obsoleti dallo spostamento di +4 posizioni causato dall'inserimento
del "Come leggere questo Tomo", sono stati sostituiti con riferimenti a
titoli di sezione (più stabili rispetto a future modifiche del file).

## Fase 2 — Conformità agli standard internazionali

Compilata il 2026-07-06 in `_meta/checklist-conformita.md`, sulla base del
Tomo I (non ancora estesa a Tomo II/UE-27). Stato:

- **CHEERS 2022** (28 item): 19 pienamente soddisfatti, 3 parziali, 6 gap.
  Gap più rilevanti: assenza di dichiarazione di finanziamento e conflitto
  di interessi (item 27–28), assenza di coinvolgimento documentato di
  pazienti/cittadini (item 21/25), assenza di abstract strutturato (item
  2). Estensione CHEERS-AI (38 item) discussa ma non compilata item per
  item (rimandata alla Fase 3, previa conferma di pertinenza).
- **9 domini HTA Core Model**: mappatura completata (già presente nel
  Livello 4); confermati come parziali i domini SAF ed EFF.
- **GRADE Evidence-to-Decision**: strutturato per la raccomandazione
  principale (scenario intermedio, 775 psicologi) — forza "forte a
  favore", con gap su valori/preferenze e accettabilità (nessuna
  consultazione di pazienti/cittadini documentata).
- **NICE HTE manual 2022**: scope e decision problem presenti; "reference
  case" non dichiarato come tale in modo unitario (le scelte equivalenti
  esistono ma sono distribuite nel testo).
- **ISPOR-SMDM TF-7**: documentazione a due livelli presente (non tecnica
  in Parte X-XI; tecnica riproducibile in Appendice XVI e nei workbook di
  `_meta/modelli-tecnici/`, non ancora mappati sezione per sezione).
- **WHO Handbook for Guideline Development**: gap strutturali su
  composizione del gruppo di lavoro e revisione esterna (l'opera ha un
  singolo autore dichiarato).
- **Reg. UE 2021/2282**: telaio HTA Core Model adottato; allineamento
  della sezione UE-27 non ancora verificato.
- **Reg. UE 2024/1689 (AI Act)**: conformità già dichiarata esplicitamente
  nel corpo dell'opera (non un gap) — sistemi IA diagnostici classificati
  ad alto rischio, supervisione umana, D.Lgs. 138/2024.

Tutti i gap identificati sono stati aggiunti a `_meta/parking-lot.md` per
assicurarne il seguito in Fase 3, senza colmarli scrivendo nuovo
contenuto nel corpo integrale (congelamento dello scope).

## Prodotti satellite

| Prodotto | Stato | Ultimo aggiornamento | Note |
|----------|-------|----------------------|------|
| Versione MMG/PLS | draft | | |
| Slide deck | draft | | |
| Tabella comparativa opzioni organizzative | draft | | Bozza già presente come sezione "Le opzioni a confronto" nel Livello 2; da estrarre come tabella autonoma. |
| FAQ stakeholder | draft | | |
| Elevator pitch (frase-tesi unica) | rivisto | 2026-07-06 | `_livelli-piramide/elevator-pitch.md`. Riprodotta identica nei Livelli 1 e 2. |
