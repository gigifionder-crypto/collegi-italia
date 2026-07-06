# Registro di verifica numerica — Tomo I (Fase 3.2)

Registro completo delle tabelle del Tomo I canonico (`tomo-1-puglia/opera-integrale-puglia.docx`), generato automaticamente il 2026-07-06 dopo la rimozione della duplicazione di Parte I/II (Fase 3.1). Una riga per tabella, nell'ordine in cui compare nel documento. Stati ammessi: `da verificare` / `verificata-ok` / `verificata-discrepanza` / `n/a-infografica`.

**Colonna Tipo:** `dati` (tabella con dati verificabili, ≥2 righe e ≥2 colonne), `infografica` (segnaposto di progettazione grafica per Canva — non contiene dati da verificare aritmeticamente, ma i valori numerici citati come esempio vanno controllati per coerenza con il testo circostante), `altro` (tabella piccola/monocolonna, verificare caso per caso).

Verifica = controllo di coerenza aritmetica interna (somme, percentuali, totali) e di coerenza con le affermazioni discorsive circostanti che citano la tabella. Le discrepanze vengono annotate qui, non corrette silenziosamente nel corpo (si veda §3.2 del piano di esecuzione).

**Totale tabelle: 1055** — 959 dati, 55 infografica, 41 altro.

**Avanzamento verifica (2026-07-06):** 26 tabelle verificate puntualmente
(17 `verificata-ok`, 9 `verificata-discrepanza`), su tutte le tabelle
"dati"/"altro" di Parte VII (Costi diretti) e Parte VIII (Risparmi
diretti), più le prime tabelle della Revisione metodologica OCSE 2026.

**Pattern emerso in Parte VII:** lo scenario Centrale/Intermedio (775
psicologi) — quello raccomandato e usato in tutti i prodotti della
piramide — risulta internamente coerente in ogni tabella verificata
finora; le discrepanze aritmetiche riscontrate (tabelle #77, #82, #85)
riguardano sempre e solo gli scenari Conservativo ed Espansivo (620 e
900 psicologi), dove i componenti elencati non sommano esattamente al
totale dichiarato nella stessa tabella. Le tabelle #73-76 presentano
inoltre un'anomalia strutturale distinta: sono a una sola colonna (solo
etichette di riga, nessun valore).

**SCOPERTA MAGGIORE emersa in Parte VIII (tabella #108):** il framework
degli scenari a tre livelli **non è coerente tra le parti del Tomo I**.
Parte VIII etichetta gli scenari come "Conservativo (~450) / Intermedio
(~700) / Espansivo (~900)" psicologi (tabelle #94, 97, 100, 103, 107 —
tutte internamente coerenti su questa base), mentre Parte X usa
620/775/900 e Parte VII non usa un'etichetta di headcount esplicita per
riga. La tabella #108 (Parte VIII) cita "Costi diretti del servizio" =
~25/~38/~50 mln€, incompatibile con la tabella master di Parte VII (#87,
verificata-ok: 54,4/45,2/36,5 mln€ lordo per gli stessi scenari nominali)
— scarto ~15-18%. Lo scenario centrale/intermedio raccomandato risulta
quindi avere **almeno tre cifre di costo diverse** a seconda della parte
consultata: ~38 (Parte VIII), ~40,5 (Parte IV/OCSE 2026), ~43,9-45,2
(Parte VII). Non corretto silenziosamente. Registrato con visibilità
massima in `_meta/status-tracker.md` e `_meta/parking-lot.md`
(2026-07-06); riconciliazione rimandata a valle della verifica
sistematica, per decisione esplicita dell'autore (si continua la
verifica tabella-per-tabella nell'ordine stabilito: Parte IX, poi X,
XI...).

| # | Parte/Appendice | Didascalia (se rilevata) | Tipo | Stato | Note |
|---|------------------|---------------------------|------|-------|------|
| 1 | (front matter) | — | dati | da verificare | Etichetta parte errata nell'estrazione automatica (falso positivo su banner decorativo); appartiene alla sezione "Revisione metodologica di governo — OCSE 2026". |
| 2 | Revisione metodologica di governo (OCSE 2026) | Tab. IV.1 — Confronto tra framework di riferimento economico: Chisholm (2016) vs OECD (202 | dati | da verificare | |
| 3 | Revisione metodologica di governo (OCSE 2026) | Tab. IV.2 — Aggiornamento sistematico del risparmio sanitario diretto (milioni di euro): C | dati | verificata-ok | Somme verificate per tutte e 6 le colonne (Base/Interm./Ottim. × Chisholm/OECD): ciascuna colonna (farmaceutico + PS/ricoveri + mobilità + specialistico) torna esattamente al "TOTALE DIRETTO" dichiarato. Quota IA coerente con il testo (10% nello scenario intermedio, come esplicitamente scoping dal testo; non è una percentuale costante tra scenari — 5% Base, 15% Ottimale — ma il testo non afferma il contrario). |
| 4 | Revisione metodologica di governo (OCSE 2026) | Tab. IV.3 — Indicatori di ROI e costo-efficacia: Chisholm 2016 vs OECD 2026 — scenario int | dati | verificata-discrepanza | **Non verificabile dai soli dati in tabella.** Il "costo totale annuo servizio" è riportato come 40,5 mln€ fisso per tutti e 3 gli scenari (Base/Intermedio/Ottimale), mentre altrove nel Tomo (Parte X, Quadro Conclusivo) il costo cresce con la copertura (43-47 mln€ su 620/775/900) — incoerenza già nota, si veda `_meta/status-tracker.md`. Inoltre il "ROI lordo" non è ricostruibile dalle sole righe della tabella: usando risparmi diretti + benefici indiretti OECD e dividendo per il costo (40,5) si ottiene, per lo scenario Base, (23,5+11,0)/40,5=0,85, non l'1:4,2 dichiarato — il calcolo del ROI deve includere altre grandezze (es. i 16 domini di Parte IX) non mostrate in questa tabella. Non correggere silenziosamente: segnalato per chiarimento con l'autore. |
| 5 | Revisione metodologica di governo (OCSE 2026) | Tab. IV.4 — Contributo dell’IA per canale (scenario intermedio) — valori aggiornati OECD 2 | dati | da verificare | |
| 6 | Parte I | Tabella 1.1 — Scomposizione del quesito di valutazione | dati | da verificare | |
| 7 | Parte I | Tabella 1.2 — I cinque livelli della cascata gerarchica piramidale | dati | da verificare | |
| 8 | Parte I | Tabella 1.3 — Le quattro cornici apicali del telaio | dati | da verificare | |
| 9 | Parte I | Tabella 1.4 — Le metodologie innestate per la rinegoziazione dei costi e dei benefici | dati | da verificare | |
| 10 | Parte I | Tabella 1.5 — Tassonomia dei costi e dei benefici e loro collocazione nel saldo | dati | da verificare | |
| 11 | Parte I | Tabella 1.6 — La batteria integrale di indicatori per dimensione | dati | da verificare | |
| 12 | Parte I | Tabella 1.7 — I vincoli metodologici invarianti | dati | da verificare | |
| 13 | Parte I | — | altro | da verificare | |
| 14 | Parte II | — | altro | da verificare | |
| 15 | Parte II | Tabella 2.1 — Il carico epidemiologico del disagio psichico in Puglia | dati | da verificare | |
| 16 | Parte II | Tabella 2.2 — Domanda, offerta e divario di copertura | dati | da verificare | |
| 17 | Parte II | — | altro | da verificare | |
| 18 | Parte II | Tabella 2.3 — Profilo demografico e socioeconomico della Puglia | dati | da verificare | |
| 19 | Parte II | — | altro | da verificare | |
| 20 | Parte II | Tabella 2.4 — L’offerta sanitaria regionale e la condizione della medicina generale | dati | da verificare | |
| 21 | Parte II | Tabella 2.5 — Il quadro finanziario e i flussi del Servizio sanitario regionale | dati | da verificare | |
| 22 | Parte II | Tabella 2.5 — Il quadro finanziario e i flussi del Servizio sanitario regionale | altro | da verificare | |
| 23 | Parte II | Tabella 2.6 — La mappa del carico multidominio della cattiva salute mentale | dati | da verificare | |
| 24 | Parte II | Tabella 2.6 — La mappa del carico multidominio della cattiva salute mentale | altro | da verificare | |
| 25 | Parte II | Tabella 2.7 — Il quadro normativo e programmatico su tre livelli | dati | da verificare | |
| 26 | Parte II | Tabella 2.7 — Il quadro normativo e programmatico su tre livelli | altro | da verificare | |
| 27 | Parte II | Tabella 2.8 — Quadro conclusivo: grandezze cardine della Parte II | dati | da verificare | |
| 28 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 29 | Parte III — L’architettura delle figure a cascata gerar | — | infografica | n/a-infografica | |
| 30 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 31 | Parte III — L’architettura delle figure a cascata gerar | — | infografica | n/a-infografica | |
| 32 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 33 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 34 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 35 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 36 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 37 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 38 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 39 | Parte III — L’architettura delle figure a cascata gerar | — | infografica | n/a-infografica | |
| 40 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 41 | Parte III — L’architettura delle figure a cascata gerar | — | altro | da verificare | |
| 42 | Parte III — L’architettura delle figure a cascata gerar | — | infografica | n/a-infografica | |
| 43 | Parte III — L’architettura delle figure a cascata gerar | — | dati | da verificare | |
| 44 | Parte III — L’architettura delle figure a cascata gerar | — | infografica | n/a-infografica | |
| 45 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.1 — I quattro elementi costitutivi del modello operativo | dati | da verificare | |
| 46 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.1 — I quattro elementi costitutivi del modello operativo | altro | da verificare | |
| 47 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.2 — Le regole di invio e di ritorno tra i livelli | dati | da verificare | |
| 48 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.3 — Le leve abilitanti organizzative e di processo | dati | da verificare | |
| 49 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.4 — La leva digitale e l’Intelligenza Artificiale lungo il ciclo assistenziale,  | dati | da verificare | |
| 50 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.4 — La leva digitale e l’Intelligenza Artificiale lungo il ciclo assistenziale,  | altro | da verificare | |
| 51 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.5 — Il quadro regolatorio e le condizioni di ammissibilità dei dispositivi terap | dati | da verificare | |
| 52 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.6 — I quattro pilastri della governance prudenziale e i presidi corrispondenti | dati | da verificare | |
| 53 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.7 — I tre scenari di copertura e i parametri di dimensionamento | dati | da verificare | |
| 54 | Parte IV — Il modello organizzativo integrato e le leve | Tabella 4.7 — I tre scenari di copertura e i parametri di dimensionamento | altro | da verificare | |
| 55 | Parte V | Tabella 5.1.A — Le quattro aree del fabbisogno formativo e il livello atteso per figura | dati | da verificare | |
| 56 | Parte V | Tabella 5.1.A — Le quattro aree del fabbisogno formativo e il livello atteso per figura | altro | da verificare | |
| 57 | Parte V | Tabella 5.2.A — I percorsi della formazione universitaria: durata, esiti, onere prevalente | dati | da verificare | |
| 58 | Parte V | Tabella 5.3.A — Le tre forme della formazione post-universitaria: durata, esiti, onere pre | dati | da verificare | |
| 59 | Parte V | Tabella 5.4.A — Le forme della formazione lavorativa: livello prevalente, costo, rendiment | dati | da verificare | |
| 60 | Parte V | Tabella 5.4.A — Le forme della formazione lavorativa: livello prevalente, costo, rendiment | altro | da verificare | |
| 61 | Parte V | Tabella 5.5.A — Le forme dell’affiancamento esperto: funzione, costo, effetto sulla curva | dati | da verificare | |
| 62 | Parte V | Tabella 5.6.A — Le quattro modalità nel percorso integrato: funzione, livello, ruolo | dati | da verificare | |
| 63 | Parte V | Tabella 5.6.A — Le quattro modalità nel percorso integrato: funzione, livello, ruolo | altro | da verificare | |
| 64 | Parte V | Tabella 5.7.A — La struttura del costo della formazione per modalità (scenario base, ordin | dati | da verificare | |
| 65 | Parte V | Tabella 5.7.B — Il confronto del rendimento: modalità singole e combinazione (Kirkpatrick– | dati | da verificare | |
| 66 | Parte V | Tabella 5.8.A — Le fasi della curva di adozione e il ruolo delle modalità formative | dati | da verificare | |
| 67 | Parte V | Tabella 5.8.A — Le fasi della curva di adozione e il ruolo delle modalità formative | altro | da verificare | |
| 68 | Parte V | — | dati | da verificare | |
| 69 | Parte Sesta | — | dati | da verificare | |
| 70 | Parte Sesta | Tabella 6.1 — Sintesi e graduazione GRADE dell’evidenza clinica sull’integrazione della ps | infografica | n/a-infografica | |
| 71 | Parte VII — Costi diretti (rinegoziazione integrale) | — | altro | da verificare | |
| 72 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-ok | Tabella FTE→costo apice (7.1.1). Fabbisogno FTE clinici × costo unitario lordo/FTE riproduce esattamente "Costo personale clinico apicale" nei 3 scenari (740×50.000=37,0; 715×44.000≈31,5; 700×38.000=26,6). |
| 73 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.1.2* — Costruzione dal basso del costo del personale clinico apicale (Psicologo  | altro | verificata-discrepanza | Tabella strutturalmente incompleta: 7 righe ma **1 sola colonna** — contiene solo le etichette di riga ("Classe di imputazione", "Grandezza fisica", "Costo unitario", ecc.) senza alcuna colonna di valori. Non contiene dati verificabili nello stato attuale del file. |
| 74 | Parte VII — Costi diretti (rinegoziazione integrale) | — | altro | verificata-discrepanza | Stessa anomalia di #73: tabella a 1 colonna, solo etichette, nessun valore (profilo di costo del secondo livello). |
| 75 | Parte VII — Costi diretti (rinegoziazione integrale) | — | altro | verificata-discrepanza | Stessa anomalia di #73: tabella a 1 colonna, solo etichette (profilo di costo del terzo livello). |
| 76 | Parte VII — Costi diretti (rinegoziazione integrale) | — | altro | verificata-discrepanza | Stessa anomalia di #73: tabella a 1 colonna, solo etichette (profilo di costo del quarto livello). |
| 77 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-discrepanza | Costo del personale di cassa per scenario. Centrale (35,8) ed Espansivo (29,1): somma dei componenti corretta. **Conservativo: componenti sommano a 42,7 (37,0+1,5+2,8+1,4), ma il totale dichiarato è ≈42,2** — scarto di 0,5 mln (~1,2%). |
| 78 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.1.8* — Consolidamento del costo del personale lungo la cascata, a regime, per sc | infografica | n/a-infografica | Valori citati nel segnaposto (35,8 mln centrale) coerenti col dato verificato in #77. |
| 79 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-ok | Costi di struttura/coordinamento/organizzazione: somma dei componenti corretta nei 3 scenari (5,9 / 4,2 / 3,1). |
| 80 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.2.6* — Consolidamento dei costi di struttura, coordinamento e organizzazione a r | infografica | n/a-infografica | Coerente con #79. |
| 81 | Parte VII — Costi diretti (rinegoziazione integrale) | — | altro | da verificare | |
| 82 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-discrepanza | Costo incrementale leva digitale/IA. Centrale: componenti (0,65+0,45+0,15=1,25) ≈ 1,2 dichiarato (arrotondamento). **Conservativo: componenti sommano a 1,7 (0,8+0,6+0,3), ma il "costo incrementale lordo" dichiarato è ≈1,3** (scarto 0,4). **Espansivo: componenti sommano a 0,9 (0,5+0,3+0,1), ma il dichiarato è ≈1,1** (scarto 0,2). Il costo netto (lordo + autofinanziamento) risulta invece coerente usando i totali dichiarati (non i componenti): 1,3−1,0=+0,3 ✓; 1,2−1,3=−0,1 ✓; 1,1−1,5=−0,4 ✓. |
| 83 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.3.7* — Costo incrementale lordo e netto della leva digitale e dell’Intelligenza  | infografica | n/a-infografica | Riporta le cifre dello scenario centrale (coerenti); non riflette la discrepanza di #82 sugli scenari laterali. |
| 84 | Parte VII — Costi diretti (rinegoziazione integrale) | — | altro | da verificare | |
| 85 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-discrepanza | Costo della formazione per modalità. Centrale: componenti sommano a 4,0, coerente. **Conservativo: componenti sommano a 5,7 (0,9+1,6+1,4+1,3+0,5), ma il "percorso formativo integrato" dichiarato è ≈5,0** (scarto 0,7). **Espansivo: componenti sommano a 2,7 (0,4+0,8+0,7+0,6+0,2), ma il dichiarato è ≈3,2** (scarto 0,5). |
| 86 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.4.9* — Consolidamento del costo della formazione a regime, per scenario, in mili | infografica | n/a-infografica | Riporta le cifre dello scenario centrale (coerenti); non riflette la discrepanza di #85. |
| 87 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-ok | **Tabella master del costo diretto complessivo** — la più citata nei prodotti della piramide. Tutti e 3 gli scenari tornano esattamente: modello base = personale + struttura; lordo = base + leva + formazione; netto = lordo − autofinanziamento. Centrale: 35,8+4,2=40,0; +1,2+4,0=45,2; −1,3=43,9 — **conferma le cifre già usate nei Livelli 1-4** (45,2 lordo / 43,9 netto). Nota: usa i totali di #77/#82/#85 così come dichiarati in quelle tabelle, non i componenti che in due casi (Conservativo, Espansivo) non tornano esattamente (si veda #77, #82, #85). |
| 88 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-ok | Profilo temporale (Anno 1-5, scenario centrale): costo operativo + una tantum = totale in ogni riga (22,2 / 26,4 / 31,5 / 38,1 / 45,2). |
| 89 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.5.5* — Profilo temporale del costo diretto complessivo lordo nello scenario cent | infografica | n/a-infografica | Coerente con #88. |
| 90 | Parte VII — Costi diretti (rinegoziazione integrale) | — | dati | verificata-ok | Distribuzione del costo lungo la cascata (scenario centrale): 34,8 (apice) + 1,0 (L3) + 1,2 (L4) + 8,2 (trasversale) = 45,2, coerente col totale dichiarato. |
| 91 | Parte VII — Costi diretti (rinegoziazione integrale) | Tabella 7.5.6* — Distribuzione del costo diretto complessivo di cassa lungo la cascata del | infografica | n/a-infografica | |
| 92 | Parte VIII | — | altro | verificata-ok | Tabella di intestazione/legenda dei quattro canali, nessuna aritmetica propria. |
| 93 | Parte VIII | — | dati | verificata-ok | Contesto farmaceutico: righe coerenti col testo circostante, nessuna somma errata. |
| 94 | Parte VIII | Tabella 8.1 — Il contesto farmaceutico pugliese e i margini di appropriatezza. Gli indicat | dati | verificata-ok | Etichette scenario "Conservativo (~450) / Intermedio (~700) / Espansivo (~900)" psicologi. Ogni componente somma esattamente al totale dichiarato. |
| 95 | Parte VIII | Tabella 8.2 — Stima prudenziale del risparmio del canale farmaceutico per scenario di cope | infografica | n/a-infografica | |
| 96 | Parte VIII | — | dati | verificata-ok | Aggregati canale 2 (PS/ricoveri): coerenti col testo. |
| 97 | Parte VIII | Tabella 8.3 — Gli aggregati di ancoraggio del secondo canale e i margini di compressione.  | dati | verificata-ok | Stesse etichette scenario 450/700/900; componenti sommano esattamente al totale dichiarato. |
| 98 | Parte VIII | Tabella 8.4 — Stima prudenziale del risparmio del canale pronto soccorso e ricoveri per sc | infografica | n/a-infografica | |
| 99 | Parte VIII | — | dati | verificata-ok | Aggregati canale 3 (mobilità passiva): coerenti col testo. |
| 100 | Parte VIII | Tabella 8.5 — Gli aggregati di ancoraggio del terzo canale e la componente intercettabile. | dati | verificata-ok | Etichette 450/700/900; componenti sommano esattamente al totale dichiarato. |
| 101 | Parte VIII | Tabella 8.6 — Stima prudenziale del risparmio del canale della mobilità passiva per scenar | infografica | n/a-infografica | |
| 102 | Parte VIII | — | dati | verificata-ok | Aggregati canale 4: coerenti col testo. |
| 103 | Parte VIII | Tabella 8.7 — Gli aggregati di ancoraggio del quarto canale e i margini di compressione. I | dati | verificata-ok | Etichette 450/700/900; componenti sommano esattamente al totale dichiarato. |
| 104 | Parte VIII | Tabella 8.8 — Stima prudenziale del risparmio del quarto canale per scenario. Le cifre son | infografica | n/a-infografica | |
| 105 | Parte VIII | — | dati | verificata-ok | Riepilogo pre-totale: coerente. |
| 106 | Parte VIII | — | infografica | n/a-infografica | |
| 107 | Parte VIII | — | dati | verificata-ok | Risparmio diretto complessivo (4 canali): ~20/~34/~50 mln€ per 450/700/900. Componenti sommano esattamente; totale coincide con le cifre già usate in tutti i prodotti della piramide (scenario centrale ≈34 mln€, arrotondato a 34,8 nel raccordo con Parte VII). |
| 108 | Parte VIII | — | dati | verificata-discrepanza | "Costi diretti del servizio (settima parte)" = ~25/~38/~50 mln€ per 450/700/900. **Incoerente con la tabella master di Parte VII (#87, verificata-ok)**, che dà il costo diretto complessivo per gli stessi tre scenari nominali come 54,4/45,2/36,5 mln€ lordo (53,4/43,9/35,0 netto) — scarto ~15-18% (6-7 mln€) non riconducibile a un semplice errore di arrotondamento o inversione di scenario. Vedi discrepanza maggiore registrata in `_meta/parking-lot.md` e `_meta/status-tracker.md` (2026-07-06): almeno tre schemi di etichettatura degli scenari (620/775/900 in Parte X; ~450/700/900 in Parte VIII; FTE non chiaramente mappato in Parte VII) e almeno tre cifre di costo per lo scenario centrale (~38 Parte VIII, ~40,5 Parte IV/OCSE 2026, ~43,9-45,2 Parte VII) coesistono nello stesso Tomo I senza riconciliazione dichiarata. Non corretto silenziosamente — riconciliazione rimandata a valle della verifica sistematica, per decisione dell'autore. |
| 109 | Parte VIII | — | infografica | n/a-infografica | |
| 110 | Parte VIII | — | infografica | n/a-infografica | |
| 111 | Parte IX | — | altro | da verificare | |
| 112 | Parte IX | — | dati | da verificare | |
| 113 | Parte IX | Tabella 9.1 — Le forme del carico lavorativo del disagio psichico e i margini di compressi | dati | da verificare | |
| 114 | Parte IX | Tabella 9.2 — Stima prudenziale del beneficio del dominio lavorativo per scenario, secondo | infografica | n/a-infografica | |
| 115 | Parte IX | — | dati | da verificare | |
| 116 | Parte IX | Tabella 9.3 — Le forme dell’uscita dal lavoro per cause psichiche e i margini di prevenzio | dati | da verificare | |
| 117 | Parte IX | Tabella 9.4 — Stima prudenziale del beneficio del dominio pensionistico per scenario. Le c | infografica | n/a-infografica | |
| 118 | Parte IX | — | dati | da verificare | |
| 119 | Parte IX | Tabella 9.5 — Le forme residue della perdita di output e i margini di conservazione. Le gr | dati | da verificare | |
| 120 | Parte IX | Tabella 9.6 — Stima prudenziale della componente residua del dominio produttivistico per s | infografica | n/a-infografica | |
| 121 | Parte IX | — | dati | da verificare | |
| 122 | Parte IX | Tabella 9.7 — Le forme del carico assistenziale dei caregiver e i margini di compressione. | dati | da verificare | |
| 123 | Parte IX | Tabella 9.8 — Stima prudenziale del beneficio del dominio assistenzialistico per scenario. | infografica | n/a-infografica | |
| 124 | Parte IX | — | dati | da verificare | |
| 125 | Parte IX | Tabella 9.9 — Le forme della spesa assistenziale non previdenziale connessa al disagio psi | dati | da verificare | |
| 126 | Parte IX | Tabella 9.10 — Stima prudenziale del beneficio del dominio welfaristico per scenario. Le c | infografica | n/a-infografica | |
| 127 | Parte IX | — | dati | da verificare | |
| 128 | Parte IX | Tabella 9.11 — Le forme della componente prospettica residua della prevenzione e i margini | dati | da verificare | |
| 129 | Parte IX | Tabella 9.12 — Stima prudenziale della componente residua del dominio prevenzionalistico p | infografica | n/a-infografica | |
| 130 | Parte IX | — | dati | da verificare | |
| 131 | Parte IX | Tabella 9.13 — Le forme del costo della giustizia connesse alla frazione piccola e mediata | dati | da verificare | |
| 132 | Parte IX | Tabella 9.14 — Stima prudenziale del beneficio del dominio criminologico per scenario. Le  | infografica | n/a-infografica | |
| 133 | Parte IX | — | dati | da verificare | |
| 134 | Parte IX | Tabella 9.15 — Le forme dell’onere amministrativo connesso alla presa in carico frammentat | dati | da verificare | |
| 135 | Parte IX | Tabella 9.16 — Stima prudenziale del beneficio del dominio burocratico per scenario. Le ci | infografica | n/a-infografica | |
| 136 | Parte IX | — | dati | da verificare | |
| 137 | Parte IX | Tabella 9.17 — Le due dimensioni del dominio culturale e il loro trattamento. Solo la comp | dati | da verificare | |
| 138 | Parte IX | Tabella 9.18 — Stima prudenziale della sola componente monetizzabile residua del dominio c | infografica | n/a-infografica | |
| 139 | Parte IX | — | dati | da verificare | |
| 140 | Parte IX | Tabella 9.19 — Le forme del carico scolastico connesso al disagio in età evolutiva e i mar | dati | da verificare | |
| 141 | Parte IX | Tabella 9.20 — Stima prudenziale del beneficio del dominio pedagogico e scolastico per sce | infografica | n/a-infografica | |
| 142 | Parte IX | — | dati | da verificare | |
| 143 | Parte IX | Tabella 9.21 — Le dimensioni del dominio accademico e il loro trattamento. Solo la compone | dati | da verificare | |
| 144 | Parte IX | Tabella 9.22 — Stima prudenziale della sola componente residua monetizzabile del dominio a | infografica | n/a-infografica | |
| 145 | Parte IX | — | dati | da verificare | |
| 146 | Parte IX | Tabella 9.23 — Le forme dell’effetto organizzativo del disagio e i margini di compressione | dati | da verificare | |
| 147 | Parte IX | Tabella 9.24 — Stima prudenziale del beneficio del dominio industriale per scenario. Le ci | infografica | n/a-infografica | |
| 148 | Parte IX | — | dati | da verificare | |
| 149 | Parte IX | Tabella 9.25 — Le dimensioni del dominio sindacale e il loro trattamento. Solo la componen | dati | da verificare | |
| 150 | Parte IX | Tabella 9.26 — Stima prudenziale della sola minima componente residua monetizzabile del do | infografica | n/a-infografica | |
| 151 | Parte IX | — | dati | da verificare | |
| 152 | Parte IX | Tabella 9.27 — Le dimensioni del dominio antropologico e il loro trattamento non monetizza | infografica | n/a-infografica | |
| 153 | Parte IX | — | dati | da verificare | |
| 154 | Parte IX | Tabella 9.28 — Le dimensioni del dominio sociale e il loro trattamento non monetizzato. En | infografica | n/a-infografica | |
| 155 | Parte IX | — | dati | da verificare | |
| 156 | Parte IX | Tabella 9.29 — Le dimensioni del dominio finanziario e il loro trattamento. La funzione di | dati | da verificare | |
| 157 | Parte IX | Tabella 9.30 — Stima prudenziale della sola componente residua di stabilizzazione del domi | infografica | n/a-infografica | |
| 158 | Parte X | — | altro | da verificare | |
| 159 | Parte X | — | dati | da verificare | |
| 160 | Parte X | — | dati | da verificare | |
| 161 | Parte X | — | dati | da verificare | |
| 162 | Parte X | Tabella 10.3 — Valore monetizzato dei guadagni di salute della riforma, per scenario, calc | dati | da verificare | |
| 163 | Parte X | Tabella 10.4 — Passaggio dal rendimento dei soli benefici economici al rendimento che incl | infografica | n/a-infografica | |
| 164 | Parte X | — | dati | da verificare | |
| 165 | Parte X | — | dati | da verificare | |
| 166 | Parte X | — | dati | da verificare | |
| 167 | Parte X | Tabella 10.7 — Sostenibilità dell’impatto di bilancio della riforma rispetto alla dimensio | infografica | n/a-infografica | |
| 168 | Parte X | — | dati | da verificare | |
| 169 | Parte X | Tabella 10.8 — Composizione del valore sociale lordo ai fini del rendimento sociale dell’i | dati | da verificare | |
| 170 | Parte X | — | dati | da verificare | |
| 171 | Parte X | Tabella 10.10 — Calcolo del rendimento sociale netto dell’investimento, per scenario, e co | infografica | n/a-infografica | |
| 172 | Parte X | — | dati | da verificare | |
| 173 | Parte X | — | dati | da verificare | |
| 174 | Parte X | — | dati | da verificare | |
| 175 | Parte X | Tabella 10.13 — Punteggio composito della sintesi multi-criterio per scenario, calcolato c | infografica | n/a-infografica | |
| 176 | Parte X | — | dati | da verificare | |
| 177 | Parte X | Tabella 10.14 — Saldo economico consolidato della riforma per scenario: la tabella master  | infografica | n/a-infografica | |
| 178 | Parte XI | — | altro | da verificare | |
| 179 | Parte XI | — | dati | da verificare | |
| 180 | Parte XI | — | dati | da verificare | |
| 181 | Parte XI | — | dati | da verificare | |
| 182 | Parte XI | Tabella 11.3 — Parametri invarianti cross-regionali del modello di Markov, costanti per l’ | infografica | n/a-infografica | |
| 183 | Parte XI | — | dati | da verificare | |
| 184 | Parte XI | — | dati | da verificare | |
| 185 | Parte XI | Tabella 11.5 — Risultati dell’analisi di sensibilità probabilistica, per scenario. Il rapp | infografica | n/a-infografica | |
| 186 | Parte XI | — | dati | da verificare | |
| 187 | Parte XI | — | dati | da verificare | |
| 188 | Parte XI | Tabella 11.7 — Le previsioni falsificabili sulla qualità della vita delle persone, nello s | infografica | n/a-infografica | |
| 189 | Parte XI | — | dati | da verificare | |
| 190 | Parte XI | — | dati | da verificare | |
| 191 | Parte XI | Tabella 11.9 — Le previsioni falsificabili sui bilanci regionali, nello scenario intermedi | infografica | n/a-infografica | |
| 192 | Parte XI | — | dati | da verificare | |
| 193 | Parte XI | Tabella 11.10 — Le previsioni falsificabili sulla burocrazia e l’efficienza amministrativa | infografica | n/a-infografica | |
| 194 | Parte XI | — | dati | da verificare | |
| 195 | Parte XI | Tabella 11.11 — Le previsioni falsificabili sui sistemi sanitari regionali, nello scenario | infografica | n/a-infografica | |
| 196 | Parte XI | — | dati | da verificare | |
| 197 | Parte XI | — | infografica | n/a-infografica | |
| 198 | Parte XII | — | altro | da verificare | |
| 199 | Parte XII | — | dati | da verificare | |
| 200 | Parte XII | Tabella 12.1 — Distribuzione illustrativa del contingente di psicologi di base tra le sei  | infografica | n/a-infografica | |
| 201 | Parte XII | — | infografica | n/a-infografica | |
| 202 | Parte XII | — | dati | da verificare | |
| 203 | Parte XII | — | dati | da verificare | |
| 204 | Parte XII | Tabella 12.3 — Le tre dimensioni del divario digitale in Puglia, la loro sovrapposizione a | infografica | n/a-infografica | |
| 205 | Parte XII | — | dati | da verificare | |
| 206 | Parte XII | — | infografica | n/a-infografica | |
| 207 | Parte XIII | — | altro | da verificare | |
| 208 | Parte XIII | — | dati | da verificare | |
| 209 | Parte XIII | Tabella 13.1 — Le principali fonti del fondamento costituzionale e convenzionale del dirit | infografica | n/a-infografica | |
| 210 | Parte XIII | — | dati | da verificare | |
| 211 | Parte XIII | — | infografica | n/a-infografica | |
| 212 | Parte XIII | — | dati | da verificare | |
| 213 | Parte XIII | — | infografica | n/a-infografica | |
| 214 | Parte XIII | — | dati | da verificare | |
| 215 | Parte XIII | Tabella 13.4 — La distribuzione delle funzioni e delle responsabilità tra le figure e le i | infografica | n/a-infografica | |
| 216 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 217 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 218 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 219 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 220 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 221 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 222 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 223 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 224 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 225 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. Analisi multi-criterio: confronto tra l‘opzione di intervento e l’opzione zer | dati | da verificare | |
| 226 | Appendice I — Mappa integrale dei domini disciplinari | — | dati | da verificare | |
| 227 | Appendice I — Mappa integrale dei domini disciplinari | — | altro | da verificare | |
| 228 | Parte II — Domini a Impatto Sistemico Indiretto | — | altro | da verificare | |
| 229 | Parte III — Il Perimetro di Impatto Economico-Sociale ( | — | dati | da verificare | |
| 230 | Parte III — Il Perimetro di Impatto Economico-Sociale ( | — | altro | da verificare | |
| 231 | Parte III — Il Perimetro di Impatto Economico-Sociale ( | — | dati | da verificare | |
| 232 | Appendice II — Quantificazione su dati primari regional | — | dati | da verificare | |
| 233 | Appendice II — Quantificazione su dati primari regional | — | dati | da verificare | |
| 234 | Appendice II — Quantificazione su dati primari regional | — | dati | da verificare | |
| 235 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 236 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 237 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 238 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 239 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 240 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 241 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 242 | Appendice III — Batteria integrale di indicatori e vari | — | dati | da verificare | |
| 243 | Appendice IV — Riconciliazione e tabella unica dei valo | — | dati | da verificare | |
| 244 | Appendice IV — Riconciliazione e tabella unica dei valo | — | dati | da verificare | |
| 245 | Appendice IV — Riconciliazione e tabella unica dei valo | — | dati | da verificare | |
| 246 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 247 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 248 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 249 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 250 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 251 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 252 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 253 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 254 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 255 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 256 | Appendice V — Analisi delle lacune e agenda di acquisiz | — | dati | da verificare | |
| 257 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 258 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 259 | Appendice VIII — Percorso clinico per intensità crescen | — | dati | da verificare | |
| 260 | Appendice VIII — Percorso clinico per intensità crescen | — | dati | da verificare | |
| 261 | Appendice VIII — Percorso clinico per intensità crescen | — | dati | da verificare | |
| 262 | Appendice VIII — Percorso clinico per intensità crescen | — | dati | da verificare | |
| 263 | Appendice IX — Modello tariffario e di costo | — | dati | da verificare | |
| 264 | Appendice IX — Modello tariffario e di costo | — | dati | da verificare | |
| 265 | Appendice IX — Modello tariffario e di costo | — | dati | da verificare | |
| 266 | Appendice IX — Modello tariffario e di costo | — | dati | da verificare | |
| 267 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 268 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 269 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 270 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 271 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 272 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 273 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 274 | Appendice X — Specifica di estrazione dei dati primari | — | dati | da verificare | |
| 275 | Appendice XI — Protocollo minimo di rilevazione | — | dati | da verificare | |
| 276 | Appendice XI — Protocollo minimo di rilevazione | — | dati | da verificare | |
| 277 | Appendice XI — Protocollo minimo di rilevazione | — | dati | da verificare | |
| 278 | Appendice XI — Protocollo minimo di rilevazione | — | dati | da verificare | |
| 279 | Appendice XII — Dispositivi terapeutici digitali su pre | — | dati | da verificare | |
| 280 | Appendice XII — Dispositivi terapeutici digitali su pre | — | dati | da verificare | |
| 281 | Appendice XIII — Approfondimento evidence-based interna | — | dati | da verificare | |
| 282 | Parte VII — La quantificazione dell’ulteriore riduzione | — | dati | da verificare | |
| 283 | Parte VII — La quantificazione dell’ulteriore riduzione | — | dati | da verificare | |
| 284 | Parte VII — La quantificazione dell’ulteriore riduzione | — | dati | da verificare | |
| 285 | Parte VII — La quantificazione dell’ulteriore riduzione | — | dati | da verificare | |
| 286 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 287 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 288 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 289 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 290 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 291 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 292 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 293 | Parte III — I dispositivi terapeutici digitali su presc | — | dati | da verificare | |
| 294 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 295 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 296 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio. | dati | da verificare | |
| 297 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 298 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 299 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 300 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 301 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 302 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 303 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 304 | Parte E — Valutazione economica | — | dati | da verificare | |
| 305 | Parte E — Valutazione economica | — | dati | da verificare | |
| 306 | Parte E — Valutazione economica | — | dati | da verificare | |
| 307 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 308 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 309 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 310 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 311 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 312 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 313 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 314 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 315 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 316 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 317 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 318 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 319 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 320 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 321 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 322 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 323 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. Analisi multi-criterio: confronto tra l‘opzione di intervento e l’opzione zer | dati | da verificare | |
| 324 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 325 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 326 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 327 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 328 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 329 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 330 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio (Corte dei Conti, GIMBE, emergenza-urgenza,  | dati | da verificare | |
| 331 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 332 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 333 | Appendice XVII — Struttura dell’opera | — | dati | da verificare | |
| 334 | Appendice XX — L’innesto dell’Intelligenza Artificiale  | — | dati | da verificare | |
| 335 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 336 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 337 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 338 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 339 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 340 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 341 | Appendice XXI — Capitolo I dello studio IA-Formazione ( | — | dati | da verificare | |
| 342 | Appendice A — Approfondimento clinico per fase del cont | — | dati | da verificare | |
| 343 | Appendice XXIV — Il telaio metodologico integrale: le q | — | dati | da verificare | |
| 344 | Appendice XXIV — Il telaio metodologico integrale: le q | — | dati | da verificare | |
| 345 | Appendice XXIV — Il telaio metodologico integrale: le q | — | dati | da verificare | |
| 346 | Parte II — Le quattro cornici e la loro integrazione | — | dati | da verificare | |
| 347 | Parte II — Le quattro cornici e la loro integrazione | — | dati | da verificare | |
| 348 | Parte II — Le quattro cornici e la loro integrazione | — | dati | da verificare | |
| 349 | Parte II — Le quattro cornici e la loro integrazione | — | dati | da verificare | |
| 350 | Parte III — L’architettura risultante e le metodologie | — | dati | da verificare | |
| 351 | Parte III — L’architettura risultante e le metodologie | — | dati | da verificare | |
| 352 | Parte III — L’architettura risultante e le metodologie | — | dati | da verificare | |
| 353 | Parte IV — Il quadro metodologico comune e la generaliz | — | dati | da verificare | |
| 354 | Parte IV — Il quadro metodologico comune e la generaliz | — | dati | da verificare | |
| 355 | Parte IV — Il quadro metodologico comune e la generaliz | — | dati | da verificare | |
| 356 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 357 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 358 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio. | dati | da verificare | |
| 359 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 360 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 361 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 362 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 363 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 364 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 365 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 366 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 367 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 368 | Parte E — Valutazione economica | — | dati | da verificare | |
| 369 | Parte E — Valutazione economica | — | dati | da verificare | |
| 370 | Parte E — Valutazione economica | — | dati | da verificare | |
| 371 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 372 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 373 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 374 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 375 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 376 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 377 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 378 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 379 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 380 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 381 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 382 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 383 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 384 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 385 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 386 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 387 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. Analisi multi-criterio: confronto tra l‘******opzione di intervento e l****** | dati | da verificare | |
| 388 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 389 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 390 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 391 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 392 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 393 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 394 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio (Corte dei Conti, GIMBE, emergenza-urgenza,  | dati | da verificare | |
| 395 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 396 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 397 | Parte I — Il contesto pugliese | — | dati | da verificare | |
| 398 | Parte I — Il contesto pugliese | — | dati | da verificare | |
| 399 | Parte I — Il contesto pugliese | — | dati | da verificare | |
| 400 | Parte II — La metodologia apicale applicata alla Puglia | — | dati | da verificare | |
| 401 | Parte II — La metodologia apicale applicata alla Puglia | — | dati | da verificare | |
| 402 | Parte III — Il cruscotto di sintesi e il piano di misur | — | dati | da verificare | |
| 403 | Parte III — Il cruscotto di sintesi e il piano di misur | — | dati | da verificare | |
| 404 | Parte IV — La quantificazione per la Puglia | — | dati | da verificare | |
| 405 | Parte IV — La quantificazione per la Puglia | — | dati | da verificare | |
| 406 | Parte IV — La quantificazione per la Puglia | — | dati | da verificare | |
| 407 | Parte IV — La quantificazione per la Puglia | Tabella C.5. Sintesi dell’evidenza sull’efficacia dell’Intelligenza Artificiale in salute  | dati | da verificare | |
| 408 | Parte IV — La quantificazione per la Puglia | Tabella C.6. L’architettura formativa pro-Intelligenza Artificiale: quattro modalità, valu | dati | da verificare | |
| 409 | Parte IV — La quantificazione per la Puglia | Tabella C.7. Quantificazione dei risparmi diretti aggiuntivi per effetto dell’integrazione | dati | da verificare | |
| 410 | Parte D — Efficacia clinica ed evidenza | Tabella D.3. Il corpus di studi sul Collaborative Care: caratteristiche degli studi e mode | dati | da verificare | |
| 411 | Parte D — Efficacia clinica ed evidenza | Tabella D.4. Esiti clinici principali del corpus: DFD, QALY e tassi di risposta per studio | dati | da verificare | |
| 412 | Parte D — Efficacia clinica ed evidenza | Tabella D.5. Profilo economico del corpus: costi incrementali, ICER e valutazione di soste | dati | da verificare | |
| 413 | Parte D — Efficacia clinica ed evidenza | Tabella D.6. Confronto tra terapia cognitivo-comportamentale computerizzata (iCBT) e cura  | dati | da verificare | |
| 414 | Parte D — Efficacia clinica ed evidenza | Tabella D.7. Stima del risparmio di produttività recuperata per paziente: confronto tra iC | dati | da verificare | |
| 415 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 416 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 417 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 418 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 419 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 420 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 421 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 422 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 423 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 424 | Appendice XXXIII — Il registro indicizzato dei file di  | — | dati | da verificare | |
| 425 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 426 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 427 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 428 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 429 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 430 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 431 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 432 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 433 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 434 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 435 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 436 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 437 | Parte E — La valutazione economica | — | dati | da verificare | |
| 438 | Parte E — La valutazione economica | — | dati | da verificare | |
| 439 | Parte E — La valutazione economica | — | dati | da verificare | |
| 440 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 441 | Parte F — Modellazione decisionale e incertezza | Tabella F.1. Risultati del caso base del modello di Markov, per paziente, su orizzonte qui | dati | da verificare | |
| 442 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 443 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 444 | Parte G — Equità e impatto distributivo | Tabella G.1. Le dimensioni dell’equità e le variabili seguite dallo studio. | dati | da verificare | |
| 445 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 446 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I riferimenti giuridici e costituzionali essenziali dell’intervento. | dati | da verificare | |
| 447 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 448 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I quadri della scienza dell’implementazione: RE-AIM per gli esiti, CFIR per i | dati | da verificare | |
| 449 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 450 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 451 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 452 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 453 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 454 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 455 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 456 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 457 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 458 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 459 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 460 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 461 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio del Piemonte. | dati | da verificare | |
| 462 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 463 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 464 | Appendice E — Glossario | — | dati | da verificare | |
| 465 | Appendice E — Glossario | — | dati | da verificare | |
| 466 | Appendice E — Glossario | — | dati | da verificare | |
| 467 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 468 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 469 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 470 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 471 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 472 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 473 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 474 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 475 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 476 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 477 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 478 | Parte E — La valutazione economica | — | dati | da verificare | |
| 479 | Parte E — La valutazione economica | — | dati | da verificare | |
| 480 | Parte E — La valutazione economica | — | dati | da verificare | |
| 481 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 482 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 483 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 484 | Parte L — Monitoraggio, valutazione e verifica ex post | — | dati | da verificare | |
| 485 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 486 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La ricomposizione dell’intervento secondo i sei criteri di valutazione OCSE-D | dati | da verificare | |
| 487 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 488 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 489 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 490 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 491 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 492 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 493 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio della Liguria. | dati | da verificare | |
| 494 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 495 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 496 | Appendice E — Glossario | — | dati | da verificare | |
| 497 | Appendice E — Glossario | — | dati | da verificare | |
| 498 | Appendice E — Glossario | — | dati | da verificare | |
| 499 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 500 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 501 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 502 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 503 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 504 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 505 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 506 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 507 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 508 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 509 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 510 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 511 | Parte E — Valutazione economica | — | dati | da verificare | |
| 512 | Parte E — Valutazione economica | — | dati | da verificare | |
| 513 | Parte E — Valutazione economica | — | dati | da verificare | |
| 514 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 515 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 516 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 517 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 518 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 519 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 520 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 521 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 522 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 523 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 524 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 525 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 526 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 527 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 528 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 529 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 530 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 531 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 532 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 533 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 534 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 535 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio della Lombardia. | dati | da verificare | |
| 536 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 537 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 538 | Appendice E — Glossario | — | dati | da verificare | |
| 539 | Appendice E — Glossario | — | dati | da verificare | |
| 540 | Appendice E — Glossario | — | dati | da verificare | |
| 541 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 542 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 543 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 544 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 545 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 546 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 547 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 548 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 549 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 550 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 551 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 552 | Parte E — Valutazione economica | — | dati | da verificare | |
| 553 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 554 | Parte E — Valutazione economica | — | dati | da verificare | |
| 555 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 556 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 557 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 558 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 559 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 560 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 561 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 562 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici del servizio nel Trentino-Alto Adige. | dati | da verificare | |
| 563 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 564 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 565 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 566 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 567 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie della batteria di indicatori. | dati | da verificare | |
| 568 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 569 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 570 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L‘******analisi multi-criterio: punteggi dell******’intervento e del non inte | dati | da verificare | |
| 571 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 572 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 573 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 574 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 575 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 576 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 577 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori di ancoraggio del Trentino-Alto Adige. | dati | da verificare | |
| 578 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 579 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 580 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 581 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 582 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 583 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 584 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 585 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 586 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 587 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 588 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 589 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 590 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 591 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 592 | Parte E — La valutazione economica | — | dati | da verificare | |
| 593 | Parte E — La valutazione economica | — | dati | da verificare | |
| 594 | Parte E — La valutazione economica | — | dati | da verificare | |
| 595 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 596 | Parte F — Modellazione decisionale e incertezza | Tabella F.1. Risultati del caso base del modello di Markov, per paziente, su orizzonte qui | dati | da verificare | |
| 597 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 598 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 599 | Parte G — Equità e impatto distributivo | Tabella G.1. Le dimensioni dell’equità e le variabili seguite dallo studio. | dati | da verificare | |
| 600 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 601 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I riferimenti giuridici e costituzionali essenziali dell’intervento. | dati | da verificare | |
| 602 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 603 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I quadri della scienza dell’implementazione: RE-AIM per gli esiti, CFIR per i | dati | da verificare | |
| 604 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 605 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 606 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie di indicatori e lo stato della baseline. Circa quaranta ind | dati | da verificare | |
| 607 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 608 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 609 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La griglia di giudizio OCSE-DAC applicata allo studio, criterio per criterio. | dati | da verificare | |
| 610 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 611 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 612 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 613 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 614 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 615 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 616 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio del Veneto. | dati | da verificare | |
| 617 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 618 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 619 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 620 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 621 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 622 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 623 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 624 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 625 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 626 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 627 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 628 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 629 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 630 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 631 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 632 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 633 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 634 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 635 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 636 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 637 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 638 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 639 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 640 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 641 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 642 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 643 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 644 | Parte E — La valutazione economica | — | dati | da verificare | |
| 645 | Parte E — La valutazione economica | — | dati | da verificare | |
| 646 | Parte E — La valutazione economica | — | dati | da verificare | |
| 647 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 648 | Parte F — Modellazione decisionale e incertezza | Tabella F.1. Risultati del caso base del modello di Markov, per paziente, su orizzonte qui | dati | da verificare | |
| 649 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 650 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 651 | Parte G — Equità e impatto distributivo | Tabella G.1. Le dimensioni dell’equità e le variabili seguite dallo studio. | dati | da verificare | |
| 652 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 653 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I riferimenti giuridici e costituzionali essenziali dell’intervento. | dati | da verificare | |
| 654 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 655 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I quadri della scienza dell’implementazione: RE-AIM per gli esiti, CFIR per i | dati | da verificare | |
| 656 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 657 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 658 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 659 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 660 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 661 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 662 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 663 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 664 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 665 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 666 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 667 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 668 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio dell’Emilia-Romagna. | dati | da verificare | |
| 669 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 670 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 671 | Appendice E — Glossario | — | dati | da verificare | |
| 672 | Appendice E — Glossario | — | dati | da verificare | |
| 673 | Appendice E — Glossario | — | dati | da verificare | |
| 674 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 675 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 676 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 677 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 678 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 679 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 680 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 681 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 682 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 683 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 684 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 685 | Parte D — L’efficacia e l’evidenza | — | dati | da verificare | |
| 686 | Parte E — La valutazione economica | — | dati | da verificare | |
| 687 | Parte E — La valutazione economica | — | dati | da verificare | |
| 688 | Parte E — La valutazione economica | — | dati | da verificare | |
| 689 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 690 | Parte F — Modellazione decisionale e incertezza | Tabella F.1. Risultati del caso base del modello di Markov, per paziente, su orizzonte qui | dati | da verificare | |
| 691 | Parte F — Modellazione decisionale e incertezza | — | dati | da verificare | |
| 692 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 693 | Parte G — Equità e impatto distributivo | Tabella G.1. Le dimensioni dell’equità e le variabili seguite dallo studio. | dati | da verificare | |
| 694 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 695 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I riferimenti giuridici e costituzionali essenziali dell’intervento. | dati | da verificare | |
| 696 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 697 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I quadri della scienza dell’implementazione: RE-AIM per gli esiti, CFIR per i | dati | da verificare | |
| 698 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 699 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 700 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 701 | Parte L — Monitoraggio, valutazione ed ex post | — | dati | da verificare | |
| 702 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 703 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 704 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 705 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 706 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 707 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 708 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 709 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 710 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio della Toscana. | dati | da verificare | |
| 711 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 712 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 713 | Appendice E — Glossario | — | dati | da verificare | |
| 714 | Appendice E — Glossario | — | dati | da verificare | |
| 715 | Appendice E — Glossario | — | dati | da verificare | |
| 716 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 717 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 718 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 719 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 720 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 721 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 722 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 723 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 724 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 725 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 726 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 727 | Parte E — Valutazione economica | — | dati | da verificare | |
| 728 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 729 | Parte E — Valutazione economica | — | dati | da verificare | |
| 730 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 731 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 732 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 733 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 734 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 735 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 736 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 737 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici dell’istituzione del servizio nel Lazio. | dati | da verificare | |
| 738 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 739 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 740 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 741 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 742 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie della batteria di indicatori. | dati | da verificare | |
| 743 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 744 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 745 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L‘analisi multi-criterio: punteggi dell’intervento e del non intervento. | dati | da verificare | |
| 746 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 747 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 748 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 749 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 750 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 751 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 752 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio del Lazio. | dati | da verificare | |
| 753 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 754 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 755 | Appendice E — Glossario | — | dati | da verificare | |
| 756 | Appendice E — Glossario | — | dati | da verificare | |
| 757 | Appendice E — Glossario | — | dati | da verificare | |
| 758 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 759 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 760 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le regioni. | dati | da verificare | |
| 761 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 762 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 763 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 764 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 765 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 766 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 767 | Parte E — Valutazione economica | — | dati | da verificare | |
| 768 | Parte E — Valutazione economica | — | dati | da verificare | |
| 769 | Parte E — Valutazione economica | — | dati | da verificare | |
| 770 | Parte E — Valutazione economica | Tabella E.3. Risparmi diretti e ricadute sociali per scenario. Le due grandezze sono di na | dati | da verificare | |
| 771 | Parte E — Valutazione economica | — | dati | da verificare | |
| 772 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 773 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 774 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 775 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 776 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 777 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 778 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 779 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 780 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 781 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le sette categorie della batteria di indicatori. | dati | da verificare | |
| 782 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 783 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 784 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 785 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 786 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 787 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 788 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario. | dati | da verificare | |
| 789 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 790 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 791 | Appendice D — Checklist di reporting | — | dati | da verificare | |
| 792 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 793 | Appendice E — Glossario | — | dati | da verificare | |
| 794 | Appendice E — Glossario | — | dati | da verificare | |
| 795 | Appendice E — Glossario | — | dati | da verificare | |
| 796 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 797 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 798 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 799 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 800 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 801 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 802 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 803 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 804 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 805 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 806 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 807 | Parte E — Valutazione economica | — | dati | da verificare | |
| 808 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 809 | Parte E — Valutazione economica | — | dati | da verificare | |
| 810 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 811 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 812 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 813 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 814 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 815 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. Distribuzione del fabbisogno di psicologi per Azienda USL e scenario. | dati | da verificare | |
| 816 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 817 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 818 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 819 | Appendice C — Dati regionali e fonti | — | dati | da verificare | |
| 820 | Appendice D — Checklist di reporting | Tabella C.1. I dati regionali fondamentali e le fonti per la Regione Umbria. | dati | da verificare | |
| 821 | Appendice E — Glossario | — | dati | da verificare | |
| 822 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 823 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 824 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 825 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 826 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 827 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 828 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 829 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 830 | Parte C — L’intervento e il modello | — | dati | da verificare | |
| 831 | Parte C — L’intervento e il modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 832 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 833 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 834 | Parte E — Valutazione economica | — | dati | da verificare | |
| 835 | Parte E — Valutazione economica | — | dati | da verificare | |
| 836 | Parte E — Valutazione economica | — | dati | da verificare | |
| 837 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 838 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 839 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 840 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 841 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 842 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 843 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici del servizio nell’Abruzzo. | dati | da verificare | |
| 844 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 845 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 846 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 847 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 848 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie della batteria di indicatori. | dati | da verificare | |
| 849 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 850 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 851 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L’analisi multi-criterio: punteggi dell’intervento e del non intervento. | dati | da verificare | |
| 852 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 853 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 854 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 855 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 856 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 857 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 858 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio dell’Abruzzo. | dati | da verificare | |
| 859 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 860 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 861 | Appendice E — Glossario | — | dati | da verificare | |
| 862 | Appendice E — Glossario | — | dati | da verificare | |
| 863 | Appendice E — Glossario | — | dati | da verificare | |
| 864 | Parte E — Valutazione economica | — | dati | da verificare | |
| 865 | Parte E — Valutazione economica | — | dati | da verificare | |
| 866 | Parte E — Valutazione economica | — | dati | da verificare | |
| 867 | Parte E — Valutazione economica | Tabella E.5. Risparmi diretti e ricadute sociali per scenario. Le due grandezze sono di na | dati | da verificare | |
| 868 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 869 | Appendice A — Il caso di riferimento e i parametri del  | — | dati | da verificare | |
| 870 | Appendice A — Il caso di riferimento e i parametri del  | Tabella A.1. Parametri principali del modello e risultati per paziente. I valori per pazie | dati | da verificare | |
| 871 | Appendice C — I dati regionali e i dati da acquisire | — | dati | da verificare | |
| 872 | Appendice E — Il glossario | — | dati | da verificare | |
| 873 | Appendice E — Il glossario | — | dati | da verificare | |
| 874 | Appendice E — Il glossario | — | dati | da verificare | |
| 875 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 876 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 877 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 878 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 879 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 880 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 881 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 882 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 883 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 884 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 885 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 886 | Parte E — Valutazione economica | — | dati | da verificare | |
| 887 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 888 | Parte E — Valutazione economica | — | dati | da verificare | |
| 889 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 890 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 891 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 892 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 893 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 894 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 895 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 896 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici del servizio nella Campania. | dati | da verificare | |
| 897 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 898 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 899 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 900 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 901 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie della batteria di indicatori. | dati | da verificare | |
| 902 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 903 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 904 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L‘analisi multi-criterio: punteggi dell’intervento e del non intervento. | dati | da verificare | |
| 905 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 906 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 907 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 908 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 909 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 910 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 911 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio della Campania. | dati | da verificare | |
| 912 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 913 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 914 | Appendice E — Glossario | — | dati | da verificare | |
| 915 | Parte E — Valutazione economica | — | dati | da verificare | |
| 916 | Parte E — Valutazione economica | — | dati | da verificare | |
| 917 | Parte E — Valutazione economica | — | dati | da verificare | |
| 918 | Parte E — Valutazione economica | — | dati | da verificare | |
| 919 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 920 | Appendice A — Il caso di riferimento e i parametri del  | — | dati | da verificare | |
| 921 | Appendice A — Il caso di riferimento e i parametri del  | — | dati | da verificare | |
| 922 | Appendice C — I dati regionali e i dati da acquisire | — | dati | da verificare | |
| 923 | Appendice E — Il glossario | — | dati | da verificare | |
| 924 | Parte E — Valutazione economica | — | dati | da verificare | |
| 925 | Parte E — Valutazione economica | — | dati | da verificare | |
| 926 | Parte E — Valutazione economica | — | dati | da verificare | |
| 927 | Parte E — Valutazione economica | — | dati | da verificare | |
| 928 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 929 | Appendice A — Il caso di riferimento e i parametri del  | — | dati | da verificare | |
| 930 | Appendice A — Il caso di riferimento e i parametri del  | — | dati | da verificare | |
| 931 | Appendice C — I dati regionali e i dati da acquisire | — | dati | da verificare | |
| 932 | Appendice E — Il glossario | — | dati | da verificare | |
| 933 | Appendice E — Il glossario | — | dati | da verificare | |
| 934 | Appendice E — Il glossario | — | dati | da verificare | |
| 935 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 936 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 937 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 938 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 939 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 940 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 941 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 942 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 943 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 944 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 945 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 946 | Parte E — Valutazione economica | — | dati | da verificare | |
| 947 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 948 | Parte E — Valutazione economica | — | dati | da verificare | |
| 949 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 950 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 951 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 952 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 953 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 954 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 955 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 956 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici del servizio nella Sicilia. | dati | da verificare | |
| 957 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 958 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 959 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 960 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 961 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie della batteria di indicatori. | dati | da verificare | |
| 962 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 963 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 964 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L‘******analisi multi-criterio: punteggi dell******’intervento e del non inte | dati | da verificare | |
| 965 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 966 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 967 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 968 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 969 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 970 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 971 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori regionali di ancoraggio della Sicilia. | dati | da verificare | |
| 972 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 973 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 974 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 975 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 976 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 977 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 978 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 979 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 980 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 981 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 982 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 983 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 984 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 985 | Parte E — Valutazione economica | — | dati | da verificare | |
| 986 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 987 | Parte E — Valutazione economica | — | dati | da verificare | |
| 988 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 989 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 990 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 991 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 992 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 993 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 994 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 995 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici del servizio nella Sardegna. | dati | da verificare | |
| 996 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 997 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 998 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 999 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 1000 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le otto categorie della batteria di indicatori. | dati | da verificare | |
| 1001 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 1002 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 1003 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L‘******analisi multi-criterio: punteggi dell******’intervento e del non inte | dati | da verificare | |
| 1004 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 1005 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 1006 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 1007 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 1008 | Parte A — Quadro, quesito e metodo | — | dati | da verificare | |
| 1009 | Parte A — Quadro, quesito e metodo | Tabella A.2. Il caso di riferimento dello studio, comune a tutte le Regioni. | dati | da verificare | |
| 1010 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 1011 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 1012 | Parte B — Problema di salute, bisogno e contesto | — | dati | da verificare | |
| 1013 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 1014 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 1015 | Parte C — L’intervento e il suo modello | — | dati | da verificare | |
| 1016 | Parte C — L’intervento e il suo modello | Tabella C.3. Gli strumenti digitali e di intelligenza artificiale a supporto del servizio. | dati | da verificare | |
| 1017 | Parte D — Efficacia clinica ed evidenza | — | dati | da verificare | |
| 1018 | Parte E — Valutazione economica | — | dati | da verificare | |
| 1019 | Parte E — Valutazione economica | Tabella E.1. Il costo del servizio a regime nei tre scenari di copertura. | dati | da verificare | |
| 1020 | Parte E — Valutazione economica | — | dati | da verificare | |
| 1021 | Parte E — Valutazione economica | Tabella E.3. Il quadro economico consolidato, con la distinzione fra caso finanziario e ca | dati | da verificare | |
| 1022 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 1023 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 1024 | Parte F — Modellazione e incertezza | — | dati | da verificare | |
| 1025 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 1026 | Parte G — Equità e impatto distributivo | — | dati | da verificare | |
| 1027 | Parte H — Profili etico, giuridico e organizzativo | — | dati | da verificare | |
| 1028 | Parte H — Profili etico, giuridico e organizzativo | Tabella H.1. I profili giuridici del servizio nella Valle d’Aosta. | dati | da verificare | |
| 1029 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 1030 | Parte I — Attuazione, fattibilità e sostenibilità | Tabella I.1. I cinque casi della decisione di investimento pubblico. | dati | da verificare | |
| 1031 | Parte I — Attuazione, fattibilità e sostenibilità | — | dati | da verificare | |
| 1032 | Parte L — Monitoraggio e valutazione ex post | — | dati | da verificare | |
| 1033 | Parte L — Monitoraggio e valutazione ex post | Tabella L.1. Le sette categorie della batteria di indicatori. | dati | da verificare | |
| 1034 | Parte M — Sintesi multidimensionale e raccomandazioni | — | dati | da verificare | |
| 1035 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.1. La sintesi dei domini della valutazione. | dati | da verificare | |
| 1036 | Parte M — Sintesi multidimensionale e raccomandazioni | Tabella M.2. L’analisi multi-criterio: punteggi dell’intervento e del non intervento. | dati | da verificare | |
| 1037 | Appendice A — Caso di riferimento e parametri | — | dati | da verificare | |
| 1038 | Appendice A — Caso di riferimento e parametri | Tabella A.1. Il caso di riferimento comune a tutte le valutazioni regionali. | dati | da verificare | |
| 1039 | Appendice A — Caso di riferimento e parametri | Tabella A.2. I parametri del modello di Markov e le distribuzioni assegnate per l’analisi  | dati | da verificare | |
| 1040 | Appendice B — Strumenti di esito e dataset minimo | Tabella A.3. Il quadro economico consolidato per scenario (costo per incarico di riferimen | dati | da verificare | |
| 1041 | Appendice B — Strumenti di esito e dataset minimo | Tabella B.1. Gli strumenti di esito e le misure derivate, impiegati nei soli punteggi comp | dati | da verificare | |
| 1042 | Appendice C — Dati regionali e fonti | Tabella B.2. Il dataset minimo: i campi del protocollo di rilevazione (dizionario dei dati | dati | da verificare | |
| 1043 | Appendice C — Dati regionali e fonti | Tabella C.1. I valori di ancoraggio della Valle d’Aosta. | dati | da verificare | |
| 1044 | Appendice D — Checklist di reporting | Tabella C.2. I dati certificati da acquisire per sostituire le stime (lacuna principale de | dati | da verificare | |
| 1045 | Appendice E — Glossario | Tabella D.1. Gli standard di reporting e di qualità adottati nello studio, per parte di ap | dati | da verificare | |
| 1046 | Appendice E — Glossario | — | dati | da verificare | |
| 1047 | Appendice E — Glossario | — | dati | da verificare | |
| 1048 | Appendice E — Glossario | — | dati | da verificare | |
| 1049 | Appendice E — Glossario | — | dati | da verificare | |
| 1050 | Appendice E — Glossario | — | dati | da verificare | |
| 1051 | Appendice E — Glossario | — | dati | da verificare | |
| 1052 | Appendice E — Glossario | — | dati | da verificare | |
| 1053 | Appendice E — Glossario | — | dati | da verificare | |
| 1054 | Appendice E — Glossario | — | dati | da verificare | |
| 1055 | Appendice E — Glossario | — | dati | da verificare | |
