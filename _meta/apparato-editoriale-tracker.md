# Registro — Fase 3.4 (apparato editoriale)

Registro dedicato alla passata sull'apparato editoriale del Tomo I
(`tomo-1-puglia/opera-integrale-puglia.docx`), come previsto dal prompt
operativo (Fase 3, quarta passata tematica: "note, tabelle, riferimenti
incrociati") e dalla checklist di Fase 2 (§ righe 122-133 di
`_meta/prompt-operativo.md`), che elenca nove item di verifica:

1. Uniformità dello stile citazionale delle ~3.891/3.915 note a piè di
   pagina (Chicago Manual of Style).
2. Verifica che ogni nota sia richiamata nel testo e non orfana.
3. Numerazione continua e coerente di tabelle e figure, con elenco
   navigabile.
4. Titoli di tabella descrittivi e autoesplicativi, con fonte esplicita.
5. Rimozione di residui placeholder infografici non completati.
6. Uniformità tipografica (trattini, virgolette, unità, numeri, date).
7. Coerenza dei riferimenti incrociati interni ("cfr. §…").
8. Front matter e back matter standard per tomo.
9. Versioning esplicito di ogni file (versione, data, changelog).

Questo file registra lo stato di avanzamento item per item. Metodologia:
analisi programmatica diretta sull'XML del `.docx` (`word/document.xml`,
`word/footnotes.xml`), non sulla sola lettura visiva — stesso rigore
della Fase 3.2. Il file `.docx` non viene modificato in questo lotto:
solo lettura e analisi.

## Stato per item (primo lotto, 2026-07-07)

### Item 2 — Note orfane o non richiamate: VERIFICATO PULITO

Cross-check fra `word/footnoteReference` (corpo del testo) e
`word/footnote` (definizioni in `footnotes.xml`): 3.915 richiami nel
testo, tutti a ID univoci; 3.917 note definite (3.915 di contenuto + 2
segnaposto strutturali Word, ID `-1` "separator" e ID `0`
"continuationSeparator", esclusi dal conteggio sostanziale). **Zero
note orfane, zero riferimenti privi di definizione, zero riferimenti
duplicati.** Conferma e aggiorna il controllo preliminare già registrato
in `_meta/status-tracker.md` (§3.4, "0 orfane/mancanti su 3.942, ora
3.915"), qui rieseguito con il cross-check esplicito ID-per-ID anziché
il solo conteggio.

### Item 2bis — NUOVA VERIFICA: integrità del contenuto delle note (non prevista testualmente dalla checklist, ma necessaria a completarla)

Il controllo "orfana/non orfana" verifica solo che gli ID combacino, non
che il corpo della nota contenga testo. Verifica aggiuntiva: **111 note
su 3.915 (2,8%) hanno un corpo interamente vuoto** — solo il marcatore
`<w:footnoteRef/>`, nessun testo, nessun campo, nessun collegamento
ipertestuale (verificato sul XML grezzo, non solo sul testo estratto).
Tutte e 111 sono regolarmente richiamate nel testo (nessuna è "orfana"
nel senso dell'item 2), quindi il controllo esistente non le avrebbe
mai intercettate.

ID coinvolti (111, esclusi i 2 segnaposto strutturali): 997, 1024, 1026,
1053, 1084, 1105, 1115, 1152, 1172, 1179, 1183, 1193, 1267, 1283, 1294,
1325, 1346, 1348, 1356, 1393, 1418, 1424, 1441, 1459, 1475, 1486, 1517,
1538, 1540, 1548, 1585, 1610, 1616, 1633, 1651, 1667, 1678, 1709, 1730,
1732, 1740, 1777, 1802, 1808, 1825, 1843, 1859, 1870, 1901, 1922, 1924,
1932, 1969, 1994, 2000, 2017, 2279, 2295, 2306, 2337, 2358, 2360, 2368,
2405, 2430, 2436, 2453, 2471, 2487, 2498, 2529, 2550, 2552, 2560, 2597,
2622, 2628, 2645, 2663, 2679, 2690, 2721, 2742, 2744, 2752, 2789, 2814,
2820, 2837, 3209, 3225, 3236, 3267, 3288, 3290, 3298, 3335, 3360, 3366,
3383, 3425, 3441, 3452, 3483, 3504, 3506, 3514, 3551, 3576, 3582, 3599.

Osservazioni:
- Distribuzione concentrata in due fasce dell'intervallo ID (≈997-2837 e
  ≈3209-3599), con spaziatura fra un ID vuoto e il successivo
  relativamente regolare — compatibile con una perdita sistematica
  avvenuta in una fase di editing/conversione precedente a questo
  progetto (il `.docx` non è mai stato modificato durante le Fasi 3.1-3.3
  di questa sessione), non con un difetto casuale isolato.
- Il testo immediatamente precedente al richiamo di nota è quasi sempre
  la frase conclusiva di un paragrafo o di una sezione (verificato su
  campione di 5 ID sparsi lungo l'intervallo), compatibile con
  un'ipotesi di nota "di chiusura di sezione" (fonte, rimando o
  precisazione finale) il cui contenuto è andato perso — ma questa è
  un'ipotesi, non un fatto verificabile senza il contenuto originale.
- `_meta/cut-darlings.md` (registro di ogni spostamento/rimozione
  intenzionale di contenuto durante questa ristrutturazione) non contiene
  alcuna voce relativa a note a piè di pagina: la perdita non risulta
  come rimozione intenzionale documentata in questo progetto.
- **Non è possibile ricostruire il contenuto perduto senza una fonte
  esterna** (versione precedente del file, backup dell'autore). Nessuna
  correzione silenziosa applicata o applicabile.

**Decisione dell'autore (2026-07-07): segnalare come limite noto del
corpus**, senza tentare un recupero (nessun backup disponibile). Azione
completata: aggiunto il punto 6 alla sezione "Limiti dichiarati e agenda
di consolidamento" del Livello 4
(`_livelli-piramide/livello-4-sintesi-tecnica.md`), con rimando a questo
tracker per l'elenco completo degli ID. Nessuna modifica al contenuto
delle note stesse (resta impossibile senza fonte esterna). **Item 2bis
chiuso.**

### Item 3 — Numerazione di tabelle e figure: VERIFICATO, DUE PATTERN DISTINTI DI DUPLICAZIONE

Estratte 812 etichette "Tabella X.Y" dal corpo del documento (regex sulle
etichette in stile "Tabella A.1", "Tabella 7.3", ecc.); 163 etichette
uniche, 42 duplicate. Le duplicazioni si dividono in due categorie di
natura diversa:

**(a) 35 etichette a lettera (A.1–M.3), duplicate 3-37 volte ciascuna.**
Struttura: ogni blocco regionale del "Tomo II" (19 regioni) più il nucleo
Puglia ripete lo stesso telaio di appendici lettera A-M con la propria
numerazione locale (es. "Tabella A.1" esiste una volta per ciascuna delle
regioni/blocchi in cui l'Appendice A si applica — da qui i conteggi fino
a 37). **Atteso e già annotato** nel controllo preliminare di
`_meta/status-tracker.md` (§3.4): non è un difetto, ma una conseguenza
diretta della struttura a blocchi ripetuti del Tomo II. Decisione
dell'autore già segnalata come pendente: rinumerare con prefisso di
regione/parte esplicito (es. "Tabella Puglia-A.1", "Tabella FVG-A.1") o
mantenere la numerazione locale così com'è, con una nota esplicita in
front matter che ne spiega la convenzione.

**(b) 7 etichette numeriche (1.1, 2.1, 4.1, 6.1, 7.1, 8.1, 9.1),
duplicate esattamente 2 volte ciascuna — collisione distinta, non
notata in precedenza.** Verificato per contenuto (non solo per numero):
la prima occorrenza di ciascuna appartiene al nucleo Puglia (Parti I-IX,
titoli come "Tabella 1.1 — Scomposizione del quesito di valutazione");
la seconda appartiene alla sezione UE-27, che ha una propria numerazione
di Parti interna che **riparte da 1.1** invece di proseguire la
numerazione del nucleo Puglia o di usare un proprio prefisso (titoli
come "Tabella 1.1. Il quadro europeo della salute mentale..."). Le due
occorrenze sono inoltre distinguibili dalla punteggiatura del titolo
(em-dash nel nucleo Puglia, punto nella sezione UE-27) — un indizio che
si tratti di due sistemi di numerazione paralleli non coordinati, non di
un errore di battitura isolato. Nessuna tabella #77-#84 della Fase 3.2
segnala questo come discrepanza di dato (i dati delle due tabelle
comunque restano distinti e corretti nel proprio contesto): è un difetto
di numerazione, non di contenuto.

**Decisione dell'autore (2026-07-07): prefisso esplicito alla sezione
UE-27.** Azione completata: rinominate le 8 etichette della sezione
UE-27 (non solo le 7 collidenti — anche "Tabella 5.1", che nel nucleo
Puglia è in realtà "Tabella 5.1.A" e quindi non collideva, è stata
uniformata per coerenza interna della sezione) da "Tabella N.M." a
"Tabella UE.N.M." Modifica applicata direttamente su
`tomo-1-puglia/opera-integrale-puglia.docx`, paragrafi indice 10994,
11003, 11016, 11051, 11056, 11065, 11072, 11079 (unico run per
paragrafo, nessun'altra formattazione toccata). Nessun riferimento
incrociato in prosa alla vecchia numerazione trovato all'interno della
sezione UE-27 (verificato: le 8 etichette compaiono solo nella propria
didascalia). Verificato dopo la modifica: 11.110 paragrafi e 1.055
tabelle invariati (nessuna alterazione strutturale); zero duplicazioni
numeriche residue tra nucleo Puglia e sezione UE-27. **Item 3(b)
chiuso.** Il pattern (a) (etichette a lettera A.1-M.3 per i 19 blocchi
regionali del Tomo II) resta con decisione pendente, non affrontato in
questo turno.

### Item 5 — Residui placeholder infografici: RICONFERMATO PULITO

Ricerca mirata di marcatori di completamento mancato ("TODO:",
"[placeholder]", "[da completare]", "[inserire]", "lorem ipsum", ecc.)
sul testo integrale: nessun riscontro reale. Gli unici falsi positivi
individuati (occorrenze di "XXX" e "todo:") sono rispettivamente
numerazione romana di appendici (Appendici XXX-XXXIII) e la parola
italiana "metodo:" (falso positivo per sottostringa, "me-TODO-:").
Conferma quanto già registrato in `_meta/verifica-numerica-tracker.md`
sulle 72 tabelle "n/a-infografica" (specifiche di progettazione, non
dati mancanti — categoria distinta, già trattata in Fase 3.2).

### Item 6 — Uniformità tipografica: SECONDO LOTTO, PARZIALMENTE RISOLTO

Analisi programmatica su trattini, virgolette, apostrofi, formati di
numero e data sul testo integrale.

- **Apostrofi — RISOLTO.** 48 apostrofi dritti (`'`) individuati, tutti
  elisioni italiane genuine in prosa (l', dell', sull', all', un', d',
  nell'), contro 26.640 apostrofi tipografici (`’`) già in uso —
  un'inconsistenza minoritaria ma reale. Sostituiti tutti e 48 con
  l'apostrofo tipografico, in 32 run distinti individuati percorrendo
  l'intero corpo del documento (paragrafi e celle di tabella).
  Verificato dopo la modifica: 11.110 paragrafi e 1.055 tabelle
  invariati; zero apostrofi dritti residui; 26.688 apostrofi tipografici
  totali (26.640+48, coerente).
- **Virgolette dritte (`"`) — VERIFICATO FALSO POSITIVO, NESSUNA
  AZIONE.** Le uniche 2 occorrenze appartengono al codice di campo Word
  del sommario (`TOC \o "1-2" \h \z \u`), sintassi interna non visibile
  al lettore: toccarle romperebbe il sommario. Non sono testo di prosa.
- **Virgolette di prosa — coesistenza di due convenzioni, non
  risolto.** «angolate» (567/568 occorrenze, aperture/chiusure
  bilanciate) e "curve" (207/209, bilanciate) coesistono nel corpo. Non
  è chiaro se sia una distinzione intenzionale (es. citazioni dirette
  vs. enfasi) o una disomogeneità di stile: richiede lettura qualitativa
  campionaria, non risolvibile con una sostituzione meccanica. Rimandato
  a un lotto successivo.
- **Trattini in intervalli numerici — inconsistenza reale individuata,
  non risolta.** Gli intervalli numerici usano sia il trattino breve
  (`700` istanze di pattern N-N, es. "800-900") sia il trattino medio
  (`499` istanze di pattern N–N, es. "2025–2050") per lo stesso scopo
  semantico. Non risolvibile con una sostituzione globale: parte delle
  occorrenze con trattino breve sono in realtà identificativi legittimi
  (ISBN, date ISO come "2026-07-06") che non vanno toccati — servirebbe
  una classificazione caso per caso. Rimandato a un lotto successivo.
- **Numeri e date — VERIFICATO PULITO.** Formato numerico italiano
  (punto per le migliaia, virgola per i decimali) coerente in tutto il
  campione analizzato (es. "30.000", "55.000", "1.304"). Solo 6 date in
  formato ISO (tutte date di redazione/riferimento interne, es.
  "2026-07-06"), nessuna commistione con altri formati di data.

### Item 9 — Versioning esplicito dei file: SODDISFATTO TRAMITE LA CONVENZIONE GIÀ IN USO NEL PROGETTO

Non introdotta un'intestazione di versione interna al `.docx` (nessuna
convenzione di questo tipo esiste altrove nel corpus, e introdurla ora
sarebbe un'aggiunta strutturale non richiesta). Il progetto usa già,
fin dalla Fase 3.1, la cronologia dei commit Git come meccanismo di
versioning esplicito: ogni modifica ha data, autore, changelog
descrittivo nel messaggio di commit, ed è tracciabile con `git log`.
Questo soddisfa lo spirito dell'item 9 (versione, data, changelog per
ogni file) senza inventare una convenzione editoriale nuova. Nessuna
azione ulteriore necessaria.

### Item 7 — Coerenza dei riferimenti incrociati interni: TERZO LOTTO, VERIFICATO

Due tipi di rimando interno verificati programmaticamente.

**(a) Riferimenti numerici a Parte/Appendice — VERIFICATO PULITO.**
Estratti tutti i riferimenti a "Parte [numero romano]" e "Appendice
[numero romano]" ovunque nel testo (non solo nei titoli), confrontati
con l'intervallo effettivamente esistente (Parti I-XV, Appendici
I-XXXIII, entrambi confermati completi contando i titoli stessi). Zero
riferimenti fuori intervallo: nessun rimando a una Parte o Appendice
inesistente.

**(b) Rimandi puntuali "cfr. …" — 5 occorrenze totali nell'intero
documento, due difetti reali individuati, entrambi con decisione
dell'autore ricevuta il 2026-07-07.**
1. **"cfr. nota 5" (paragrafo 479) — rimando disallineato — RISOLTO.**
   Il paragrafo tratta il monito sulla non significatività statistica
   dei risparmi sanitari diretti (il caveat Unützer et al. 2008,
   ricorrente in tutti i prodotti della piramide). Verificato che la
   "nota 5" in ordine di lettura (5° `footnoteReference` nel corpo,
   w:id XML `32`) era in realtà una nota sul regolamento UE
   sull'intelligenza artificiale (Regolamento UE 2024/1689), non
   pertinente al contesto. La nota che tratta effettivamente il caveat
   Unützer/IMPACT trial è la 3ª in ordine di lettura (w:id XML `30`).
   **Decisione dell'autore: correggere in "nota 3".** Azione completata:
   testo del paragrafo 479 modificato da "cfr. nota 5" a "cfr. nota 3"
   — terza modifica di contenuto al `.docx` canonico nel progetto.
2. **"cfr. Volume 0.A" / "cfr. Volume 0.B" (6 occorrenze) — rimando a un
   bersaglio non definito — SEGNALATO COME LIMITE NOTO, NESSUNA
   MODIFICA.** Il testo rimanda ripetutamente a un "Volume 0.A" (per
   l'asse italiano/Puglia) e "Volume 0.B" (per l'asse unionale) come
   sede del "Reference Case" metodologico condiviso, ma **nessuna
   intestazione "Volume 0" esiste in nessun punto dei 11.110 paragrafi
   del documento** — verificato con ricerca esaustiva. Due letture
   possibili, non distinguibili dal solo testo: (i) "Volume 0" è
   un'autoreferenza implicita al nucleo Puglia/Tomo I stesso, mai
   esplicitata con questa etichetta; (ii) è un documento distinto,
   previsto dall'architettura dei 23 Volumi ma non incluso in questo
   file. **Decisione dell'autore (2026-07-07): segnalare come limite
   noto**, nessuna modifica al testo (il bersaglio resta non
   accertabile senza informazioni esterne).

**Scoperta collaterale utile alla lettura di (b):** la sezione UE-27
(Volume 22) ha una propria struttura interna in "Capitoli" (1-9, non
"Parti"), distinta da quella del nucleo Puglia — confermata leggendo il
suo indice interno ("Capitolo 1 — Il quadro europeo...", ..., "Capitolo
9 — Il verdetto tripartito..."). I rimandi "cfr. Capitolo N" trovati
altrove nel testo sono risultati, a un controllo puntuale, interni e
validi a questa struttura (o riferiti a un "progetto ufficiale" esterno
già esplicitamente dichiarato come tale nel testo, non un rimando rotto)
— nessun'altra azione necessaria per questo sotto-caso.

**Nuova scoperta non prevista da nessun item testuale della checklist,
ma emersa durante questa verifica: corruzione tipografica da markup non
convertito — RISOLTA.** 62 occorrenze di sequenze di asterischi (`****`,
`******`, `********`) incastonate a metà parola nel testo (es.
"dell‘******efficacia", "L'********efficacia e l********'evidenza"),
concentrate nell'intestazione template "Parte D — L'efficacia e
l'evidenza" e nelle didascalie "Tabella D.1/F.3/G.1/G.2/H.2/M.2"
ripetute nei blocchi regionali del Tomo II. Pattern compatibile con
markup Markdown di grassetto (`**testo**`) non convertito in
formattazione Word durante l'assemblaggio del documento. **Decisione
dell'autore (2026-07-07): rimuovere solo gli asterischi**, senza
applicare grassetto (non verificabile quale fosse l'enfasi originale).
Azione completata: rimosse tutte le sequenze di 3 o più asterischi
consecutivi (79 sequenze in 40 run, individuate percorrendo l'intero
corpo del documento) — quarta modifica di contenuto al `.docx`
canonico. **Deliberatamente non toccate le sequenze di 1-2 asterischi**
(25 singole, 16 doppie residue), fuori dallo scopo esatto della
decisione: un campione di queste è confermato legittimo (marcatori di
nota tipo "Tabella 7.1.2*" o "(*)" su valori tabellari), mentre altre
(es. "**Formazione Puglia**", "**Spettabile** [Ente/Ordine/Associazione]**")
sembrano dello stesso tipo di markup non convertito ma in contesti
diversi (lettera/appendice di template) non descritti nella decisione
presa — registrate separatamente in `_meta/parking-lot.md` per una
decisione futura distinta. Verificata l'integrità strutturale dopo il
salvataggio: 11.110 paragrafi e 1.055 tabelle invariati; zero sequenze
di 3+ asterischi residue.

**Residuo di 1-2 asterischi — RISOLTO (2026-07-08).** Decisione
dell'autore: estendere la stessa pulizia ai residui. Esaminati
singolarmente tutti i 21 asterischi rimasti nel documento a quella
data (il conteggio di 25/16 della scoperta originale includeva
occorrenze già corrette incidentalmente durante la riconciliazione di
Fase 3.2): 12 singoli confermati legittimi come marcatori di nota
("Tabella/Schema X.Y*" ×9, tre trailing "*" a fine didascalia con lo
stesso ruolo) e 2 "(*)" nelle tabelle #862/#866 confermati legittimi —
non toccati. Rimossi i 10 asterischi non legittimi: intestazione
ricorrente di pagina (§158, §747), un inciso in prosa (§4630), il
template di lettera (§6063), due didascalie di tabella (tabelle #248,
#255), una riga di totale (tabella #333), e la cella Molise già nota
(tabella #864 riga 7, preservato il marcatore legittimo "(*)")  —
tredicesima modifica di contenuto al `.docx` canonico. Verificata
l'integrità strutturale (11.110 paragrafi, 1.055 tabelle invariati);
zero asterischi non legittimi residui.

### Item 8 — Front matter e back matter standard: TERZO LOTTO, VERIFICATO

Confronto diretto tra la sequenza osservata nel Tomo I e il modello
dichiarato (World Bank Group Publications Editorial Style Guide,
richiamato nella checklist di Fase 2): frontespizio, indice, prefazione,
elenco abbreviazioni; poi testo; poi appendici, glossario, riferimenti.

**Front matter — un elemento mancante, un ordine invertito (minore).**
- Frontespizio (paragrafi 0-12): presente e completo (titolo, autore,
  qualifica, edizione, data).
- "Avvertenza di edizione" + "Come leggere questo Tomo I" + "Mappa dei
  destinatari" (paragrafi 15-21): equivalgono alla prefazione richiesta
  dal modello — presenti.
- "Indice generale del volume" (paragrafo 22): presente, ma **collocato
  dopo la prefazione anziché prima o accanto al frontespizio** come nel
  modello dichiarato — uno scostamento minore, non raro in pratiche
  editoriali diverse dal WBG, non necessariamente un difetto.
- **Elenco delle abbreviazioni: assente nel front matter del Tomo I.**
  Un elenco esiste, ma solo nel Livello 4 della piramide (§12,
  aggiunto in Fase 3.3, primo lotto) — un prodotto derivato, non il
  Tomo I stesso. Il Tomo I canonico non ha una propria sezione
  dedicata alle abbreviazioni in apertura. Gap reale, non colmato in
  questo lotto (richiederebbe compilare un elenco specifico per il
  Tomo I, un'attività redazionale a sé, non una verifica).

**Back matter — struttura a bibliografia distribuita, nessun glossario
consolidato per il nucleo Puglia.**
- Appendici Integrative (paragrafi 41-43): presenti, I-XXXIII, in
  posizione corretta dopo il testo principale.
- **Bibliografia distribuita, non consolidata in un'unica sezione
  finale.** "Note Bibliografiche Integrali" ricorre come sezione a sé
  dopo diverse Parti del nucleo Puglia (almeno 8 occorrenze, paragrafi
  187, 318, 378, 474, 727, 893, 2871, 4069) — un modello "riferimenti
  per parte", alternativo ma legittimo rispetto a un'unica sezione
  finale. Una sezione "Note Bibliografiche con mini-riassunto" esiste
  alla fine assoluta del file (paragrafo 11094, 14 voci), ma è la
  bibliografia di chiusura della sola sezione UE-27/Volume 22, non un
  riferimento consolidato per l'intera opera.
- **Nessun glossario consolidato per il nucleo Puglia.** "Appendice E —
  Glossario" ricorre 16 volte, ma sempre come glossario **locale a un
  singolo blocco regionale** del Tomo II (telaio A-M ripetuto per
  regione, stesso pattern già noto per la numerazione tabelle) — non
  esiste un glossario unico e consolidato per il nucleo Puglia
  (Parti I-XV) in quanto tale.

Nessuna correzione applicata: entrambi i gap (elenco abbreviazioni,
glossario consolidato) richiederebbero produrre contenuto redazionale
nuovo, non una correzione meccanica — attività distinta da valutare con
l'autore.

### Item 4 — Titoli di tabella descrittivi e indicazione della fonte: QUINTO LOTTO, VERIFICATO

A differenza degli altri item, qui è stato possibile un **censimento
completo** delle 1.055 tabelle (non solo un campione), perché la
domanda ("esiste una didascalia? esiste una fonte?") è verificabile
programmaticamente sulla posizione dei paragrafi immediatamente
prima/dopo ogni tabella; la valutazione qualitativa di
autoesplicatività resta invece a campione, come previsto.

**Metodologia**: per ciascuna delle 1.055 tabelle, cercata una
didascalia in stile "Tabella X.Y" o "Tab. X.Y" fino a 6 paragrafi prima
E fino a 6 dopo (il corpus usa **due convenzioni coesistenti**: nel
nucleo Puglia la didascalia precede la tabella con trattino lungo,
"Tabella 2.2 — Titolo"; nei blocchi regionali del Tomo II e nella
sezione UE-27 la didascalia segue la tabella con punto, "Tabella
L.1. Titolo" — la stessa distinzione già osservata per la collisione di
numerazione UE-27/nucleo Puglia). Cercata una menzione di fonte
("Fonte"/"Fonti", coprendo entrambe le varianti) nella stessa finestra.

**Copertura delle didascalie: 993/1.055 tabelle (94,1%).** 617 con
didascalia prima (convenzione nucleo Puglia), 376 con didascalia dopo
(convenzione Tomo II/UE-27). Delle 62 tabelle senza didascalia
individuata in questa finestra, 20 sono già classificate
`n/a-infografica` nella Fase 3.2 (segnaposto di progettazione, non
tabelle di dati — nessuna didascalia attesa). Le restanti 42 sono
tabelle di dati (`verificata-ok`/`verificata-discrepanza`) verificate
come genuinamente prive di didascalia rilevabile — su un campione di 5
lette per intero (tabelle #28, #71, #111, #255, #821): #28 risulta
davvero priva di una riga-didascalia dedicata, introdotta solo da
prosa; #71 ha in realtà una didascalia ma etichettata **"Schema 7.1.1*"
anziché "Tabella"** (incoerenza di nomenclatura, non un'assenza reale);
#111 è una tabella strutturale di indice/apertura di Parte (natura
diversa da una tabella di dati); #255 non ha testo rilevabile in un
raggio di 3 paragrafi in nessuna delle due direzioni (da verificare
caso per caso se richiesto); #821 ha una didascalia ma **priva di
numero** ("Tabella. La mappa di lettura del corpus...", blocco
Abruzzo). Il campione suggerisce che la maggior parte delle 42 non è
un'assenza netta, ma una combinazione di nomenclatura non uniforme
("Schema" invece di "Tabella") e numerazione mancante in casi isolati —
non generalizzabile senza lettura di tutte le 42 senza campionamento.

**Descrittività (valutazione qualitativa a campione, ~15 didascalie
lette per intero lungo tutto il corpus)**: la grande maggioranza delle
didascalie trovate è autoesplicativa fuori contesto — dichiara
chiaramente l'oggetto della tabella (es. "Tabella 2.2 — Domanda,
offerta e divario di copertura", "Tabella G.1. Le dimensioni
dell'equità e le variabili seguite dallo studio", "Tabella M.2.
L'analisi multi-criterio: punteggi dell'intervento e del non
intervento"). Nessun caso di didascalia vaga o dipendente dal contesto
("la tabella seguente", senza oggetto proprio) individuato nel
campione. Giudizio: **positivo**, non esaustivo.

**Indicazione della fonte: 10/1.055 tabelle (0,95%) — GAP QUASI
UNIVERSALE, IL RISULTATO PIÙ NETTO DI QUESTO ITEM.** Solo 10 tabelle su
1.055 hanno un'indicazione esplicita di fonte ("Fonte:"/"Fonti:")
individuabile entro 6 paragrafi. Esempio dei rari casi conformi:
Tabella 2.2, con "Fonti: Ministero della Salute; legge regionale
11/2023; elaborazioni dello studio." Per il resto del corpus, la
provenienza dei dati è normalmente affidata a citazioni in nota a piè
di pagina collegate al testo discorsivo circostante, non a
un'annotazione dedicata sotto la tabella — verificato che le didascalie
stesse non portano quasi mai un richiamo di nota (0 su 471 didascalie
campionate nella convenzione "prima"). Non corretto silenziosamente:
aggiungere 1.045 annotazioni di fonte presupporrebbe conoscere,
tabella per tabella, quale nota o fonte discorsiva le sia associata —
un lavoro di produzione redazionale, non una correzione meccanica.
**Il gap più rilevante trovato in questo item**, da segnalare
prioritariamente all'autore.

### Item 1 — Uniformità dello stile citazionale delle note: SESTO LOTTO, VERIFICATO A CAMPIONE

Due metodi combinati: (a) un campione sistematico di 98 note (ogni 40ª,
lungo l'intero intervallo di ID 28-3942); (b) un censimento completo
—non a campione— di tutte le citazioni delle due fonti più ricorrenti
nell'intero corpus (Guyatt et al. 2008, sistema GRADE, 6 occorrenze;
Unützer et al. 2002/2008, trial IMPACT, 24 occorrenze), per verificare
se la STESSA fonte sia citata nello stesso formato ogni volta che
ricorre — il test più diretto e verificabile di uniformità.

**Genere delle note: tre tipi coesistenti, non riducibili a un unico
stile.** Dal campione di 98: la maggioranza sono note esplicative o
metodologiche senza citazione bibliografica formale (rimandi interni,
precisazioni, glosse); una minoranza sono citazioni bibliografiche
formali in senso proprio; alcune sono citazioni normative/legali
(regolamenti UE, leggi regionali), con una convenzione propria e
distinta. Il requisito Chicago Style si applica pienamente solo al
secondo gruppo.

**Non uniformità confermata sulla stessa fonte, citata più volte — RISOLTA per le due fonti campione (2026-07-07).**
- **Guyatt et al. 2008 (GRADE), 4 citazioni dirette, 4 formati
  diversi (prima della correzione)**: nota #28 senza volume né pagine
  ("BMJ, 336, 2008"); nota #128 con notazione volume(fascicolo) in
  stile Vancouver e pagine ("BMJ, 336(7650), 2008, pp. 924–926",
  trattino medio); nota #148 con notazione "vol. 336" in stile Chicago,
  tre autori nominati anziché "et al.", pagine con trattino breve ("pp.
  924-926"); nota #112 in forma discorsiva con il nome della rivista
  per esteso ("British Medical Journal" anziché "BMJ", lasciata
  invariata: è un discorso, non una citazione formale).
- **Unützer et al. 2002/2008 (trial IMPACT), 24 citazioni, ampia
  variazione (prima della correzione)**: lunghezza dell'elenco autori,
  notazione di volume, stile del trattino nelle pagine, "et al." vs "e
  collaboratori", presenza/assenza del sottotitolo, forme brevi
  eterogenee.

**Decisione dell'autore (2026-07-07): uniformare solo Guyatt e Unützer
(30 citazioni totali fra le due fonti), non estendere alle restanti
~3.885 note.** Azione completata — **quinta modifica di contenuto al
`.docx` canonico**:
- **Guyatt 2008**: le 3 citazioni formali (note #28, #128, #148)
  uniformate alla forma canonica "Guyatt G.H., Oxman A.D., Vist G.E. et
  al., «GRADE: an emerging consensus on rating quality of evidence and
  strength of recommendations», BMJ, vol. 336, n. 7650, 2008, pp.
  924-926." (mantenuto il testo esplicativo di ciascuna nota dopo la
  citazione, invariato). Nota #112 (discorsiva) lasciata invariata,
  fuori scopo.
- **Unützer 2002/2008**: le citazioni formali del trial IMPACT (2002:
  note #72, #91, #127, #157 già conforme, #2852, #2935, #3806; 2008:
  #163, #201, #217, #228) uniformate a due forme canoniche, una per
  anno — 2002: "Unützer J., Katon W., Callahan C.M. et al.,
  «Collaborative care management of late-life depression in the
  primary care setting: a randomized controlled trial», JAMA, vol.
  288, n. 22, 2002, pp. 2836-2845."; 2008: "Unützer J., Katon W., Fan
  M.-Y. et al., «Long-term cost effects of collaborative care for
  late-life depression», The American Journal of Managed Care, vol.
  14, n. 2, 2008, pp. 95-100." Nota #2852 (unica con "JAMA" in corsivo
  su un run separato) ricondotta a testo semplice, coerente con la
  maggioranza delle altre citazioni che non usano corsivo sul nome
  della rivista. Nota #3806 (citazione minima, priva di volume e
  pagine) completata con entrambe le citazioni canoniche (2002 +
  aggiornamento 2008), coerente con l'esercizio di uniformazione
  approvato. Le forme brevi per citazioni successive alla prima
  ("cit.", "op. cit.") **non toccate**: restano una convenzione valida
  e distinta dalla citazione integrale, fuori dallo scopo della
  decisione presa. Nota #216 (Katon et al. 2010, opera diversa dal
  trial IMPACT) e le menzioni puramente discorsive (es. #286, #291,
  #321, #540, #549, #560, #3157, #3822) lasciate invariate: non sono
  citazioni formali da uniformare.

**Nuova scoperta maggiore, quantificata con precisione: 12 rimandi
interni in sintassi Markdown non convertita (`[^N]`), tutti con
bersaglio disallineato da uno scarto costante e verificato di
esattamente +299 — RISOLTA.** Tutti e 12 concentrati nel blocco
regionale dell'Umbria (note #2908-2953), nella forma "cit. alla nota
[^N]" o "cfr. nota [^N]" — sintassi di rimando a piè di pagina in
Markdown (`[^numero]`), mai convertita in un riferimento incrociato
nativo di Word, analoga per natura alla scoperta degli asterischi di
grassetto non convertiti (Fase 3.4, lotto 3-4), stessa origine presunta
(assemblaggio del documento da una fonte Markdown). Il bersaglio
corretto è stato **verificato con certezza per tutti e 12 i casi**
(non solo 7 come nella prima verifica), leggendo il contenuto sia della
nota citante sia della nota bersaglio dichiarata e di quella
effettivamente corrispondente per contenuto: in ogni caso, sommando
esattamente 299 all'ID scritto in `[^N]` si ottiene la nota che
effettivamente contiene la citazione descritta (es. "[^2605]" → nota
#2904, "Umbria24/GIMBE, «Sanità in crisi: il Rapporto GIMBE...»",
corrispondenza esatta; verificato per tutti gli altri: [^2601]→2900,
[^2602]→2901, [^2603]→2902, [^2604]→2903, [^2606]→2905, [^2636]→2935,
[^2638]→2937, [^2646]→2945, [^2649]→2948). Compatibile con un
inserimento di 299 note in un punto precedente del documento, in una
fase di editing antecedente a questo progetto. **Decisione dell'autore
(2026-07-07): correggere tutti e 12.** Azione completata — **sesta
modifica di contenuto al `.docx` canonico**: ciascun rimando
`[^N originale]` sostituito col numero corretto (N+299) in testo
semplice, senza parentesi né accento circonflesso, preservando la
parola "nota"/"note" già presente nel testo circostante (nessuna
duplicazione).

Verificata l'integrità strutturale dopo entrambe le modifiche (quinta e
sesta) al `.docx`: 11.110 paragrafi e 1.055 tabelle invariati.

## Perimetro

Questo lotto copre solo il file canonico
`tomo-1-puglia/opera-integrale-puglia.docx`. I quattro prodotti della
piramide (Livelli 1-4) non hanno un apparato di note a piè di pagina o
di tabelle numerate in senso HTA-tecnico e non rientrano nello stesso
tipo di verifica (già trattati per registro linguistico in Fase 3.3).

## Stato

Fase 3.4: **primo lotto chiuso, con due decisioni dell'autore ricevute e
applicate lo stesso giorno (2026-07-07)**:
- Item 2bis (111 note vuote): segnalato come limite noto in Livello 4
  (§10, punto 6). Nessuna modifica al contenuto delle note.
- Item 3(b) (collisione numerica nucleo Puglia / sezione UE-27): risolta
  con prefisso esplicito "Tabella UE.N.M" applicato alle 8 tabelle della
  sezione UE-27, direttamente sul file `.docx` canonico — **prima
  modifica di contenuto a questo file in tutto il progetto** (Fasi
  3.1-3.3 avevano lavorato solo sui prodotti derivati e sui tracker).
  Verificata l'integrità strutturale post-modifica (paragrafi e tabelle
  invariati in numero).

Item 3(a) (etichette a lettera A.1-M.3, attese/strutturali) resta con
decisione pendente.

**Secondo lotto (2026-07-07)** — item 6 (uniformità tipografica) e item
9 (versioning): apostrofi dritti corretti (48→0, seconda modifica di
contenuto al `.docx`); virgolette dritte verificate come falso positivo
(codice di campo del sommario, non toccato); coesistenza di virgolette
angolate/curve e di trattino breve/medio negli intervalli numerici
individuate come inconsistenze reali ma non risolte meccanicamente
(richiedono classificazione qualitativa caso per caso, rimandate a un
lotto successivo); numeri e date verificati coerenti. Item 9 soddisfatto
tramite la convenzione di versioning già in uso nel progetto (cronologia
Git), senza introdurre una convenzione nuova.

**Terzo lotto (2026-07-07) — item 7 (coerenza dei rimandi interni) e
item 8 (front/back matter)**:
- Item 7: riferimenti numerici a Parte/Appendice verificati puliti
  (zero fuori intervallo). Scoperta collaterale: la sezione UE-27 ha una
  propria struttura in "Capitoli" (1-9), distinta dalle "Parti" del
  nucleo Puglia — i rimandi "cfr. Capitolo N" trovati sono risultati
  validi.
- Item 8: front matter completo tranne l'elenco delle abbreviazioni
  (assente nel Tomo I, presente solo nel Livello 4); indice collocato
  dopo la prefazione anziché prima (scostamento minore). Back matter:
  bibliografia distribuita per Parte anziché consolidata in un'unica
  sezione finale (modello alternativo legittimo); nessun glossario
  consolidato per il nucleo Puglia (solo glossari locali per regione nel
  Tomo II). Entrambi i gap richiederebbero produzione di contenuto
  nuovo, non una correzione meccanica — non risolti in questo lotto.

**Quarto lotto (2026-07-07) — tre decisioni dell'autore ricevute e
applicate sulle scoperte del terzo lotto:**
- "cfr. nota 5" (paragrafo 479): **corretto in "cfr. nota 3"** — terza
  modifica di contenuto al `.docx` canonico.
- 6 rimandi a "Volume 0.A/0.B": **segnalati come limite noto**, nessuna
  modifica (bersaglio non accertabile).
- 62 occorrenze di sequenze di 3+ asterischi (markup non convertito):
  **rimossi solo gli asterischi**, senza applicare grassetto — quarta
  modifica di contenuto al `.docx` canonico (79 sequenze in 40 run).
  Deliberatamente non toccati 25 asterischi singoli e 16 doppi residui,
  fuori dallo scopo esatto della decisione (alcuni legittimi marcatori
  di nota, altri dello stesso tipo di markup ma in contesti diversi non
  coperti dalla decisione presa) — nuova voce distinta in
  `_meta/parking-lot.md` per una decisione futura.
  Verificata l'integrità strutturale dopo entrambe le modifiche: 11.110
  paragrafi e 1.055 tabelle invariati.

Due decisioni dell'autore restano pendenti (item 3a — etichette a
lettera A.1-M.3; residui di 1-2 asterischi in contesti diversi),
registrate in `_meta/parking-lot.md`. Quattro modifiche di contenuto al
`.docx` finora in tutta la Fase 3.4 (rinumerazione UE-27, correzione
apostrofi, correzione nota 5→3, rimozione asterischi 3+).

**Quinto lotto (2026-07-07) — item 4 (titoli di tabella e fonte)**:
censimento completo (non a campione) delle 1.055 tabelle per copertura
di didascalia e di fonte, più una lettura qualitativa a campione (~15
didascalie + 5 letture integrali) per la descrittività. Risultati:
copertura didascalie 993/1.055 (94,1%), positiva sulla descrittività
nel campione letto; **copertura di fonte esplicita solo 10/1.055
(0,95%) — gap quasi universale, il risultato più rilevante di questo
item**, non correggibile meccanicamente (richiederebbe produzione
redazionale, non una correzione). Scoperte minori sul campione delle 42
tabelle prive di didascalia rilevabile: incoerenza di nomenclatura
"Schema" invece di "Tabella" (tabella #71); didascalia priva di numero
(tabella #821, blocco Abruzzo) — non generalizzate all'intero corpus,
solo osservate sul campione di 5. Nessuna modifica al `.docx` in questo
lotto: solo lettura e analisi.

Item 1 non ancora avviato (richiede campionamento qualitativo di scala
paragonabile alla Fase 3.2, natura diversa da item 4 perché la domanda
qui non è "esiste una fonte" ma "è nello stile citazionale corretto e
uniforme", non verificabile con un censimento posizionale).

**Sesto lotto (2026-07-07) — item 1 (uniformità stile citazionale)**:
campione sistematico di 98 note (ogni 40ª lungo l'intero intervallo
28-3942) più censimento completo delle citazioni delle due fonti più
ricorrenti (Guyatt et al. 2008 GRADE, 6 occorrenze; Unützer et al.
2002/2008 IMPACT, 24 occorrenze). Tre generi di nota coesistenti
(esplicativa/metodologica, citazione bibliografica formale, citazione
normativa/legale) — il requisito Chicago Style si applica pienamente
solo al secondo. **Non uniformità confermata sulla stessa fonte citata
più volte**: Guyatt 2008 in 4 formati diversi su 4 citazioni dirette;
Unützer 2002/2008 con ampia variazione (lunghezza elenco autori,
notazione di volume, stile del trattino nelle pagine, "et al." vs "e
collaboratori") su 24 citazioni.

**Nuova scoperta maggiore, quantificata con precisione**: 12 rimandi
interni in sintassi Markdown non convertita (`[^N]`, es. "cit. alla
nota [^2605]"), tutti concentrati nel blocco Umbria, con bersaglio
disallineato da uno scarto costante di **esattamente +299**, verificato
inizialmente per 7 dei 12 casi, poi per tutti e 12.

**Settimo lotto (2026-07-07) — due decisioni dell'autore ricevute e
applicate lo stesso giorno**:
- **Uniformare Guyatt e Unützer (30 citazioni), non estendere alle
  restanti ~3.885 note.** Applicata la forma canonica alle 3 citazioni
  di Guyatt 2008 e alle 10 citazioni formali di Unützer 2002/2008 (due
  forme canoniche, una per anno) — quinta modifica di contenuto al
  `.docx` canonico. Forme brevi ("cit."/"op. cit.") e menzioni
  discorsive non toccate, fuori scopo.
- **Correggere tutti e 12 i rimandi `[^N]`+299.** Verificato con
  certezza di contenuto per la totalità dei 12 casi (non solo 7);
  ciascun rimando sostituito col numero corretto in testo semplice —
  sesta modifica di contenuto al `.docx` canonico.

Verificata l'integrità strutturale dopo entrambe le modifiche: 11.110
paragrafi e 1.055 tabelle invariati. Con questo si chiude il perimetro
dichiarato dei nove item della checklist di Fase 3.4 (fermo restando
che la natura campionaria dell'item 1 non lo rende una verifica
esaustiva delle 3.915 note, a differenza degli altri item ormai censiti
per intero). Due decisioni minori dell'autore restano pendenti (item
3a — etichette a lettera A.1-M.3; residui di 1-2 asterischi in contesti
diversi), registrate in `_meta/parking-lot.md`.
