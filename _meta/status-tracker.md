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

## Fase 3 — Editing per passate tematiche separate

### 3.1 — Passata sulla struttura (CHIUSA il 2026-07-06)

- Duplicazione Parte I/II: **risolta**, rimossa la versione breve dal
  corpo del Tomo I (si veda `_meta/anomalie-corpus.md` per il dettaglio
  dell'operazione e la verifica di integrità: 11.215→11.110 paragrafi,
  1.060→1.055 tabelle, 3.942→3.915 note, zero note orfane).
- Le due voci d'indice "da integrare al conferimento del file definitivo"
  per Parte XIV/XV, ormai stale, sono state aggiornate in
  "(integrata il 2026-07-06)".
- Nessun'altra duplicazione strutturale analoga è stata riscontrata da
  Parte III in poi.

**Non riaprire questa sotto-fase** nelle successive (vincolo §2.5/Fase 3
del prompt operativo).

### 3.2 — Passata sulla verifica numerica (esaustiva, multi-sessione — IN CORSO)

Registro dedicato: `_meta/verifica-numerica-tracker.md`, popolato il
2026-07-06 con tutte le 1.055 tabelle del Tomo I (dopo la rimozione di
Parte I/II breve), classificate per tipo: **959 "dati"** (tabelle con
contenuto numerico verificabile), **55 "infografica"** (segnaposto di
progettazione grafica per Canva — non tabelle di dati; coerente con
l'osservazione del prompt operativo §6 sulla presenza di residui
infografici da completare/rimuovere), **41 "altro"** (piccole/monocolonna).

**Verificate finora: 131 su 1.055** (Tab. IV.1-IV.4 della Revisione OCSE
2026 e tutte le tabelle "dati"/"altro" di Parte VII — Costi diretti —,
Parte VIII — Risparmi diretti —, Parte IX — Benefici indiretti, 16
domini —, Parte X — Sintesi economica integrata: ICER, SROI, sintesi
multi-criterio, saldo consolidato —, Parte XI — Modello di Markov, PSA,
previsioni falsificabili —, Parte XII — Equità territoriale e digitale —
e Parte XIII — Cornice etico-giuridico-organizzativa):

- **121 verificata-ok**: Tab. IV.2 (risparmi per canale/scenario); tabella
  FTE→costo apice; costi di struttura/coordinamento; tabella master del
  costo diretto complessivo (#87 — conferma le cifre 45,2 lordo/43,9
  netto già usate nei Livelli 1-4); profilo temporale (#88); distribuzione
  lungo la cascata (#90); tutte le tabelle "dati"/"altro" di Parte VIII
  (#92, 93, 94, 96, 97, 99, 100, 102, 103, 105, 107 — risparmio diretto
  per canale e complessivo, coerenti internamente sullo schema di
  scenario "Conservativo ~450 / Intermedio ~700 / Espansivo ~900"
  psicologi); tutte le tabelle "dati" dei 16 domini di Parte IX (#111-157
  — ogni dominio somma esattamente al totale dichiarato, per tutti e tre
  gli scenari; si veda però la SECONDA SCOPERTA MAGGIORE sotto); tutto il
  cluster di Parte X (#158-177 — ICER, valore monetizzato della salute,
  traiettoria quinquennale, SROI, sintesi multi-criterio a 6 criteri
  ricalcolata esattamente, tabella master #176 — ogni calcolo
  ricontrollato torna esatto); tutta Parte XI (#178-197 — modello di
  Markov: probabilità di transizione che sommano esattamente a 1,00,
  analisi di sensibilità probabilistica coerente col risultato
  deterministico di Parte X, previsioni falsificabili con bande e soglie
  di confutazione ben formate in ogni tabella — nessuna nuova
  discrepanza); tutta Parte XII (#198-206 — distribuzione territoriale
  del contingente per ASL, quote sommano a 100%, allocazione coerente con
  le quote di popolazione; gruppi di attenzione, divario digitale e
  dimensioni dell'equità sono tabelle qualitative senza aritmetica da
  verificare — ma si veda la quarta cifra di headcount, ~840, aggiunta
  alla SCOPERTA MAGGIORE sotto); tutta Parte XIII (#207-215 — cornice
  costituzionale, protezione dei dati, deontologia professionale e
  distribuzione di funzioni/responsabilità: parte dichiarata
  esplicitamente "normativa e non quantitativa" dalla propria Avvertenza,
  nessuna tabella numerica presente, nessuna aritmetica applicabile).
- **10 verificata-discrepanza**: Tab. IV.3 (ROI non ricostruibile dai dati
  mostrati); 4 tabelle a una sola colonna prive di valori numerici
  (#73-76); 3 tabelle (#77 personale, #82 leva digitale/IA, #85
  formazione) i cui componenti non sommano esattamente al totale
  dichiarato **negli scenari Conservativo ed Espansivo** — lo scenario
  Centrale (775 psicologi, raccomandato) risulta invece sempre coerente
  in ogni tabella verificata finora; la tabella #108 di Parte VIII (si
  veda la SCOPERTA MAGGIORE sotto); e la tabella #162 di Parte X (si
  veda la SECONDA SCOPERTA MAGGIORE, raffinata sotto). Dettaglio completo
  in `_meta/verifica-numerica-tracker.md`; tutti i gap tracciati anche in
  `_meta/parking-lot.md`.

**⚠️ SCOPERTA MAGGIORE (2026-07-06) — il framework degli scenari a tre
livelli non è coerente tra le parti del Tomo I.** Emersa verificando la
tabella #108 di Parte VIII ("Costi diretti del servizio", settima parte):
~25/~38/~50 mln€ per gli scenari Conservativo/Intermedio/Espansivo. Questa
cifra è **incompatibile** con la tabella master di Parte VII (#87, già
verificata-ok), che dà lo stesso costo diretto complessivo, per gli
stessi tre scenari nominali, come 54,4/45,2/36,5 mln€ lordo (53,4/43,9/
35,0 netto) — uno scarto del 15-18% (6-7 mln€) non riconducibile a un
errore di arrotondamento o a un'inversione dell'ordine degli scenari.

Il problema è più ampio di questa singola tabella: **coesistono almeno
tre schemi di etichettatura dello scenario "centrale/intermedio"**
(headcount di Psicologi di Base) nello stesso Tomo I —
- Parte VIII: ~450 / **~700** / ~900
- Parte X (Quadro Conclusivo): 620 / **775** / 900
- Parte VII: nessuna etichetta di headcount esplicita per riga (FTE
  740/715/700, organico in testa 880/840/800 — non corrispondenti in modo
  ovvio a nessuno dei due schemi sopra)

— e **almeno tre cifre di costo diverse per lo stesso scenario centrale
raccomandato**: ~38 mln€ (Parte VIII), ~40,5 mln€ (Parte IV/ancoraggio
OCSE 2026, usato in tutti i prodotti della piramide Livelli 1-4), ~43,9-
45,2 mln€ (Parte VII, tabella master #87).

**Nessuna correzione è stata applicata al testo.** Per decisione esplicita
dell'autore (2026-07-06), la scoperta viene registrata con visibilità
massima qui e in `_meta/parking-lot.md`, e la verifica sistematica
tabella-per-tabella prosegue nell'ordine già stabilito (dopo Parte VIII:
Parte IX, poi X, XI...) senza fermarsi a riconciliare il framework ora —
la riconciliazione resta un'attività distinta, da affrontare quando la
verifica sarà più completa.

**Aggiornamento (Parte XII):** la distribuzione territoriale del
contingente per ASL (tabella #199) somma a un totale di ~840 Psicologi
di base per lo "scenario centrale" — una **quarta cifra di headcount**,
diversa da 700 (Parte VIII) e 775 (Parte X), ma coincidente con
l'"organico in testa" dello scenario intermedio già letto in Parte VII
(840). Utile indizio per la riconciliazione futura (suggerisce che
Parte VII/XII usino una base "organico in testa" diversa dalla base
"netta"/FTE di Parte VIII/X), ma non la risolve.

**⚠️ SECONDA SCOPERTA MAGGIORE (2026-07-06) — i "benefici indiretti"
hanno due basi di calcolo incompatibili nello stesso Tomo I.** Emersa
verificando i 16 domini di Parte IX (lavorativo, pensionistico,
produttivistico residuo, assistenzialistico, welfaristico,
prevenzionalistico residuo, criminologico, burocratico, culturale,
pedagogico-scolastico, accademico, industriale, sindacale,
antropologico, sociale, finanziario). Ogni dominio, preso singolarmente,
è internamente coerente (i componenti sommano esattamente al totale di
dominio dichiarato). Ma **sommando i 16 totali di dominio** per ciascuno
scenario si ottiene: Conservativo (~450) = 69 mln€, Intermedio (~700) =
104 mln€, Espansivo (~900) = 147 mln€ di benefici indiretti/anno —
cifre drasticamente superiori (da 3 a 6 volte) a quelle
dell'ancoraggio OCSE 2026 già usato in tutti i prodotti della piramide
(Tab. IV.3: Base 11,0 / Intermedio **27,0** / Ottimale 49,0 mln€), con un
rapporto non costante tra le due basi (6,3× per lo scenario
Conservativo/Base, 3,9× per l'Intermedio, 3,0× per l'Espansivo/
Ottimale) che esclude un semplice fattore di conversione.

Questo **conferma e quantifica** un sospetto già registrato in
`_meta/parking-lot.md` (voce sulla Tab. IV.3, "il calcolo del ROI
verosimilmente include grandezze aggiuntive [i 16 domini di Parte IX]
non mostrate in tabella"): il buildup analitico dal basso di Parte IX e
l'ancoraggio macro-econometrico OCSE 2026 non sono la stessa grandezza e
non sono sommabili — ma il testo non dichiara esplicitamente quale delle
due debba prevalere come cifra ufficiale dei "benefici indiretti" dello
studio, né la corretta esiste una nota di raccordo tra Parte IX e la
Revisione metodologica di governo. Non corretto silenziosamente.

Per la stessa decisione dell'autore già presa per la prima scoperta
maggiore (opzione a: registrare e proseguire), questa seconda
incoerenza non ferma la verifica sistematica, che continua con Parte X.
Entrambe le scoperte maggiori (framework di scenario in Parte VII/VIII e
base di calcolo dei benefici indiretti in Parte IX) restano oggetto di
un'unica riconciliazione da affrontare a valle, quando la verifica sarà
più completa.

**Raffinamento della seconda scoperta (Parte X):** l'intero cluster di
tabelle di Parte X (ICER, SROI, sintesi multi-criterio, saldo
consolidato) è internamente perfettamente autoconsistente — ogni
calcolo è stato ricontrollato e torna esatto — ma usa una **terza cifra**
per i "benefici economici/sociali indiretti": ~65/~98/~139 mln€ per
Conservativo/Intermedio/Espansivo, diversa sia dalla somma verificata
dei 16 domini di Parte IX (69/104/147 — scarto piccolo, 4-8 mln€/5-6%,
forse dovuto all'esclusione non dichiarata di 2-3 domini minori) sia,
soprattutto, dall'ancoraggio OCSE 2026 (11,0/27,0/49,0 — scarto di un
ordine di grandezza). **La stessa grandezza nominale ("benefici
indiretti dello scenario intermedio") assume quindi tre valori diversi
nel Tomo I: ~27 (Parte IV/OCSE 2026, usato nella piramide), ~98 (Parte
X), ~104 (somma dei domini di Parte IX).** Nessuna correzione applicata;
si prosegue con Parte XI.

**Le restanti ~924 righe sono ancora "da verificare"/"n/a-infografica".**
Data la scala (959 tabelle dati), questa sotto-fase richiede molte
sessioni successive per essere completata: l'autore ha scelto
esplicitamente la verifica esaustiva (non un campionamento a rischio),
riconoscendo che questo comporta un impegno pluri-sessione.

### 3.3 — Passata sul registro linguistico (NON ANCORA AVVIATA)

Da eseguire solo dopo la chiusura di 3.2.

### 3.4 — Passata sull'apparato editoriale (NON ANCORA AVVIATA)

Controlli automatizzati preliminari già eseguiti il 2026-07-06 (prima di
3.1): note a piè di pagina coerenti (0 orfane/mancanti su 3.942, ora 3.915
dopo la rimozione di 27 relative alla versione breve rimossa); 818
etichette "Tabella N.M" individuate, 48 duplicate (atteso per la
ripetizione del telaio "Parte A–M" nelle appendici, da decidere con
l'autore in questa sotto-fase se rinumerare o mantenere con
qualificazione per parte/appendice).

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
