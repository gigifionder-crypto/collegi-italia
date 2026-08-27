# Le ricerche approfondite — nota di raccordo

*Documenti dell'opera «Italia Nera», acquisiti il 27 agosto 2026. Prodotti con
sistemi di intelligenza artificiale sotto direzione e responsabilità umana.*

> **L'appartenenza a un'organizzazione non è prova di condotta.** Nessuna riga di
> questi rapporti indica alcuno come responsabile di un reato al di fuori di un
> giudicato definitivo. Sono ricostruzioni di reti e di rapporti: un arco fra due
> nomi dice che un legame è attestato, non che chi sta a un capo risponda di ciò
> che è avvenuto all'altro.

Nove rapporti monografici. Sono **ciò che le schede di presa in consegna
descrivono**: dove l'inventario dice «scheda n. 6 — L'architetto del caos», qui
c'è l'architetto del caos per esteso. Le due cartelle vanno lette insieme, e
nessuna delle due sostituisce l'altra.

| Rapporto | Parole | Materia |
|---|---:|---|
| [`architetto-del-caos-dugin-e-l-eurasiatismo.md`](architetto-del-caos-dugin-e-l-eurasiatismo.md) | 17.428 | dieci capitoli e cento sottocapitoli su Dugin e l'eurasiatismo, dal substrato evoliano ai partiti europei |
| [`nazisti-in-urss-l-esodo-tecnologico.md`](nazisti-in-urss-l-esodo-tecnologico.md) | 9.368 | gli specialisti del Terzo Reich in URSS, 1945-1959: Osoaviakhim e l'Alsos sovietico |
| [`russia-unita-la-diplomazia-partitica.md`](russia-unita-la-diplomazia-partitica.md) | 6.477 | la proiezione geopolitica russa attraverso gli accordi fra partiti |
| [`ayman-al-zawahiri-radici-e-reti.md`](ayman-al-zawahiri-radici-e-reti.md) | 6.335 | la traiettoria anteriore all'undici settembre |
| [`network-finanziario-sud-africa.md`](network-finanziario-sud-africa.md) | 5.850 | istituti, gruppi e cariche del sistema finanziario sudafricano |
| [`veritas-ubique-la-rete-di-aginter-press.md`](veritas-ubique-la-rete-di-aginter-press.md) | 5.837 | la centrale di Lisbona, 1966-1974: struttura, finanziamenti, ramificazioni |
| [`ordre-et-tradition-e-l-ecosistema-del-terrore.md`](ordre-et-tradition-e-l-ecosistema-del-terrore.md) | 5.556 | architettura e reticoli della guerra non convenzionale, 1964-1974 |
| [`le-cercle-architettura-occulta.md`](le-cercle-architettura-occulta.md) | 5.436 | il network conservatore transnazionale, 1951-1991 |
| [`internazionale-parallela-gli-accordi-bilaterali.md`](internazionale-parallela-gli-accordi-bilaterali.md) | 2.346 | la rete globale degli accordi bilaterali interpartitici |

---

## Due rapporti che vanno letti con una cautela in più

Non perché siano fatti peggio degli altri, ma perché nominano **persone viventi**
in contesti che una lettura frettolosa trasforma in accuse.

**Il network finanziario del Sud Africa** è un elenco di cariche: chi è
amministratore delegato di quale gruppo, chi direttore finanziario, chi siede in
quale consiglio. Sono dati societari pubblici. Il rapporto **non contesta nulla a
nessuno**, e il fatto che stia in una cartella intitolata «Italia Nera» non
aggiunge una sola parola a ciò che dice. Chi lo legge come una lista di sospetti
gli attribuisce un contenuto che non ha. È anche il rapporto strutturalmente più
povero del lotto — arriva come sequenza di nomi e ruoli, senza narrazione — e
questo lo rende il più facile da fraintendere.

**Russia Unita** e **L'Internazionale parallela** trattano di figure politiche
viventi, alcune delle quali soggette a misure restrittive internazionali. Il
rapporto ricostruisce accordi fra partiti: atti pubblici, firmati e pubblicati.
Un accordo interpartitico è un fatto, e resta un fatto qualunque giudizio si dia
di chi lo ha firmato.

## Che cosa si è misurato prima di archiviare

Nessuno dei nove è contenuto nel corpus già archiviato: il contenimento agli
8-grammi resta sotto il **2 per cento** per sette di essi, e per i due sulla
diplomazia russa sotto il **12**, che è la quota del lessico condiviso con il
Registro V77 e non un ricalco.

Sono stati scartati tre file: `architetto_del_caos_4.pdf` e
`architetto_del_caos_5.docx` sono lo **stesso documento** della redazione qui
archiviata — il PDF al **100 per cento** agli 8-grammi, il DOCX al **98**, dove il
2 per cento di scarto è differenza di conversione e non di testo — e
`Nazisti_in_URSS_1.docx` sta al **96** dentro il PDF corrispondente. Fra le due
copie di ciascun documento si è tenuta quella in PDF, perché conserva la
struttura in capitoli che il DOCX perde.

## Come sono stati convertiti, e che cosa la conversione non ha recuperato

Da PDF a markdown con `_verifiche/generatori/conv_pdf.py`. L'estrazione ordinaria
restituisce **una parola per riga** — il PDF porta la spaziatura come geometria e
non come testo — e il paragrafo andrebbe perduto: la conversione lavora quindi
sulla resa a impaginato, toglie il filo di testa che si ripete a ogni pagina,
ricuce i paragrafi spezzati dal salto e rimette una voce per riga negli elenchi
bibliografici.

**Ciò che non ha recuperato va detto.** I titoli di capitolo sono riconosciuti
dove il PDF li stacca, e restano dentro il testo corrente dove non li stacca: nel
rapporto su Dugin l'indice si ricostruisce quasi per intero, in quello sui
nazisti in URSS le dieci aperture di capitolo sono nel testo e non nei titoli. È
una perdita di navigazione, non di contenuto: **nessuna parola è stata aggiunta,
tolta o riordinata**, e chi cerca «Capitolo 4» lo trova cercandolo.
