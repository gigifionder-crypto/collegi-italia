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
| 5 | Corpo integrale (riclassificazione) | rivisto (parziale) | 2026-07-06 | Livello tomo: fatto per tutti e 3 i file canonici (Tomo I, Tomo II Linea A, Tomo II Linea B), ciascuno con "Come leggere questo Tomo" + tabella "Mappa dei destinatari" inserite via manipolazione diretta dell'XML, subito dopo l'avvertenza di edizione esistente. Verificato: nessuna tabella corrotta, conteggio paragrafi/tabelle coerente (Tomo I: 11.124 par./1.060 tab.; Tomo II Linea A: 2.741 par./266 tab.; Tomo II Linea B: 5.188 par./632 tab.). **Livello parte: non fatto.** Il §3.5 del prompt richiede anche che "ogni parte maggiore si apra con un riassunto di un paragrafo e i key messages": non ancora eseguito per le 15 Parti del Tomo I (compito distinto e di portata maggiore — richiede localizzare l'inizio di ciascuna parte, che nel documento sorgente non ha un confine uniforme: solo Parte IV e VII hanno un heading "Parte N —" esplicito nel corpo, le altre iniziano con sottosezioni numerate sotto un'intestazione generica "Premessa"/"Introduzione") né per i volumi di Tomo II. |

## Prodotti satellite

| Prodotto | Stato | Ultimo aggiornamento | Note |
|----------|-------|----------------------|------|
| Versione MMG/PLS | draft | | |
| Slide deck | draft | | |
| Tabella comparativa opzioni organizzative | draft | | Bozza già presente come sezione "Le opzioni a confronto" nel Livello 2; da estrarre come tabella autonoma. |
| FAQ stakeholder | draft | | |
| Elevator pitch (frase-tesi unica) | rivisto | 2026-07-06 | `_livelli-piramide/elevator-pitch.md`. Riprodotta identica nei Livelli 1 e 2. |
