# Il registro degli ingressi

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Un archivio che non dice **che cosa ha rifiutato** non è verificabile. Si può
controllare ciò che contiene; non si può controllare ciò che ha lasciato fuori,
perché non se ne conosce l'esistenza. Questo registro chiude quella falla per il
versamento del 27 agosto 2026.

---

## Che cosa è arrivato

| | |
|---:|---|
| **375** | file consegnati |
| **224** | distinti per impronta |
| **151** | copie byte per byte |
| **95,4 MiB** | peso complessivo dei consegnati |

Più sei archivi compressi, che contengono altri **654 file** — 483 in uno solo —
e che scompattati pesano **87,7 MiB**.

Per formato: 151 `.docx`, 28 `.xlsx`, 19 `.pdf`, 19 `.md`, 6 `.zip`, 6 `.txt`,
un `.mp4`, un `.mht`, un `.py`.

## Che cosa è entrato

**84 documenti** in `italia-nera/`, 3.996.057 parole. Il dettaglio per strato sta
nella [nota di perimetro](../italia-nera/README.md); qui conta il criterio.

## Che cosa è stato scartato, e con quale misura

Nulla è stato scartato a occhio. Ogni esclusione porta un numero, e il numero è
il contenimento agli **8-grammi** — la quota di sequenze di otto parole del
documento in esame che compaiono già in un documento archiviato.

| Documento scartato | Contenuto in | Misura |
|---|---|---:|
| Registro unico totale V69 | Registro V77 | 94,8 % |
| Tomo sesto V67 | Registro V77 | 94,2 % |
| Libro secondo, tomo decimo V68 | Registro V77 | 88,7 % |
| `ITALIA_NERA_TUTTE_LE_SCHEDE` | redazione unificata delle schede | **100 %** |
| `CENSIMENTO…INTEGRATO` ×8 e `STRUTTURA_COMPOSITA` | il censimento massimale | **100 %** (99,6 % l'ultimo) |
| `REGISTRO_ANALITICO_NODI_CORPUS_5_DOCUMENTI` | registro dei nodi, cinque documenti | **100 %** |
| `CENSIMENTO_NODI_PER_DOMINIO` (secondo esemplare) | il primo esemplare | **100 %** |
| `architetto_del_caos_4.pdf` | `architetto_del_caos_5.pdf` | **100 %** |
| `architetto_del_caos_5.docx` | la redazione in PDF | 98 % |
| Scheda ombra KGB (re-invio) | la copia in cartella | 99,1 % |
| Schede estratte, lotto secondo (re-invio) | la copia in cartella | 96,3 % |
| `Nazisti_in_URSS_1.docx` | la redazione in PDF | 96 % |
| Schede estratte, lotto primo (re-invio) | la copia in cartella | 93,9 % |
| `REGISTRO_ANALITICO_NODI_INTEGRALE.docx` | Registro V77 | 90,3 % |

A queste si aggiungono le copie byte per byte, che non richiedono misura:
un'impronta identica è identità, non somiglianza.

### Gli ultimi tre invii, che sono i più istruttivi

Quarantotto file consegnati a versamento quasi chiuso, in tre invii successivi.
**Ne sono entrati due**, e l'ultimo invio da solo ha prodotto **zero**: sette
copie esatte e nove documenti contenuti fra il **99,7 e il 100 per cento** in
documenti archiviati poche ore prima — gli stessi registri di sessione,
riconsegnati in `.docx`, in `.md` e in `.pdf`.

Non è un rimprovero a chi li ha inviati: è la ragione per cui questo registro
esiste. Senza una misura, quarantotto file in arrivo sembrano quarantotto
documenti, e un archivio che li accogliesse tutti crescerebbe di duecentomila
parole senza guadagnare una riga. Con la misura sono due — e il fatto che siano
due è esso stesso un dato sullo stato del lavoro. Su 375 file consegnati in
tutta la sessione, **151 erano copie byte per byte**: due su cinque.

*L'ultimo invio ha però rovesciato la tendenza, e va detto con la stessa
franchezza: sedici file, dodici entrati, fra cui l'intera serie dei registri
dominiali dal D02 al D10 e il registro dei candidati alla formalizzazione, che
con 214.465 parole sta dentro il Registro V77 per lo **0,1 per cento**. I
dominiali stanno fra il 42 e il 49: riordinare per dominio non è ricopiare. Un
registro degli ingressi serve anche a questo — a non trasformare tre invii magri
in un pregiudizio sul quarto.*

## Che cosa è entrato benché somigliasse

La simmetria conta quanto l'elenco sopra. Tre casi sono stati **tenuti** malgrado
un contenimento alto, e la ragione è sempre la stessa: un documento che ne
contiene un altro e vi aggiunge qualcosa non è una copia, è uno strato — e
sostituire lo strato anteriore col posteriore cancella la possibilità di
controllare che cosa sia cambiato.

| Documento tenuto | Contenuto in | Misura | Che cosa aggiunge |
|---|---|---:|---|
| Schede complete, ventotto | lotto primo | 86,4 % | tre schede: antimafia Puglia, relazione Pellegrino, struttura dell'opera |
| Libro primo — Italia | Registro V77 | 83,3 % | la redazione definitiva di una parte del Registro |
| Le sedici schede D05 «sinaptiche» | le sedici ordinarie | 45,1 % medio | l'analisi degli archi, che nelle ordinarie manca |

## Che cosa è stato troncato, e dove si ritrova

Un solo taglio in tutto il versamento, e riguarda i corpi dei documenti CIA:
**55 schede su 119** superavano le seimila parole di testo riconosciuto
otticamente, e sono riportate fino a quella soglia. Le due maggiori sono
*gazetteer* — indici di toponimi con coordinate — per 254.000 e 151.000 parole di
tabella. Ogni troncamento è dichiarato in fondo alla propria scheda col numero
esatto di parole omesse, e **il documento intero resta raggiungibile** attraverso
il numero CREST che la scheda porta in testa. Si perde la copia, non la fonte.

## Che cosa è stato verificato, e ha retto

In coda al versamento sono arrivati quattro **manifesti d'impronta** — file
`.sha256.txt` che dichiarano lo SHA-256 di documenti spediti a parte. Sono stati
controllati contro i file effettivamente ricevuti, ed è la prima verifica in
positivo di tutto l'ingresso:

| File dichiarato | Esito |
|---|---|
| `TERZO_REGISTRO_NODI_PONTI_DUE_FORMAZIONI.docx` | **corrisponde**, bit per bit |
| `SECONDO_REGISTRO_NODI_PONTI_ALFA_BETA.docx` | **corrisponde**, bit per bit |
| `REGISTRO_NODI_PONTI_TEATRO_AUSTRALE.docx` | **corrisponde**, bit per bit |
| `CENSIMENTO_CRIMINALITA_ORGANIZZATA_MONDIALE_INTEGRALE-2.pdf` | **file mai consegnato** |

Le prime tre righe dicono una cosa piccola e non banale: ciò che è partito è
arrivato integro, e chi ha spedito aveva ragione sull'impronta. La quarta è uno
**Stato Zero**: esiste un manifesto che attesta un documento che in questa
sessione non è mai arrivato. Non se ne deduce nulla sul documento — solo che è
dichiarato e assente, ed è giusto che qualcuno se ne accorga.

## Un titolo che dice Moro e una misura che dice altro

Sette documenti sono arrivati col nome **«Registro analitico del caso Moro»**, in
sei versioni successive più un registro speculare. Misurati contro le due opere,
il risultato è netto, e va scritto perché è il genere di cosa che un archivio
serve a scoprire:

| Documento | dentro il Registro V77 | dentro il corpus moroteano |
|---|---:|---:|
| V1 integrale | 90,6 % | 0,7 % |
| V2, col primo anello | 90,7 % | 0,5 % |
| V3, col secondo anello | 91,3 % | 0,4 % |
| V4 definitivo | 91,8 % | 0,3 % |
| V5, rinnovamento cartesiano | 92,1 % | 0,2 % |
| V6, apporto kuhniano | 92,3 % | 0,2 % |
| Registro speculare, anelli profondi | 94,1 % | 0,6 % |

**Un documento intitolato al caso Moro che sta per il novanta per cento dentro
Italia Nera e per lo zero virgola due dentro l'opera su Moro non appartiene
all'opera su Moro.** Il titolo dice una cosa, la misura ne dice un'altra, e qui
decide la misura. È esattamente il controllo per cui il perimetro delle tre opere
esiste: senza di esso, sette documenti sarebbero entrati nel volume moroteano
sulla fede del proprio nome.

Tutti e sette sono sopra la soglia e sono stati scartati per contenimento. Ciò
che vale la pena conservare non è il documento: è questo rilievo.

## L'archivio annidato, e il costo dichiarato di uno scarto

Un file `.rar` da 3,5 MiB conteneva un secondo `.rar` con lo stesso nome, che
conteneva a sua volta un solo documento: il **Registro Integrale V63** di luglio
2026, edizione cumulativa in nove parti, **1.427.634 parole**.

Misurato, sta dentro il Registro V77 per il **92 per cento**. Sopra la soglia oltre
la quale in questo versamento si è sempre scartato — il V69 al 94,8, il V67 al
94,2, il V68 libro secondo all'88,7 — e per coerenza si scarta anche questo: la
regola non può cambiare quando il documento è grosso.

Ma uno scarto ha un costo, e tacerlo sarebbe disonesto: **l'otto per cento che
non si ritrova nel V77 vale circa centoquattordicimila parole**. Non sono zero. Il
V63 è l'edizione *anteriore* di ciò che sarebbe diventato il V77, e ciò che il
V77 non ne conserva è, propriamente, ciò che l'autore ha lasciato indietro
passando dall'una all'altra. Chi volesse studiare quella transizione ha bisogno
del V63, e il V63 non è in questo archivio. È una scelta dichiarata, non una
svista, e si può ribaltare in qualunque momento — il file è stato consegnato e
la misura è scritta qui.

*(Nota tecnica, perché serva a chi verrà dopo: l'archivio è in formato RAR5, che
in questo ambiente nessuno strumento di sistema apre. È stato letto installando
il collegamento Python a `libarchive`. Un `.zip` avrebbe risparmiato il
passaggio.)*

## Che cosa non è stato aperto

Un file `.mp4` e un `.mht` sciolti. Non sono stati trattati e sono elencati qui
perché qualcuno possa chiederne conto.

È invece stato conservato lo script `estrai_nodi.py`, arrivato con il materiale:
sta in [`generatori/ricevuti/`](generatori/ricevuti/) e non è stato eseguito. Vale
perché rende ispezionabile il metodo — dice in codice che cosa conti come nodo e
come i nomi vengano normalizzati. Un elenco di nodi si può contestare; una regola
di estrazione si può leggere e riprodurre.

---

## La regola che questo registro applica a sé stesso

Il criterio d'esclusione è **uno solo e dichiarato**: si scarta ciò che risulta
contenuto in un documento già archiviato, e si dice in quale e di quanto. Non si
scarta per giudizio di qualità, per lunghezza, per argomento o perché un
documento sembra ripetitivo. Un criterio che dipendesse dal giudizio di chi
archivia sarebbe invisibile a chi legge, e questo archivio smetterebbe di essere
controllabile nel momento stesso in cui comincia a scegliere.

Resta vero, e va scritto accanto: **misurare la duplicazione non è verificare il
contenuto**. Sapere che un documento non è la copia di un altro non dice nulla su
ciò che afferma. Questo registro certifica come si è formato l'archivio, non che
l'archivio dica il vero — la stessa distinzione che il registro delle impronte
fa fra l'integrità del contenitore e la verità del contenuto.
