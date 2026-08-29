# La sorgente unica dell'ordine dell'opera

*Nota tecnica ai generatori. Prodotta con sistemi di intelligenza artificiale sotto
direzione e responsabilità umana.*

## Il difetto che c'era

L'ordine dei documenti dell'opera integrale — quali entrano, con quale titolo, in
quale sequenza — **esisteva in tre copie**, una per generatore:

| file | che cosa produceva | forma della lista |
|---|---|---|
| `b_integrale.js` | il volume DOCX e, per il tramite di `p_integrale.js`, il PDF | `{title, file}` |
| `gen_note.py` | l'apparato bibliografico conclusivo | `(etichetta, breve, file)` |
| `gen_figs.py` | i grafici a piè di capitolo | `(etichetta, file)` |

Tre copie della stessa informazione sono tre occasioni di divergere, e **la
divergenza si era già verificata**: aggiungendo documenti al volume senza toccare
`gen_figs`, i grafici erano risultati centodue contro centoquattro parti, e il
generatore si era fermato con un errore di indice.

Quella volta l'errore fu rumoroso e si vide subito. **Non c'è alcuna garanzia che
lo sia la prossima**: una lista più corta di un elemento produce un volume che si
compone *senza errori* e porta i grafici sbagliati sotto i capitoli sbagliati, dal
punto della divergenza in poi. Un guasto silenzioso in un'opera di 2.465 pagine è
molto peggio di un guasto rumoroso.

## Che cosa si è fatto

L'ordine sta ora in un solo file, **`parti.json`**, e i tre generatori lo leggono:

```
parti.json  ──┬──►  b_integrale.js   (tutto, apparato bibliografico compreso)
              ├──►  gen_note.py      (tutto tranne l'apparato, che è ciò che produce)
              └──►  gen_figs.py      (tutto tranne l'apparato, che porta i propri due grafici)
```

Ogni voce ha quattro campi: `etichetta` (la sigla breve, «Libro dodicesimo · XXVII»),
`breve` (il titolo per l'apparato bibliografico), `titolo` (il titolo esteso che va
sull'occhiello di parte nel volume), `file` (il percorso). La voce finale porta
`solo_volume: true`, ed è l'apparato bibliografico: entra nel volume e non nelle
altre due liste, perché è il prodotto di una di esse.

**Chi aggiunge un documento all'opera tocca `parti.json` e nient'altro.**

## La verifica, prima di comporre

```bash
node -e "const p=require('./_verifiche/generatori/parti.json').parti;
         console.log(p.length, p.filter(x=>!x.solo_volume).length)"
```

I due numeri devono differire **esattamente di uno** — allo stato attuale, 107 e
106. E ogni percorso deve esistere: la stessa riga con un `fs.existsSync` lo
stabilisce, ed è il controllo che sarebbe servito la prima volta.

## La regola generale, che è il vero contenuto di questa nota

Il difetto non era di programmazione: era di **architettura dell'informazione**, ed
è lo stesso che quest'opera corregge nei propri testi. Un dato che vive in più
luoghi diverge, e diverge in silenzio; la manutenzione non consiste nel ricordarsi
di aggiornare tutte le copie, ma nell'**eliminare le copie**.

È la ragione per cui, nel dossier di invio, le cifre del libro sono state tolte da
sette documenti e lasciate in due; per cui il registro delle impronte non misura sé
stesso; e per cui i conteggi delle tre matrici sono stati rifatti a macchina invece
che a memoria. **Ogni copia di un dato è un errore in attesa della propria
occasione.**
