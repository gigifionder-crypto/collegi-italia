# Registro delle impronte SHA-256

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file porta qui la propria impronta crittografica. Chi ne riceve uno può
accertare in un comando che è **bit per bit** quello depositato, e non una copia
alterata, troncata o rimontata.

**Stato al commit `e71d4fb9c43f`** del ramo `claude/amnistiati-tribunale-speciale-a82lzn`.

---

## Tre lavori, non uno

Il repository ospita **tre opere distinte**, e vanno tenute separate anche qui.
Il corpus lo dichiara già per conto proprio: `INDICE-DOCUMENTI-BRANCH.md` scrive
alla terza riga che i documenti del caso Moro sono «estranei al progetto
principale del repository (Studio Integrale Puglia)».

| | file | byte |
|---|---:|---:|
| **L'opera — il caso Moro** | 187 | 85.885.296 |
| Terza opera — Italia Nera | 48 | 15.765.807 |
| Altro lavoro — Studio Integrale Puglia | 78 | 156.820.907 |
| **Totale nel repository** | 313 | 258.472.010 |

Le impronte valgono per tutte e tre, perché tutte e tre stanno nel repository e
chiunque le riceva ha diritto di verificarle. **L'attribuzione no**: contarle
insieme sotto un'unica intestazione sarebbe un errore di descrizione, e in
un'opera che misura la distanza fra un fatto e la sua attribuzione sarebbe
l'errore peggiore da commettere.

*Annotazione — La prima stesura di questo registro, del 27 agosto 2026,
presentava i 209 file come se fossero un'opera sola. La cifra era esatta, la
descrizione no. L'errore è corretto qui e annotato, non cancellato: le impronte
di allora restano valide, l'intestazione che le raccoglieva era sbagliata.*

*Seconda annotazione, stessa data — La correzione parlava di **due** lavori. Con
l'archiviazione di Italia Nera i lavori sono diventati **tre**, e questa
intestazione è stata estesa di conseguenza. Non è una smentita della prima
annotazione: è lo stesso criterio applicato a un perimetro che si è allargato.
Il legame fra Italia Nera e l'opera su Moro è dichiarato dalla parte
moroteana — «Questa opera nasce dal Registro V77 e ne è la seconda figlia» — ed
è **genealogico, non testuale**: misurato agli 8-grammi, l'opera seconda sui
cinquantacinque giorni sta dentro il V77 per lo **0,5 per cento**, e il V77 tocca
l'intero corpus moroteano per lo **0,77**. Una parentela non è un'appartenenza,
e qui la differenza si conta.*

---

## L'impronta dell'opera

Una stringa sola per il caso Moro. È l'impronta del manifesto dell'opera, cioè
del file che elenca i 173 file versionati che le appartengono:

```
c809d4b60787459b6e29925d22bc6f2dac7e5465888c8a9aa4c1f3cf906004f6
```

Riproducibile da chiunque, in un comando:

```
sha256sum IMPRONTE-OPERA-MORO.txt
```

## L'impronta della terza opera

La stessa cosa per Italia Nera e i suoi 48 file:

```
673bbc44befed5cd04a0940a9f39981a0707ae8500e6aec9829bf54c635c7641
```

```
sha256sum IMPRONTE-ITALIA-NERA.txt
```

## L'impronta dell'insieme versionato

La stessa cosa per tutti i 299 file versionati del repository, le tre
opere insieme:

```
b5daaae81c002866fe39f4b776ff456c9882bbd5a12699efab9fc98d02772216
```

```
sha256sum IMPRONTE-SHA256.txt
```

Se una di queste stringhe coincide, **l'insieme che copre è quello depositato**:
non un file di meno, non un file di più, nessun file diverso. Se differisce, il
confronto riga per riga dice quale.

### I file che restano fuori, e perché

I manifesti elencano ogni file versionato **tranne i manifesti stessi e questo
registro**. Non è una svista, ed è l'unica esclusione. Un registro non può
certificare sé stesso: i suoi file cambiano a ogni rigenerazione, e l'impronta
che vi si scrivesse dentro sarebbe falsa nell'istante in cui viene scritta. La
catena si chiude comunque, e senza circoli: i file sono certificati dal
manifesto, il manifesto è certificato dalla stringa qui sopra, e questo registro
non ha bisogno di esserlo perché **è interamente ricavabile dal manifesto** —
chi vuole controllarlo lo rigenera.

---

## Come si verifica

Tutti i file versionati in un colpo solo, dalla radice del repository:

```
sha256sum --check IMPRONTE-SHA256.txt       # le tre opere
sha256sum --check IMPRONTE-OPERA-MORO.txt   # il solo caso Moro
sha256sum --check IMPRONTE-ITALIA-NERA.txt  # la sola Italia Nera
```

Un file solo, dalla cartella che lo contiene:

```
sha256sum UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf     # Linux
shasum -a 256 UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf # macOS
```

Su Windows, da PowerShell:

```
Get-FileHash UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf -Algorithm SHA256
```

La stringa che compare va confrontata con quella di questo registro. Se coincide,
il file è integro. Se differisce anche per un solo carattere, **non è lo stesso
file**: non va letto come se lo fosse, e va richiesta una copia nuova.

---

## Che cosa l'impronta certifica, e che cosa no

Va detto con precisione, perché è esattamente il genere di distinzione su cui
quest'opera è costruita.

**L'impronta certifica** che il file ricevuto è identico a quello depositato. È una
garanzia sull'**integrità del supporto**: nessuno ha cambiato una cifra, tolto una
pagina, sostituito un allegato.

**L'impronta non certifica** che ciò che il file contiene sia vero. Un documento
falso conserva la propria impronta con la stessa fedeltà di un documento esatto.
L'integrità è una proprietà del contenitore, non del contenuto.

Chi riceve quest'opera deve poter fare due cose distinte: **accertare** di averla
ricevuta integra — e a questo serve il registro — e **verificare** ciò che afferma,
che è invece il lavoro reso possibile dai gradi dichiarati, dalle sedi d'archivio
nominate e dagli Stati Zero. La prima cosa è meccanica. La seconda no.

---

## Il sommario

| Sezione | File | Byte |
|---|---:|---:|
| I volumi rilegati | 28 | 73.696.818 |
| I documenti del corpus | 42 | 6.343.789 |
| Il Libro dodicesimo e i suoi originali | 40 | 1.971.469 |
| Le appendici alla Fase settima | 11 | 208.311 |
| Le verifiche e i generatori | 22 | 313.920 |
| Il dossier di invio dell'opera | 30 | 1.442.427 |
| Terza opera — Italia Nera | 48 | 15.765.807 |
| Altro lavoro — la radice | 2 | 1.951 |
| Altro lavoro — apparato e modelli | 28 | 1.490.636 |
| Altro lavoro — diffusione | 5 | 22.024 |
| Altro lavoro — pubblicazione finale | 13 | 123.536.718 |
| Altro lavoro — livelli della piramide | 8 | 54.505 |
| Altro lavoro — paper accademico | 7 | 396.324 |
| Altro lavoro — Tomo I, Puglia | 8 | 27.135.817 |
| Altro lavoro — Tomo II, nazionale | 5 | 3.833.161 |
| Altro lavoro — estensione ai ventisette | 2 | 349.771 |
| Gli archivi dell'opera intera | 1 | 51.930.357 |
| Il volume diviso in tre parti | 3 | 29.956.554 |
| Il pacchetto dei grafici | 14 | 1.908.562 |
| **Totale** | **313** | **258.472.010** |

---

## Le impronte, sezione per sezione

### I volumi rilegati

*Le edizioni tipografiche in DOCX e PDF: è la forma in cui l'opera viaggia fuori dal repository.*

28 file · 73.696.818 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `ALDO_MORO_FASE_DECIMA_IL_PRINCIPIO_PERSONALISTICO.docx` | 30.037 | `c9ca9e95ccd2c0f67985fa9a1598d38ac63e9216ded764d48d18d69f9f17633a` |
| `ALDO_MORO_FASE_DECIMA_IL_PRINCIPIO_PERSONALISTICO.pdf` | 350.729 | `c972b0f5c8f02e5ad1f7adbd786ab9c23c7c1c5e1db365d6ef7e9401cacc1758` |
| `ALDO_MORO_MINISTRO_DEGLI_ESTERI_LA_DIMENSIONE_DIPLOMATICA.docx` | 206.178 | `0f348422e47e31bdcd621a3a2e719afaeadc01c734a6e866b001ca135411d9d3` |
| `ALDO_MORO_MINISTRO_DEGLI_ESTERI_LA_DIMENSIONE_DIPLOMATICA.pdf` | 1.738.517 | `e52c6ad84119c77a8f36cb644a7b8338e493bbc94885b3cd4a6ca5c314299c5b` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_EDIZIONE_STRUTTURATA.docx` | 21.678 | `a25584e4066f1938b0f1c021174047ec57c3465f0a044e65401d35b7f49232c8` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_EDIZIONE_STRUTTURATA.pdf` | 262.132 | `032bd96ccbeb36508c79c6bbcbd05dcaa123cee03f907de6aed8df26201625cc` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_OPERA_COMPLETA.docx` | 67.875 | `d0e715905a8fd6732e31233debb1998c79f118646237ba2a124411756c51051c` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_OPERA_COMPLETA.pdf` | 836.587 | `3269bebfd8ce10818ed8eefa25a174b7506ff9c6ad0d738c6a391830cc6ab394` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_TRE_CONTINUAZIONI.docx` | 32.042 | `e17e23e3f865f5d601eba4503c7a3b1a18accb8c7489d3145275bca6f2828ede` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_TRE_CONTINUAZIONI.pdf` | 375.353 | `42a8c1756b93f98531408b30b85ecbf29b6780e23ec110776f6df185a004fb43` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_TRE_NUOVE_FASI.docx` | 31.049 | `a4a1356ca7e149b1e553535ed6e83733963ba5d688f54cfade6c158ae40a1d6f` |
| `ALDO_MORO_UNA_GUERRA_SENZA_FINE_TRE_NUOVE_FASI.pdf` | 377.996 | `ec222a698991f59844a1bc0ca30a52a97634655868ddfb7b902a7d6cd03675d8` |
| `GUEVARA_LA_PARABOLA_INTEGRALE_1928-1967.docx` | 59.643 | `27db60da108942005989cb0c2416eaf2c93cb798b20179ab2c45d5a94bc0552f` |
| `GUEVARA_LA_PARABOLA_INTEGRALE_1928-1967.pdf` | 655.812 | `6570a4fac4da79b809bacfd709035df2a87427f4d19a2c44082b7eb2060f6f49` |
| `IL_CODICE_E_LA_SUA_TRASMISSIONE_KISSINGER_MILLE_BLOCCHI.docx` | 965.238 | `07dde8c9fd03a04b4b67243f9102e5ce7542f4b32b52e85dddb44885c542f866` |
| `IL_CODICE_E_LA_SUA_TRASMISSIONE_KISSINGER_MILLE_BLOCCHI.pdf` | 8.323.305 | `379f71c8c74c3d340cd95c3eea23260d65c278848f81d0385322ad73008d8783` |
| `IL_DITTICO_DELLA_RICERCA_AGENDA_E_NOVE_CANTIERI.docx` | 197.214 | `ce39c66353b2326e09d84d0c2c8e2adcd00016728d7e81bcd6a09415a3ec3509` |
| `IL_DITTICO_DELLA_RICERCA_AGENDA_E_NOVE_CANTIERI.pdf` | 1.871.603 | `062bfc31d52b7fe68d4a9a9468af06257755f9bc00f66adfdb2b5da62afbf51c` |
| `IL_FASCICOLO_APERTO_PROGRAMMA_INVESTIGATIVO.docx` | 94.992 | `a34c4259bc64a1e1ba03bb4287fed803fd6ab29f878dabbce8224cc992e6961d` |
| `IL_FASCICOLO_APERTO_PROGRAMMA_INVESTIGATIVO.pdf` | 1.081.294 | `cd08b669d09da1dc003496cf501297c2bdc7ff19c413806d1a0f03d7747b1900` |
| `IL_MERIDIANO_E_LA_VALLE_DAL_SUD_AFRICA_ALLA_PAYPAL_MAFIA.docx` | 211.128 | `b74d9251d91aea4de058c6e79f585795a3008327748e980b53d9a0a5315a2349` |
| `IL_MERIDIANO_E_LA_VALLE_DAL_SUD_AFRICA_ALLA_PAYPAL_MAFIA.pdf` | 1.803.878 | `7b3e43494a9a64d37f210aa964b95bee14fd49f1df617ae7eb5563936e5d71f6` |
| `IL_VETTORE_E_IL_TRIBUNALE_DUE_STUDI_1926-1972.docx` | 50.739 | `7bf4f729fb443bef58d1e7f1d60094fd010cbc7fd45a99118047f23c2e049592` |
| `IL_VETTORE_E_IL_TRIBUNALE_DUE_STUDI_1926-1972.pdf` | 648.595 | `63606ed164cebd9454392b0ec6f2af788a6d0776b894f5873bae8ebe688ce2a4` |
| `LA_TERZA_STRADA_CEPPO_SIMIONI_E_NODO_HYPERION.docx` | 25.456 | `4199b465ec9407fb01dd50ca776e42b5afa142c51043f9cde977bd3065ec252d` |
| `LA_TERZA_STRADA_CEPPO_SIMIONI_E_NODO_HYPERION.pdf` | 333.155 | `1769f46f2b618bb79c32bd889c13ae91d3c8ed466d263b9f6d5f07b9ed2c865e` |
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.docx` | 13.683.355 | `fbddbb1d96eb72f017f48fd18920998a25ee3bbe592598636b27dc8dba4b872e` |
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf` | 39.361.238 | `b4b2e8b86e37fcbd9f929f3a5fc72104b2a346c12af91ecd19b80c48c2382b75` |

### I documenti del corpus

*Le sorgenti in markdown del Portale, dei quattordici Libri e delle tre Appendici, con gli indici e gli apparati.*

42 file · 6.343.789 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `GUIDA-ALLA-LETTURA.md` | 22.661 | `186c9d92a2d6e5cc853e3a7a25b5fff30ec3b9b202fb8470eaac706b7cd3e4cb` |
| `INDICE-DOCUMENTI-BRANCH.md` | 75.006 | `5dc2f01bc4e2e35e1bc8d9ed8d07ae3d93a16429d9ab68c18a1069ab1d2dc22f` |
| `agenda-di-ricerca-del-nuovo-caso-moro.md` | 120.075 | `f2dffd0bc5202005bc5e625cbafc730092250d116866a7d59f8ec34a561f038c` |
| `aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md` | 11.181 | `c96e44cc8867fa970e270f23f88e036e6d134dc8eedec25227a17fe1c5f7dff0` |
| `aldo-moro-una-guerra-senza-fine-edizione-strutturata.md` | 27.726 | `22b7c8c0454d2f9c591190237e7741d2c84b1d0992f64b5e9d08a07ec7f4e92d` |
| `aldo-moro-una-guerra-senza-fine-fase-decima-responsabilita-personali.md` | 17.129 | `659d07fc1f0ba928bf579b9a8d8d7db370940cbd69370c23f0e5b78b91495fb0` |
| `aldo-moro-una-guerra-senza-fine-fase-nona-repertorio-del-caso.md` | 12.603 | `5dc7a368c9f411ad23e3b88e80239e838e243c6f81edd23178c0ce4451fbe04b` |
| `aldo-moro-una-guerra-senza-fine-fase-ottava-il-ritratto.md` | 13.659 | `5d39082b1e771d987dba189a9d8d326ea8916aae161771a186dac7ea6b676e7f` |
| `aldo-moro-una-guerra-senza-fine-fase-sesta.md` | 14.016 | `537f9606cfac6ce3d986ee9d7c70575f5889a015ae83f303f5a43192342b1a7d` |
| `aldo-moro-una-guerra-senza-fine-fase-settima-registro-giudiziario.md` | 15.786 | `b71ca9a74581ee3983241cd4f198bad918de6d234cfc2900644217fdc28e169c` |
| `aldo-moro-una-guerra-senza-fine-parte-terza.md` | 22.680 | `d84e43507c52cc4bf437edba1c8bb929c691ce947e9eadcf8de90bf56602e404` |
| `amnistiati-tribunale-speciale.md` | 16.867 | `615b786c3c69531309e27f411ca0133b7b240d656c000c42f29db53bc769cc54` |
| `approfondimento-piste-di-testa.md` | 13.898 | `24b36a4157f3004c05627faa3505302d69ab18e7199d2ae3f4de52ed1233dcc5` |
| `approfondimento-piste-entita.md` | 39.929 | `c0361b319b26fd26032343e94fb19788947ec4ad69308f1eb3e760962af89920` |
| `ceppo-simioni-cpm-superclan-hyperion.md` | 17.694 | `0398f0454e442ff23d17de1c1114c348db1b77f187249b7d7c5f2b9f0001c12a` |
| `compose-registro-docx.js` | 11.453 | `83e7cbbe413e1c3bf43a0fda893b70e6fb6fe7aaef8111658cc840b6824a6c68` |
| `cronologia-guevara-moro.html` | 20.210 | `bd34a9e82a042eb76bd638760e398fe068d42ec6efa5a72c26ef6a3e2422449f` |
| `dal-che-a-moro-una-guerra-senza-fine.md` | 12.559 | `7002fa51ab9305064f15cd897f6a26939f6326b13982a55aaf1276a0566cfc86` |
| `dossier-maggiore-una-pace-senza-pace.md` | 1.763.081 | `2177521a5a6f75fb3ce502302f3d71e85102c0afc36a26ac657eae4d7bef9a27` |
| `feltrinelli-il-vettore.md` | 17.727 | `4a6b62e4bf10b8e6e0696437161477aefebb593ede84711a1abbc0396ce6f19c` |
| `guevara-bibliografia-critica.md` | 8.719 | `b5fc07fda2e608125afe17688fb3c637d21f3ccf35845cd27d39d0ab7572d728` |
| `guevara-campagna-boliviana-1966-1967.md` | 9.574 | `7a18a932059be8343922546d3361b657a3e11af1a1a35abe766bee03c7e54e9a` |
| `guevara-messico-avana-1954-1965.md` | 25.592 | `af2e8e286594987c608089e6aa37ee004f7d15969881b2e0f0b4892535ec99dc` |
| `guevara-mosca-bolivia-1964-1966.md` | 24.335 | `4af4bedb4f5301b2b76d48e43935da180a675b2fa833ef8ba7cbc7c1a42d8915` |
| `guevara-origini-esilio-messicano.md` | 15.412 | `1f8b7ffe6332b5af886abeba3544db4b61d3fcc24e0b9c829689d356317fff40` |
| `il-meridiano-e-la-valle-mille-blocchi.md` | 504.370 | `be9db6e69e75392773ed90cec74924d29279a5a067897215cc4152ea9d8ef261` |
| `il-registro-dei-cinquantacinque-giorni-opera-seconda.md` | 307.967 | `7ebd954f67c0c8a51aa6adf981acd690c8537aedd15cf6fecec6262d0a287c27` |
| `kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md` | 2.400.306 | `754eea844fde0a471f13b549805f85814c2fd507dc1a7a84f2769af06ec5beaa` |
| `le-pene-oltre-confine-mitterrand-mulinaris.md` | 12.314 | `620e2299da71f18efc52bc13f7f4743211f1709a523c843eb1bf37fbfd5b8138` |
| `manuale-investigativo-nuovo-caso-moro.md` | 104.736 | `8669efe737f67785354604348850f5843185efbbc266a5cb2ce124ea8004a74b` |
| `metodologie-del-dossier-sinaptogenesi-e-strumenti.md` | 15.749 | `2b6f198ec9cf61b850bcf1aa392f7c65e61d4b5c6df8bf7a90305797cda54cf9` |
| `note-bibliografiche-opera-integrale.md` | 143.719 | `387c238a9a392c6e22e767884f272798b30ac7364042425ca8bb0765e54fab2c` |
| `nove-cantieri-mille-blocchi.md` | 357.586 | `c6c38d83a5adb41abf45a4a4c6973574ba521214a2c867da7302b4a63859d0db` |
| `programma-investigativo-caso-moro.md` | 25.994 | `043bd0a175892bf4a874add1d28078b1e3d1dccafc2d7101dd5886cbcfd8cfc0` |
| `relazione-stato-lavori-stile-moro.md` | 6.543 | `dd5bbf37ef9ba2b6f5bbe084395b1c68e9804cdb2ffc2250d6c3ac3f2d5982a5` |
| `triangolazione-condannati-corpus.md` | 22.340 | `cbdc3593873d7acae3289e12d7e5a44ae93768514e40d93c3229b2f253b70cd7` |
| `triangolazione-feltrinelli-corpus.md` | 13.744 | `a4f5354f9bba0934600a590ac83f63a9f8048f458e1958e75c8df016ee126870` |
| `triangolazione-feltrinelli-hyperion.md` | 9.234 | `51ba5dc410fefa7d1ed6194f331ba86a1231154dd7288c04593dad63982185d7` |
| `triangolazione-hyperion-corpus.md` | 12.067 | `59d1c735892d6bcdd40fb1924d99cb1947921d8ccc048ecb9f96b1e237c4c6c6` |
| `triangolazioni-guevara-moro.md` | 30.965 | `7025c1d58d4c1ed833ebb94e65921cb9608b7e18019ffa888a2632aa608c231e` |
| `tribunale-speciale-approfondimento-sottonodi.md` | 10.911 | `a4b9012a0120e40d7c8a155e7d8f30a4cce7767efa0033189704b2371f65ed45` |
| `tribunale-speciale-storia-istituzione.md` | 15.672 | `2900e103611d64ea162ff50926d599ac39f7ed8a59e0e96db5ad5c650082de9f` |

### Il Libro dodicesimo e i suoi originali

*La dimensione diplomatica: le ricognizioni Farnesina per esteso, i documenti State Dept, l'edizione HTML navigabile.*

40 file · 1.971.469 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `moro-ministro-esteri/README.md` | 13.804 | `3b5ec3d05cbc6ee2d1cf5973f451e818cd6f909f9fc6ab98ec526c5da51e4612` |
| `moro-ministro-esteri/documenti-state-dept-1965-1978.md` | 12.945 | `8ea018f4e65e4434124234b7f0d908ed00a93dda0a0de2990cd99d058a9444cf` |
| `moro-ministro-esteri/manifest-sha256.txt` | 2.073 | `54f976389d8a0d7437f863c68e65930ba531f9bc2d3c1d4b10b1ec9ac2f7ab94` |
| `moro-ministro-esteri/originali/documenti-italiani-spagnoli-opus-dei.md` | 48.039 | `668bbcd1171ca8d6b90a0a76c2f3d893c074f2919c19395776a166ce50c34f7f` |
| `moro-ministro-esteri/originali/germania-opus-dei-1952-1985.md` | 47.083 | `6dd0b6a431215a847d37b2db6529554355a57fe8be22edb0a03b8386ea227d9b` |
| `moro-ministro-esteri/originali/grecia-opus-dei-1969-1985.md` | 45.718 | `e43654b066a3ffad797d71f5f84540a6a6e00abfdd6fbe69d9139d4abcef59a6` |
| `moro-ministro-esteri/originali/portogallo-opus-dei.md` | 37.154 | `2af68c5242acc647f72148597db2ccb71602c27066718944b91c75ff14cf338f` |
| `moro-ministro-esteri/originali/portogallo-santa-sede-1969-1974.md` | 47.743 | `48e9e5330446704cdfb9606550fdebad2752a119377f22076056cc08b67ba1a8` |
| `moro-ministro-esteri/originali/ricognizione-ministro-esteri-1969-1974.md` | 38.079 | `85d55144e94e4162dc4680ccd62671acf4edfe9eae560613d3e64d6b72b09ebe` |
| `moro-ministro-esteri/originali/santa-sede-due-germanie-oder-neisse.md` | 48.519 | `8d591016ecb21aeedfbee9fd2e5e9a9fddab3d1799399d14fc6dc6e80df51c2c` |
| `moro-ministro-esteri/originali/santa-sede-turchia-attentato-giovanni-paolo-ii.md` | 60.680 | `34d0282d67a63ae55782041243b22fefa62d1f1880b15824117a20bce5f9f91e` |
| `moro-ministro-esteri/originali/state-dept-djvu-ocr-grezzo.txt` | 42.102 | `4b2b96941be39250a044c0bec7401798327076984673f1758a1d1f94aa8af880` |
| `moro-ministro-esteri/originali/turchia-opus-dei-1969-1975.md` | 71.356 | `6bc630be9d7a17121933d0f7806f67acacc6b6ed576da725da00a322c5ae68c8` |
| `moro-ministro-esteri/terza-campagna/decima-ricognizione-revisione-del-modello.md` | 40.197 | `a103ded453c518d2d8beeafc3b27c3f81ccdfeea06c84066eafcdb34251219e1` |
| `moro-ministro-esteri/terza-campagna/diciassettesima-ricognizione-santa-sede-e-sudafrica.md` | 33.418 | `1cf555f2a90ed9da5a1912ca23ba5d247e23d9f93d369630da76d8c410fc90e5` |
| `moro-ministro-esteri/terza-campagna/diciottesima-ricognizione-nazioni-unite-ed-embargo.md` | 30.345 | `5b0d62ec5375e0a4190ac69278fbe9b11d8c79703c0939b65f008ae72fba11c5` |
| `moro-ministro-esteri/terza-campagna/dodicesima-ricognizione-sette-casi-extraeuropei.md` | 38.874 | `473f8c9d5e73b9575f3bf8ff6c9659457a6581e078ca80b1d14e92b94fd0f13a` |
| `moro-ministro-esteri/terza-campagna/nona-ricognizione-la-sequenza-oder-neisse.md` | 45.596 | `5654b8478eb359a02a977a3b147ba6cc9abcac56d6ebf618c8dd472b80e11b3a` |
| `moro-ministro-esteri/terza-campagna/ottava-ricognizione-mediterraneo-orientale.md` | 47.105 | `8495e7d65107b3d8e8049a22b8bb7a79892f9f42f39f5da9847311497f138c9e` |
| `moro-ministro-esteri/terza-campagna/quarta-ricognizione-portogallo-santa-sede.md` | 41.594 | `95fe1e8f33aa49e448f9ecdf867c64da87f798c13106b763d98b4ef322f0a2cd` |
| `moro-ministro-esteri/terza-campagna/quarto-registro-la-scala-degli-stati-zero.md` | 23.510 | `c6b3ee0a35ea0fd3fc78cd1c2773fe2221b5a2e06602f24af006a4b55aa6222e` |
| `moro-ministro-esteri/terza-campagna/quattordicesima-ricognizione-la-calibrazione-libica.md` | 33.641 | `5f98f9ab452295f0c7a87754b32957777aab542d83d1bd855be593bb50b4be82` |
| `moro-ministro-esteri/terza-campagna/quindicesima-ricognizione-aermacchi-e-il-sudafrica.md` | 38.275 | `5f67dfaba736a51b5d8304372f8fab495bd2313d639f3bfd93f53ca06368289c` |
| `moro-ministro-esteri/terza-campagna/quinta-ricognizione-portogallo-le-sei-lacune.md` | 37.309 | `b3100a82499e6c88522ef7bade270019f8886c0ee2c30386107a72531ebeb334` |
| `moro-ministro-esteri/terza-campagna/quinto-registro-la-tavola-unica.md` | 19.242 | `e2ffa74cfe361bbfd2342c5ac9d7b57bd328b4792f377938170fd7b325b5fb32` |
| `moro-ministro-esteri/terza-campagna/registro-dei-nodi-e-dei-ponti-teatro-australe.md` | 41.962 | `0f8fc212e6d0f4c5a6e65ec249217116efa0fc06a2ee6ead0011fc5698c19fac` |
| `moro-ministro-esteri/terza-campagna/registro-delle-undici-ricognizioni.md` | 43.030 | `8466ac5e851da1871b7b49143381b83da22313211e61ce2c0f577941713bb961` |
| `moro-ministro-esteri/terza-campagna/secondo-registro-dei-nodi-e-dei-ponti.md` | 33.746 | `5a7e9164ba56572e451653d2b5a3e29ba649179f8d5fc9200b4c1c9eac6874c6` |
| `moro-ministro-esteri/terza-campagna/sedicesima-ricognizione-il-dossier-namibiano.md` | 37.906 | `910fa109a8daab06fa2057bdd90a852009130ced6ec4aa719f439dc365767405` |
| `moro-ministro-esteri/terza-campagna/sesta-ricognizione-il-ribaltamento-iberico.md` | 35.237 | `29895f4e7d3c63857346745dadb532c7eeec862a368cd9896e28e33381ed5350` |
| `moro-ministro-esteri/terza-campagna/sesto-registro-strumenti-e-volume.md` | 20.459 | `b4963a71b4c934cee55d8d106eb91f179592b8c835f623e991e5c9b074242c93` |
| `moro-ministro-esteri/terza-campagna/settima-ricognizione-turchia-e-attentato.md` | 42.877 | `7f9119b0f4bcfc403f1eeaf6b5d395f735603ee9c9691136edc7cb3aedd28bf0` |
| `moro-ministro-esteri/terza-campagna/settimo-registro-la-riqualificazione.md` | 15.505 | `e108444a56fd0911182dfdd62b03eea24619e43c41914c986904333d02e06b92` |
| `moro-ministro-esteri/terza-campagna/terza-ricognizione-spagna-opus-dei.md` | 38.824 | `1ce17c9ccba4a1802390f696455ca0b1f349a23e3eefacb0ab999788b473d47f` |
| `moro-ministro-esteri/terza-campagna/terzo-registro-dei-nodi-e-dei-ponti.md` | 29.452 | `c92c350c0f514f180cbf79bd1fd2565c71565c3877cbe87d45ae8698398dae60` |
| `moro-ministro-esteri/terza-campagna/tredicesima-ricognizione-aginter-i-due-silenzi.md` | 36.824 | `c166fd917cfb7844d39914922771ae0e9229cfe24f2b0754fa4322282c10a649` |
| `moro-ministro-esteri/terza-campagna/undicesima-ricognizione-strauss-e-aginter.md` | 38.494 | `5b10cc5c454099a016517061a82bd709989327f910fe7e8bc60e7ce789210ec2` |
| `moro-ministro-esteri/triangolazione-seconda-campagna.md` | 39.418 | `574b3a22479712cd9288b97ba5e2d76daa98ee5380cda9411917547f23cd5864` |
| `moro-ministro-esteri/triangolazione-terza-campagna.md` | 13.000 | `d3734a34a68434390e30e546ebba2c523b203b89a5011c332d5466e1d49af515` |
| `moro-ministro-esteri/volume.html` | 560.334 | `aef519447a3d02869ee9ee70dce6c61bce7a73577bf3cfbc282b57f9cadaf96f` |

### Le appendici alla Fase settima

*Le undici appendici al Libro nono, dalla quinta alla quindicesima: la serie chiusa.*

11 file · 208.311 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `appendici-fase-settima/appendice-decima-fase-settima.md` | 16.189 | `1da9c618af41cee71b16c4fedf092395e240f9993a7f7514e8cde72074de6df5` |
| `appendici-fase-settima/appendice-dodicesima-fase-settima.md` | 20.147 | `993461ecc5bb7e7743ad4b03131ee1d1aa082f1277d95b307c85409401cecbf1` |
| `appendici-fase-settima/appendice-nona-fase-settima.md` | 18.039 | `527de6d7215fc1090bc57b977a5ab613425e78b35fdbea0d5240dbfb2f80fd0d` |
| `appendici-fase-settima/appendice-ottava-fase-settima.md` | 24.904 | `e7396a601da6bd5820c6f316e274d6b970b0e000e480026d14d1a2c7e85f9d53` |
| `appendici-fase-settima/appendice-quattordicesima-fase-settima.md` | 16.126 | `183a50fe548923e2db884b952fc678a0546ecda8a1f2700d5713507f6377b2f7` |
| `appendici-fase-settima/appendice-quindicesima-fase-settima.md` | 16.010 | `c9c6b4504ac57990a00d3dc3cb8c3335a00ff14bca02fe7ead834359acf09f39` |
| `appendici-fase-settima/appendice-quinta-fase-settima.md` | 17.594 | `fa4bc2c7581bc50ff9867d956fc4548085a2c3d11fc52f69f107258605cc9891` |
| `appendici-fase-settima/appendice-sesta-fase-settima.md` | 25.897 | `406f5ca205324b3660e4a18be2d668307af4598d1377a00a77650d93dec47b1c` |
| `appendici-fase-settima/appendice-settima-fase-settima.md` | 23.680 | `44dba4103f05ffa9670ffc7ead89e2173814ca4ed699417fbd7a202d577fa879` |
| `appendici-fase-settima/appendice-tredicesima-fase-settima.md` | 16.214 | `9120cf5bdea148fb67932414bcf4ce784a1792d903be2c3f8f7bda316ef26a3b` |
| `appendici-fase-settima/appendice-undicesima-fase-settima.md` | 13.511 | `8159266384ace8667008d84b9218a4ee1edbfe0b9388390f5c67c9a4ed4149c6` |

### Le verifiche e i generatori

*Le schede di verifica e gli script che ricompongono l'opera, i grafici, le note e questo stesso registro.*

22 file · 313.920 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_verifiche/certificazione-numeri-p2.md` | 14.229 | `d3b7349b8c9ef7584d467569833522627dccca09bef83d64e1b6dc9147b7704a` |
| `_verifiche/generatori/analisi_numeri.py` | 6.194 | `46da3df08a09dce6c25a83234d44c72ff35789a3364f7a702520477bb9c4d414` |
| `_verifiche/generatori/b_dossier.js` | 8.136 | `f00b3e46076a59ac85b3f7096fd75162709043a1218848a557695c9b579d9755` |
| `_verifiche/generatori/b_integrale.js` | 26.457 | `b8729ea2cf2aa176c78ddb53811576205f84b09c71f0940a0675b8b21d18c68a` |
| `_verifiche/generatori/build_cert.py` | 5.365 | `d393e4d5f00f299ff78d8007660c94620652030ecfdf56028c87e072558e9f7f` |
| `_verifiche/generatori/build_impronte.py` | 19.116 | `ded2e3a8c098c380a8acf2e548b53e0a33b1bb235f7f64de84ce8b2042a85ef6` |
| `_verifiche/generatori/build_pec.py` | 5.127 | `ef8de620af635fd6b0e6e79c4bff68def5a88a08df6197ce30c8091770a9ed29` |
| `_verifiche/generatori/build_tessere.py` | 25.340 | `eb06a585baffb9a54ece95ba8f6ab4d1e6bd78f52a9dab355bec55ba8fc4521e` |
| `_verifiche/generatori/calibrazione.py` | 3.202 | `5b0a8af8be0b7b23c7049915e301f8925907a46863b02d2d24e9034d8d97b1e8` |
| `_verifiche/generatori/conv16.py` | 2.343 | `8580145ac58059c108ae98d32b0bf2a734489d5d807817ea11f1e67c4e53f09a` |
| `_verifiche/generatori/conv_tab.py` | 2.845 | `4118e44164b329d6c79e36331745983d5e522df757bbd58a8b993386b06d36a4` |
| `_verifiche/generatori/conv_xlsx.py` | 1.847 | `62d427541412f02e4e1695f44381ab94f23687e50aae83ec76fcef337ab8edab` |
| `_verifiche/generatori/gen_calibrazione.py` | 3.674 | `93589daf5c028e28ecc4bc790050dc0fd92173f3c7dd21d437dde1b75b40c4cc` |
| `_verifiche/generatori/gen_figs.py` | 41.158 | `b0a1469a8b8580280bf3a1f99272f183e0f702451011cf1cdfc94f8ce8b46b4b` |
| `_verifiche/generatori/gen_impronte.py` | 21.081 | `c41648b395b1911462acd1f0fad1671f00ff259c0b9621a9ce5d973db054d5c6` |
| `_verifiche/generatori/gen_note.py` | 18.444 | `a2b9159ff3e5aab6b818d655eac8034892e077399a3ae9a6db63d3de00e4dc7b` |
| `_verifiche/generatori/gen_numeri_p2.py` | 7.435 | `e6adaccadd466cd43f4e1fc29e24eb917135c5c1d3fa20bde1ad437ee7c619a3` |
| `_verifiche/generatori/gen_verifica_p2.py` | 19.504 | `4f2ccd98963d24d8056fcffaf0bdf54fdb10ebdf3d2f3715228b3b0d3804da90` |
| `_verifiche/generatori/p_dossier.py` | 7.438 | `cc9a003c320e5f9b23696c28e6dfdd86d970e5c97f0e20be83eee4f277c80dbe` |
| `_verifiche/generatori/p_integrale.js` | 25.556 | `ca8aad411d55a3b7992b69585fd0f2f4ec840023c4ac46b3fa6ab9d99988119f` |
| `_verifiche/memorandum-operativo-riapertura-verifiche.md` | 37.272 | `b8e06f0a11445d72af56cb7da75460b964207470f41bd56e060723b2ed76bc27` |
| `_verifiche/verifica-elenco-trentatre-nomi-p2.md` | 12.157 | `b2ef83d9301731bb1cffb623e556e49ef7231488ff56cfbe84c290861eb4c749` |

### Il dossier di invio dell'opera

*Proposte editoriali, lettere istituzionali, registro dei canali PEC, checklist di spedizione.*

30 file · 1.442.427 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.docx` | 20.322 | `40c55f1e9b7124b9598065b64cc36ce7a84eaaaac9c972e257e8144dc5138696` |
| `_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.pdf` | 179.489 | `b057cf4d660c8b4b25359776c8e34cd1e80af8c74ce6d259fc2625505af0a4a4` |
| `_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.docx` | 11.122 | `e250bbeacd006f6d4f7d36e31d7ae0571a890998f45a3c7039a230971268efcf` |
| `_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.pdf` | 68.198 | `af31368b77f988f2af4df10c3ef17de95c8756ff5f128b49cabd9418307aff1b` |
| `_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.docx` | 12.440 | `127bf320c933c5714ed46452f822e6b5d9869722ac9ad848591831724946be95` |
| `_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.pdf` | 83.574 | `f42a8599cce5c7170653d6b7f7daf216449133bace3b8ed98b571cdde77e0f7e` |
| `_diffusione-opera/CHECKLIST_DI_INVIO.docx` | 16.717 | `d4892ea180a8e41cb25af72ff8147b88259dacb74976760489067612dbd5bf40` |
| `_diffusione-opera/CHECKLIST_DI_INVIO.pdf` | 253.683 | `c474d3c0a0d7faf2d0ff67196b92f760e24dae35134a274206a170217570c1bf` |
| `_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.docx` | 14.487 | `a7da865a818af51fde526eb3642a0cbfce9c8fe9f4af7adfe8f35097e27e4404` |
| `_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.pdf` | 116.292 | `0c351401226a5d4592bea4637b2347e03f5a6be62ebe90f184b94c2c3203a6ef` |
| `_diffusione-opera/PEC_UNICA_FORMALE.docx` | 14.803 | `955ccad0fb14abe90314ff8ca67b6e9341636724af2ea4085ad1743c33f910ea` |
| `_diffusione-opera/PEC_UNICA_FORMALE.pdf` | 148.695 | `8e7e9df640bb9f256ad5237a27f0db0a53e3a6ae4af78c1fbc3aa8f0c5514692` |
| `_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.docx` | 14.344 | `02f336b7e3940f078a440f248f4e817160c982d05cfcfd71bf1b27780efa10b6` |
| `_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.pdf` | 121.259 | `1d8ea6677b6765b0a3a7603b1e481f45c219928833cd6db4cdf665eefc6dc656` |
| `_diffusione-opera/README.md` | 5.894 | `15fdb4e0141aacb9cb9ad3266f27da27b5f2f7710353e597d15822d892d85162` |
| `_diffusione-opera/RELAZIONE_SUL_PROGETTO.docx` | 19.324 | `08f52776b7b0bc5a88b271b27156e524d0401f98af984e154d7e5b12350dc854` |
| `_diffusione-opera/RELAZIONE_SUL_PROGETTO.pdf` | 188.219 | `fa46f61b0efc6ca76d15249a08d4a215b7c7a51bb9d7c695a1772dfe1887a7a2` |
| `_diffusione-opera/capitolo-campione.md` | 23.221 | `d7c27e0665b89564d9965bf2cc6df402c365a5329a62d2ff9a663193a30b610d` |
| `_diffusione-opera/checklist-di-invio.md` | 12.083 | `7452685bc08372ab0a8ef6f0d13ce26a2799b0ea74cd0fac7eeb84faf876b390` |
| `_diffusione-opera/curriculum-modello.md` | 3.886 | `79eae88d23ad05d9f280445583e3a80f589890332e1fc8724634033fd38f5a83` |
| `_diffusione-opera/lettera-fondazione-aldo-moro.md` | 11.221 | `4a959a542a6e04b88caebf19a38e25cd6cfa2411a44d6c53e9c439a4575e977c` |
| `_diffusione-opera/mappa-dei-destinatari.md` | 7.354 | `bb0a4fea47582bf82a5d0f7fb7918597e5dfc00b11869dd7e64aae7217b2c545` |
| `_diffusione-opera/pec-archivio-flamigni.md` | 8.788 | `30629e30ed1efcac5f5cd02c9045533799c158ec45ea89255e20f0d37f1726fc` |
| `_diffusione-opera/pec-unica-formale.md` | 10.121 | `0f28a36090e815c725c6ce5e60a46728f2ae44e40ac1738ee7aaf85a65d07a14` |
| `_diffusione-opera/proposta-editrice-laterza.md` | 7.269 | `9a66fe93f89ef6424713389e43f0845a4d89c866bbf677012dc2e3ddfd5f3578` |
| `_diffusione-opera/proposte-chiarelettere-bompiani.md` | 12.025 | `315d094a4056ce3eb09dfd6e2832f160ad9c3b22874c802c7b16d436819c2cec` |
| `_diffusione-opera/proposte-mulino-carocci-einaudi.md` | 15.347 | `144b4d6ad806405c0df77f3a510cb5c0d6307066c5ca4ce06f21979e90e55053` |
| `_diffusione-opera/registro-pec-e-canali.md` | 14.921 | `937f9f84cd4db8ba931666440aeeb1c6da9b7ef53fec7dd8a4e364f725676a3f` |
| `_diffusione-opera/relazione-al-centro-flamigni.md` | 20.353 | `5d9f5244bb68dd0a9bb523ccfbb4fd620cd2579d5374e9e8be96cd2bf8ff4921` |
| `_diffusione-opera/scheda-dell-opera.md` | 6.976 | `d9e9472373df20d6633168e914b2171b627313c8ddf75d6b6cedd41a8ede54dc` |

### Terza opera — Italia Nera

*Il Registro V77 e i suoi otto documenti compagni: opera autonoma, imparentata con quella su Moro ma non contenuta in essa.*

48 file · 15.765.807 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `italia-nera/README.md` | 7.347 | `07272e73e8a7dc7a484cee9694c47ab2e753ca2ed1c5c4da2678e395fa1a0d44` |
| `italia-nera/apparato-tabellare/README.md` | 5.519 | `a95dcf93eab9f9a6e5d5c7c62d4cfb16aef7df3b6a590546b5d7087e47270f3b` |
| `italia-nera/apparato-tabellare/archivi-operativo.md` | 30.983 | `760b1a6c2c30c48bb47c513763e0c2a8468c9d65ba557acdad95738a9bc38011` |
| `italia-nera/apparato-tabellare/campagna-fase-due-accesso-remoto.md` | 9.264 | `e5461d7492fa309fa068f2b15672acf5adc743cbc402b5f5e7958d2ff55cfe14` |
| `italia-nera/apparato-tabellare/certificato-di-acquisizione.md` | 3.924 | `c5e1a7704b64d39ddf8cb144533359c1c72f9df88cf914d6a70ea53f78e4f33a` |
| `italia-nera/apparato-tabellare/lacune-dai-censimenti.md` | 4.279 | `c822f2e165fdd283fa639af62a6333d85d4ef102f0579382ed7235f3df10a8ec` |
| `italia-nera/apparato-tabellare/nodi-aginter-apartheid-approfondimento.md` | 16.498 | `761575212575ff90cd4bca458e8cb3393a3dcfb3ade4daf9400b31c59b9af387` |
| `italia-nera/apparato-tabellare/nodi-aginter-apartheid-integrazione.md` | 26.461 | `aa5e59cd81efb0912b164ff7bfc861e44c6ecaa32405cd46abe9b353878eb427` |
| `italia-nera/apparato-tabellare/nodi-d1-criminalita-organizzata.md` | 11.579 | `3acf6e6307a21acf537861840691e512b4f48f3b8dc8d08817c855445e342e7e` |
| `italia-nera/apparato-tabellare/nodi-in-integrazione-e-archi.md` | 11.588 | `ba96e7ee15021ed7e2bc2aba7e2874439f3471eb078f26a7ccd9f1111391cd90` |
| `italia-nera/apparato-tabellare/p2-hub-archivi-e-sinapsi.md` | 4.825 | `4e4445cf9aea45041af7f17dd318c9a70e34ae463a58344868cdabc18dfe942b` |
| `italia-nera/apparato-tabellare/putin-1970-1994-dieci-blocchi.md` | 12.425 | `5345b0873f85f48cd1e0f8a17ddac51a8cc58995cb13d939752af8140cc1ac67` |
| `italia-nera/apparato-tabellare/putin-venti-blocchi-e-archivi.md` | 10.538 | `c44edb01ccbda4264d557b717656a8519099c4209b221a46ec4f7810ab5ecafb` |
| `italia-nera/apparato-tabellare/triangolazione-integrale-putin.md` | 9.450 | `6549c5e5b3a311223630cac2213a8daad68bb72df62c9723db5d7b5aadf6fc0a` |
| `italia-nera/apparato-tabellare/triangolazione-putin-e-galassia-nera.md` | 7.210 | `fa111a883aa775662f342c00ed0997f4a62d94858191cd25b1c0934aaf4dc602` |
| `italia-nera/apparato-tabellare/url-censiti.md` | 845.363 | `8d3039f318a707365a82c86f3ac18e9e5f0d1fb8fe60697ecc8d1506491b4b8b` |
| `italia-nera/apparato-tabellare/verifica-biografica-putin.md` | 7.079 | `b7a623b9c6867952d37ff7b190ff32ceb54f7a49b9a814a5e1139e64f4dbd4de` |
| `italia-nera/censimenti/README.md` | 5.716 | `d735ef05d8545f866b43b86f2f17c7e63d524ccfa707fb135ec25f31d778c88e` |
| `italia-nera/censimenti/cap1-definitivo-134-schede.md` | 21.555 | `97d2e654e42bb25ab43a52f2efda2ba6017ef2dc92d47a2825ea461989a49d0a` |
| `italia-nera/censimenti/cap1-espanso-forza-italia-pdl-82-schede.md` | 30.194 | `5a7f2d7786e36ac1bfdbeecbea3b5d0609ba0a8aa1865eb0a4b5bf6776b162ee` |
| `italia-nera/censimenti/cap1-sezione-c-espansione-regionale.md` | 14.481 | `71dc80a15a6ea0a0fd93cb7b9d74443114279f35e0533403c794bafab7831b21` |
| `italia-nera/censimenti/cap1-sezione-d-regionale-cinque-regioni.md` | 12.307 | `bba6555b4a5feb8ec594ee11a6827c80a19b1d0a552573d381f784b9fa8dcaea` |
| `italia-nera/censimenti/cap1-sezione-e-capillare-2025-2026.md` | 8.533 | `7737a7005ecc014e92e089ae2f573eb1a19be6356f32d616b1da472117733c2f` |
| `italia-nera/censimenti/cap1-sezione-f-censimento-capillare-province.md` | 18.607 | `adf766ac46f17974c0264819044847313be85a66c636155fb31cb42c91a5da69` |
| `italia-nera/censimenti/cap2-embrionale-ventidue-schede.md` | 7.272 | `fd715524378152022b65fb144dba4e31c2a2defcdf86c8847f6f3098e8a577f7` |
| `italia-nera/censimenti/cap2-integrato-cinquantotto-schede.md` | 24.914 | `e3f2f24e7a82f4bdbde2047bbfbe8866140f9bc2030bc2150444e1732983575a` |
| `italia-nera/censimenti/cap2-trentaquattro-schede-sette-campi.md` | 22.794 | `603502c483eec184d2a53d17063bffd94ad9e2ca1294ea4a58bdc7c282e8367d` |
| `italia-nera/censimenti/schedario-aemilia-kyterion-grimilde-pesci.md` | 20.795 | `95e29906bae19c79ddb29e60f4be797717730fb1a3ae7473397b02b4d0ce50e2` |
| `italia-nera/il-ponte-transatlantico-cinquanta-blocchi.md` | 50.630 | `9d15eb5df3a2be7bb26741dd573b9758a854a81d8a4671cd25ef8a3669f66d1b` |
| `italia-nera/registro-analitico-dei-nodi-cinque-documenti.md` | 25.523 | `b722a90762a44da25bf2e65183dd379e3478696f9aa04bfd13df01ab2d904a05` |
| `italia-nera/registro-analitico-dei-nodi-corpus-aginter.md` | 79.913 | `1945eaafca258aaa56fa01fce5ad0afaeeadab1d68c440afc1b1eab4a7a96c37` |
| `italia-nera/registro-v77-l-opera-simile-a-se-stessa.md` | 13.619.501 | `0462c33417891471f1353899cc10bc4dea5283460399528ef6bf254ea9af7f84` |
| `italia-nera/scheda-di-consegna-aldo-moro-tutta-la-verita.md` | 4.200 | `67bcff5b9b826c64e487a0deb18d69b0e576c95167addfc27ba8224bfde10e67` |
| `italia-nera/scheda-ombra-kgb-e-riscrittura-dei-nodi.md` | 13.855 | `9a0069d16e1e05e75cb92896577ea3f775ee5d37eed80477b4e2d16dd215e250` |
| `italia-nera/schede-di-presa-in-consegna/README.md` | 6.465 | `534913df7a3040779e56ca8bd2bd2a75167ae4fc025895b65e57c605bdb0826d` |
| `italia-nera/schede-di-presa-in-consegna/blocco-quarto.md` | 30.781 | `b21a1599c9ab18c8bb2572f6d93d2db3b85d2fb047fa890a1f4ec9c1736880ca` |
| `italia-nera/schede-di-presa-in-consegna/blocco-quinto.md` | 16.267 | `475e05ea3c741c7bbd99728813ea6962633763e7b747564c498b9b8268455f84` |
| `italia-nera/schede-di-presa-in-consegna/blocco-secondo-verbali-x-legislatura.md` | 53.805 | `e68430d43d7a1d493bf844b6b4955e7aeab6c90888abfa3aa734e8c38aa2a733` |
| `italia-nera/schede-di-presa-in-consegna/blocco-terzo.md` | 26.403 | `41830c4c2e62ae5dfb325851d65f187a5373a24a24094373488e776ece86ee6e` |
| `italia-nera/schede-di-presa-in-consegna/scheda-nodo-wanda-vannacci-addendum-correttivo.md` | 15.365 | `4e7a27cbad73c545e9576b1a061b15b2e95ed4da8a583e28d7c5a649b6255321` |
| `italia-nera/schede-di-presa-in-consegna/schede-complete-ventotto.md` | 55.889 | `f0d0ce241d3dfad10f54db0260db10b4a3271c2c80b62350c49b181505ec0929` |
| `italia-nera/schede-di-presa-in-consegna/triangolazione-schede-dossier-v63.md` | 29.941 | `c044e255c9840edd89fa0ea623a6fae1a6b8133923ae78d7338469431f8f877e` |
| `italia-nera/schede-di-presa-in-consegna/v63-scheda-diagnostica-computazionale.md` | 13.514 | `1ca7bbfe01113fc55140d03c83803b8a6a5acfc7444a5bd4a6400c02b3c7dbec` |
| `italia-nera/schede-di-presa-in-consegna/volume-02-tomo-i-allegati-doc-xxiii-2-quater.md` | 54.783 | `bbaf2754a3716d58cd8ad6cb12e07c8b11a82d872b903e05acba9418164a1eca` |
| `italia-nera/schede-estratte-lotto-primo.md` | 52.043 | `c7621a9212aeca6568c0f0127a855d7d36ebb37e1a14f3e228ebb7b52d5177c8` |
| `italia-nera/schede-estratte-lotto-secondo.md` | 62.516 | `0e6df5b9e16e1219b0962af74a234d743d96f121a998346a60f2de59bd493ab4` |
| `italia-nera/undici-nodi-ex-novo.md` | 9.968 | `1861b577eb501d0e881772765b01241105de33c066567bc8331c66b11241442c` |
| `italia-nera/v68-libro-terzo-il-cantiere-di-riserva.md` | 332.945 | `c9eefcff43d6baed371a976e6429c712ad25c8ff7192df1b5e5a71045f7f4d03` |

### Altro lavoro — la radice

*Il README del repository e la configurazione: appartengono allo Studio Integrale Puglia, non all'opera.*

2 file · 1.951 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `.gitignore` | 110 | `7800638938600959ab98e4500d73a3e883406b7d823631858254c3adc366f4d3` |
| `README.md` | 1.841 | `e546510b9cea21ad289c0fcf4d20e723675f556b69c9e502f5a3e598bcad912b` |

### Altro lavoro — apparato e modelli

*Tracker di lavorazione, registri di verifica numerica e modelli di analisi economica dello Studio Puglia.*

28 file · 1.490.636 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_meta/anomalie-corpus.md` | 10.972 | `26d6b4b8cd2362bda7daf3518ef1ff239dd6e894e38cc197320de394f7185da8` |
| `_meta/apparato-editoriale-tracker.md` | 41.379 | `8b0f1742a5f25414e3c5847d6ee6cd49cc2a5e0441f4c3715b1eb7a3d39d4783` |
| `_meta/checklist-conformita.md` | 22.323 | `27907335c1c57b23f67a652273620620ebab6fd4b10baf5e942e2b6a38c5160c` |
| `_meta/cut-darlings.md` | 472 | `7535a4ebabd7ce993c34070b12311faa14ec4e74fe8a1b017395b92c09296ed3` |
| `_meta/materiale-per-derivati-futuri/bozza-4-capitoli-puglia_EN.docx` | 90.872 | `6a340ba9fb00667cad8b524d9b767615e72738c46bfea029ce93b2e064e8dfa4` |
| `_meta/materiale-per-derivati-futuri/bozza-4-capitoli-puglia_IT.docx` | 101.132 | `b9a2b84dbbc8cb352e433a6570ad0f616e1546bc2b437ed64012c33d750fbdf8` |
| `_meta/metadati-deposito.md` | 4.335 | `d35def6fbf3a0862f42db86d7ba27baa45cfa180b0922b57f21a77502223ee3b` |
| `_meta/modelli-tecnici/BIA_Sensitivity_Model.xlsx` | 32.950 | `265ef8497cab5c37a70c568a4dc5b480e8a1826ccb5e006a024c7aaef9b86ae9` |
| `_meta/modelli-tecnici/BIA_Sensitivity_iCBT_vs_CollaborativeCare.xlsx` | 43.172 | `bd0801703211709062e41dd428a77546e9fa926efc2cce786e58029905066b52` |
| `_meta/modelli-tecnici/BIA_Tornado_Diagram_1.xlsx` | 23.380 | `e32a91bcdb574b5ff5642a0fff102fc6fda2f0c3ab276f6285608fa66610384c` |
| `_meta/modelli-tecnici/BIA_Tornado_Diagram_3.xlsx` | 28.930 | `a3ed15badcd4dd0860073407274bc61dc5fab4eab7e21495ce4bb6662b61182e` |
| `_meta/modelli-tecnici/BIA_Tornado_Diagram_4.xlsx` | 22.723 | `a8158ba94d060549c46edd6fc930e46d56b2525e92c06cb708a0d1e285a1ab31` |
| `_meta/modelli-tecnici/BIA_Tornado_Diagram_5.xlsx` | 22.723 | `a8158ba94d060549c46edd6fc930e46d56b2525e92c06cb708a0d1e285a1ab31` |
| `_meta/modelli-tecnici/Tornado_Diagram_BIA.xlsx` | 25.749 | `4130479bd37b9accb307021929a12d18bce207d46b85ea0b2980df1f4970d9dd` |
| `_meta/modelli-tecnici/guida_tornado_diagram_CEA.docx` | 21.863 | `3a7f3f0384b62f0b68a22f4be515b39e61c9a66217708bd11abe9c111477a1e1` |
| `_meta/modelli-tecnici/iCBT_vs_CollaborativeCare_CUA_4.xlsx` | 21.982 | `a5c476c99ac27f918f3a266136cb04c330eccd27c5f1b297b813581aff75703c` |
| `_meta/modelli-tecnici/icbt_collaborative_care_cea_2.xlsx` | 28.493 | `eed74c7a05e06e55933724bde2708e16aa125411156171039ab5665b3db70648` |
| `_meta/modelli-tecnici/produttivita_HCA_FCA.xlsx` | 19.996 | `532e05ea14ea71a62b74c17915828fbd127df41fe4e7bf626bbe4c9dda2c009a` |
| `_meta/modelli-tecnici/tornado_diagram_CEA.xlsx` | 22.446 | `ecc5b48e52c710ff8935d1dfda0f13a2f923e706eafffdcc9a330af3cc973978` |
| `_meta/modelli-tecnici/tornado_diagram_hta.xlsx` | 17.439 | `1e23ac9550907aba5f33f46270ec6afdb7c667f93caa838a0e5cc0e0430c71e0` |
| `_meta/parking-lot.md` | 91.446 | `7e991f412d1718646414b4f124882bb46c7513439477a4756b67763cac333365` |
| `_meta/piano-aggiornamento-futuro.md` | 3.832 | `10a4314f084143cca46e64214092517f952ab978e889dbaf5010c2e1f2ca878c` |
| `_meta/prompt-operativo.md` | 23.704 | `d4588882f407f90211e4691ef1a2e4195e3b87a44e27f12c25b8c32e2c00683e` |
| `_meta/protocollo-validazione-fase4.md` | 7.894 | `d1fd478530dbed1fad8d3805d706748d53c04ab831e9411ecb14a0d0757a622c` |
| `_meta/registro-linguistico-tracker.md` | 13.020 | `ba3fee01ef527b341fe49ba7798efe2737eedc37966b2442d47a2c5d21d2bf8a` |
| `_meta/status-tracker.md` | 105.839 | `60f5f6b1bed9d28cf5a14255f78f05e1d5d1f107b5aaeb15efb2ed84c0d09354` |
| `_meta/verifica-numerica-tomo2-lineaB-tracker.md` | 263.693 | `d28b077ae11f22f6338d647366467882db5b73a3a8c91f3f8ca54d0b2f3befe4` |
| `_meta/verifica-numerica-tracker.md` | 377.877 | `962c2b0f1297ff1f3ae3a7967b8d452fad046be6cff610b66d1e66fa6a73373f` |

### Altro lavoro — diffusione

*Destinatari e lettere della campagna dello Studio Puglia.*

5 file · 22.024 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_diffusione/README.md` | 1.856 | `63b5ab1a66ba350f723c29b5ff0d3c0af83320cd56497aa8eafd49589623866b` |
| `_diffusione/elenco-destinatari.md` | 4.103 | `c02f7dc18d09fd3b8b58a25ed86fcf6c6cd42bbfa16186d36ae15a9c0da0eb86` |
| `_diffusione/lettera-accompagnamento.md` | 3.121 | `49c50e451c5daa0c7a162253632c270d6da1f03688b396801f1a3b22c83f3404` |
| `_diffusione/pec-invio.md` | 6.474 | `cf08d9428ee20b2747556389d5d15179d97327ba9d4be6182f9567c57f7df636` |
| `_diffusione/prompt-ricerca-destinatari.md` | 6.470 | `39309785a6a97c45618fc8d5d1b519426bb6fad86f657113c52a1383d64da3f0` |

### Altro lavoro — pubblicazione finale

*L'impaginato conclusivo dello Studio Puglia, col proprio indice generale.*

13 file · 123.536.718 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_pubblicazione-finale/README.md` | 5.123 | `f63786e7397d822f250a5cb866f9c81007940506fd3bf2d7f5568839f1ed28b5` |
| `_pubblicazione-finale/pdf/00-indice-generale.pdf` | 90.060 | `26f954c1d6282820753b1d3536c73806d7ea705c44c7cb70742887eff62cf0d0` |
| `_pubblicazione-finale/pdf/abstract-strutturato.pdf` | 68.752 | `058d7227859fc7a4949795c5ea814ea6247b2a5628bc6b0d314d5985a73a5633` |
| `_pubblicazione-finale/pdf/elevator-pitch.pdf` | 53.792 | `b49bccc38574f7929b32514374b7c3d029fb8391681025666dce5d87c8aac5fc` |
| `_pubblicazione-finale/pdf/livello-1-one-pager.pdf` | 67.286 | `30803ec18849563b7da6851bdaaf4439ecbb3d4ec88570acdd2f8e11d2ea540d` |
| `_pubblicazione-finale/pdf/livello-2-policy-brief.pdf` | 93.801 | `70e8751c6e0337fb086eced6213dd161d639d38f200c0923f46dbca7129ead6f` |
| `_pubblicazione-finale/pdf/livello-3-executive-summary.pdf` | 106.765 | `715d0cdc3e962d8e493445529dd91040a916a847b496369576a1eaba3d2bdbeb` |
| `_pubblicazione-finale/pdf/livello-4-sintesi-tecnica.pdf` | 226.575 | `be0f24352b56bd56971be0e0adeb6f7a1bdd8d80345bf3953fec6ad39a7b745d` |
| `_pubblicazione-finale/pdf/opera-completa.pdf` | 61.208.563 | `d94b63c12fdff7b4cbcbb0a08889e71de440467491b25740aad574ec7b6b6d42` |
| `_pubblicazione-finale/pdf/tomo-1-puglia.pdf` | 35.472.397 | `314181740191371054b322163411039f1a73f062ca8f3a9a053217d3e09d95ac` |
| `_pubblicazione-finale/pdf/tomo-2-linea-a.pdf` | 6.660.784 | `8cba138a9def3513c09ca1e11fe9326a859d7626f387a808d66be5fb370951ce` |
| `_pubblicazione-finale/pdf/tomo-2-linea-b.pdf` | 19.393.323 | `7a98df671387fa7d43a8bf6ab3fe06ed1cda433dcc1c5b394f8226ee4ea6fe9f` |
| `_pubblicazione-finale/pdf/versione-mmg-pls.pdf` | 89.497 | `83269bbbaf2f53c040eafea7f555667bb0df41d9bd0b7b6cf6d9a90d716be9d9` |

### Altro lavoro — livelli della piramide

*Le riduzioni progressive dello Studio Puglia.*

8 file · 54.505 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_livelli-piramide/README.md` | 574 | `83e951bb143c22fca6c6148c7d5792c770e5ef77b526c73b6a1b1f9924f2580c` |
| `_livelli-piramide/abstract-strutturato.md` | 3.674 | `49eb603cc3fcfe6a248c4c395dc99fa5d7018edb0c8a385812193adbacab40d8` |
| `_livelli-piramide/elevator-pitch.md` | 1.282 | `3102e253724c0cff1defc1c90413a7f15dd64cbebb1d89b877482dc561c7feec` |
| `_livelli-piramide/livello-1-one-pager.md` | 2.463 | `cb0462b6c0e4bf2fe9700ceddb371b468ea53f9ba1faeff8e2433b04291eb11b` |
| `_livelli-piramide/livello-2-policy-brief.md` | 6.698 | `991cac3657ff9cd59ad0a7eb8a2e529c5f1ad38d6ed9ef9033901a4386355fca` |
| `_livelli-piramide/livello-3-executive-summary.md` | 11.163 | `56b59919937684b6bda8e55cffad194832061de2aebf967add7aceb7c87ccbab` |
| `_livelli-piramide/livello-4-sintesi-tecnica.md` | 23.850 | `ab95cb8cc22965dade98d1091237a80beff74960b013ffa16720da8b70b91421` |
| `_livelli-piramide/versione-mmg-pls.md` | 4.801 | `9783ec063b8a0cca14fc9b690179fb7499e16525c86045edcb0aca05c42164f6` |

### Altro lavoro — paper accademico

*La versione accademica dello Studio Puglia, anche in inglese.*

7 file · 396.324 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_paper-accademico/README.md` | 4.458 | `b7ce07bad1554d2767dd9a19fc3312d39a2e0708ee5ca6727ef2fce823ac9fe9` |
| `_paper-accademico/docx/paper-english-oxford.docx` | 44.587 | `871fb23ec3fed794283987eb55db365aa598b230ab55f27fa020dd17b6cf7f62` |
| `_paper-accademico/docx/paper-italiano-crusca.docx` | 44.930 | `52c71a4fa2708059a43c22dd28d58471b5fff43732ca5a7a07d7c64fc2df1cc5` |
| `_paper-accademico/paper-english-oxford.md` | 21.811 | `ad01707c847a8c8e33ccf3c991284c79f5df54bf1f0979a6c4018afcf18d1977` |
| `_paper-accademico/paper-italiano-crusca.md` | 22.408 | `2545903843a36d4e1a669ae1c104c55ec1c4904b66bd0d9a644bfa9b186cf4ed` |
| `_paper-accademico/pdf/paper-english-oxford.pdf` | 125.335 | `03513704ab9659c1c62f0e48bb40c87b236fbc255e601a966a7549e5fadfc7e7` |
| `_paper-accademico/pdf/paper-italiano-crusca.pdf` | 132.795 | `3656168cc0bb7c214fa8d59d5ac38e06706c4528caec092e81d864bb0c4da5d1` |

### Altro lavoro — Tomo I, Puglia

*Il nucleo regionale dello Studio Puglia.*

8 file · 27.135.817 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `tomo-1-puglia/README.md` | 4.016 | `93de4d433624cf321085f7d504e50b095e415128d3e4d677c360300323097ef3` |
| `tomo-1-puglia/opera-integrale-puglia.docx` | 2.927.440 | `495e3ce3bb3e837bfedc7f125d7f47debb2f301b286410ff71f6fbfa8c75fd6b` |
| `tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_RIORDINATO-fonte-parte-XIV-XV.docx` | 1.420.832 | `53f3865a0a1753ae92ba35f58c590b977fc05ccacf45faa1ebbd65161e3b75af` |
| `tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_con-68-infografiche-non-integrate.docx` | 10.620.526 | `4d3df6c617ede59c937d6d7ad366c23449f032ae8ae16e321e3218febb14a9ab` |
| `tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_pre-integrazione-parte-XIV-XV.docx` | 2.912.499 | `c7081e71f25a3446fbaa34acff680b1cfc7cd6d8bef87a465b4299fa21ff2bbf` |
| `tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_pre-rimozione-parte-I-II-breve.docx` | 2.944.642 | `5d817d4c9c4d1259e3cc22efa857f209ef5f3855d06874c34587299e8e8f15ba` |
| `tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_v-50d7b8c3-meno-sviluppata.docx` | 2.806.110 | `64ee61ff6c25a51fd609dfebc2e55356a1ace2554a50b01ddfcb9ee41ca2047c` |
| `tomo-1-puglia/versioni-precedenti/opera-integrale-puglia_v-e1918ebe.docx` | 3.499.752 | `e4a4ba0b84180825f39732d59c4d43dcf20adceb5280b6a8b891542dfb5fa5bd` |

### Altro lavoro — Tomo II, nazionale

*L'estensione nazionale dello Studio Puglia.*

5 file · 3.833.161 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `tomo-2-nazionale/README.md` | 2.815 | `fc7fd8bcf9e826bb38b30802276629f531eb95c5a4f6d23a86f6353417a94b8e` |
| `tomo-2-nazionale/blocco-regionale/tomo-ii-blocco-regionale.docx` | 1.294.873 | `b182fd23caf8c76cef187cbb2587b5f13742c0a77d7baebd2ae1b7fec6a7077c` |
| `tomo-2-nazionale/blocco-regionale/versioni-precedenti/tomo-ii-blocco-regionale_tranche-4-ocse2026.docx` | 1.087.394 | `88d68670f2215f0ce9df52426706453a21ebdecc5a5cd2774f2b3e45ce59b873` |
| `tomo-2-nazionale/blocco-regionale/versioni-precedenti/tomo-ii-blocco-regionale_v-651fd061.docx` | 1.098.941 | `5743fe688060e99798f173f8242479bce197ae4804703b34c45f218e04c6566f` |
| `tomo-2-nazionale/opera-unificata-nazionale-e-ue27.docx` | 349.138 | `d11dd0a0a77fa37e776a5410522199111f542be59aa3ec6229bf7eaada08a3b1` |

### Altro lavoro — estensione ai ventisette

*Lo Studio Puglia esteso all'UE-27.*

2 file · 349.771 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `ue-27/README.md` | 633 | `e7e8f06c0b412b7e5bf1e209c1e53912c01f786e8f0c73a89b32616a0cb03132` |
| `ue-27/opera-unificata-nazionale-e-ue27.docx` | 349.138 | `d11dd0a0a77fa37e776a5410522199111f542be59aa3ec6229bf7eaada08a3b1` |

### Gli archivi dell'opera intera

*I pacchetti che si consegnano interi. Non sono versionati: duplicherebbero cio' che il repository gia' contiene, e non entrano nei totali perche' sommarli conterebbe due volte gli stessi file. Sono elencati qui quelli che esistono al momento della rigenerazione: un archivio costruito su una edizione anteriore non viene ridichiarato, perche' la sua impronta resterebbe esatta mentre la descrizione che l'accompagna sarebbe scaduta.*

1 file · 51.930.357 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `OPERA_INTERA_CASO_MORO.zip` | 51.930.357 | `76c8763bc4282bb819cf416712c39feb993f938da1bb8ef02bcf327c2a5cd288` |

### Il volume diviso in tre parti

*Le 2.425 pagine dell'edizione integrale pesano 37,5 MiB e il canale di consegna ne accetta 30: il volume viaggia in tre parti, tagliate su confini di Libro e non a caso. La prima porta dal Portale al Libro dodicesimo, la seconda i Libri tredicesimo e quattordicesimo, la terza il Libro quindicesimo con le quattro Appendici e l'Apparato conclusivo. Ogni parte ripete la copertina, cosi' che nessuna arrivi anonima; a parte quelle due pagine le tre non si sovrappongono, e la numerazione del volume intero e' dichiarata nelle proprieta' di ciascun file. Non entrano nei totali: sono lo stesso volume, tagliato.*

3 file · 29.956.554 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `OPERA_INTEGRALE_1-di-3_LIBRI_I-XII.pdf` | 15.529.848 | `eb09869c8e64dd36276e5a9c1b458d7fdb9422c896ca06f985c513fe7c416314` |
| `OPERA_INTEGRALE_2-di-3_LIBRI_XIII-XIV.pdf` | 10.163.943 | `dcb764ad61252631a86f87cb593b5a0f9a6e72c8c7db29a7fecb907407b9fd94` |
| `OPERA_INTEGRALE_3-di-3_LIBRO_XV_E_APPENDICI.pdf` | 4.262.763 | `092537a63dd7646b481ec32654417f6ea3832290ffb8aece93600f4d859207d0` |

### Il pacchetto dei grafici

*Le nove infografiche della verifica, la nota di metodo e l'archivio compresso. Non sono versionate: viaggiano a parte, e per questo l'impronta conta di più.*

14 file · 1.908.562 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `10_le-due-numerazioni-sulla-stessa-retta.png` | 104.252 | `94870100455a3514766df6e89095fe914d1e378ae17b315c443aea622f02b9e7` |
| `11_scarto-dalla-retta.png` | 137.029 | `bd044e395e4454d0cbda18fe6b938110b796b01f3a41b1f3cc2260710ab01ae8` |
| `12_un-archivio-deriva.png` | 83.468 | `5c273ae8c02eca58ca5d142ace63eb81943862d10cbddee8be7f31c795b9fdaa` |
| `1_imbuto-della-verificabilita.png` | 67.753 | `c6b0424bf2293c248575a66f2c44c790edc3c671adc190a94e8e0bbedbad3625` |
| `2_tessere-sotto-la-soglia-documentata.png` | 75.207 | `1a5c989e77f1e2c1b719d9eb6eae074b824bc6eb5cec4135303e7aecbf3c2832` |
| `3_i-trentatre-per-sede-istituzionale.png` | 71.597 | `f61a057b4315fd6eacf9a9a9726498dd1abdaa0e69d2285911274d4bc35a7f5b` |
| `4_composizione-documentata-dei-962.png` | 77.397 | `068e589fa336ffa8f587711677f87f195c4c4b72273516e2785dbc2fbf2acbe3` |
| `5_distanza-fra-i-fatti-e-la-prova.png` | 60.499 | `fc6860ccc09b8d17e2c7ae4d2627e3414d60570f0c447d34f2d2b82eb8eaeef0` |
| `6_finestra-sei-mesi-materia-disponibile.png` | 97.589 | `29db330279ad0a1b9bb8ebb51c06926d629387032f0613caf91825873b62e4dd` |
| `7_quota-dei-trentatre-sul-totale.png` | 67.111 | `09247c55e134b965157c3ce1a034611a5771e72b831488d5aea924496d887c35` |
| `8_date-di-affiliazione-disponibili.png` | 67.109 | `6b6c451f03a59689c3a9a4b45eca4e572d6a8e67e2c99569984bbde57f29b4f6` |
| `9_finestra-e-i-due-dati-datati.png` | 58.109 | `ca23774f52b68d21c204dca2f3d1632ef6917b6460331fc8f81b76a4d169b55a` |
| `LEGGIMI.txt` | 4.188 | `f915aaa3ebfdb56ca6ba10451661cb77242f895e0d29128642aab87bd49f3cf7` |
| `GRAFICI_VERIFICA_P2.zip` | 937.254 | `85a6ddb61d1412ed9edd44dd62580210fd7ef375fd57afa2d632eacc55d53543` |

---

## Il commit, che è un'altra cosa

L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git:

```
e71d4fb9c43f03c72f20f109d0253051da1f3922
```

Sono due garanzie diverse e vanno tenute distinte. Il commit fissa **lo stato del
repository** — quali file esistevano e con quale contenuto in quel momento.
L'impronta SHA-256 fissa **il singolo file** anche quando viaggia fuori dal
repository: in allegato a una PEC, su una chiave, dentro un deposito d'archivio.
Un file staccato dal repository perde il commit e conserva l'impronta.

Il pacchetto dei grafici lo mostra bene: non è versionato, quindi non ha commit —
e ha comunque un'impronta.

---

*Le impronte si ricalcolano a ogni nuova edizione. Un registro che non cambia
quando cambiano i file non certifica nulla: va rigenerato con*
`python3 _verifiche/generatori/gen_impronte.py` *e ricommesso insieme all'opera.*
