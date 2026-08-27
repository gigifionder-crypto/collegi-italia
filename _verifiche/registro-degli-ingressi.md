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
| **232** | file consegnati |
| **174** | distinti per impronta |
| **58** | copie byte per byte |
| **81,0 MiB** | peso complessivo dei consegnati |

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

### L'ultimo invio, che è il più istruttivo

Sedici file consegnati a versamento quasi chiuso. **Ne è entrato zero.** Quattro
erano copie esatte l'uno dell'altro; i dodici restanti stanno fra il **93,9 e il
100 per cento** dentro documenti archiviati poche ore prima — gli stessi registri
di sessione, riconsegnati in `.docx`, in `.md` e in `.pdf`.

Non è un rimprovero a chi li ha inviati: è la ragione per cui questo registro
esiste. Senza una misura, sedici file in arrivo sembrano sedici documenti, e un
archivio che li accogliesse tutti crescerebbe di ottantamila parole senza
guadagnare una riga. Con la misura, sono zero — e il fatto che siano zero è esso
stesso un dato sullo stato del lavoro.

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

## Che cosa non è stato aperto

Un file `.mp4` e un `.mht` sciolti, e alcuni `.txt` che contengono impronte di
file `.pdf` mai consegnati. Non sono stati trattati e sono elencati qui perché
qualcuno possa chiederne conto.

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
