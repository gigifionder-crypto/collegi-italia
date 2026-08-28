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
