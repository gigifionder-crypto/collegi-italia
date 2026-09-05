# OPERA NERA — Il Secolo Nero della Bella Europa

## Edizione integrale e omnicomprensiva

L'opera integrale esiste in **due formati della stessa composizione**, non in
due edizioni diverse: **il volume unico** e **gli undici tomi**. Stesso testo,
stessa impaginazione, stesso corpo tipografico; cambia solo in quanti file
sta. *Chi confronta una pagina dell'uno con la stessa pagina degli altri deve
trovarle identiche* — e ora le trova.

| | volume unico | undici tomi |
|---|---:|---:|
| **File** | 1 | 11 |
| **Pagine** | 3.556 | 3.596 |
| **Peso** | 39,8 MiB | 40,4 MiB |
| **Parti del corpus** | 154 | 154 |
| **Parole** | 2.089.199 | 2.093.564 |
| **Segnalibri** | 3.098 | uno per tomo |

La differenza di quaranta pagine e di quattromila parole è tutta nel
frontespizio: i tomi lo ripetono undici volte, il volume una sola.

**Sul peso.** I PDF escono da Chromium con l'albero dei tag scritto in chiaro:
per un'opera di due milioni di parole sono **centosettantatremila oggetti** che
da soli pesavano un terzo del file. La sigillatura li impacchetta in flussi
d'oggetti — **nulla si perde, ed è verificato prima e dopo: pagine, segnalibri,
struttura accessibile, metadati** — e il volume unico scende **da 61,3 a 39,8
MiB**, l'edizione ridotta da 4,7 a 2,5. *La ricompressione è deterministica,
perciò l'impronta resta riproducibile.*

```
_monografia/compila_volume.sh    <cartella>   # il volume unico
_monografia/compila_integrale.sh <cartella>   # gli undici tomi
sha256sum <cartella>/*.pdf
```

La compilazione è **riproducibile**: le date interne dei PDF sono fissate e non
prese dall'orologio, perciò due compilazioni della stessa sorgente danno lo
stesso SHA-256. **È questa la ragione per cui l'impronta certifica qualcosa.**

**Il Tomo I è la guida e i dieci che seguono sono il corpus**; nel volume unico
la guida è la prima parte e il corpus la seconda. Nella guida stanno il prologo
sulla scala di triangolazione, il proemio con i sei nomi, i sette libri
narrativi coi loro referti, il congedo, il quadro sinottico delle piste e gli
apparati. Nel resto sta tutto il resto: **non una scelta, tutto**, nell'ordine
in cui `parti.json` lo registra.

## Il difetto che ha fatto nascere questa nota

**Tre tomi su undici sono stati composti, e consegnati, di due terzi.** Il testo
c'era tutto e i segnalibri funzionavano; era il corpo tipografico a essere
sbagliato — **11 punti d'interlinea invece di 16,5** — e a occhio nudo, su un
PDF che nessuno affianca a un altro, non si vede.

**La causa non era la lunghezza: era la larghezza.** Alcuni indirizzi
dell'apparato bibliografico non stavano nella riga e non andavano a capo: un
solo elemento più largo della pagina fa scattare in Chromium l'adattamento alla
larghezza, che **rimpicciolisce l'intero documento** per farci stare quell'unico
elemento. Un indirizzo di 1.362 pixel su una pagina di 794 ha rimpicciolito
centoventicinque pagine di apparato — che infatti, composte come si deve, sono
duecentocinquantadue.

**Due rimedi, e il secondo è quello che conta.** I gettoni lunghi ora si
spezzano (`overflow-wrap`), così nulla straripa; e **il compositore si rifiuta
di comporre** se qualcosa straripa ancora, nominando l'elemento e la sua
larghezza. *Un difetto che non si vede va reso impossibile, non corretto una
volta*: la stessa regola per cui questa filiera già si rifiuta di comporre
quando il font non è quello dichiarato.

*L'errore resta scritto qui accanto alla sua correzione, come ogni correzione
di quest'opera.*

## Le regole di questa edizione

**I libri e i capitoli non portano titolo: portano la loro numerazione.** Un
titolo è già una lettura, e anteporne una a ogni documento contraddirebbe
un'opera costruita per separare il fatto dalla sua interpretazione. *Ciò che il
documento dice di sé resta*: il titolo che ciascuna parte si dà è la sua prima
riga, un gradino più in basso nella gerarchia.

**Nessuna parte è spezzata fra due tomi.** Un documento è un'unità: tagliarlo a
metà per far quadrare un conto di pagine farebbe prevalere la contabilità sul
contenuto. Le parti che da sole superano il bersaglio fanno tomo da sé — il
Tomo V è una parte sola in 557 pagine — e i tomi sono perciò diseguali: **è la
conseguenza voluta della regola, non un difetto della ripartizione.**

**L'ordine appende e non rinumera.** Una campagna aggiunta dopo entra in coda
anche se il suo Libro era stato aperto molto prima, e un tomo può perciò
passare da un'Appendice a un Libro già incontrato. **Non è disordine: è la
storia del corpus leggibile nel suo ordine**, preferita a una risistemazione
che cancellerebbe l'ordine in cui il lavoro è realmente cresciuto.

**Le sigle «bis».** La terza campagna del Libro dodicesimo ripartì da IV e
riusò i numerali della seconda. Il registro **non è stato rinumerato**; alla
seconda occorrenza di un numerale si aggiunge «bis» **in composizione**, perché
un rinvio dev'essere univoco. *«bis» non afferma nulla: dice soltanto che quel
numero compare per la seconda volta nel registro.*

**Questi file non entrano in nessun registro dell'opera.** Ricompongono
documenti già contati, e contarli sarebbe contare due volte ogni documento che
portano: `registro_convergenze.py` e `registro_savona.py` escludono
`_integrale/` per nome, con la ragione scritta accanto. *Le celle aperte
restano centoquarantadue, le conferme del risultato ricorrente dodici, gli
archi Savona cinquantasei.*

## Che cosa sta nel repository e che cosa no

**Il volume unico c'è** — `_integrale/OPERA-NERA-volume-unico.pdf` — perché un
lettore che lo vuole non deve dover compilare un repository per averlo. **I markdown assemblati e i PDF dei tomi
no**: sono derivati per intero da documenti che il repository già custodisce, e
versare la copia di ciò che l'archivio contiene non aggiunge una fonte —
aggiunge un secondo esemplare da tenere allineato al primo, e prima o poi
disallineato.

## La composizione

Barlow Semi Condensed in sei tagli, carta bianca con gradiente crema al 5%,
inchiostro blu navy con gradiente nero al 5%, testo giustificato con
sillabazione italiana propria — **`hyphens:auto` è inerte in questo Chromium,
verificato con una prova, non supposto**. I PDF sono **taggati**, con
**segnalibri** e **numerazione di pagina**, e ciascuno porta nei metadati
l'impronta della propria sorgente (`/SourceSHA256`).
