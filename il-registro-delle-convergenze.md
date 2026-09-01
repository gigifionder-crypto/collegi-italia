# Il registro delle convergenze — quante volte, e su che cosa

> **Dichiarazione.** Questo registro è **generato automaticamente** da
> `_verifiche/generatori/registro_convergenze.py`. **Non è un accertamento:
> è una misura riproducibile.** Chiunque abbia il repository può rieseguirlo
> e ottenere gli stessi numeri.

## Perché esiste

Il corpus ripete in più capitoli che il proprio risultato ricorrente —
**«orientamento condiviso, ponti reali, nessun comando comune provato»** —
è stato ottenuto un certo numero di volte consecutive. Quel numero era
**scritto a mano**, in capitoli diversi, e ha derivato.

Il rilievo non è di chi scrive: viene dalla campagna *Roy Cohn*, sezione
C9, che ha chiesto se il numero fosse stabile fra i capitoli e ha risposto
**no**, elencando le divergenze. **È un errore di contabilità, non di
ricerca** — e la cura di un errore di contabilità non è riscrivere i
numeri: è **smettere di scriverli a mano**.

## Il criterio, dichiarato e applicato meccanicamente

Un documento conta come conferma **se il suo testo contiene almeno una
delle formule del risultato**:

- `nessun comando comune`
- `nessuna regia accertata`
- `orientamento condiviso, ponti reali`
- `convergenza (?:di interesse )?(?:è |e )?accertata, il concerto no`
- `convergenza senza concerto`

L'appartenenza è dunque una proprietà **del testo**, non un giudizio di chi
compila: chiunque riesegua lo script ottiene la stessa lista. L'**ordine** è
la data del commit che ha introdotto il documento nel repository,
verificabile in `git log --diff-filter=A`. Il **numero** è la posizione in
quell'ordine.

Sono esclusi per costruzione i tomi ricomposti e l'edizione breve, che
ripetono testo già contato; il romanzo, che non è ricerca; gli indici e le
guide, che descrivono invece di accertare.

## Che cosa questo registro **non** dice

**Non dice che le conferme siano indipendenti fra loro.** Alcune insistono
su materiali contigui, e chi le legge deve pesarle, non sommarle. **Non
dice che siano di pari valore probatorio.** Conta le volte in cui la stessa
forma è stata trovata su materiali dichiarati — e questo è tutto ciò che un
conteggio può fare. Un numero alto non rende la forma più vera: la rende
più **ricorrente**, che è un'altra cosa e va detta con un'altra parola.

## Il conto

**12 documenti** dell'opera portano il risultato.

| n. | data d'ingresso | documento | occorrenze |
|---:|---|---|---:|
| 1 |  | [`triangolazione-mengele-barbie-delle-chiaie-badalamenti.md`](triangolazione-mengele-barbie-delle-chiaie-badalamenti.md) | 2 |
| 2 | 2026-08-24 | [`triangolazione-feltrinelli-hyperion.md`](triangolazione-feltrinelli-hyperion.md) | 1 |
| 3 | 2026-08-25 | [`triangolazione-condannati-corpus.md`](triangolazione-condannati-corpus.md) | 1 |
| 4 | 2026-08-30 | [`la-congettura-dell-isomorfismo.md`](la-congettura-dell-isomorfismo.md) | 1 |
| 5 | 2026-08-31 | [`il-parallelo-delle-due-piste-mille-studi-sincronici.md`](il-parallelo-delle-due-piste-mille-studi-sincronici.md) | 5 |
| 6 | 2026-08-31 | [`il-ponte-mosca-new-york.md`](il-ponte-mosca-new-york.md) | 1 |
| 7 | 2026-08-31 | [`le-fonti-caricate-ricognizione.md`](le-fonti-caricate-ricognizione.md) | 5 |
| 8 | 2026-08-31 | [`le-quattro-europe.md`](le-quattro-europe.md) | 2 |
| 9 | 2026-08-31 | [`chi-favorisce-quale-europa.md`](chi-favorisce-quale-europa.md) | 2 |
| 10 | 2026-08-31 | [`il-registro-dei-mandanti.md`](il-registro-dei-mandanti.md) | 1 |
| 11 | 2026-08-31 | [`il-vivaio-e-il-tronco.md`](il-vivaio-e-il-tronco.md) | 2 |
| 12 | 2026-08-31 | [`il-censimento-delle-quattro-europe.md`](il-censimento-delle-quattro-europe.md) | 1 |

## I numeri scritti a mano che questo registro sostituisce

Restano nei loro capitoli, dove furono scritti, perché **una correzione sta accanto all'errore e non al suo posto**. Ciascuno era esatto il giorno in cui fu scritto, e ha smesso di esserlo il giorno dopo.

| documento | formula |
|---|---|
| [`INDICE-DOCUMENTI-BRANCH.md`](INDICE-DOCUMENTI-BRANCH.md) | «Quinta conferma consecutiva» |
| [`_verifiche/edizione-breve/n06-il-mediterraneo-conteso.md`](_verifiche/edizione-breve/n06-il-mediterraneo-conteso.md) | «sette prove consecutive» |
| [`_verifiche/edizione-breve/n11-il-ponte-con-un-nome.md`](_verifiche/edizione-breve/n11-il-ponte-con-un-nome.md) | «sette prove consecutive» |
| [`chi-favorisce-quale-europa.md`](chi-favorisce-quale-europa.md) | «Otto prove consecutive» |
| [`il-vivaio-e-il-tronco.md`](il-vivaio-e-il-tronco.md) | «quinta conferma consecutiva» |
| [`le-fonti-caricate-ricognizione.md`](le-fonti-caricate-ricognizione.md) | «sette
prove consecutive» |
| [`le-quattro-europe.md`](le-quattro-europe.md) | «sette prove consecutive» |
| [`roy-cohn-il-ponte-con-un-nome.md`](roy-cohn-il-ponte-con-un-nome.md) | «sette prove
consecutive» |
| [`roy-cohn-mille-blocchi.md`](roy-cohn-mille-blocchi.md) | «otto prove consecutive» |
| [`roy-cohn-mille-blocchi.md`](roy-cohn-mille-blocchi.md) | «quinta conferma consecutiva» |
| [`roy-cohn-mille-blocchi.md`](roy-cohn-mille-blocchi.md) | «sette prove consecutive» |

**Il numero corrente è 12, e non va più trascritto: va letto qui.** Chi aggiunge una conferma non deve aggiornare nessun capitolo — deve solo scrivere la formula, e il registro la conta.
