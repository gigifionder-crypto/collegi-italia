# OPERA NERA — edizione integrale e omnicomprensiva

## Che cosa c'è qui, che cosa non c'è, e perché

**Questa cartella contiene la macchina dell'edizione integrale, non l'edizione.**
Ci sono il manifesto dei tomi, le impronte SHA-256 di ciascuno e questa nota.
**Non ci sono né i PDF né i markdown dei tomi**, e la ragione è la stessa che
ha prodotto l'edizione in tomi: sono **sessantuno megabyte di PDF e quattordici
di markdown**, e sono **interamente derivati** da documenti che il repository
già custodisce. *Versare in un archivio la copia di ciò che l'archivio contiene
non aggiunge una fonte: aggiunge un secondo esemplare da tenere allineato al
primo, e prima o poi disallineato.*

**Si ricostruiscono con un comando**, e l'impronta deve tornare identica:

```
_monografia/compila_integrale.sh <cartella>
sha256sum <cartella>/*.pdf
```

La compilazione è **riproducibile**: le date interne dei PDF sono fissate e non
prese dall'orologio, perciò due compilazioni della stessa sorgente danno lo
stesso SHA-256. **È questa la ragione per cui l'impronta certifica qualcosa.**
*Verificato: ricompilando il Tomo IX si è riottenuta l'impronta identica.*

## L'edizione in breve

| | |
|---|---|
| **Tomi** | 11 |
| **Parti del corpus** | 154, nessuna spezzata fra due tomi |
| **Parole** | 2.083.941 |
| **Pagine** | 3.261 |

**Il Tomo I è la guida e i dieci che seguono sono il corpus.** Nella guida
stanno il prologo sulla scala di triangolazione, il proemio con i sei nomi, i
sette libri narrativi coi loro referti, il congedo, il quadro sinottico delle
piste e gli apparati. Negli altri sta tutto il resto: **non una scelta, tutto**,
nell'ordine in cui `parti.json` lo registra.

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

**Questi tomi non entrano in nessun registro dell'opera.** Ricompongono
documenti già contati, e contarli sarebbe contare due volte ogni documento che
portano: `registro_convergenze.py` e `registro_savona.py` escludono `_integrale/`
per nome, con la ragione scritta accanto. *Le celle aperte restano
centoquarantadue, le conferme del risultato ricorrente dodici, gli archi
Savona cinquantasei.*

## La composizione

Barlow Semi Condensed in sei tagli, carta bianca con gradiente crema al 5%,
inchiostro blu navy con gradiente nero al 5%, testo giustificato con
sillabazione italiana propria — **`hyphens:auto` è inerte in questo Chromium,
verificato con una prova, non supposto**. I PDF sono **taggati**, con
**segnalibri** e **numerazione di pagina**, e ciascuno porta nei metadati
l'impronta della propria sorgente (`/SourceSHA256`).
