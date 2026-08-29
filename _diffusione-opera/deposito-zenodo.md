# Il deposito Zenodo — foglio operativo

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Questo foglio serve a fare una cosa sola e a farla oggi: **ottenere il DOI**.
Finché non c'è, nessuna delle dodici lettere può partire, perché tutte lo citano.
È l'unico anello che blocca dodici destinatari insieme, e si scioglie in un'ora.

---

## Perché prima di tutto il resto

Il DOI fa tre cose che nessun altro canale fa. **Data** il deposito in modo
opponibile a terzi. **Rende citabile** l'opera prima che un editore la
pubblichi, il che cambia il tono di ogni proposta: non si offre un manoscritto,
si segnala un lavoro già depositato. E **stacca l'opera dal repository**: un
file su Zenodo sopravvive alla cancellazione di un ramo Git, e questa opera
esiste solo in un ramo Git.

Va fatto prima delle lettere perché il numero entra nel corpo delle lettere.
Farlo dopo significa riscriverle tutte.

---

## Che cosa caricare

Tre file, non uno. Il volume intero pesa circa 38 MiB e Zenodo lo accetterebbe,
ma un revisore non apre un PDF di duemilaquattrocento pagine e passa: apre la
parte che lo riguarda.

| File | Peso, all'ultima composizione |
|---|---:|
| `OPERA_INTEGRALE_1-di-3_LIBRI_I-XII.pdf` | ~14 MiB |
| `OPERA_INTEGRALE_2-di-3_LIBRI_XIII-XIV.pdf` | ~10 MiB |
| `OPERA_INTEGRALE_3-di-3_LIBRI_XV-XVI_E_APPENDICI.pdf` | ~5 MiB |

*Il nome della terza parte è cambiato con la settima edizione — porta ora due
Libri, non uno — e chi avesse annotato il nome precedente cercherebbe un file che
non esiste più. È il genere di dettaglio che blocca un deposito per mezz'ora.*

*Le impronte SHA-256 delle tre parti non sono ricopiate qui, ed è una scelta, non
una dimenticanza: **questo foglio è rilegato dentro il volume** come Appendice
IV.xvi, e un'impronta scritta dentro il file che essa misura è falsa nell'istante
in cui viene scritta. Vale la stessa regola per cui il registro delle impronte
non certifica sé stesso. Le impronte correnti si leggono in
[`../IMPRONTE-SHA256.md`](../IMPRONTE-SHA256.md), sezione «Il volume diviso in
tre parti», e si ricopiano di lì al momento del deposito.*

E due file piccoli che valgono più del loro peso:

| File | Perché |
|---|---|
| `IMPRONTE-OPERA-MORO.txt` | il manifesto: 199 righe, una per file, verificabile con un comando |
| `IMPRONTE-SHA256.md` | il registro leggibile, che spiega che cosa l'impronta certifica e che cosa no |

**Non caricare** il volume intero da 37,9 MiB: duplica le tre parti e raddoppia
il peso del record senza aggiungere nulla. **Non caricare** `italia-nera/`: è
un'opera distinta, e se un giorno va depositata avrà un DOI proprio.

---

## I metadati, pronti da incollare

**Upload type** — Publication → Book

**Title**

```
Aldo Moro. Ottanta anni di Pace: una guerra senza fine — opera integrale
```

**Authors** — `De Michele, Luigi`. Se hai un ORCID, mettilo: è la differenza fra
un deposito anonimo e un deposito attribuibile. Se non ce l'hai, si apre in
cinque minuti su orcid.org ed è gratuito.

**Description** (incolla così com'è)

> Corpus di ricerca storica sul caso Moro e sul suo contesto internazionale,
> prodotto fra il 2025 e il 2026 con sistemi di intelligenza artificiale sotto
> direzione umana e sotto una disciplina metodologica scritta prima del lavoro e
> resa vincolante. La dichiarazione di generazione assistita apre ogni documento
> dell'opera, non ne chiude nessuno.
>
> L'opera non ricostruisce i fatti del 1978 e non propone una tesi sul sequestro.
> Non indica responsabili: nessuna persona vi è indicata come responsabile di un
> reato al di fuori di un giudicato definitivo, e la regola che governa l'intero
> corpus è che l'appartenenza a un'organizzazione non è prova di condotta. Ciò
> che l'opera produce sono bersagli di ricerca: domande formulate in modo che un
> terzo possa andare in archivio a rispondervi, ciascuna col grado di ciò che si
> sa già e con la sede in cui si cercherebbe.
>
> Ogni proposizione porta un grado dichiarato — A giudicato, B accertamento, C
> congettura, F fatto pubblico — e le ricerche condotte senza esito sono
> registrate come Stati Zero, validi soltanto se la sede consultata è nominata.
> Le correzioni sono annotate accanto all'errore e non applicate in silenzio; le
> divergenze fra fonti sono riportate e non risolte d'autorità.
>
> Settima edizione integrale, 29 agosto 2026: oltre duemilaquattrocento pagine in
> 107 documenti, sedici Libri e quattro Appendici, 245 grafici su 107 capitoli,
> 1.258 citazioni a
> 692 indirizzi distinti su 358 domini. Il Libro sedicesimo porta le tavole delle
> ipotesi concorrenti sulle tre questioni maggiori del caso — la custodia,
> l'agguato, le omissioni — e il quesito peritale sulla sola cella che quelle
> tavole dichiarano riempibile. Depositata in tre parti
> tagliate su confini di Libro; le parti non si sovrappongono e insieme fanno il
> volume. Ogni file porta la propria impronta SHA-256 nel manifesto allegato:
> l'impronta certifica l'integrità del contenitore, non la verità del contenuto,
> e la distinzione è dichiarata nel registro.

**Version** — `7.0` **· Publication date** — `2026-08-29` **· Language** —
`Italian` **· License** — Creative Commons Attribution 4.0 (CC BY 4.0)

*Sulla licenza.* CC BY è la scelta consigliata: chiunque può citare e
ridistribuire purché attribuisca, il che è esattamente ciò che serve a un'opera
che vuole essere verificata. Se preferisci vietare gli usi commerciali (CC
BY-NC) sappi che molte riviste e archivi non ridistribuiscono materiale NC, e
perderesti proprio i canali che ti interessano.

**Keywords**

```
Aldo Moro; Brigate Rosse; caso Moro; storia contemporanea italiana; strategia della tensione; Loggia P2; Gladio; Commissione Moro; fonti parlamentari; metodo storiografico; gradi probatori; ricerca assistita da intelligenza artificiale
```

**Additional notes** — l'impronta va copiata dal registro al momento del
deposito, per la ragione detta sopra:

> Opera prodotta con sistemi di intelligenza artificiale sotto direzione e
> responsabilità umana. Impronta SHA-256 del manifesto dell'opera:
> `«copiare da IMPRONTE-SHA256.md, sezione "L'impronta dell'opera"»`.
> Il manifesto elenca i file versionati che compongono l'opera e si verifica con
> `sha256sum --check IMPRONTE-OPERA-MORO.txt`.

*Il conteggio esatto delle pagine è volutamente lasciato in tondo e va sostituito
con la cifra che si legge sulla copertina del volume al momento del deposito. La ragione è la stessa dell'impronta: **questo foglio è
rilegato dentro il volume che conta**, e ogni volta che si scrive qui il numero
esatto il foglio si allunga e il numero cambia. Un documento non può misurare
sé stesso dall'interno; può però dire dove il numero si legge, ed è ciò che fa.
Gli altri numeri — documenti, grafici, citazioni, domini — non hanno questo
problema e sono esatti: si rileggono comunque sul registro prima di incollarli.*

> **Annotazione del 29 agosto 2026, apposta accanto e non in sostituzione.**
> Aggiornando questo foglio alla settima edizione vi era stato scritto il numero
> esatto delle pagine, e in tre punti: nel testo, in una colonna della tavola dei
> file, nella description. **Era una violazione della regola che questo foglio
> stesso enuncia due paragrafi più sopra** — un documento rilegato dentro il volume
> che conta non può contarne le pagine, perché scrivendo il numero lo cambia. Le
> tre occorrenze sono state riportate in tondo. La regola era scritta; a violarla è
> stato chi l'ha riletta subito dopo averla scritta, ed è il motivo per cui vale la
> pena rileggere i propri documenti invece di ricordarseli.
>
> Anche i pesi dei file sono ora arrotondati, e per la stessa ragione: cambiano a
> ogni ricomposizione. Ciò che non cambia — documenti, Libri, grafici, citazioni,
> indirizzi, domini — resta esatto.

---

## L'ordine delle operazioni

1. Apri l'account Zenodo (o accedi). Se non hai un ORCID, aprilo prima e
   collegalo.
2. **New upload** → trascina i cinque file → compila i metadati qui sopra.
   *Il nome della terza parte è cambiato con la settima edizione* — porta ora due
   Libri, non uno — *e chi avesse annotato il nome precedente cercherebbe un file
   che non esiste più.*
3. **Save** senza pubblicare. Rileggi la description sullo schermo: è il testo
   che leggeranno per primo, ed è l'unico che non puoi correggere dopo la
   pubblicazione senza generare una nuova versione.
4. **Publish.** Il DOI compare subito; l'indicizzazione richiede fino a un'ora.
5. Copia il DOI e **torna qui**: va inserito in undici lettere e nella scheda
   dell'opera. È una sostituzione meccanica, la faccio io in un passaggio.

---

## Dopo il DOI

Il DOI entra in: la scheda dell'opera, la PEC unica formale, la lettera alla
Fondazione Aldo Moro, la PEC all'Archivio Flamigni, la relazione al Centro
Flamigni, e le sei proposte editoriali. Undici documenti, una stringa.

Poi, e solo poi, si spedisce. La checklist di invio dice in che ordine.

---

*Una avvertenza che vale la pena scrivere prima che serva: **un deposito Zenodo
non si cancella**. Si può ritirare dalla vista pubblica, ma il DOI resta e la
pagina resta, con la dicitura di ritiro. Ciò che si carica oggi è definitivo. È
il motivo per cui questo foglio insiste sul punto 3: rileggere prima di
premere.*
