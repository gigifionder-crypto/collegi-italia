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

**Le quattro passate tematiche previste dal prompt operativo (§Fase 3)
sono ora tutte chiuse** (3.1 struttura, 3.2 verifica numerica, 3.3
registro linguistico, 3.4 apparato editoriale — quest'ultima chiusa il
2026-07-07 con sette lotti, tutti i nove item della sua checklist
coperti). Il benchmark di successo dichiarato dal prompt per la Fase 3
("ciascuna delle parti dell'opera risulta marcata come 'validata'...
senza eccezioni pendenti") **non è ancora soddisfatto**: le 15 Parti
del nucleo Puglia restano allo stato `rivisto` (tabella sopra), non
`validato`, perché esistono eccezioni pendenti reali, non chiuse per
decisione esplicita di rimandarle:
- **39 discrepanze aritmetiche/strutturali** documentate in Fase 3.2
  (`_meta/parking-lot.md`), mai riconciliate per decisione dell'autore
  di registrare e proseguire, rimandando la riconciliazione a
  un'attività distinta.
- **2 decisioni minori dell'autore ancora pendenti** dalla Fase 3.4
  (etichette a lettera A.1-M.3 duplicate nei 19 blocchi regionali;
  residui di 1-2 asterischi di markup non convertito in contesti
  diversi da quello già corretto).
- **Perimetro dichiaratamente non esteso**: la Fase 3.3 ha coperto solo
  i Livelli 1-4 della piramide, non le 33 Appendici Integrative, il
  Tomo II (20 volumi regionali) né la sezione UE-27; l'item 1 della
  Fase 3.4 (stile citazionale) resta campionario, non un censimento
  esaustivo delle ~3.915 note.

Promuovere le Parti a `validato` richiederebbe prima chiudere questi tre
fronti (o dichiarare esplicitamente che restano fuori scope per la
validazione). Non fatto in autonomia in questa sessione: è una
decisione sull'accettabilità del rischio residuo, non una verifica
tecnica.

## Riconciliazione delle 39 discrepanze di Fase 3.2 (avviata il 2026-07-08)

Su richiesta dell'autore ("riconciliazione"), avviato il lavoro di
chiusura delle 39 righe `verificata-discrepanza` di
`_meta/verifica-numerica-tracker.md`. Metodo concordato: istruttoria a
cura dell'assistente per ciascuna discrepanza/filone (lettura più
plausibile, motivazioni), decisione puntuale dell'autore prima di
qualunque correzione; ordine concordato: categorie a rischio più basso
prima, i due filoni sistemici maggiori per ultimi.

**Primo lotto (2026-07-08) — 13 righe chiuse come `riconciliata`**:
- **Tabelle #73-76** (Parte VII, struttura a una colonna senza valori):
  segnalate come limite noto, nessuna correzione — il contenuto
  sostanziale è comunque presente in prosa subito dopo ciascuna
  tabella.
- **Scarti aritmetici minori #77/#82/#85/#339/#783** (0,05-0,7 mln€ o
  ~1-2%, scenario centrale sempre esatto): chiusi come arrotondamento
  in calcoli multi-step, nessuna correzione numerica.
- **Residui di copia #571/#579/#619 e corruzione di cella #778**:
  corretti direttamente nel `.docx` canonico, con il testo verificato
  dalla stessa fonte nello stesso blocco regionale per ciascuno —
  **settima modifica di contenuto al file canonico nel progetto**.
  Verificata l'integrità strutturale dopo la modifica (11.110
  paragrafi, 1.055 tabelle invariati).

**Secondo lotto (2026-07-08) — conflitto interno Molise risolto, 4
righe chiuse (#863, #864, #865, #867)**: istruttoria completa su
richiesta esplicita dell'autore prima di decidere. Solo lo scenario
Conservativo era in conflitto (Base ed Espansivo già coerenti). Il
costo di 0,4 mln€ (tabella #864, scomposizione bottom-up verificata
esatta) è risultato confermato da un riscontro indipendente — 0,4
mln€/6 incarichi ≈ 66.700 €/incarico, coincidente esattamente col
modello di costo già documentato per il Molise — contro il costo di
1,0 mln€ dichiarato in tabella #863, senza riscontro in alcun modello
del corpus. **Decisione dell'autore: applicare 0,4 mln€ come costo
autorevole.** Corrette le tabelle #863, #865, #867 (saldo diretto,
saldo complessivo, BCR ricalcolati di conseguenza: BCR
Conservativo 3,2-3,3:1 → 8,0:1) — **ottava modifica di contenuto al
`.docx` canonico nel progetto**. Verificata l'integrità strutturale
post-modifica.

**Terzo lotto (2026-07-08) — cluster Valle d'Aosta risolto, 6 righe
chiuse (#1006, #1018, #1019, #1020, #1035, #1039)**: istruttoria
completa, tre decisioni dell'autore.
- **Conflitto "saldo complessivo"**: tabella #1006 (+8,1/+12,1 per
  Base/Espansivo) in conflitto con #1020/#1039 (+6,1/+8,5, verificate
  esatte). Corretta #1006 — **nona modifica di contenuto al `.docx`
  canonico nel progetto**.
- **Rapporto beneficio-costo** (4,0/4,8/5,3:1, non ricostruibile da
  ritorno/costo — l'unico caso fra le 19 regioni in cui l'intera serie
  di BCR non torna, scarto 15-24%): nessuna lettura alternativa
  verificabile trovata. **Segnalato come limite noto**, nessuna
  correzione.
- **Due scarti minori** (#1019, #1035): chiusi come arrotondamento,
  stessa categoria già decisa per Marche/Parte VII. Tabella #1018
  (costo per incarico anomalo) confermata come caratteristica
  distintiva del blocco, nessuna correzione.

Verificata l'integrità strutturale dopo la modifica: 11.110 paragrafi
e 1.055 tabelle invariati.

**Quarto lotto (2026-07-08) — Basilicata/Calabria confermate, 2 righe
chiuse (#915, #924) — CHIUDE LA CATEGORIA C**: verificato per intero
entrambi i blocchi economici. Basilicata esatta al centesimo su tutte
le formule (compensi 50.000€/incarico + sovrattassa 12.500€/incarico,
costanti sui tre scenari; risparmi diretti, saldo diretto, ritorno
complessivo, saldo complessivo, BCR tutti ricostruiti esattamente).
Calabria coerente con solo un arrotondamento trascurabile sul costo per
incarico. **Nessun errore aritmetico trovato in nessuna delle due
regioni**: il modello di costo alternativo (compensi+sovrattassa), già
condiviso col Molise, è confermato coerente al proprio interno.
Decisione dell'autore: confermare senza correzione. Nessuna modifica al
`.docx` in questo lotto.

Con questo lotto si chiude interamente la **categoria C** (difetti
strutturali/di contenuto) del piano di riconciliazione.

Restano **14 righe** non riconciliate, interamente i due filoni
sistemici maggiori (framework degli scenari a righe #108/#631 e
derivate; sei basi dei benefici indiretti a righe #162/#225/#406 e
derivate, con la tabella IV.3 del ROI lordo collegata a quest'ultimo)
— l'unico lavoro restante della riconciliazione, il più delicato
perché tocca le cifre già usate in tutti i prodotti della piramide.

**Quinto lotto (2026-07-08) — categoria A, filone 1: primo
sotto-problema risolto**: istruttoria approfondita sul modello di
costo di Parte VII (§7.1) su richiesta dell'autore. Scoperto che Parte
VII e Parte VIII/X usano "Conservativo/Centrale/Espansivo" per due assi
diversi — Parte VII fa variare l'ipotesi contrattuale sul costo
unitario a fabbisogno clinico sostanzialmente fisso (organico
~700-880, indipendente dallo scenario), Parte VIII/X fanno variare la
scala di dispiegamento effettivo (headcount crescente) a costo
unitario pressoché fisso. Confermato che Parte X eredita l'asse di
Parte VIII (tabella #158), e che le etichette erano disallineate anche
**internamente** a Parte VIII (il riassunto §1346 dichiarava già
"620/775/900" per le stesse cifre che le tabelle nel corpo etichettavano
"450/700/900"). **Decisione dell'autore: correggere le etichette su
tutte le tabelle interessate.** Corrette le intestazioni di headcount
in 24 tabelle (Parte IV, VIII, X e due tabelle-quadro) da
"(~450)/(~700)" a "(~620)/(~775)", senza toccare alcun valore in euro o
anni-di-vita — **decima modifica di contenuto al `.docx` canonico nel
progetto**. Verificata l'integrità strutturale (11.110 paragrafi, 1.055
tabelle invariati).

**Sesto lotto (2026-07-08) — categoria A, filone 1: riga #108 chiusa**:
decisione dell'autore di adottare il costo lordo di Parte VII
(54,4/45,2/36,5 mln€) come "costo del servizio" autorevole. Inventario
completo prima di correggere: la stessa sintesi Puglia ricorre in **16
tabelle** (non solo #107), incluse cinque copie quasi identiche in
appendici successive. Calcolato l'impatto sul rapporto beneficio-costo
complessivo (3,6/4,3/5,0:1 → ~1,7/~3,6/~6,8:1): **violerebbe il
vincolo metodologico invariante** dichiarato dalla stessa Parte VII
(intervalli 2,3-3,0:1 / 3,3-5,7:1) su entrambi gli estremi — segno che
le "ricadute economico-sociali" delle 16 tabelle sono state costruite
per essere coerenti col costo di Parte VIII, non con quello di Parte
VII. **Decisione dell'autore: fermare la propagazione al solo "costo
del servizio" e "saldo diretto"** — "ricadute economico-sociali",
"saldo complessivo" e "rapporto beneficio-costo" restano
intenzionalmente invariati, da riconciliare col secondo filone
maggiore (benefici indiretti). Corretti costo e saldo diretto nelle 16
tabelle, completato il fix di headcount residuo in 2 tabelle mancate
dal lotto precedente, riscritto il testo di giudizio ormai falso nella
griglia OCSE-DAC, aggiornati 8 paragrafi narrativi — **undicesima
modifica di contenuto al `.docx` canonico nel progetto**. Verificata
l'integrità strutturale (11.110 paragrafi, 1.055 tabelle invariati).

**Nuovo problema scoperto, non ancora risolto**: 6 paragrafi della
sezione "Caso commerciale (Five Case Model)" ri-derivano esplicitamente
la vecchia cifra 25/38/50 da un calcolo bottom-up dichiarato
(~55.000€/incarico × headcount) — lasciati invariati in questo lotto,
sono ora in contraddizione visibile con le tabelle corrette; richiedono
una decisione editoriale distinta non ancora presa.

**Settimo lotto (2026-07-08) — residuo Five Case Model risolto, filone
1 chiuso sul lato Puglia**: decisione dell'autore — mantenere il
benchmark di 55.000€/incarico (riscontro reale di fattibilità
contrattuale, non una stima del costo del servizio), aggiornare
l'headcount a 620/775/900 e ricalcolare la spesa illustrativa che ne
deriverebbe (34,1/42,6/49,5 mln€), distinguendo esplicitamente questo
confronto dal "costo del servizio" autorevole di Parte VII
(54,4/45,2/36,5 mln€). Corretti tutti e 6 i paragrafi — **dodicesima
modifica di contenuto al `.docx` canonico nel progetto**. Verificata
l'integrità strutturale (11.110 paragrafi, 1.055 tabelle invariati).
Il filone 1 (framework degli scenari) è ora chiuso per l'intero nucleo
Puglia.

**Ottavo lotto (2026-07-08) — i 6 cluster regionali chiusi, nessuna
modifica al `.docx`**: istruttoria sui cluster residui con esito
diverso da quanto atteso. **FVG (#631)**: errore di attribuzione
della verifica originale, non del documento — la tabella con "costo
27/40/53 mln€" attribuita al FVG appartiene invece all'Emilia-Romagna
(esatta al centesimo col modello standard, headcount 490/730/960);
confusione nata dal fatto che FVG e Veneto sono le uniche due regioni
della serie prive dell'intestazione ricorrente "STUDIO REGIONALE". Il
FVG non possiede una propria tabella di quadro economico consolidato
— una lacuna strutturale distinta, non un errore. Corretta solo la
nota di verifica. **Marche (#767/#770/#787) e Umbria (#807/#809)**:
non sono errori — entrambe dichiarano esplicitamente nel proprio testo
(Marche §8436; Umbria §8737, sezione "la lacuna dei dati") che le
proprie grandezze economiche sono stime top-down (conti nazionali per
quota di popolazione), non bottom-up (headcount×tariffa): la
divergenza crescente con la scala è strutturale al metodo dichiarato.
Decisione dell'autore: confermare tutte e 6 le righe senza modifiche al
`.docx`.

**Con questo lotto il filone 1 (framework degli scenari) è chiuso per
intero**, incluse tutte le propagazioni regionali. Restano **7 righe**
non riconciliate, tutte del secondo filone maggiore (basi dei benefici
indiretti: #4, #162, #225, #281, #284, #336, #406), non ancora
avviato.

**Nono lotto (2026-07-08) — TRAGUARDO: filone 2 chiuso, tutte e 39 le
discrepanze di Fase 3.2 riconciliate**: istruttoria completa sulle 7
righe residue, nessuna modifica al `.docx` (nessun errore trovato in
nessuna delle 7). Ricalcolata da zero la somma dei 13 domini
monetizzati di Parte IX (68/102/144 mln€), coerente a meno di
arrotondamento con la cifra propria di Parte X (65/98/139) — #162
chiusa. Rintracciato il paragrafo (§2716) che dichiara la base
top-down (conti nazionali per quota di popolazione, ~6,6%) di un
trattamento parallelo di Puglia col template "A-M" (lo stesso dei 19
studi regionali) — stessa metodologia già confermata per Marche/Umbria
— #225 chiusa. Confermato il modello non additivo dello "stack"
IA+formazione tramite la tabella #289 — #281/#284/#336 chiuse.
Rintracciata l'origine della riga #406 in un documento autonomo
completamente separato incorporato nel corpo, con propria numerazione
indipendente — chiusa. La riga #4 (Chisholm 2016 vs OECD 2026) resta
segnalata come lacuna di completezza (non un conflitto), stessa
categoria delle tabelle #73-76.

**Con questo lotto si chiudono tutte e 39 le discrepanze registrate
durante la Fase 3.2. La riconciliazione avviata il 2026-07-08 è
completa: 944 `verificata-ok`, 39 `riconciliata`, 0
`verificata-discrepanza` residue, 72 `n/a-infografica`.** Il benchmark
di successo della Fase 3 dichiarato in apertura di questa sezione
("ciascuna parte marcata come 'validata', senza eccezioni pendenti")
è ora soddisfatto per quanto riguarda le 39 discrepanze aritmetiche di
Fase 3.2 — restano solo i 2 fronti minori già segnalati nella chiusura
complessiva di Fase 3 (2 decisioni minori pendenti di Fase 3.4, e i
limiti di perimetro già dichiarati per Fase 3.3/3.4).

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

### 3.2 — Passata sulla verifica numerica (esaustiva, multi-sessione — CHIUSA il 2026-07-06)

Registro dedicato: `_meta/verifica-numerica-tracker.md`, popolato il
2026-07-06 con tutte le 1.055 tabelle del Tomo I (dopo la rimozione di
Parte I/II breve), classificate per tipo: **959 "dati"** (tabelle con
contenuto numerico verificabile), **55 "infografica"** (segnaposto di
progettazione grafica per Canva — non tabelle di dati; coerente con
l'osservazione del prompt operativo §6 sulla presenza di residui
infografici da completare/rimuovere), **41 "altro"** (piccole/monocolonna).

**TRAGUARDO FINALE: 1.055 righe su 1.055 verificate — Fase 3.2 CHIUSA**
(944 `verificata-ok`, 39 `verificata-discrepanza`, 72 `n/a-infografica`;
zero righe `da verificare`). Completate in questa sessione le 65 righe
residue del nucleo Puglia (Parti I-VII, righe #1-84): in gran parte
tabelle qualitative/definitorie e segnaposto infografici, nessuna nuova
discrepanza aritmetica, con alcuni riscontri incrociati esatti (es.
costo formazione per modalità #64: 0,4+0,8+0,9+1,9=4,0 mln€/anno esatto;
BCR 7-8:1 su questo costo dà 28-32 mln€/anno, coincidente esattamente
col dichiarato in #68). Corretto anche un errore di editing introdotto
in questa stessa sessione (due righe infografiche, #29 e #31, erano
state accidentalmente cancellate durante una sostituzione; individuato
con un controllo di integrità sul conteggio delle righe e ripristinato).
**L'intera sezione "Tomo II" (19 studi regionali, righe #425-1045) e la
sezione UE-27 finale (righe #1046-1055) erano già state completamente
verificate in precedenza in questa sessione.** La sezione UE-27
presentava un riscontro
incrociato esatto (fasce di distanza dal benchmark 8+11+8=27, copertura
esatta di tutti gli Stati Membri UE senza omissioni né duplicazioni) e
nessuna discrepanza aritmetica propria (è dichiaratamente un
"placeholder" con cifre attribuite, coerente col README). Corrette
anche due righe rimaste erroneamente "da verificare" (#874, #934,
tabelle di confine di Campania e Sicilia, già implicitamente verificate
nei rispettivi blocchi).
**Le 65 righe ancora "da verificare" sono tutte concentrate nelle righe
#1-84 (Parti I-VII del corpo Puglia), un gap preesistente a questa
sessione di lavoro** — tutte le tabelle oggetto del lavoro di questa
sessione (19 regioni + UE-27) sono verificate al 100%. Prossimo passo:
completare la verifica delle 65 tabelle residue del nucleo Puglia in
una sessione futura per chiudere integralmente la Fase 3.2.
**Blocco Valle d'Aosta (righe #1006-1045) completato — 19° e ultimo
studio regionale con banner**: il blocco più denso di discrepanze fra
le 19 regioni. Conflitto diretto fra due tabelle dello stesso blocco sul
saldo complessivo Base/Espansivo (+8,1/+12,1 in tabella #1006 vs
+6,1/+8,5 nelle tabelle #1020/#1039, queste ultime coerenti con
ritorno−costo); un componente di risparmio che non somma al totale
dichiarato; **il BCR non si ricostruisce da ritorno/costo per nessuno
dei tre scenari** (primo caso su 19 regioni in cui l'intera serie, non
solo l'Espansivo, non torna); un costo per incarico implicito
(86.700-100.000€) molto più alto e non costante rispetto al parametro
standard ~55.000€. Tutto registrato in `_meta/parking-lot.md`.
**Blocco Sardegna (righe #974-1005) completato** (telaio abbreviato,
manca l'intera sezione Appendici A-E): tutte le tabelle numeriche
verificate esatte (170/250/340 psicologi ↔ 9/14/19 mln€, coerente col
modello standard nonostante il modello organizzativo dipartimentale a
dipendenza; multi-criterio 77,40/39,20). Nessuna discrepanza né residuo
di copia.
**Blocco Sicilia (righe #935-973) completato** (telaio completo A-M):
tutte le tabelle numeriche verificate esatte (520/780/1.030 psicologi ↔
29/43/57 mln€, coerente col modello standard ~55.000€/incarico;
multi-criterio 78,35/39,20). Nessuna discrepanza né residuo di copia.
**Blocco Campania (righe #875-914) completato, pienamente coerente col
modello standard (nessuna discrepanza). SCOPERTA (righe #915-933): oltre
al Molise, anche Basilicata e Calabria sono blocchi regionali non
censiti** — il totale corretto è **19 studi regionali**, non 16 né 17.
Tutti e tre condividono l'assenza del banner "Elemento/Definizione" e un
secondo tratto comune: un costo per incarico costante e moderatamente
più alto (~60.700-66.700€, scomposto in compensi 50.000€ + sovrattassa
variabile) rispetto al parametro "~55.000€" standard delle altre 16
regioni — uno schema di scomposizione del costo mai visto nei blocchi
con banner, ulteriore indizio che questi tre blocchi siano stati
prodotti con un template diverso. A differenza del Molise (conflitto fra
tabelle sullo stesso scenario), Basilicata e Calabria sono internamente
coerenti: l'unico problema è lo scarto costante rispetto al parametro
dichiarato altrove. Tutto registrato in `_meta/anomalie-corpus.md` e
`_meta/parking-lot.md`.
**SCOPERTA precedente (righe #863-873): il blocco "Tomo II" ha in realtà
17 studi regionali, non 16 come corretto lo stesso giorno in
`_meta/anomalie-corpus.md`** — manca il Molise, l'unico blocco privo
del banner "Elemento/Definizione" che aveva reso invisibile la sua
esistenza alla mappatura strutturale iniziale (individuato solo dalla
verifica tabella-per-tabella). Il blocco Molise (11 tabelle) presenta
un conflitto interno inedito: due tabelle dello stesso blocco
dichiarano costi diversi (1,0 vs 0,4 mln€) per il medesimo scenario
Conservativo, e una terza tabella usa entrambi i valori in righe
diverse — il primo caso di incoerenza *interna al blocco* piuttosto che
fra il blocco e un modello standard esterno. Anche qui il consueto
scarto sul BCR Espansivo (4,63 calcolato vs 4,8 dichiarato). Tutto
registrato in `_meta/parking-lot.md` e `_meta/anomalie-corpus.md`,
nulla corretto silenziosamente.
**Blocco Abruzzo (righe #822-862) completato** (telaio completo A-M):
tutte le tabelle numeriche verificate esatte (85/180/280 psicologi ↔
5/10/15 mln€, coerente col modello standard ~55.000€/incarico;
multi-criterio 78,15/39,50). Nessuna discrepanza né residuo di copia —
conferma che il sotto-tipo "scarto crescente con la scala" (Marche,
Umbria) non è universale.
**Blocco Umbria (righe #795-821) completato** (telaio abbreviato a 27
tabelle, senza glossario): due nuove discrepanze dello stesso sotto-tipo
già aperto in Marche — scarto crescente con la scala fra costo
dichiarato e modello standard ~55.000€/incarico (tabella #807:
Cons. ~4% sotto, Base ~21,2% sopra, Espansivo ~38,2% sopra), qui reso
esplicito dal fatto che la tabella #818 della stessa regione dichiara
sia il parametro (~55.000€) sia l'headcount (~210) senza che il
prodotto torni; effetto a cascata sul BCR Espansivo (tabella #809: 4,63
calcolato vs 4,8 dichiarato). Registrate in `_meta/parking-lot.md`.
**Blocco Marche (righe #757-794) completato** (telaio completo A-M):
cinque nuove discrepanze — uno scarto costo/headcount **crescente con
la scala dello scenario** (Cons. ~1,8%, Base ~7,0%, Espansivo ~37,6%,
tabella #767), un conseguente scarto sul BCR Espansivo (4,68 calcolato
vs 4,9 dichiarato, tabella #770), un difetto strutturale non aritmetico
(testo di cella troncato e confluito nella cella successiva, tabella
#778) e una discrepanza minore nel punteggio multi-criterio (tabella
#783). Tutte registrate in `_meta/parking-lot.md`, nessuna corretta
silenziosamente.
**Blocco Lazio (righe #715-756) completato** (telaio completo A-M,
unica regione finora senza alcun servizio pregresso — "istituzione ex
novo"): tutte le tabelle numeriche verificate esatte (620/930/1.230
psicologi ↔ 34/51/68 mln€, coerente col modello standard
~55.000€/incarico; multi-criterio 78,00/39,50). Nessuna discrepanza né
residuo di copia — terza conferma consecutiva (dopo Emilia-Romagna e
Toscana).
**Blocco Toscana (righe #673-714) completato** (telaio completo A-M):
tutte le tabelle numeriche verificate esatte (400/600/790 psicologi ↔
22/33/44 mln€, coerente col modello standard ~55.000€/incarico;
multi-criterio 82,65/39,25/+43,40). Nessuna discrepanza né residuo di
copia — seconda conferma consecutiva che il modello standard regge
nella maggioranza dei blocchi regionali.
**Blocco Emilia-Romagna (righe #632-672) completato** (telaio completo
A-M): tutte le tabelle numeriche verificate esatte (490/730/960
psicologi ↔ 27/40/53 mln€, pienamente coerente col modello standard
~55.000€/incarico; multi-criterio 81,45/39,25/+42,20). Nessuna
discrepanza né residuo di copia in questo blocco — conferma che
l'anomalia costo/headcount del FVG (4x) è un'eccezione regionale, non
un difetto sistemico del modello economico. Nota di confine: la tabella
#673 (dati Toscana) precede il banner del blocco Toscana (#674), unica
inversione di posizione osservata finora.
**Blocco Friuli-Venezia Giulia (righe #619-631) completato**: telaio
parziale A-C (coerente con lo stato dichiarato in tabella #255). Due
anomalie: (1) un quarto residuo di copia fra blocchi regionali (tabella
#619, "Residenti sardi" invece del demonimo corretto per il FVG); (2)
la discrepanza costo/headcount più acuta finora riscontrata (tabella
#631: costo del servizio dichiarato 27/40/53 mln€/anno per un headcount
di 130/195/260 psicologi — il modello standard ~55.000€/incarico usato
in tutte le altre regioni predirebbe ~7,15/10,7/14,3 mln€, uno scarto di
circa 4x). La tabella #631 resta internamente coerente su saldo diretto,
saldo complessivo e BCR usando le sue stesse cifre di risparmi/ricadute/
costo. Entrambe registrate in `_meta/parking-lot.md`.
**Blocco Veneto (righe #580-618) completato**: tutte le tabelle
numeriche verificate esatte (530/800/1.050↔30/45/58 mln€, multi-criterio
80,7/39,25/+41,45), nessun residuo di copia riscontrato.
**Blocchi Piemonte (#424-465), Liguria (#466-497), Lombardia (#498-539)
e Trentino-Alto Adige (#540-579) completati**: tutte le tabelle
numeriche verificate esatte o quasi esatte (Piemonte: 470/700/920↔
26/38/51 mln€, multi-criterio 81,75/39,25/+42,50; Liguria: 170/250/330↔
9/14/18 mln€, multi-criterio 80,80/39,25; Lombardia: 1.100/1.700/2.190↔
60/95/120 mln€, multi-criterio 80,7/39,25/+41,45; Trentino-Alto Adige:
120/180/240↔7/11/14 mln€, multi-criterio 81,00/39,20). **Nuovo tipo di
difetto individuato nel blocco Trentino-Alto Adige**: due tabelle
(#571, #579) contengono residui di copia da altri blocchi regionali non
aggiornati (un comparatore "PNES" non pertinente; una voce di glossario
sulla mobilità sanitaria che descrive erroneamente la Sicilia) — un
difetto di contenuto, non aritmetico, registrato in
`_meta/parking-lot.md`,
stessa metodologia già applicata alla Puglia.
Righe #350-423 coprono la seconda ricorrenza del telaio regionale
"Parte A-M" (quasi interamente duplicati esatti già verificati) e il
capitolo IA-Formazione specifico per la Puglia con materiale
bibliografico sul Collaborative Care — con le tabelle #405-406 che
aggiungono una sesta cifra di beneficio totale (~200 mln€, BCR 5,3:1,
vicino alla fascia della "stima di vertice" 6-12:1 già nota) alla
seconda scoperta maggiore (si veda sotto).
Righe #297-349 coprono la prima ricorrenza completa del telaio
regionale "Parte A-M" più Appendici A-E e le mappature strutturali del
telaio Five Case Model (Appendice XXIV) — quasi interamente duplicati
esatti di tabelle già verificate, salvo la tabella #334 (Appendice XX),
una scomposizione dettagliata dei costi diretti annui verificata esatta
al centesimo (38.810.800€), che introduce una quinta cifra di headcount
(800 FTE) per lo scenario "Base", e due discrepanze minori (tabella
#339, avvio del programma formativo; tabella #336, duplicato della
discrepanza già nota sulla tabella #284).
Copertura completa (Tab. IV.1-IV.4 della Revisione OCSE 2026 e tutte le
tabelle "dati"/"altro"/"infografica" di): Parte VII — Costi diretti —,
Parte VIII — Risparmi diretti —, Parte IX — Benefici indiretti, 16
domini —, Parte X — Sintesi economica integrata: ICER, SROI, sintesi
multi-criterio, saldo consolidato —, Parte XI — Modello di Markov, PSA,
previsioni falsificabili —, Parte XII — Equità territoriale e digitale —,
Parte XIII — Cornice etico-giuridico-organizzativa —, le tabelle di
Parte XIV/XV/Appendice I (identificate sotto i banner decorativi
"Parte I/L/M" del telaio Five Case Model, righe #216-227), Appendice III
(Batteria integrale di indicatori di monitoraggio, righe #235-242),
Appendice IV (Riconciliazione e tabella unica dei valori, righe
#243-245 — contiene una riconciliazione esplicita "stima di vertice"
[~270 mln, BCR 6-12:1] vs "revisione su dati primari" [~20-50 mln, BCR
3,6-5:1] per il risparmio diretto, con ragioni della differenza
dichiarate nel testo; non copre però la discrepanza sui "benefici
indiretti" già registrata nella SECONDA SCOPERTA MAGGIORE, che resta
irrisolta), Appendice V (Analisi delle lacune, righe #246-256 — le
ultime tre risultano mislabeled: contengono in realtà il registro file
dell'Appendice XXXIII, 315 file verificati esatti), Parte D (Efficacia
clinica), Appendice VIII (Percorso clinico stepped-care), Appendice IX
(Modello tariffario — qui per la prima volta derivata e verificata da
zero l'aritmetica completa che produce i costi ~25/38/50 mln€ da
tariffa×ore×incarichi, sullo schema di headcount 450/700/900), Appendice
X (Specifica estrazione dati), Appendice XI (Protocollo di rilevazione),
Appendice XII (Dispositivi terapeutici digitali), Appendice XIII
(quantificazione dell'ulteriore riduzione da IA/formazione, righe
#282-291 — con una nuova discrepanza sui costi incrementali e un
raffinamento alla tabella #289, si veda sotto) e le prime tabelle di
Appendice XVII (telaio "Parte A-M", righe #292-296):

- **verificata-ok** (dettaglio principale): Tab. IV.2 (risparmi per canale/scenario); tabella
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
  nessuna tabella numerica presente, nessuna aritmetica applicabile);
  tabelle di implementazione (RE-AIM/CFIR, dispiegamento, rischi,
  copertura finanziaria — Parte XIV), monitoraggio (categorie di
  indicatori, cronoprogramma, costruzione di indici compositi — Parte
  XV) e sintesi valutativa (criteri DAC/OCSE, analisi multi-criterio con
  punteggio ponderato ricalcolato esatto — Parte XV), tutte coerenti.
- **11 verificata-discrepanza** (di cui 1 nuova in questo lotto): Tab. IV.3 (ROI non ricostruibile dai dati
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

**Secondo raffinamento (tabella #225, sintesi Five Case Model):** una
tabella di saldo economico consolidato — internamente perfetta (saldo
diretto, saldo complessivo e rapporto beneficio-costo tutti ricalcolati
esatti) — cita "Ricadute economico-sociali" = ~70/~130/~200 mln€ per gli
scenari "Cons./Base/Esp.": una **quarta cifra** per la stessa grandezza
nominale. **Il quadro completo per lo scenario centrale/intermedio è
quindi: ~27 mln€ (Parte IV/OCSE 2026, piramide), ~98 mln€ (Parte X), ~104
mln€ (somma dei 16 domini di Parte IX), ~130 mln€ (tabella #225).**
Nessuna delle quattro cifre è dichiarata esplicitamente come autorevole
rispetto alle altre; nessuna correzione applicata. Riconciliazione
rimandata a valle, coerentemente con la decisione dell'autore.

**Discrepanza aggiuntiva (tabella #281, Appendice XIII — stack
formazione+IA):** il "risparmio diretto a regime dello stack complessivo"
(315-350 mln€) non si ricostruisce sommando il "modello base" (~270
mln€) con gli strati formativo (~45-55 mln€) e strumentale IA (~60-110
mln€) descritti nella stessa tabella — una somma semplice darebbe
375-435 mln€. Non è chiaro se "315-350" comprenda entrambi gli strati,
uno solo, o applichi un fattore di non sovrapposizione non esplicitato.
Registrata in `_meta/parking-lot.md`, non corretta; discrepanza distinta
dalle due scoperte maggiori (riguarda l'affinamento del modello con IA,
non lo schema di scenario di base).

**Raffinamento (tabella #289):** una tabella successiva, verificata
pienamente coerente, offre un modello alternativo per lo stesso
incremento IA — risparmio totale = base (≈270 mln€) + **solo**
l'incremento IA, la cui entità dipende dalla "profondità di adozione"
esplicitamente etichettata "(effetto formazione)" — senza un addendo
formativo separato. Con questo modello tutti e tre gli scenari tornano
esatti. Suggerisce che le tabelle #281/#284 (che sommano formazione e IA
come due strati) trattino come additiva una componente che è in realtà
abilitante. Nessun modello dichiarato autorevole sull'altro; non
corretto silenziosamente.

**Ulteriore discrepanza minore (tabella #284):** il "costo incrementale
(IA+formazione)" dichiarato (≈5/5,3/5,5 mln€) non corrisponde alla somma
dei costi separatamente dichiarati altrove (formativo ~4 mln + IA ~5
mln ≈ 9 mln) — sembra contare solo la componente IA. Non corretta
silenziosamente.

**Terzo raffinamento (tabelle #405-406):** una coppia di tabelle,
entrambe internamente esatte, introduce una **sesta cifra** di beneficio
totale per lo scenario centrale/intermedio: ~200 mln€ (contro costo ~38
mln€), con BCR = 5,3:1 — sistematicamente più alto del BCR "consolidato"
(3,6/4,3/5,0:1) usato ovunque nella piramide, e più vicino alla fascia
della "stima di vertice" (6-12:1) già notata nella tabella #243. **Il
quadro completo per lo scenario centrale/intermedio è quindi: ~27 mln€
(OCSE 2026/piramide), ~98 mln€ (Parte X), ~104 mln€ (Parte IX), ~130
mln€ (tabella #225), ~164 mln€ ("ritorno complessivo", tabella #306),
~200 mln€ (tabelle #405-406).** Sei cifre diverse, nessuna dichiarata
autorevole sulle altre. Non corretto silenziosamente; riconciliazione
rimandata a valle.

**⚠️ SCOPERTA STRUTTURALE (2026-07-06) — la sezione "Tomo II" in coda al
Tomo I è molto più estesa del previsto.** Proseguendo la verifica oltre
la riga #423, si è confermato che a partire dalla tabella #425 (paragrafo
5789, banner "Blocco Regionale I — Italia settentrionale") il file
contiene **16 studi regionali completi** (Piemonte, Liguria, Lombardia,
Trentino-Alto Adige, Veneto, Friuli-Venezia Giulia, Emilia-Romagna,
Toscana, Lazio, Marche, Umbria, Abruzzo, Campania, Sicilia, Sardegna,
Valle d'Aosta), ciascuno con il telaio "Parte A-M + Appendici A-E"
completo (non un riassunto), seguiti da un accenno a una sezione UE-27
nell'ultima tabella (#1055). Questo blocco copre **circa 630 delle 1.055
tabelle del file (60%)** — molto più della "sezione sommaria" descritta
nel README di `tomo-1-puglia/` (che la qualifica comunque già come
placeholder non autorevole "in caso di conflitto"). Documentato in
dettaglio in `_meta/anomalie-corpus.md` (voce 2). **Nessuna decisione
presa su come trattare questo nella Fase 3.2** fino alla decisione
dell'autore (2026-07-06): **verifica esaustiva anche su questo blocco**,
con lo stesso rigore già applicato al corpo Puglia — coerente con la
scelta già fatta di verifica esaustiva e non campionaria. La Fase 3.2
prosegue quindi oltre la riga #423 senza distinzioni di trattamento.

**Le restanti ~502 righe sono ancora "da verificare"** (di cui ~435
appartengono al blocco "Tomo II" per le 11 regioni ancora da verificare
dopo Piemonte, Liguria, Lombardia, Trentino-Alto Adige e Veneto —
Friuli-Venezia Giulia, Emilia-Romagna, Toscana, Lazio, Marche, Umbria,
Abruzzo, Campania, Sicilia, Sardegna, Valle d'Aosta — più l'eventuale
sezione UE-27 finale).
Data la scala (959 tabelle dati), questa sotto-fase richiede molte
sessioni successive per essere completata: l'autore ha scelto
esplicitamente la verifica esaustiva (non un campionamento a rischio),
riconoscendo che questo comporta un impegno pluri-sessione.

### 3.3 — Passata sul registro linguistico (due lotti CHIUSI, il secondo il 2026-07-07)

Registro dedicato: `_meta/registro-linguistico-tracker.md`. Chiarimento di
perimetro emerso in apertura: il requisito del prompt operativo §5 sulla
"definizione di ogni acronimo al primo utilizzo" si applica **a ciascun
prodotto della piramide** (Livelli 1-5), non a ciascuna parte del Tomo I
— questo ha spostato il baricentro della verifica sui quattro derivati
sintetici (Livelli 1-4), dove l'intensità richiesta è massima o alta,
prima ancora che sul corpo integrale (dove è "non nulla ma
proporzionalmente minore").

**Correzioni applicate** (4, tutte di tipo "aggiunta di glossa breve",
nessuna riscrittura di prosa argomentativa):
- **ROI**: mai definito in nessuno dei quattro Livelli nonostante
  compaia nella frase-tesi di apertura di ciascuno — corretto con
  l'aggiunta di "(ritorno sull'investimento)" al primo uso in tutti e
  quattro i file.
- **QALY**: sigla nuda affiancata alla soglia di costo-efficacia nei
  Livelli 2 e 3 senza tag esplicito — corretto con l'aggiunta di
  "(anno di vita ponderato per la qualità)" al primo uso in entrambi.
- **ISPOR-SMDM**: citato senza espansione nel Livello 4 — corretto con
  espansione inline.
- **Elenco delle abbreviazioni** aggiunto come nuova sezione 12 del
  Livello 4 (18 voci), il prodotto con la densità di sigle più alta;
  non aggiunto ai Livelli 1-3 per proporzionalità (1-3 sigle ciascuno,
  sufficiente la definizione inline).

**Verificato e giudicato non azionabile** (documentato, nessuna
modifica): terminologia "Psicologo di Base" (variazione di
capitalizzazione nel Tomo I interamente spiegabile da ruolo grammaticale
o da una convenzione di sottotitolo già uniforme, nessuna incoerenza
reale su 737 occorrenze totali); "cura per intensità crescente" vs "cura
a intensità crescente" (2 occorrenze minoritarie, entrambe dentro
citazioni bibliografiche del modello NHS, non nella prosa propria dello
studio); MMG/PLS/HTA/CBT usati come sigle nude in punti dove il concetto
è già stabilito per esteso altrove nello stesso documento o in un
rimando esplicito che lo definisce.

**Secondo lotto (2026-07-07)** — verifica riga per riga delle regole
esplicite del §5 sui Livelli 1-3 (dove l'intensità richiesta è
"massima"), rimasta scoperta dal primo lotto. Metodologia: scissione
**meccanica** delle frasi lunghe, solo in corrispondenza di virgole,
punti e virgola o due punti già esistenti che separano due proposizioni
già compiute — nessuna parola aggiunta o tolta, nessuna riscrittura di
prosa argomentativa, frase-tesi da 76 parole (identica nei quattro
prodotti per requisito di progetto) intoccata.

- **Frasi sotto le 25 parole** (soglia indicativa del prompt, non
  assoluta): Livello 1, 5/12 frasi lunghe → 4/13 dopo 1 scissione;
  Livello 2, 16/32 → 14/40 dopo 8 scissioni; Livello 3, 30/41 → 25/57
  dopo 16 scissioni. Le frasi lunghe residue rientrano in tre categorie
  non azionabili: la frase-tesi protetta; proposizioni singole senza un
  punto di scissione meccanico disponibile; frasi di rimando
  bibliografico dalla struttura idiomatica.
- **Hedging nelle raccomandazioni**: le sezioni "La raccomandazione" /
  "Che cosa fare" dei tre Livelli risultavano già pulite — le cautele
  metodologiche erano già confinate nelle sezioni dedicate "I limiti
  dichiarati" / "Le incertezze dichiarate". Nessuna modifica necessaria.
- **Latinismi e arcaismi**: ricerca mirata nei tre Livelli; trovati solo
  "status quo" (×3, termine tecnico consolidato di confronto tra
  opzioni di policy) ed "ex post" (×1, termine tecnico), entrambi
  esplicitamente esentati dal piano approvato. Nessuna sostituzione.

Dettaglio completo in `_meta/registro-linguistico-tracker.md`, sezione
5.

**Perimetro non coperto dai due lotti**: le 33 Appendici Integrative
del Tomo I, il Tomo II e la sezione UE-27 non sono state sottoposte alla
stessa verifica sistematica (attività distinta, da programmare a parte
data la scala); le regole del §5 non sono state riverificate riga per
riga sulle Parti I-XV del Tomo I stesso (dove l'intensità richiesta è
"non nulla ma proporzionalmente minore").

### 3.4 — Passata sull'apparato editoriale (sette lotti, il settimo CHIUSO il 2026-07-07 — tutti i nove item coperti)

Registro dedicato: `_meta/apparato-editoriale-tracker.md`. Nove item di
verifica individuati dal prompt operativo (§ righe 122-133): (1)
uniformità Chicago Style delle note; (2) note non orfane; (3)
numerazione di tabelle/figure; (4) titoli di tabella descrittivi con
fonte; (5) rimozione di residui placeholder infografici; (6) uniformità
tipografica; (7) coerenza dei rimandi interni; (8) front/back matter
standard; (9) versioning esplicito dei file. In questo primo lotto,
analisi programmatica diretta sull'XML del `.docx` (non sulla sola
lettura visiva, stesso rigore della Fase 3.2) per gli item 2, 3 e 5;
item 1, 4, 6, 7, 8, 9 non ancora avviati (richiedono metodologie diverse,
qualitative o di scala paragonabile alla Fase 3.2).

**Item 2 (note orfane)**: riconfermato pulito con cross-check esplicito
ID-per-ID fra riferimenti nel testo (3.915) e definizioni in
`footnotes.xml` (3.917, di cui 2 segnaposto strutturali Word) — zero
orfane, zero mancanti, zero duplicate.

**Item 2bis, nuova scoperta, RISOLTA**: il controllo "orfana/non orfana"
verifica solo la corrispondenza degli ID, non il contenuto. Verifica
aggiuntiva del corpo di ogni nota: **111 note su 3.915 (2,8%) hanno
corpo interamente vuoto** (solo il marcatore, nessun testo recuperabile),
tutte regolarmente richiamate nel testo. Il `.docx` non è mai stato
modificato in questo progetto prima d'ora (Fasi 3.1-3.3 hanno lavorato
solo sui Livelli 1-4 e sui tracker) — la perdita è preesistente al
progetto di ristrutturazione, non introdotta da esso. `_meta/cut-darlings.md`
non documenta alcuna rimozione intenzionale di note. **Decisione
dell'autore (2026-07-07): segnalare come limite noto**, nessun tentativo
di recupero (nessun backup disponibile). Aggiunto il punto 6 alla
sezione "Limiti dichiarati" del Livello 4
(`_livelli-piramide/livello-4-sintesi-tecnica.md`, §10). Nessuna
modifica al contenuto delle note (resta impossibile senza fonte
esterna). Elenco completo dei 111 ID in
`_meta/apparato-editoriale-tracker.md` e in `_meta/parking-lot.md`.

**Item 3 (numerazione tabelle)**: due pattern distinti di duplicazione,
non uno solo come inizialmente registrato. (a) 35 etichette a lettera
(A.1-M.3) duplicate 3-37 volte ciascuna — atteso, dovuto alla
ripetizione del telaio di appendici in ciascuno dei 19 blocchi regionali
del Tomo II più il nucleo Puglia; nessun difetto, decisione dell'autore
ancora pendente su rinumerare o mantenere con nota esplicita. (b)
**7 etichette numeriche (1.1, 2.1, 4.1, 6.1, 7.1, 8.1, 9.1), duplicate
esattamente 2 volte ciascuna — RISOLTA.** Collisione fra la numerazione
del nucleo Puglia (Parti I-IX) e quella della sezione UE-27, che
ripartiva da 1.1 invece di proseguire o usare un proprio prefisso.
**Decisione dell'autore (2026-07-07): prefisso esplicito alla sezione
UE-27.** Azione completata: le 8 etichette della sezione UE-27
(le 7 collidenti più "Tabella 5.1", uniformata per coerenza pur non
collidendo — il corrispondente del nucleo Puglia è "Tabella 5.1.A")
rinominate da "Tabella N.M." a "Tabella UE.N.M." **direttamente nel file
`.docx` canonico — prima modifica di contenuto a questo file in tutto
il progetto** (le Fasi 3.1-3.3 avevano lavorato solo sui prodotti
derivati e sui tracker). Verificata l'integrità strutturale dopo la
modifica: 11.110 paragrafi e 1.055 tabelle invariati; zero duplicazioni
numeriche residue tra nucleo Puglia e sezione UE-27.

**Item 5 (residui placeholder)**: riconfermato pulito — nessun
placeholder reale, solo falsi positivi di sottostringa (numerazione
romana delle Appendici, parola italiana "metodo:").

**Secondo lotto (2026-07-07) — item 6 (uniformità tipografica) e item
9 (versioning)**:
- **Apostrofi — RISOLTO**: 48 apostrofi dritti (elisioni italiane in
  prosa: l', dell', sull', ecc.) sostituiti con l'apostrofo tipografico
  già usato nelle altre 26.640 occorrenze — seconda modifica di
  contenuto al `.docx` canonico. Verificata l'integrità strutturale
  post-modifica (11.110 paragrafi, 1.055 tabelle invariati).
- **Virgolette dritte**: le uniche 2 occorrenze sono nel codice di campo
  Word del sommario (`TOC \o "1-2" \h \z \u`), non testo di prosa — non
  toccate.
- **Non risolte, rimandate**: coesistenza di virgolette angolate «» e
  curve "" in prosa (567/568 vs 207/209 occorrenze — non chiaro se
  distinzione intenzionale o disomogeneità); coesistenza di trattino
  breve e medio negli intervalli numerici (700 vs 499 occorrenze — non
  risolvibile con sostituzione globale perché alcuni trattini brevi sono
  in realtà identificativi legittimi come ISBN o date ISO). Entrambe
  richiedono classificazione qualitativa caso per caso, documentate in
  `_meta/parking-lot.md`.
- **Numeri e date**: verificato pulito — formato italiano coerente
  (punto per le migliaia, virgola per i decimali), nessuna commistione
  nei formati di data.
- **Item 9 (versioning)**: soddisfatto tramite la convenzione già in uso
  nel progetto (cronologia dei commit Git, con data e changelog per ogni
  modifica) — non introdotta una convenzione di versione interna al
  `.docx`, assente altrove nel corpus.

Due modifiche di contenuto al file `.docx` finora in questo Fase 3.4
(rinumerazione UE-27, correzione apostrofi).

**Terzo lotto (2026-07-07) — item 7 (coerenza dei rimandi interni) e
item 8 (front/back matter)**:

**Item 7**: i riferimenti numerici a "Parte [romano]" e "Appendice
[romano]" sono verificati puliti in tutto il documento — zero rimandi
fuori dall'intervallo esistente (Parti I-XV, Appendici I-XXXIII). Sui
soli 5 rimandi puntuali "cfr. …" presenti nell'intero corpus, due
difetti reali: (1) "cfr. nota 5" (paragrafo 479) punta, in ordine di
lettura, a una nota sul regolamento UE sull'IA anziché al caveat
Unützer/IMPACT trial di cui tratta il paragrafo — la nota pertinente è
la 3ª in ordine di lettura, non la 5ª; compatibile con un
disallineamento da rinumerazione precedente a questo progetto; (2) 6
occorrenze di "cfr. Volume 0.A"/"Volume 0.B" rimandano a
un'intestazione "Volume 0" che **non esiste in nessuno degli 11.110
paragrafi** del documento (verificato esaustivamente) — bersaglio non
definito, causa non accertabile dal solo testo (autoreferenza implicita
al Tomo I stesso, o documento distinto mancante). **Entrambi non
corretti silenziosamente: decisione dell'autore richiesta.**
Scoperta collaterale: la sezione UE-27 ha una propria struttura interna
in "Capitoli" 1-9 (distinta dalle "Parti" del nucleo Puglia); i rimandi
"cfr. Capitolo N" trovati altrove sono risultati validi rispetto a
questa struttura o a un progetto esterno già dichiarato come tale.
**Nuova scoperta maggiore, non prevista da alcun item testuale della
checklist**: 62 occorrenze di sequenze di asterischi incastonate a metà
parola (es. "dell'******efficacia"), concentrate nel telaio regionale
del Tomo II (intestazione "Parte D — L'efficacia e l'evidenza" e
didascalie di tabella D.1/F.3/G.1/G.2/H.2/M.2) — pattern compatibile con
markup Markdown di grassetto (`**testo**`) non convertito in
formattazione Word durante l'assemblaggio del documento. Non corretto
silenziosamente: rimuovere gli asterischi presuppone di sapere se il
grassetto andasse applicato o solo eliminato — tocca la formattazione
voluta dall'autore. **Decisione dell'autore richiesta.**

**Item 8**: front matter del Tomo I completo (frontespizio, prefazione
equivalente, indice) tranne l'elenco delle abbreviazioni, assente nel
Tomo I stesso (esiste solo nel Livello 4, un prodotto derivato);
l'indice è collocato dopo la prefazione anziché prima come nel modello
dichiarato (World Bank Group Style Guide) — scostamento minore. Back
matter: bibliografia distribuita in sezioni "Note Bibliografiche
Integrali" dopo diverse Parti (almeno 8 occorrenze) anziché consolidata
in un'unica sezione finale — modello alternativo legittimo, non
necessariamente un difetto; nessun glossario consolidato per il nucleo
Puglia ("Appendice E — Glossario" ricorre 16 volte ma sempre come
glossario locale a un singolo blocco regionale del Tomo II). Entrambi i
gap richiederebbero produzione di contenuto redazionale nuovo, non una
correzione meccanica — non risolti in questo lotto.

Tutto il lavoro del terzo lotto è stato lettura e analisi, nessuna
modifica al `.docx`.

**Quarto lotto (2026-07-07) — tre decisioni dell'autore ricevute e
applicate sulle scoperte del terzo lotto**:
- **"cfr. nota 5" → corretto in "cfr. nota 3"** (paragrafo 479) — terza
  modifica di contenuto al `.docx` canonico nel progetto.
- **6 rimandi a "Volume 0.A/0.B" → segnalati come limite noto**,
  nessuna modifica applicata (bersaglio non accertabile senza fonti
  esterne).
- **62 occorrenze di sequenze di 3+ asterischi → rimossi solo gli
  asterischi**, senza applicare grassetto (non verificabile quale fosse
  l'enfasi originale) — quarta modifica di contenuto al `.docx`
  canonico (79 sequenze in 40 run). Deliberatamente non toccate 25
  sequenze singole e 16 doppie residue di asterischi, fuori dallo scopo
  esatto della decisione presa (alcune sono marcatori di nota
  legittimi, altre sembrano lo stesso tipo di markup non convertito ma
  in contesti diversi — es. intestazione di pagina ricorrente, template
  di lettera, annotazioni di sensibilità — non descritti nella
  decisione, registrate a parte per un lotto futuro).
- Verificata l'integrità strutturale dopo entrambe le modifiche: 11.110
  paragrafi e 1.055 tabelle invariati in entrambi i casi.

Quattro modifiche di contenuto al `.docx` finora in tutta la Fase 3.4
(rinumerazione UE-27, correzione apostrofi, correzione nota 5→3,
rimozione asterischi 3+). Due decisioni dell'autore restano pendenti
(item 3a — etichette a lettera A.1-M.3; residui di 1-2 asterischi in
contesti diversi), registrate in `_meta/parking-lot.md`.

**Quinto lotto (2026-07-07) — item 4 (titoli di tabella e indicazione
della fonte)**: unico item per cui è stato possibile un **censimento
completo delle 1.055 tabelle**, non solo un campione, perché la
domanda ("esiste una didascalia? esiste una fonte?") è verificabile
programmaticamente sulla posizione dei paragrafi adiacenti — il corpus
usa due convenzioni coesistenti (didascalia prima della tabella nel
nucleo Puglia, dopo nei blocchi regionali del Tomo II e nella sezione
UE-27). Risultati:
- **Copertura delle didascalie: 993/1.055 (94,1%)**. Delle 62 tabelle
  senza didascalia rilevata, 20 sono segnaposto infografici già noti
  (nessuna attesa); su un campione di 5 delle restanti 42, trovate due
  incoerenze minori non generalizzate al resto del corpus: una
  didascalia etichettata "Schema" anziché "Tabella" (tabella #71), una
  didascalia priva di numero (tabella #821, blocco Abruzzo).
- **Descrittività (valutazione qualitativa su ~15 didascalie + 5
  letture integrali)**: positiva — nessuna didascalia vaga o dipendente
  dal contesto individuata nel campione.
- **Indicazione della fonte: solo 10/1.055 tabelle (0,95%) — gap quasi
  universale, il risultato più rilevante di questo item.** La
  provenienza dei dati è normalmente affidata a citazioni discorsive o
  di nota nel testo circostante, non a un'annotazione dedicata sotto la
  tabella (le didascalie stesse non portano quasi mai un richiamo di
  nota: 0/471 nel campione controllato). Non corretto silenziosamente:
  richiederebbe produzione redazionale tabella per tabella, non una
  correzione meccanica.

Nessuna modifica al `.docx` in questo lotto: solo lettura e analisi.

**Sesto lotto (2026-07-07) — item 1 (uniformità dello stile
citazionale)**: campione sistematico di 98 note (ogni 40ª lungo
l'intero intervallo di ID 28-3942) più censimento completo delle
citazioni delle due fonti più ricorrenti nel corpus (Guyatt et al.
2008, sistema GRADE, 6 occorrenze; Unützer et al. 2002/2008, trial
IMPACT, 24 occorrenze) — il test più diretto di uniformità: la stessa
fonte è citata sempre allo stesso modo?

- **Tre generi di nota coesistenti**: esplicativa/metodologica (la
  maggioranza), citazione bibliografica formale, citazione
  normativa/legale. Il requisito Chicago Style si applica pienamente
  solo al secondo genere.
- **Non uniformità confermata**: Guyatt et al. 2008 (GRADE) compare in
  4 formati diversi sulle sue 4 citazioni dirette (con/senza volume e
  pagine, notazione Vancouver vs Chicago, nome rivista abbreviato vs
  per esteso). Unützer et al. 2002/2008 (trial IMPACT) mostra ampia
  variazione su 24 citazioni (lunghezza dell'elenco autori, notazione
  di volume, stile del trattino nelle pagine, "et al." vs "e
  collaboratori", forme brevi eterogenee). Non corretto silenziosamente:
  presuppone una scelta editoriale sulla forma canonica. **Decisione
  dell'autore richiesta.**
- **Nuova scoperta maggiore, quantificata con precisione**: 12 rimandi
  interni in sintassi Markdown non convertita (`[^N]`, es. "cit. alla
  nota [^2605]"), tutti concentrati nel blocco Umbria, con bersaglio
  disallineato da uno scarto **costante e verificato di esattamente
  +299** (verificato con certezza di contenuto per 7 dei 12 casi — es.
  "[^2605]" corrisponde esattamente alla nota #2904, "Umbria24/GIMBE,
  «Sanità in crisi...»"). Stessa origine presunta degli asterischi di
  grassetto non convertiti già corretti nel quarto lotto: assemblaggio
  del documento da una fonte Markdown, rimandi scritti come testo
  letterale anziché come campo dinamico di Word, mai aggiornati dopo
  l'inserimento di 299 note in un punto precedente del documento. Non
  corretto silenziosamente nonostante l'alta confidenza. **Decisione
  dell'autore richiesta**: correggere (bersaglio+299, sintassi
  semplificata) o segnalare come limite noto.

Nessuna modifica al `.docx` in quel lotto: solo lettura e analisi.

**Settimo lotto (2026-07-07) — due decisioni dell'autore ricevute e
applicate lo stesso giorno sulle scoperte dell'item 1**:
- **Uniformare Guyatt e Unützer (30 citazioni), non estendere alle
  restanti ~3.885 note.** Applicata una forma canonica alle 3 citazioni
  di Guyatt 2008 e alle 10 citazioni formali di Unützer 2002/2008 (due
  forme, una per anno) — **quinta modifica di contenuto al `.docx`
  canonico**. Forme brevi ("cit."/"op. cit.") e menzioni discorsive non
  toccate, fuori scopo della decisione.
- **Correggere tutti e 12 i rimandi `[^N]`+299.** Verificato con
  certezza di contenuto per la totalità dei 12 casi (non solo 7 come
  nella prima verifica); ciascun rimando sostituito col numero corretto
  in testo semplice — **sesta modifica di contenuto al `.docx`
  canonico**.

Verificata l'integrità strutturale dopo entrambe le modifiche: 11.110
paragrafi e 1.055 tabelle invariati. Con questo si chiude il perimetro
dei nove item della checklist di Fase 3.4 (item 1 resta per natura
campionario, non un censimento esaustivo delle 3.915 note, a
differenza degli altri item ormai censiti per intero). Due decisioni
minori dell'autore restano pendenti (item 3a — etichette a lettera
A.1-M.3; residui di 1-2 asterischi in contesti diversi), registrate in
`_meta/parking-lot.md`.

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
