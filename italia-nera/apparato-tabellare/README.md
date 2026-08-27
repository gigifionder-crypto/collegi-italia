# L'apparato tabellare — nota di raccordo

*Tavole dell'opera «Italia Nera», acquisite il 27 agosto 2026. Prodotte con
sistemi di intelligenza artificiale sotto direzione e responsabilità umana.*

> **L'appartenenza a un'organizzazione non è prova di condotta.** Le tavole di
> nodi e di archi registrano legami documentati, non colpe: un arco fra due nodi
> dice che un rapporto è attestato, non che chi sta a un capo risponda di ciò che
> è avvenuto all'altro. Nessuna riga indica alcuno come responsabile di un reato
> al di fuori di un giudicato definitivo.

Quindici documenti: quattordici tavole convertite da fogli di calcolo e una
scheda di campagna. Sono l'apparato analitico di Italia Nera — i nodi, gli archi,
gli archivi e gli URL su cui il Registro V77 poggia.

---

## Le tavole

**Il fascio su Putin** — cinque tavole che entrano nel corpus dalla porta più
esposta e sono perciò le più caricate di cautele:

| Tavola | Che cosa porta |
|---|---|
| [`verifica-biografica-putin.md`](verifica-biografica-putin.md) | diciassette tappe cronologiche riscontrate online, con grado e fonte |
| [`putin-1970-1994-dieci-blocchi.md`](putin-1970-1994-dieci-blocchi.md) | trenta righe di fatti datati fra il 1970 e il 1994 |
| [`putin-venti-blocchi-e-archivi.md`](putin-venti-blocchi-e-archivi.md) | venti blocchi ancorati ciascuno a un archivio o a un dominio del censimento |
| [`triangolazione-integrale-putin.md`](triangolazione-integrale-putin.md) | ventotto nodi per dominio, tredici archi maestri, dieci reperti negativi |
| [`triangolazione-putin-e-galassia-nera.md`](triangolazione-putin-e-galassia-nera.md) | sei temi del corpus messi alla prova, e sette che non reggono |

Va detto con precisione che cosa queste cinque tavole **non** dicono, perché è la
parte che si perde per prima. La colonna dei reperti negativi è la più
istruttiva: Aginter Press, la galassia dell'apartheid e la loggia P2 di Gelli
sono iscritte come **«assenza di riscontro»** rispetto a Putin, cioè come tesi
cercate e non trovate. Le tavole registrano un legame reale — il milieu criminale
pietroburghese e la sua cerniera con Brighton Beach — e negano tre legami
attraenti. Chi le legge come una convergenza generale della «galassia nera» su
Putin legge il contrario di ciò che vi è scritto. Il ponte ideologico e di metodo
è a sua volta dichiarato come **eco di metodo, non continuità organizzativa**.

**Aginter, apartheid, P2, criminalità organizzata** — le tavole del corpus
storico:

| Tavola | Che cosa porta |
|---|---|
| [`nodi-aginter-apartheid-integrazione.md`](nodi-aginter-apartheid-integrazione.md) | cinquantasette nodi, ventiquattro archi, quattordici reperti negativi |
| [`nodi-aginter-apartheid-approfondimento.md`](nodi-aginter-apartheid-approfondimento.md) | ventidue nodi nuovi e otto reperti negativi, con la monografia di provenienza |
| [`p2-hub-archivi-e-sinapsi.md`](p2-hub-archivi-e-sinapsi.md) | dodici nodi-archivio con collocazione fisica e stato di accessibilità |
| [`nodi-d1-criminalita-organizzata.md`](nodi-d1-criminalita-organizzata.md) | i nodi del dominio D1, italiani, statunitensi e trasversali |
| [`nodi-in-integrazione-e-archi.md`](nodi-in-integrazione-e-archi.md) | trentanove nodi nuovi dai censimenti, con stato probatorio, e diciannove archi |

Due righe di queste tavole vanno lette con l'avvertenza in testa a questa pagina
davanti agli occhi, perché nominano persone viventi: la scheda su Gianfranco Fini
registra una **condanna di primo grado** del 2024, che non è un giudicato e non
rende alcuno responsabile di alcunché; quella su Giuseppe Scopelliti registra una
condanna **definitiva** del 2018, che invece lo è. La differenza è l'intera
distanza fra le due righe, e la tavola la scrive.

Due tesi celebri sono qui iscritte fra i falsi: il manuale **FM 30-31B** è
riconosciuto come contraffazione, e l'attribuzione di Piazza Fontana a una regia
americana è chiusa da un'**assoluzione definitiva**.

**Il censimento delle sedi e delle fonti**:

| Tavola | Che cosa porta |
|---|---|
| [`archivi-operativo.md`](archivi-operativo.md) | cinquantanove sedi d'archivio con base normativa, consistenza, procedura d'accesso e limiti |
| [`lacune-dai-censimenti.md`](lacune-dai-censimenti.md) | diciassette sedi rilevate dai censimenti e mancanti dal repertorio |
| [`url-censiti.md`](url-censiti.md) | 1.722 URL per categoria, con dominio, provenienza e stato del controllo |
| [`certificato-di-acquisizione.md`](certificato-di-acquisizione.md) | quindici documenti con parole estratte, impronta del testo e verdetto |
| [`campagna-fase-due-accesso-remoto.md`](campagna-fase-due-accesso-remoto.md) | le sette sedi che consentono una qualche consultazione a distanza |

Sulla tavola degli URL una precisazione che la tavola stessa dà, e che è
importante non perdere: la colonna dello stato riporta per ogni riga **«non
controllato — egress policy»**. Nessuno di quei 1.722 indirizzi è stato aperto:
sono censiti, non verificati. È un inventario di ciò che andrà controllato, non
un attestato che risponda.

---

## Come sono state convertite

Da `.xlsx` a markdown, un foglio per sezione e una riga per riga, senza
riordinare, riaggregare o normalizzare i contenuti. I fogli a colonna unica —
gli statuti, le legende, le cautele — sono resi in prosa anziché incolonnati,
perché una tabella a una colonna è illeggibile e la conversione non deve
peggiorare l'originale. Il generatore è `_verifiche/generatori/conv_xlsx.py`.
