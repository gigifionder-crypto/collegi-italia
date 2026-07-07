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

### Item 1, 4 — non ancora avviati

Da affrontare in lotti successivi, dato che richiedono metodologie
diverse dall'analisi programmatica sin qui applicata, e una scala
paragonabile alla Fase 3.2:
- **Item 1** (uniformità Chicago Style delle ~3.915 note): richiede
  campionamento e classificazione qualitativa dello stile citazionale
  nota per nota (formato Autore-Anno vs Autore-Titolo-Anno, forma
  breve dopo prima citazione, ecc.).
- **Item 4** (descrittività dei titoli di tabella e indicazione della
  fonte, su 1.055 tabelle): richiede lettura qualitativa a campione.

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

Item 1, 4 non ancora avviati (richiedono campionamento qualitativo di
scala paragonabile alla Fase 3.2). Due decisioni dell'autore restano
pendenti (item 3a — etichette a lettera A.1-M.3; nuova voce sui residui
di 1-2 asterischi in contesti diversi), registrate in
`_meta/parking-lot.md`. Quattro modifiche di contenuto al `.docx`
finora in tutta la Fase 3.4 (rinumerazione UE-27, correzione apostrofi,
correzione nota 5→3, rimozione asterischi 3+).
