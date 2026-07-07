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

### Item 1, 4, 6, 7, 8, 9 — non ancora avviati

Da affrontare in lotti successivi, dato che richiedono metodologie
diverse dall'analisi programmatica sin qui applicata:
- **Item 1** (uniformità Chicago Style delle ~3.915 note): richiede
  campionamento e classificazione qualitativa dello stile citazionale
  nota per nota (formato Autore-Anno vs Autore-Titolo-Anno, forma
  breve dopo prima citazione, ecc.) — attività di scala paragonabile
  alla Fase 3.2, non completabile in un solo lotto.
- **Item 4** (descrittività dei titoli di tabella e indicazione della
  fonte): richiede lettura qualitativa campione per campione.
- **Item 6** (uniformità tipografica): verificabile programmaticamente
  (conteggio di varianti di trattino, virgolette, formati numero/data)
  ma non ancora eseguito.
- **Item 7** (coerenza dei rimandi "cfr. §…"): richiede mappatura di
  ogni rimando interno alla sezione effettivamente esistente.
- **Item 8** (front matter/back matter standard): richiede verifica
  strutturale sull'ordine delle sezioni di apertura/chiusura di
  ciascun tomo.
- **Item 9** (versioning esplicito per file): verificabile rapidamente,
  non ancora eseguito.

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
decisione pendente. Item 1, 4, 6, 7, 8, 9 non ancora avviati.
