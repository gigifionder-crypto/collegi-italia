# Anomalie del corpus — registro fattuale

Questo file registra difetti o incoerenze rilevate nel corpo integrale
durante il lavoro di ristrutturazione, **senza deciderne il trattamento**.
Nessuna correzione viene applicata al testo finché l'autore non decide come
procedere. Si veda anche `_meta/status-tracker.md` per lo stato generale.

## 1. Duplicazione non dichiarata di Parte I e Parte II (Tomo I)

**Rilevata:** 2026-07-06, durante la pianificazione dell'inserimento di
riassunto + key messages per parte (Livello 5).

**Descrizione:** `tomo-1-puglia/opera-integrale-puglia.docx` contiene due
versioni distinte sia di Parte I sia di Parte II, senza che questa
duplicazione sia dichiarata nell'"Avvertenza di edizione" del volume (che
pure documenta minuziosamente altre scelte editoriali: stato della Parte
VI, integrazione differita di Parte XIV/XV, ondate di integrazione delle
appendici, esclusioni motivate di materiale estraneo).

**Versione breve** (paragrafi contati nello stato del file al 2026-07-06,
dopo l'inserimento del "Come leggere questo Tomo"):
- Paragrafi 46–96: "Premessa"/"Introduzione" + Heading 1 "Parte I —
  Fondamento giuridico-istituzionale e razionale scientifico", articolata
  in sottosezioni 1.1–1.11 (oggetto dell'intervento normativo, crisi
  epidemiologica, determinanti socioeconomici, paradosso dell'offerta,
  evidenze internazionali, Collaborative Care Model, prevenzione,
  dimensione economica, modello organizzativo, monitoraggio,
  conclusioni). Corrisponde quasi verbatim al contenuto della bozza a 4
  capitoli superata, archiviata in
  `_meta/materiale-per-derivati-futuri/bozza-4-capitoli-puglia_IT.docx`
  (e nella sua versione inglese `..._EN.docx`).
- Paragrafi 97–148: Heading 1 "Parte II — Quadro di contesto: bisogni,
  criticità e razionale della riforma", articolata in sottosezioni
  2.1–2.5 (transizione demografica, burden epidemiologico, determinanti
  socioeconomici, sistema sanitario regionale, sintesi del razionale).

**Versione ricca** (già trattata come "la vera Parte I/II" nel Livello 4
— Sintesi Tecnica — e nella tabella delle 15 parti di
`_meta/status-tracker.md`):
- Paragrafi 151–196: "Revisione metodologica di governo — Il passaggio
  all'ancoraggio OCSE 2026" (numerata internamente IV.1–IV.6).
- Paragrafi 197–317: una seconda "Parte I", preceduta solo da un banner
  decorativo in stile Body Text ("Parte I" / "Quadro, mandato, metodo e
  perimetro integrale"), senza una propria intestazione di Livello 1.
  Sottosezioni 1.1–1.9: scopo/mandato/quesito di valutazione, perimetro
  integrale e principio ordinatore della cascata, telaio metodologico
  ibrido (quattro cornici apicali), metodologie innestate per la
  rinegoziazione, tassonomia costi/benefici e regola di non duplicazione,
  batteria integrale di indicatori, graduazione GRADE, posizionamento
  dell'IA e della formazione, fonti/limiti/agenda di verifica.
- Paragrafi 318–423: una seconda "Parte II", stesso pattern (banner
  decorativo, nessuna intestazione di Livello 1 propria). Sottosezioni
  2.1–2.6: epidemiologia e divario di trattamento, contesto
  demografico-sociale-economico, sistema sanitario regionale, quadro
  finanziario, mappa del carico multidominio, quadro normativo.
- Paragrafo 484: Heading 1 "Parte III —", da cui in poi non è stata
  riscontrata alcuna duplicazione analoga.

**Ipotesi di lavoro (non confermata dall'autore):** la versione breve
sembra un residuo della bozza a 4 capitoli, rimasto nel documento durante
una fusione con la versione consolidata a 15 parti, senza essere
rimosso né segnalato nell'Avvertenza di edizione.

**Trattamento — RISOLTO il 2026-07-06 (Fase 3, passata sulla struttura):**
su decisione dell'autore, la versione breve è stata rimossa dal corpo del
Tomo I. Operazione eseguita tramite manipolazione diretta dell'XML:
estratti e rimossi 110 elementi (105 paragrafi, 5 tabelle) corrispondenti
a "Premessa"/"Introduzione" del capitolo legacy e alle sezioni brevi di
Parte I e Parte II, insieme alle 27 definizioni di note a piè di pagina
(id 1–27) usate esclusivamente al loro interno (verificato che nessuna di
queste note fosse richiamata altrove nel documento prima della rimozione).
Verificato dopo la rimozione: 11.215 → 11.110 paragrafi, 1.060 → 1.055
tabelle, 3.942 → 3.915 note, zero note orfane o mancanti, zero errori di
accesso alle tabelle, contenuto della versione ricca di Parte I e Parte II
confermato intatto.

Il file precedente la rimozione è conservato integralmente in
`tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_pre-rimozione-parte-I-II-breve.docx`
(la versione breve rimossa corrisponde ai paragrafi 46–150 di quel file).

Contestualmente sono state aggiornate le due voci d'indice che
dichiaravano ancora Parte XIV e XV "da integrare al conferimento del file
definitivo" (superate dall'integrazione già eseguita il 2026-07-06),
sostituendo il testo con "(integrata il 2026-07-06)".
