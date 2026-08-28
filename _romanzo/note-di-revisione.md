# Note di revisione — prima lettura di seguito

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana. La dichiarazione sta in apertura, non in calce.*

Rilegata la prima stesura, il libro è stato letto di seguito per la prima volta —
cosa che sui capitoli sciolti non era possibile. Queste sono le note che ne
escono. Sono **misurate e non impressionistiche**: lo strumento è
[`_verifiche/generatori/analisi_romanzo.py`](../_verifiche/generatori/analisi_romanzo.py),
il criterio è nello script, e chiunque può rifare le misure e smentirle.

---

## 1. L'equilibrio delle due voci

Misura: quota di parole in corsivo (prosopopea) sul totale del capitolo.

| parte | parole | corsivo | tondo | quota corsivo |
|---|---:|---:|---:|---:|
| I — L'elenco che arriva | 1.387 | 854 | 533 | 62% |
| II — L'uomo prima del caso | 1.665 | 1.054 | 611 | 63% |
| III — Gli anni della Farnesina | 1.518 | 827 | 691 | **54%** |
| IV — Le lettere che qualcuno ha scelto | 1.570 | 915 | 655 | 58% |
| V — L'archivio | 1.658 | 1.115 | 543 | **67%** |
| VI — L'aritmetica | 2.002 | 1.233 | 769 | 62% |
| VII — Ottocentotredici volte «non trovato» | 1.998 | 1.101 | 897 | 55% |

Media 60%, estremi 54% e 67%. **La banda è stretta e non richiede intervento.**

Merita però una nota: i due estremi non sono casuali e non vanno pareggiati. La
parte terza è la più povera di voce perché è quella in cui l'oggetto è l'ufficio
che egli tenne, e il vincolo impone che il racconto lo faccia l'apparato. La
parte quinta è la più ricca perché il suo oggetto — che cosa sia una fonte — è
per intero un problema di prova, cioè il solo terreno su cui la voce prestata ha
titolo. **La quota di corsivo misura, senza volerlo, quanto ciascun capitolo sia
lontano dalla persona di Aldo Moro.** È il grafico del vincolo.

---

## 2. Il ritmo, e l'unico blocco che si è dovuto rompere

Misura: parole per paragrafo, parole per sezione.

I paragrafi stanno fra 38 e 49 parole di media, col più lungo a 111: è un passo
uniforme e non c'è nulla da fare. Le sezioni stavano invece fra 154 e 256 parole
di media, con **una sola fuori scala: il §II della parte terza, 510 parole in un
blocco unico** — tredici voci di cronaca in fila, ciascuna con la sua data, il
suo luogo e il suo grado.

**Intervento eseguito.** Quel blocco era una tabella travestita da prosa, ed è
stato reso alla propria forma: tredici righe con data, luogo, fatto e grado. Ne
sono nate due sezioni nuove che prima stavano sepolte nel flusso — *Le tre
divergenze, che restano aperte* e *Le due correzioni, scritte accanto
all'errore* — e il guadagno non è di sola leggibilità: le divergenze e le
correzioni sono la disciplina del libro, e stavano nascoste dentro un elenco.
Ora si vedono.

Effetto collaterale, misurato: la quota di corsivo della parte terza sale dal 46%
al 54%, e il capitolo rientra nella banda degli altri. Non era lo scopo; è la
conferma che il blocco era gonfio di apparato.

---

## 3. La ripetizione fra capitoli

Misura: contenimento di 8-grammi fra ogni coppia di capitoli — lo strumento con
cui il corpus decide se un documento è un doppione.

**Un solo incrocio sopra lo zero: parte I e parte VI, undici 8-grammi condivisi,
lo 0,75%.** La soglia di scarto del corpus è il 90%. Non c'è duplicazione.

Gli undici 8-grammi sono una sola frase, ed è deliberata: *nessun numero di
tessera dei trentatré è stato letto sulla fonte*. Ricorre nella parte I, nella V
e nella VI. **Si tiene.** È il basso continuo del libro: la proposizione che
nessuna delle sue centoquaranta pagine future potrà cancellare, e che va
ripetuta esattamente perché il lettore, procedendo, comincia a credere il
contrario.

---

## 4. Un errore di misura, corretto qui

La prima passata di questa analisi ha riportato la locuzione «onde» dieci volte,
quattro delle quali nella sola parte settima, e l'aveva segnalata come un tic da
diradare.

**Era falso.** Il conteggio cercava la stringa e non la parola, e contava «onde»
dentro «risponde». Le occorrenze vere sono **tre in tutto il libro, una per
capitolo nelle parti terza, quinta e settima**: è una firma della voce, non un
vezzo, e non si tocca.

Lo si scrive qui, e non si emenda in silenzio, perché è la terza volta in questo
lavoro che accade la stessa cosa e sarebbe disonesto lasciar credere che accada
solo agli altri: una probabilità ritirata perché dipendeva da un parametro non
dichiarato, un conteggio ritirato perché dipendeva da un perimetro non
dichiarato, e ora una frequenza sbagliata perché il criterio confondeva la
stringa con la parola. **La regola è sempre la medesima, e questa volta ha colpito
lo strumento con cui si controllano gli altri.**

Lo script è stato corretto, e la correzione porta accanto il commento che dice
perché.

---

## 5. Che cosa non si è toccato, e perché

**La banda 54-67% del corsivo.** Vedi il §1: misura il vincolo, non uno squilibrio.

**Il ritorno del grado B nelle parti IV e VI** (cinque e sei occorrenze contro una
altrove). Sono i due capitoli che lavorano su documenti non letti alla fonte:
la concentrazione è del materiale, non della scrittura.

**La lunghezza disuguale dei capitoli** (1.387 la parte I, 2.002 la sesta). In una
prima stesura è informazione utile: dice dove il materiale abbondava. Si pareggia
in estensione, non in taglio.

---

## 6. Che cosa la lettura di seguito ha mostrato e le misure non dicono

Tre cose, e vanno dette come giudizio e non come dato.

**Il libro ha un arco, e non era stato progettato.** Le parti sono state scritte
nell'ordine in cui il materiale era pronto — la sesta per prima, la terza per
ultima — e lette in fila raccontano una discesa regolare: un foglio che arriva,
un uomo che non si può conoscere dalle carte, un ufficio che non lascia l'uomo,
delle lettere che non si possono citare, un archivio che non si apre,
un'aritmetica che si ritira, un registro di ciò che non si è trovato. **Sette
capitoli, sette forme di non-accesso.** Se il libro ha una tesi, è questa, e non è
mai enunciata.

**Manca un respiro.** Sette capitoli che dicono tutti, con mezzi diversi, «non si
può sapere» sono giusti singolarmente e monotoni in fila. Serve almeno un punto
in cui la verifica **riesce** — e ce n'è uno vero, già nel materiale: le due righe
di Berlusconi e Costanzo che il riscontro indipendente conferma esattamente. Nella
stesura attuale è un inciso della parte quinta. **In estensione va data a quel
riscontro la scena che merita**, perché senza un successo il metodo sembra un
modo elegante di non concludere, e non lo è.

**La parte seconda è il capitolo che regge il peso maggiore**, ed è il più corto
dei tre lunghi. È l'unico ritratto d'uomo del libro, ed è quello in cui la voce si
ferma. In estensione è il primo su cui tornare.

---

## 7. Ordine dei lavori, se si estende

1. **Parte II** — il ritratto: è il capitolo che il lettore ricorderà, e oggi è
   asciutto.
2. **Parte III** — la Farnesina: lo spoglio ha reso ventitré proposizioni datate,
   e ne sono entrate tredici. Le altre dieci vanno vagliate.
3. **Parte V** — l'archivio: qui va la scena del riscontro riuscito (§6).
4. **Le ore dei cinquantacinque giorni** — resta la ricerca d'archivio più
   fruttuosa, dopo l'allegato 21. Non è materia di scrittura: è materia di
   archivio, e non si supplisce.

---

## 8. Interventi eseguiti sulle note stesse — 28 agosto 2026

Le due voci del §7 in cima all'ordine dei lavori sono state eseguite. Si
annotano qui, sotto le note che le prescrivevano, invece che riscrivere quelle.

**Il respiro (§6).** La parte quinta ha ora la scena del riscontro riuscito, in
due sezioni nuove.

*«Le due righe che tornano»* racconta l'unica verifica del libro che riesce:
diciassette ricerche indipendenti, che non si conoscevano fra loro e non
sapevano l'esito atteso, riportano gli stessi due numeri su cui l'intera
calibrazione poggiava — e con essi quattro dati che il testo pervenuto non aveva
fornito (sigla, gruppo, giorno dell'affiliazione, qualifica), più il presupposto
che valeva più dei numeri: che l'elenco porti per ciascun nome due numeri
distinti, fascicolo e tessera. E una terza coppia attestata che nessuno aveva
chiesto.

*«Quanto vale una conferma»* è la sezione che impedisce alla prima di diventare
un trionfo. Una conferma non vale per il fatto di essere una conferma: vale in
proporzione a quanto facilmente avrebbe potuto non venire. Quella poteva
fallire, e lo sappiamo per la ragione più persuasiva che esista — **sugli altri
due nomi è fallita davvero**, nello stesso giorno e per le stesse mani. È il
punto: quelle righe pesano non perché siano tornate, ma perché sono tornate da
uno strumento che quel giorno ha dimostrato di saper dire di no. *Una prova che
non può fallire non è una prova: è uno specchio.* E la misura del guadagno resta
piccola e dichiarata: due righe su trentatré non certificano trentatré righe; si
è passati dal non sapere se il testo contenesse qualcosa di vero al sapere che ne
contiene, ed è una soglia che si attraversa una volta sola.

**La parte seconda (§7.1).** Estesa da 1.665 a 2.208 parole. Sono entrati i dati
che mancavano e che il corpus aveva: il Movimento dei Laureati Cattolici
1945-46, la guida spirituale di Montini, le cariche fino alle cinque presidenze
del Consiglio fra il 1963 e il 1976, e soprattutto **la data e il luogo delle
formule** — la strategia dell'attenzione al congresso regionale pugliese, Bari,
15 giugno 1969; la «terza fase» in un articolo per *Il Giorno* del dicembre
1976; e la tesi nelle sue parole pubbliche, riportata al grado F quanto
all'averla sostenuta e al grado C quanto a ogni giudizio sul suo fondamento.

È entrata anche una sezione nuova, *«L'enunciato che tiene aperte due strade»*,
ed è la ragione per cui il capitolo si è esteso più del previsto: la formula
ampia, che di Moro è il tratto più discusso, **è un problema di prova** e cade
perciò esattamente nel campo della voce prestata. Se un enunciato fu costruito
perché reggesse due letture, non esiste un significato nascosto da riportare
alla luce: esiste un enunciato che due letture reggono, e sceglierne una non è un
accertamento ma una decisione dell'interprete, che egli attribuisce all'autore.
La sezione porta anche il suo costo, come le altre: chi parla così non risponde
delle letture altrui, ma risponde di averle rese tutte possibili.

**Misure dopo l'intervento.** Le due parti passano a 63% e 65% di corsivo, dentro
la banda. Il volume passa da 34 a 36 pagine e da 14.288 a 15.422 parole. La
sezione più lunga resta il §II della parte terza (519 parole), che però è ora in
massima parte tabella e non blocco di prosa.

**Restano aperti** i punti 2 e 4 del §7: le dieci proposizioni dello spoglio non
ancora vagliate, e le ore dei cinquantacinque giorni — che non sono materia di
scrittura.

---

## 9. Il vaglio delle proposizioni residue — 28 agosto 2026

Eseguito anche il punto 2 dell'ordine dei lavori: le proposizioni dello spoglio
non entrate nella parte terza sono state vagliate a una a una. Nella tavola sono
salite da tredici a quindici righe, e il vaglio ha prodotto un nuovo §III che è
tutto sullo strumento.

**Cinque delle ventitré sono la stessa proposizione**: le due date del mandato,
ripetute in cinque documenti che se le trasmettono. Contate una per una fanno
cinque, contate per ciò che dicono fanno una. **Il numero ventitré ha lo stesso
vizio del numero 813**, e ora il capitolo lo dice in apertura invece di lasciarlo
credere.

**Quattro sono fuori dal mandato e tre lo dichiarano da sé** — il Trattato di non
proliferazione (28 gennaio 1969), l'accordo Comunità-Cipro (19 dicembre 1972),
l'udienza vaticana del 12 gennaio 1973 che il corpus stesso dice coinvolgere Moro
«solo per contiguità cronologica e ambientale». Il vaglio non le ha escluse: ha
letto che erano già escluse.

**Una era un falso candidato prodotto dallo strumento.** Una proposizione
accostava il 23 luglio 1969 alla frase «la Farnesina di Moro non vi si oppose»,
data anteriore di tredici giorni all'insediamento: sembrava un errore del corpus.
Non lo è — quel giorno è, nel documento, lo scoppio di un caso spagnolo, e il
taglio automatico delle frasi aveva unito due cose contigue. **L'errore era del
criterio, non della fonte.**

**E il criterio aveva scartato un fatto che valeva.** La soglia chiedeva una data
risolvibile almeno al mese, e una proposizione datata «primavera 1970» è passata
sotto: è quella per cui, in una sequenza diplomatica spagnola fittissima, l'Italia
compare **una volta sola e per opporre un rifiuto**. È entrata, dichiarata. Con
essa è entrata anche l'apertura della CSCE a Helsinki, 3 luglio 1973, quattro
giorni prima del rientro alla Farnesina.

**La lezione, e la sezione nuova in corsivo che la porta.** Una regola
d'ammissione è la condizione della serietà — senza, la ricerca non è rifacibile —
e nel medesimo atto in cui rende visibile ciò che le corrisponde rende invisibile
tutto il resto, che non è irrilevante: la regola non fu fatta sulla rilevanza, fu
fatta sulla forma. Qui **la soglia misurava la precisione della fonte e ha
filtrato la rilevanza del fatto.** Ne discendono i due obblighi che il §IV
enuncia: la regola si dichiara prima — chi la scriva dopo aver veduto gli esiti
ha descritto la propria selezione con le parole di un criterio — e si rilegge
fuori dalla regola ciò che la regola ha scartato, dicendo di averlo fatto.

**Misure.** La parte terza passa da 1.518 a 2.386 parole e da 42% a **52%** di
corsivo, rientrando in banda (l'aggiunta del solo apparato l'aveva portata fuori,
e la sezione in corsivo l'ha riportata dentro — misurato, non stimato). Il volume:
**37 pagine, 15.986 parole**.

**Resta aperto** il solo punto 4: le ore dei cinquantacinque giorni, che non sono
materia di scrittura.

---

## 10. Estesa la parte prima, e la regola che governa il libro finalmente argomentata — 28 agosto 2026

La parte prima era la più corta del libro (1.387 parole) ed è quella che un
editore legge per prima. Estesa a 2.249 con tre sezioni nuove, due in corsivo e
una in tondo, che colmano una lacuna vera: **la regola che governa ogni pagina
era enunciata e mai argomentata.**

*«L'appartenenza e la condotta»* la argomenta, e non come cortesia verso i
nominati: è una proposizione di logica. L'inferenza vietata scende da una
proposizione sulla classe a una proposizione sull'individuo, e non tiene perché
una classe può essere omogenea sotto il rispetto per cui la si è definita e
disomogenea sotto ogni altro. Con la chiusa che vale per tutto il libro: la
regola protegge, nel medesimo atto e con la stessa forza, i quattro nomi di cui
non si è trovata conferma — *una regola che valesse soltanto per chi ci è
simpatico sarebbe una preferenza munita di articoli.*

*«Il dato empirico contro l'inferenza collettiva»* porta in tondo, coi gradi, il
fatto che la voce richiama: nel caso spagnolo del 23 luglio 1969 chi denunciò e
chi ne fu travolto appartenevano al medesimo sodalizio. **Grado F** per la
denuncia e l'arresto, **B** per l'appartenenza comune. Con le due cautele che il
dato richiede: un arresto non è un giudicato e nessuna imputazione discende da
queste righe; e il dato non stabilisce che l'appartenenza sia sempre irrilevante
— stabilisce che l'inferenza dalla classe all'atto non vale come regola, e che
chi voglia servirsene deve provarla nel caso, cioè fare il lavoro che
l'inferenza gli prometteva di risparmiare.

*«Verificare contro il proprio desiderio»* è il motore morale, e mancava. Chi
verifica non parte neutro; non ci si libera dell'inclinazione, si dispongono le
prove in modo che il desiderio non le raggiunga — criterio fissato prima,
smentita dichiarata prima, esito negativo scritto con la stessa cura del
positivo. E la prova di collaudo, che vale per questo metodo come per ogni
altro: **produce, di tanto in tanto, risultati che dispiacciono a chi lo
adopera?** Se non ne produce mai, non è un metodo.

**Misure.** Le due sezioni in corsivo avevano portato la parte prima al 74%, fuori
banda; la sezione in tondo l'ha riportata al **66%**. Tutte e sette le parti
stanno ora fra 52% e 66%. Il volume: **39 pagine, 16.700 parole circa.** La parte
quarta è ora la più corta (1.570) ed è la prossima da estendere.

## 11. Il registro delle impronte riconosce una quarta famiglia

Il romanzo è entrato nel registro SHA-256, e **non dentro l'opera**. È una quarta
famiglia accanto alle tre esistenti — l'opera su Moro, Italia Nera, lo Studio
Puglia — e ha un proprio manifesto, `IMPRONTE-ROMANZO.txt`, con la propria
impronta.

La ragione è la stessa che il registro applica a sé stesso: **contare dentro
l'opera ciò che l'opera ha prodotto sarebbe contarlo due volte**, ed è la forma
più insidiosa di doppio conteggio, perché a differenza delle altre non si vede.
La nota di progetto del romanzo lo dichiarava dal primo giorno — *questa cartella
non fa parte del corpus* — e ora lo dichiara anche l'aritmetica.
