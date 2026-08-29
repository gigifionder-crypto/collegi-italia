# Registro delle impronte SHA-256

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file porta qui la propria impronta crittografica. Chi ne riceve uno può
accertare in un comando che è **bit per bit** quello depositato, e non una copia
alterata, troncata o rimontata.

**Stato al commit `8b4266cbf1ca`** del ramo `claude/amnistiati-tribunale-speciale-a82lzn`.

---

## Tre lavori, non uno

Il repository ospita **tre opere distinte**, e vanno tenute separate anche qui.
Il corpus lo dichiara già per conto proprio: `INDICE-DOCUMENTI-BRANCH.md` scrive
alla terza riga che i documenti del caso Moro sono «estranei al progetto
principale del repository (Studio Integrale Puglia)».

| | file | byte |
|---|---:|---:|
| **L'opera — il caso Moro** | 214 | 87.321.022 |
| Terza opera — Italia Nera | 140 | 40.759.569 |
| Altro lavoro — Studio Integrale Puglia | 92 | 158.024.567 |
| **Totale nel repository** | 446 | 286.105.158 |

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
del file che elenca i 199 file versionati che le appartengono:

```
4a17735a92d4c67a8f3226ab1d2ee7aec146c94edbc53896a19480cbf38d957b
```

Riproducibile da chiunque, in un comando:

```
sha256sum IMPRONTE-OPERA-MORO.txt
```

## L'impronta della terza opera

La stessa cosa per Italia Nera e i suoi 140 file:

```
7b5e391fe718a035060587c6808b5c5051482c45a43c1ce5068da7749824a769
```

```
sha256sum IMPRONTE-ITALIA-NERA.txt
```

## L'impronta dell'insieme versionato

La stessa cosa per tutti i 431 file versionati del repository, le tre
opere insieme:

```
5274da23709185914cc5dfd00cb3fcaf3da8d72721b750f9ac058fc7c3f834d8
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
| I volumi rilegati | 26 | 73.964.623 |
| I documenti del corpus | 40 | 6.521.908 |
| Il Libro dodicesimo e i suoi originali | 40 | 1.960.845 |
| Le appendici alla Fase settima | 11 | 206.415 |
| Le verifiche e i generatori | 43 | 515.366 |
| Il dossier di invio dell'opera | 39 | 2.013.688 |
| Terza opera — Italia Nera | 140 | 40.759.569 |
| Opera derivata — il romanzo | 14 | 1.203.660 |
| Altro lavoro — la radice | 2 | 1.951 |
| Altro lavoro — apparato e modelli | 28 | 1.490.636 |
| Altro lavoro — diffusione | 5 | 22.024 |
| Altro lavoro — pubblicazione finale | 13 | 123.536.718 |
| Altro lavoro — livelli della piramide | 8 | 54.505 |
| Altro lavoro — paper accademico | 7 | 396.324 |
| Altro lavoro — Tomo I, Puglia | 8 | 27.135.817 |
| Altro lavoro — Tomo II, nazionale | 5 | 3.833.161 |
| Altro lavoro — estensione ai ventisette | 2 | 349.771 |
| Gli archivi dell'opera intera | 6 | 211.848.970 |
| Il volume diviso in tre parti | 3 | 30.075.131 |
| Il pacchetto dei grafici | 15 | 2.138.177 |
| **Totale** | **446** | **286.105.158** |

---

## Le impronte, sezione per sezione

### I volumi rilegati

*Le edizioni tipografiche in DOCX e PDF: è la forma in cui l'opera viaggia fuori dal repository.*

26 file · 73.964.623 byte

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
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.docx` | 14.289.251 | `472cf6eefbe201385183905529a467902015d10667d94186b4e437a79d900c84` |
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf` | 39.738.602 | `9756b6b1dd639c0cc98cba09dd722945d597fd1ee7e54a706184e7ba4c67f17c` |

### I documenti del corpus

*Le sorgenti in markdown del Portale, dei quattordici Libri e delle tre Appendici, con gli indici e gli apparati.*

40 file · 6.521.908 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `GUIDA-ALLA-LETTURA.md` | 30.126 | `07842e957c7734536c97dce8b34823ce11473a9cfe9d60dd7746390398740cd5` |
| `IMPRONTE-SHA256.html` | 237.724 | `040f221cbdc4a06aeaa00b681c50be9c2efad391307977db0b4f93428f687fe6` |
| `INDICE-DOCUMENTI-BRANCH.md` | 84.487 | `7276e96397f5e5e0a80fe3bfc300c18b875ca8050346854d59bcf2a430c28992` |
| `agenda-di-ricerca-del-nuovo-caso-moro.md` | 120.075 | `f2dffd0bc5202005bc5e625cbafc730092250d116866a7d59f8ec34a561f038c` |
| `aldo-moro-una-guerra-senza-fine-apparato-dei-gradi.md` | 11.181 | `c96e44cc8867fa970e270f23f88e036e6d134dc8eedec25227a17fe1c5f7dff0` |
| `aldo-moro-una-guerra-senza-fine-edizione-strutturata.md` | 28.364 | `34c7e4c4b08d947d64bbdfe833bb22c8974e6cc6728fe86dee2beb5c70be462a` |
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
| `dossier-maggiore-una-pace-senza-pace.md` | 1.763.081 | `2177521a5a6f75fb3ce502302f3d71e85102c0afc36a26ac657eae4d7bef9a27` |
| `feltrinelli-il-vettore.md` | 17.727 | `4a6b62e4bf10b8e6e0696437161477aefebb593ede84711a1abbc0396ce6f19c` |
| `il-fascicolo-della-custodia.md` | 24.077 | `758c1b4873fe1d3c9a8dffd3b1816bcfd96194b93c89d5e2068c7953b7994ea2` |
| `il-meridiano-e-la-valle-mille-blocchi.md` | 504.370 | `be9db6e69e75392773ed90cec74924d29279a5a067897215cc4152ea9d8ef261` |
| `il-quesito-della-sabbia.md` | 10.683 | `266cbd22b04477d4a3ac4227fc9827324b47a57b7a33c8dc476c442a601c5881` |
| `il-registro-dei-cinquantacinque-giorni-opera-seconda.md` | 303.339 | `78c1f784b7e4d631b282221cd40f88d72cdf5bf3877b9d5eb45da4b4cdbe609a` |
| `kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md` | 2.400.306 | `754eea844fde0a471f13b549805f85814c2fd507dc1a7a84f2769af06ec5beaa` |
| `la-matrice-della-custodia.md` | 14.986 | `5af28f0812ad3b53c07e1e52f1927e115903c269b063e13dcdb8b8849974c2e9` |
| `la-matrice-delle-omissioni.md` | 14.203 | `90f4e335927b9f4937c2bde4f74886e7e0e40e3ed78e1a552156d0b1a4d14467` |
| `la-matrice-di-via-fani.md` | 12.942 | `4bfbdc343c11cffebb741ab0f29880195a6c16ed8e16dbb99d9e0c902bc571b1` |
| `le-pene-oltre-confine-mitterrand-mulinaris.md` | 12.314 | `620e2299da71f18efc52bc13f7f4743211f1709a523c843eb1bf37fbfd5b8138` |
| `manuale-investigativo-nuovo-caso-moro.md` | 104.736 | `8669efe737f67785354604348850f5843185efbbc266a5cb2ce124ea8004a74b` |
| `metodologie-del-dossier-sinaptogenesi-e-strumenti.md` | 15.749 | `2b6f198ec9cf61b850bcf1aa392f7c65e61d4b5c6df8bf7a90305797cda54cf9` |
| `note-bibliografiche-opera-integrale.md` | 141.633 | `f3c5ea33091b032a411ccd5d531056e4ac305b853449441329e48904b2f3233a` |
| `nove-cantieri-mille-blocchi.md` | 357.586 | `c6c38d83a5adb41abf45a4a4c6973574ba521214a2c867da7302b4a63859d0db` |
| `programma-investigativo-caso-moro.md` | 25.994 | `043bd0a175892bf4a874add1d28078b1e3d1dccafc2d7101dd5886cbcfd8cfc0` |
| `relazione-stato-lavori-stile-moro.md` | 6.543 | `dd5bbf37ef9ba2b6f5bbe084395b1c68e9804cdb2ffc2250d6c3ac3f2d5982a5` |
| `triangolazione-condannati-corpus.md` | 22.340 | `cbdc3593873d7acae3289e12d7e5a44ae93768514e40d93c3229b2f253b70cd7` |
| `triangolazione-feltrinelli-corpus.md` | 13.744 | `a4f5354f9bba0934600a590ac83f63a9f8048f458e1958e75c8df016ee126870` |
| `triangolazione-feltrinelli-hyperion.md` | 9.234 | `51ba5dc410fefa7d1ed6194f331ba86a1231154dd7288c04593dad63982185d7` |
| `triangolazione-hyperion-corpus.md` | 12.067 | `59d1c735892d6bcdd40fb1924d99cb1947921d8ccc048ecb9f96b1e237c4c6c6` |
| `tribunale-speciale-approfondimento-sottonodi.md` | 10.911 | `a4b9012a0120e40d7c8a155e7d8f30a4cce7767efa0033189704b2371f65ed45` |
| `tribunale-speciale-storia-istituzione.md` | 15.672 | `2900e103611d64ea162ff50926d599ac39f7ed8a59e0e96db5ad5c650082de9f` |

### Il Libro dodicesimo e i suoi originali

*La dimensione diplomatica: le ricognizioni Farnesina per esteso, i documenti State Dept, l'edizione HTML navigabile.*

40 file · 1.960.845 byte

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
| `moro-ministro-esteri/terza-campagna/decima-ricognizione-revisione-del-modello.md` | 39.709 | `31d79c22bd27c6d7f07b8a02eb3e281159f81aa09b522b5c61f5ccfbe906c8bc` |
| `moro-ministro-esteri/terza-campagna/diciassettesima-ricognizione-santa-sede-e-sudafrica.md` | 32.810 | `e808fd019ef4d5f6ca951cc8cf79ad76962898a41b6947b95f11a1b86d5d2bd0` |
| `moro-ministro-esteri/terza-campagna/diciottesima-ricognizione-nazioni-unite-ed-embargo.md` | 29.697 | `bdfa4b7582abf51d5f624386216cefeb0aa97aa3335c7a3e392d1c3033e365ce` |
| `moro-ministro-esteri/terza-campagna/dodicesima-ricognizione-sette-casi-extraeuropei.md` | 38.294 | `01bd1db98327acd6351f67e125ad01f4826e2f1ecab3ccad831b4446a11ac6b9` |
| `moro-ministro-esteri/terza-campagna/nona-ricognizione-la-sequenza-oder-neisse.md` | 44.964 | `86cc9c255ae436dd60a2b82c36098ef3f14926ddc68ee897a5a4711a8791050b` |
| `moro-ministro-esteri/terza-campagna/ottava-ricognizione-mediterraneo-orientale.md` | 46.593 | `b15a8529aa84ca973247b6b6cad889f0943cdfd1f286b1be2930b8dddac082cf` |
| `moro-ministro-esteri/terza-campagna/quarta-ricognizione-portogallo-santa-sede.md` | 41.226 | `5a06c0b0217f1f05d99a5145628b006377e51b31459852648ab48f7fd2c51fbb` |
| `moro-ministro-esteri/terza-campagna/quarto-registro-la-scala-degli-stati-zero.md` | 23.290 | `f4e1a574fed518430816abe7863ff6c9b3bda276d79070030e4adec003faa01a` |
| `moro-ministro-esteri/terza-campagna/quattordicesima-ricognizione-la-calibrazione-libica.md` | 33.041 | `7606404f3f042ca78eb57613d4597e7bdc378e670d4122bcc5ba49dcc75a297c` |
| `moro-ministro-esteri/terza-campagna/quindicesima-ricognizione-aermacchi-e-il-sudafrica.md` | 37.603 | `143d1cc7ef4e70ab0688923138273669c7b55a625342bf888fbe149aa9385f3b` |
| `moro-ministro-esteri/terza-campagna/quinta-ricognizione-portogallo-le-sei-lacune.md` | 36.937 | `4c39caf8e55b476119ee6e87ad2b7948e5a9176d5c2b6dd1fffb0f7f90b04025` |
| `moro-ministro-esteri/terza-campagna/quinto-registro-la-tavola-unica.md` | 19.074 | `6717b4841cfc7861937f9f6a654460e71ae76438913405dea831c5f12bbcdd00` |
| `moro-ministro-esteri/terza-campagna/registro-dei-nodi-e-dei-ponti-teatro-australe.md` | 41.634 | `e2c21d72826f13dba7b7dc081b5b125fc255493243a5b0f0242d8ef50f37fe07` |
| `moro-ministro-esteri/terza-campagna/registro-delle-undici-ricognizioni.md` | 42.454 | `bd3d72342ffaaecb0c121225f0a9d6020813a2eee691746aaef341d07c48a237` |
| `moro-ministro-esteri/terza-campagna/secondo-registro-dei-nodi-e-dei-ponti.md` | 33.478 | `c00c6e897812526d9b7bb3f3f6c14381b9ed9ea7e7f1b946efdbdf2ab63c49d4` |
| `moro-ministro-esteri/terza-campagna/sedicesima-ricognizione-il-dossier-namibiano.md` | 37.274 | `9a33423a05a38aa45cc7b3477c05d337ca35089ddb18f41431a884a573e56e1e` |
| `moro-ministro-esteri/terza-campagna/sesta-ricognizione-il-ribaltamento-iberico.md` | 34.801 | `a0f2117e2fe303076bd5a6705df655f25ec5ce11f6fd1f93cd47bad8c39846f8` |
| `moro-ministro-esteri/terza-campagna/sesto-registro-strumenti-e-volume.md` | 20.259 | `ab914c34466bf7fc2e479d17d193c356be0a710b8a0a16b1ac4dc20d9924031a` |
| `moro-ministro-esteri/terza-campagna/settima-ricognizione-turchia-e-attentato.md` | 42.441 | `ef6553487abf30ecb748e934be20020f338f40670c46749ae6c4fc74d707390b` |
| `moro-ministro-esteri/terza-campagna/settimo-registro-la-riqualificazione.md` | 15.357 | `39c02820b143973b612588cde25f1b8cb6b42f0b96133c1dd70fd7004761f192` |
| `moro-ministro-esteri/terza-campagna/terza-ricognizione-spagna-opus-dei.md` | 38.520 | `5f0b2c7ee68df4973a4e72d2ed9e39df2543a35ae43390ba182853f6ad534981` |
| `moro-ministro-esteri/terza-campagna/terzo-registro-dei-nodi-e-dei-ponti.md` | 29.184 | `fb382223b5e0ab330efbad13f518fc4e1d6f152251b6710915edefc4de1b6823` |
| `moro-ministro-esteri/terza-campagna/tredicesima-ricognizione-aginter-i-due-silenzi.md` | 36.208 | `4cc71e229453e35857048d511e4dbc8a84dd064d0bc2570feecf789c68a9a42e` |
| `moro-ministro-esteri/terza-campagna/undicesima-ricognizione-strauss-e-aginter.md` | 37.950 | `cf2e8e2da65545fa90dc23eca2835a60a11e67a413303cf14e57d2c7c1bd26fe` |
| `moro-ministro-esteri/triangolazione-seconda-campagna.md` | 39.418 | `574b3a22479712cd9288b97ba5e2d76daa98ee5380cda9411917547f23cd5864` |
| `moro-ministro-esteri/triangolazione-terza-campagna.md` | 13.000 | `d3734a34a68434390e30e546ebba2c523b203b89a5011c332d5466e1d49af515` |
| `moro-ministro-esteri/volume.html` | 560.334 | `aef519447a3d02869ee9ee70dce6c61bce7a73577bf3cfbc282b57f9cadaf96f` |

### Le appendici alla Fase settima

*Le undici appendici al Libro nono, dalla quinta alla quindicesima: la serie chiusa.*

11 file · 206.415 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `appendici-fase-settima/appendice-decima-fase-settima.md` | 16.013 | `2bf0d59199aea2878b2148f57b171ee3698f887bd707a6c52e3e0e6027c238d0` |
| `appendici-fase-settima/appendice-dodicesima-fase-settima.md` | 19.947 | `bcc6d36d85df731b6b6f4576d7cf84fc950031e11f96911a4769c8ad311bf386` |
| `appendici-fase-settima/appendice-nona-fase-settima.md` | 17.843 | `ca5b2cb47d713cad9c0f5e99978657472461f13ed40c285a7c38ecad16c35251` |
| `appendici-fase-settima/appendice-ottava-fase-settima.md` | 24.712 | `a0a458d87a93e3acfaefe8975fd3abbcda0f9b5fbfba85c9f1663294ebfb5f1f` |
| `appendici-fase-settima/appendice-quattordicesima-fase-settima.md` | 15.990 | `a4bcce1ef922e490be809b44eb8165aa890303b3f471703de7af1713ef244ad5` |
| `appendici-fase-settima/appendice-quindicesima-fase-settima.md` | 15.874 | `23b3bbd6989c086ac433a6f7e5792fba7ae674ddc7eb45fb3e5bb5f841385364` |
| `appendici-fase-settima/appendice-quinta-fase-settima.md` | 17.434 | `20964d05bfb0c65406452e572064127af37fd14848c4678950a5485a9835d234` |
| `appendici-fase-settima/appendice-sesta-fase-settima.md` | 25.681 | `8fd65a1f1f1ffbb142f71ec99b7511a08c1941c540767e2d3fcb01009a87c31e` |
| `appendici-fase-settima/appendice-settima-fase-settima.md` | 23.488 | `1de6a2dd5eee4d856ec4b37e6a3c4d516cabbdc44ca087fd71f062d6c7d93f3e` |
| `appendici-fase-settima/appendice-tredicesima-fase-settima.md` | 16.058 | `f1ef0ed360ef70378db57309ab496b1b472a170933370c6cc804cc85a8de106f` |
| `appendici-fase-settima/appendice-undicesima-fase-settima.md` | 13.375 | `5644510adffab241f1b57e328f4b603e0dde8b3e19fb210dabbdb1e571a513fc` |

### Le verifiche e i generatori

*Le schede di verifica e gli script che ricompongono l'opera, i grafici, le note e questo stesso registro.*

43 file · 515.366 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_verifiche/campagna-ricerca-numeri-p2-relazione.md` | 90.929 | `9c19e49e3df2d1267f98ec9c66e7b62f120b3a6fde6801dd0eb812e673a82e34` |
| `_verifiche/certificazione-numeri-p2.md` | 28.815 | `ca1a5ca46ae200784bfc7c91a8ec93a72ae60b0a30c3dd896a2836cf6ea72152` |
| `_verifiche/generatori/NOTA-SORGENTE-UNICA.md` | 3.328 | `fb1ffe43cc7ddde6abe6e401cb1d9bcf61df00c9f557352b41e81d96d37ab48e` |
| `_verifiche/generatori/analisi_numeri.py` | 6.194 | `46da3df08a09dce6c25a83234d44c72ff35789a3364f7a702520477bb9c4d414` |
| `_verifiche/generatori/analisi_romanzo.py` | 3.958 | `c88b409afc5aee040f740933dff4bd649020a5ed42686d9cae375019bff7d1b4` |
| `_verifiche/generatori/aritmetica_scarto_p2.py` | 1.314 | `f35ebbde273cd93a5ea32a2a0a9cdbf829d1c522b14bd08e5dd27e5dd0bb8953` |
| `_verifiche/generatori/audit_gradi.py` | 2.744 | `e1d9f5d75e53b60b1799484129d20bd48092e97a02ed2bf557a25bc9f4e3dc06` |
| `_verifiche/generatori/b_dossier.js` | 8.448 | `bef5c01681896bd00dba322f61a4cc851a6d15a29cb7318778b7edf76da34c8e` |
| `_verifiche/generatori/b_integrale.js` | 15.554 | `406bc071bb7be2d51512cae80c4d5f366b978a371852988994b67b527c1d098b` |
| `_verifiche/generatori/b_romanzo.js` | 3.749 | `9d9cd816f70778405ef57d50571e12ac722b1b103a83cd9b23047279202064a0` |
| `_verifiche/generatori/build_cert.py` | 6.079 | `d5f00a391dc90854b995aa0013622389a83fece41ce51c609b6e850497084f88` |
| `_verifiche/generatori/build_impronte.py` | 19.931 | `6252a583cfcc633069f45d925c8b1390b17e2d76e865d1e62b05060de7bb1ac8` |
| `_verifiche/generatori/build_pec.py` | 5.127 | `ef8de620af635fd6b0e6e79c4bff68def5a88a08df6197ce30c8091770a9ed29` |
| `_verifiche/generatori/build_tessere.py` | 25.340 | `eb06a585baffb9a54ece95ba8f6ab4d1e6bd78f52a9dab355bec55ba8fc4521e` |
| `_verifiche/generatori/calibrazione.py` | 3.202 | `5b0a8af8be0b7b23c7049915e301f8925907a46863b02d2d24e9034d8d97b1e8` |
| `_verifiche/generatori/conv16.py` | 2.343 | `8580145ac58059c108ae98d32b0bf2a734489d5d807817ea11f1e67c4e53f09a` |
| `_verifiche/generatori/conv_pdf.py` | 5.154 | `316d96389e08bc3fc661033bf9a8a5f02e98c5c281d8c040cc74563d82f73c19` |
| `_verifiche/generatori/conv_tab.py` | 2.845 | `4118e44164b329d6c79e36331745983d5e522df757bbd58a8b993386b06d36a4` |
| `_verifiche/generatori/conv_xlsx.py` | 1.847 | `62d427541412f02e4e1695f44381ab94f23687e50aae83ec76fcef337ab8edab` |
| `_verifiche/generatori/estrai_stati_zero.py` | 3.378 | `729b2eaed8e88e1ce2ae84727fb39892310622e9ed04b8f1ae3e1e93cbc3b979` |
| `_verifiche/generatori/fig_scarto.py` | 3.172 | `260cbc30d37ad782b2edaa22be64dd12228c1eb06515819705c5f2132b5a5bd6` |
| `_verifiche/generatori/gen_calibrazione.py` | 3.674 | `93589daf5c028e28ecc4bc790050dc0fd92173f3c7dd21d437dde1b75b40c4cc` |
| `_verifiche/generatori/gen_figs.py` | 33.082 | `3ef4e90c58815cb5589151626c3351ed207fdcd04b1a0e63a694741c3d92459c` |
| `_verifiche/generatori/gen_impronte.py` | 23.233 | `b35f85d71f8de1e841fa44c416eb31b45f435054a22faf07f113460f80e638e6` |
| `_verifiche/generatori/gen_note.py` | 6.378 | `6fbf735461c3848959690bede5f65be140aeaefa234121ed109e86634629ab0d` |
| `_verifiche/generatori/gen_numeri_p2.py` | 7.435 | `e6adaccadd466cd43f4e1fc29e24eb917135c5c1d3fa20bde1ad437ee7c619a3` |
| `_verifiche/generatori/gen_verifica_p2.py` | 19.504 | `4f2ccd98963d24d8056fcffaf0bdf54fdb10ebdf3d2f3715228b3b0d3804da90` |
| `_verifiche/generatori/p_dossier.py` | 7.693 | `6ee8f6f48fe457dffc5e1f25e212c9dad943401d91302f14a7038ba30367d575` |
| `_verifiche/generatori/p_integrale.js` | 26.819 | `229b30bfbd15ea9b7395695336323125b29b6db0c7309bc58be62400b83209b0` |
| `_verifiche/generatori/p_romanzo.js` | 2.801 | `010a7e1810a90b29fc212a6e07918ddfcdd76a6ca457650db18ad28f32c4939e` |
| `_verifiche/generatori/parti.json` | 27.521 | `1bfaf0dce73240f13be6239497391e40a57fb369a290ea82f0682f4ca5551297` |
| `_verifiche/generatori/ricevuti/NOTA-PARTI.md` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `_verifiche/generatori/ricevuti/README.md` | 1.214 | `a254e7dd9343fa8dd486d6a0abe418f66b2ddc5de35330d96d657b2ce3c2b02f` |
| `_verifiche/generatori/ricevuti/build_v65.py` | 2.558 | `e6fdf77ae0c84ca2ee1e9d0ab0e9d967219a3a2bdaf04f064018cc8cfeb9ecae` |
| `_verifiche/generatori/ricevuti/build_v651.py` | 2.558 | `e6fdf77ae0c84ca2ee1e9d0ab0e9d967219a3a2bdaf04f064018cc8cfeb9ecae` |
| `_verifiche/generatori/ricevuti/estrai_nodi.py` | 2.805 | `1d5436b3febaa11246c587d6d1f7f1331da3a2f05873f54258b368eaef883e93` |
| `_verifiche/generatori/ricevuti/gen_prompt_v65.py` | 27.770 | `c252b855259d5f9e757c63e6300bcba20a76e3325b0a200e5e69203bc23f2734` |
| `_verifiche/generatori/rilega_romanzo.py` | 7.840 | `a07679104d99e4e5791e0c9757633d79e63a71e2881efd21c7ce78cd8345da17` |
| `_verifiche/generatori/sgrassa.py` | 2.541 | `6a5f2bc4b0e3ecfa9c8ab7998f7bfda9391cd96cfe0173401feccd586f7277cb` |
| `_verifiche/generatori/spoglio_farnesina.py` | 3.493 | `3cd033221ff072b2fe97a208d5dc443f5251f265eeb230e84c777f6c6a6ce89b` |
| `_verifiche/memorandum-operativo-riapertura-verifiche.md` | 36.620 | `063df1425312d34b0fb35ed1994942d869a555816d78cf25b63b277b6dc76690` |
| `_verifiche/registro-degli-ingressi.md` | 14.219 | `ab6c730e71e2b97a43541a804d0c8b7a9bf78430c90bd832a0cbc0e640347db6` |
| `_verifiche/verifica-elenco-trentatre-nomi-p2.md` | 12.157 | `b2ef83d9301731bb1cffb623e556e49ef7231488ff56cfbe84c290861eb4c749` |

### Il dossier di invio dell'opera

*Proposte editoriali, lettere istituzionali, registro dei canali PEC, checklist di spedizione.*

39 file · 2.013.688 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.docx` | 20.322 | `4b717486889de92865213226662a23053381bb632bb46d74a5ed13fe93ab053d` |
| `_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.pdf` | 179.489 | `538c62dd8eef21b3c67b45507583ad614128303ec4411280251db0b7bda06131` |
| `_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.docx` | 11.120 | `ed966de551754f0f91d04ec3cafb07d0e015406defe3c97ee92586bc5dd13e69` |
| `_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.pdf` | 68.198 | `1f1258f66eca2288ebbf9713f94660286afdcd2c20a6960837bf893e323a1b1c` |
| `_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.docx` | 14.176 | `6ea34703764c1943de0fbc7f2e90b384b33a35485cabca99675d5942c1917aaf` |
| `_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.pdf` | 111.028 | `f171363746f94bea3a5967b2e3aec49db15427d3b595fb8f043459c4c196680e` |
| `_diffusione-opera/CHECKLIST_DI_INVIO.docx` | 18.803 | `a0903183affb554f6e8db3598842f17c284848a5c3771fcba0e13ffb54366ee9` |
| `_diffusione-opera/CHECKLIST_DI_INVIO.pdf` | 287.366 | `bbedd425f4ad9116455855e86972b54b066d371f476d580121687cb64feb492e` |
| `_diffusione-opera/DEPOSITO_ZENODO.docx` | 13.325 | `fa8e6332988a9bf3c9690b2f52301b414eb3dabf6b1e34efa50eb695a88ed534` |
| `_diffusione-opera/DEPOSITO_ZENODO.pdf` | 135.451 | `1ed7f53cf03a10665800a41356f060ecfe69f138cb49c4e18ae6e78059e80213` |
| `_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.docx` | 14.486 | `1835156c0e2af63623522b197f73bd92b9c3f6580addfb06541e6f1f7e8cc4f4` |
| `_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.pdf` | 116.292 | `faf63795044dbc21dfc26569e92e79fb37a30821aa0336afca1b6ec52c2d7fb7` |
| `_diffusione-opera/PEC_PRESENTAZIONE_CASE_EDITRICI.docx` | 14.068 | `c02bc243e061eb8951385f36a9ddaa6e793570f42b65aabca9bb65518e3f9ee6` |
| `_diffusione-opera/PEC_PRESENTAZIONE_CASE_EDITRICI.pdf` | 127.400 | `35992034157c8aa170624e7ba1eb229a877088dbaab9d84f219c58ec1f027756` |
| `_diffusione-opera/PEC_UNICA_FORMALE.docx` | 15.131 | `997726710a151eaf08b655b0f9b246bb56f219bb9ee7fdbd09e6a63e6e80260d` |
| `_diffusione-opera/PEC_UNICA_FORMALE.pdf` | 152.949 | `134d60fd72ab5ba04b1fa0a5c54c9e875ba66e46a7aa79e8db0fbbfaebc18524` |
| `_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.docx` | 14.603 | `ce85daa7c39ba30a579cf03f08c2ccfcb67452f3ab7ff398611164453af9bc3b` |
| `_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.pdf` | 123.104 | `92a25cc99000ab01bdabe58bb45dab17031fb637b15d4078bf7705a12efef63e` |
| `_diffusione-opera/README.md` | 5.988 | `f43a63f7edd0278959c22da7e4d87546b49e0135024607b19a926c37ee2fbee1` |
| `_diffusione-opera/RELAZIONE_SUL_PROGETTO.docx` | 19.323 | `4dbd5835118f431b59b69e57c1599b85acfec3d6b2f5d49772e5b6127dfe8f8c` |
| `_diffusione-opera/RELAZIONE_SUL_PROGETTO.pdf` | 188.219 | `202e2caef58e212c3d1b9e3d83d400f99b47c78a06bf4c1a30beaed6e0f64932` |
| `_diffusione-opera/RICHIESTA_ARCHIVIO_CAMERA.docx` | 14.305 | `d44aef616082e6dca4ca9bb4405bed258afa161efd7d8e47ee82106f8f675c16` |
| `_diffusione-opera/RICHIESTA_ARCHIVIO_CAMERA.pdf` | 155.543 | `c439a7986afb49df9826c68a5a6f36c1c660ff6f3106150cf2b3214b3c8f1847` |
| `_diffusione-opera/capitolo-campione.md` | 23.221 | `d7c27e0665b89564d9965bf2cc6df402c365a5329a62d2ff9a663193a30b610d` |
| `_diffusione-opera/checklist-di-invio.md` | 16.001 | `299f16a2007d6c30f7460a0d1410b231ff493f374b13d217806574aed2d53fe2` |
| `_diffusione-opera/curriculum-modello.md` | 3.886 | `79eae88d23ad05d9f280445583e3a80f589890332e1fc8724634033fd38f5a83` |
| `_diffusione-opera/deposito-zenodo.md` | 7.825 | `bcb0602860667fa212a586149adad7355d268883b2fc7b5dbe266db3f0c58990` |
| `_diffusione-opera/lettera-fondazione-aldo-moro.md` | 11.221 | `4a959a542a6e04b88caebf19a38e25cd6cfa2411a44d6c53e9c439a4575e977c` |
| `_diffusione-opera/mappa-dei-destinatari.md` | 7.354 | `bb0a4fea47582bf82a5d0f7fb7918597e5dfc00b11869dd7e64aae7217b2c545` |
| `_diffusione-opera/pec-archivio-flamigni.md` | 8.788 | `30629e30ed1efcac5f5cd02c9045533799c158ec45ea89255e20f0d37f1726fc` |
| `_diffusione-opera/pec-presentazione-case-editrici.md` | 11.642 | `85585b5fa7529000e99e6e6ac54707ddcb1460fc8148f7bf28bd8977b617b238` |
| `_diffusione-opera/pec-unica-formale.md` | 10.740 | `dff26be5c85227eeceda25bbb1abe0d04c1026ddefd234fce52ab61b9286c763` |
| `_diffusione-opera/proposta-editrice-laterza.md` | 7.268 | `95bbc96a9cb71a091b8cb17fb677579d3279a6858610c876c7adc73ef0bb5984` |
| `_diffusione-opera/proposte-chiarelettere-bompiani.md` | 12.600 | `6dc2656637650c502c0f91502ba9a9f452d3d408c0d3035b6d5f2f3216a27592` |
| `_diffusione-opera/proposte-mulino-carocci-einaudi.md` | 15.732 | `c168169988bc5011c5c455d1d5496602f19d7787813c6b613ad0ffe83fb9ed69` |
| `_diffusione-opera/registro-pec-e-canali.md` | 16.783 | `22358f8bcf18fcd512d3af1fbf7bba05b2fcdc623eb9d8ccec9575839f17eb4e` |
| `_diffusione-opera/relazione-al-centro-flamigni.md` | 20.353 | `5d9f5244bb68dd0a9bb523ccfbb4fd620cd2579d5374e9e8be96cd2bf8ff4921` |
| `_diffusione-opera/richiesta-archivio-storico-camera.md` | 10.286 | `e3aa116b1bbb789743b38f5f1748d5cc37d5da6715c5389b52e1c3f7759bd582` |
| `_diffusione-opera/scheda-dell-opera.md` | 9.299 | `dbd2b900d6872434872c9cd68cbad06d8b960ed714eef6d2071fe0b87b6c05fc` |

### Terza opera — Italia Nera

*Il Registro V77 e i suoi otto documenti compagni: opera autonoma, imparentata con quella su Moro ma non contenuta in essa.*

140 file · 40.759.569 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `italia-nera/README.md` | 8.838 | `d64f267fdf59c4f2b905c2522643c9564f8a8033c2d770fd117f2327f24d2570` |
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
| `italia-nera/apparato-tabellare/registro-analitico-dei-nodi-integrale.md` | 40.412 | `4583658eb5222a205d21774374fb864409b0157a0a54c02fba6f710c76973a46` |
| `italia-nera/apparato-tabellare/registro-unico-dei-nodi-v63.md` | 85.368 | `910eae5e835f1359edae9c684190a15b9a9913ffaaeaf343f1bd6c53408b61c1` |
| `italia-nera/apparato-tabellare/triangolazione-integrale-putin.md` | 9.450 | `6549c5e5b3a311223630cac2213a8daad68bb72df62c9723db5d7b5aadf6fc0a` |
| `italia-nera/apparato-tabellare/triangolazione-putin-e-galassia-nera.md` | 7.210 | `fa111a883aa775662f342c00ed0997f4a62d94858191cd25b1c0934aaf4dc602` |
| `italia-nera/apparato-tabellare/url-censiti.md` | 845.363 | `8d3039f318a707365a82c86f3ac18e9e5f0d1fb8fe60697ecc8d1506491b4b8b` |
| `italia-nera/apparato-tabellare/verifica-biografica-putin.md` | 7.079 | `b7a623b9c6867952d37ff7b190ff32ceb54f7a49b9a814a5e1139e64f4dbd4de` |
| `italia-nera/arsenale-sardo-delle-brigate-rosse-lula-1982.md` | 20.263 | `f4bf30f97de67c1bcde7e1d2596688f17a89f16c73b7cfd942efc2d716195765` |
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
| `italia-nera/censimenti/censimento-criminalita-organizzata-documento-unico.md` | 3.810.937 | `817dd93cf7b31c1485a8143155e7221b5f4025e9feac17cc170ff6212588bdf3` |
| `italia-nera/censimenti/censimento-dei-nodi-per-dominio.md` | 57.863 | `4100e74dca2a3a5c921d3e26b3a0a84ea94fb7490133bcd1409a9943a24b91ff` |
| `italia-nera/censimenti/schedario-aemilia-kyterion-grimilde-pesci.md` | 20.795 | `95e29906bae19c79ddb29e60f4be797717730fb1a3ae7473397b02b4d0ce50e2` |
| `italia-nera/edizione-v67/README.md` | 1.756 | `09289cd9c70f121883a060b87e3edec19567947bf20b5341bd3d5eec5d9f7a48` |
| `italia-nera/edizione-v67/atto-di-federazione-v67.md` | 16.681 | `7b661a2a1650509eeb7940d03f4e9a572bf97ab19bd009a00357d69bf572991b` |
| `italia-nera/edizione-v67/registro-unico-federato-v67.md` | 54.902 | `a476d58666335485350263cd733cbd05ea10c1991ca6de15f205a88f4df36848` |
| `italia-nera/edizione-v67/struttura-dell-opera-v67.md` | 55.940 | `1305d644e66d6edc6bef9a77dc6fbd4b792989e7e3b9a633d0d6a008e8c1ea1e` |
| `italia-nera/edizione-v67/tomo-primo-titanico.md` | 1.428.317 | `18ed8750bc88a19d9e525334bd9a292ce4e0144cfcbaac1703a048239953a9e5` |
| `italia-nera/edizione-v67/tomo-terzo-titanico.md` | 1.056.000 | `3da53a780c5a49cbc9f4a4597619ab1392711a70d16a6e706297a03df6801eda` |
| `italia-nera/fonti-cia-foia/sala-di-lettura-foia.md` | 2.912.455 | `411d1c72e9211498ce4390da25d271920d271f69d249b4ee47e1c93a37c6876c` |
| `italia-nera/fonti-parlamentari/README.md` | 2.711 | `ed5fa87de90bcb2900c201208be94c33fe0fd2a20f7597177a6b19f9998ff9b3` |
| `italia-nera/fonti-parlamentari/altre-fonti.md` | 403.277 | `9580407cfc050961d87d6d3b234e4059301c783c271d88267bd7b8998045c567` |
| `italia-nera/fonti-parlamentari/commissione-stragi-sedute-segrete.md` | 64.057 | `49b2a901639e4e9cfe8c5d760ad397698b68fa52c7e369a7a6d3e47503eed523` |
| `italia-nera/fonti-parlamentari/commissione-stragi.md` | 460.471 | `2793af14393d0033c1070181ba5da9fc862afc4a66f9582f4c5b96401aaa40c3` |
| `italia-nera/fonti-parlamentari/documenti-doc.md` | 476.125 | `ed61ac2a3be60802c4441a5d33d5bc8de164f6b3909131685053ffd945f91f68` |
| `italia-nera/fonti-parlamentari/trattato-di-pace.md` | 224.019 | `94c29cf8114b2d7f6b293bfa32758ee7eccb0f766d3301282d6956003360d453` |
| `italia-nera/fonti-parlamentari/x-legislatura.md` | 246.151 | `2542b3958352e79f7d329d764983dc3ce409e533126ebe350dfd4c80f0dc3eba` |
| `italia-nera/fonti-parlamentari/xi-legislatura.md` | 540.006 | `58351e8eb8342d01d09e1faafc5c02bf4db94d746adb54444ce90a75ee9292b1` |
| `italia-nera/fonti-parlamentari/xii-legislatura.md` | 751.578 | `0e541b5039c13fc6ba00768870c3992c8066f61a38e1fdf9985766b873f8e2a5` |
| `italia-nera/il-ponte-transatlantico-cinquanta-blocchi.md` | 50.630 | `9d15eb5df3a2be7bb26741dd573b9758a854a81d8a4671cd25ef8a3669f66d1b` |
| `italia-nera/libro-primo-italia-il-campo-di-battaglia.md` | 633.885 | `5fa4b18f96f236e974d0f80c8fc6a7b9d85fcca7c6321cbfd5e7082cc639b5c4` |
| `italia-nera/registri-analitici/README.md` | 4.041 | `3752f44e9c6504f55b67bb9d027cd2c7ff2b6836b14c3aa0af09871696bd2288` |
| `italia-nera/registri-analitici/analisi-strutturale-dei-file-caricati-v61.md` | 9.125 | `8312334967e3a875d545cd430f4765ff8d952e852ce8f4ddeefe22fd05557817` |
| `italia-nera/registri-analitici/atto-di-ricezione-integrativo-v67.md` | 19.222 | `957fb1a62531067301b5ebd183d529dfce22d28787c855ecaeb75728c504f744` |
| `italia-nera/registri-analitici/codice-relazionale-dei-registri-alpha.md` | 23.250 | `08d4c0d270ba521960de53dba6b23bd5925699d41da3af43e7f5360c9f33b0c7` |
| `italia-nera/registri-analitici/dossier-v7-chiusura-pendenze.md` | 157.351 | `6cf000ba5cce87623f82596e70776fcd4d2d2fcccb7de3d260236f5568b9f74b` |
| `italia-nera/registri-analitici/elenco-p2-per-fascicolo-v61.md` | 12.019 | `929e71b27eae84a765be7928ddd7d3901e60c5e81217263e1eb607ad715d79a0` |
| `italia-nera/registri-analitici/estrazione-nodi-d1-criminalita.md` | 6.824 | `6eebd7006ad08efb28e93633089cb11cfc28bfd2dfffef8d55112291d1d2c96a` |
| `italia-nera/registri-analitici/prompt-evoluto-v64-registro-unico-federato.md` | 34.539 | `7140c63f38052491cb20bc2af8990ee4d9f3565faf3f49c8245208731839c80c` |
| `italia-nera/registri-analitici/prompt-evoluto-v65-metodo-e-camera-istruttoria.md` | 53.789 | `51e19618abcd70fa3998febeccdfa7d95ddede93b3619dc1219914d34e29c107` |
| `italia-nera/registri-analitici/prompt-evoluto-v65-strato-elitista-formalista.md` | 23.724 | `e51178ced6f1e314f303721a1b7176acfcd4cd93e74155c483d34962e44db2d9` |
| `italia-nera/registri-analitici/quarta-serie-cinquanta-blocchi-certificazione-v70.md` | 26.053 | `819be38e27aaa4f703f7413049e255b34fa45f67733c2698d7f9cb302ebb27c9` |
| `italia-nera/registri-analitici/registro-dei-candidati-alla-formalizzazione.md` | 1.580.232 | `5855cc314dcdc031fb1060cc07b7fdd99452fb7f94d48632029b71d56aadc88e` |
| `italia-nera/registri-analitici/registro-dei-dossier.md` | 47.128 | `003fc9188cc2442931d6b2a14db51e1860a77433675e3ae16b71b17c031af540` |
| `italia-nera/registri-analitici/registro-dei-pattern-avanzati.md` | 29.145 | `d2fe957c48c0998bd5891b30666164cd25334be00eadc369d0f8cb145672d4ea` |
| `italia-nera/registri-analitici/registro-di-triangolazione-sacro-guevara-moro.md` | 78.414 | `64cf3d97c11d8128daf388d2e189f3cfe50b24bf9868457349e53167392a67ae` |
| `italia-nera/registri-analitici/registro-dominiale-d02-potere-politico.md` | 107.769 | `c5c9fa22a6b17c1feaa256be283d60c1c988ee12c6106aaf3f2f472763e73538` |
| `italia-nera/registri-analitici/registro-dominiale-d03-intelligence.md` | 40.872 | `c401e8c62c338cb3e3cfb6b6e21c2227c292e05f2d1b961d6e30b052b474f529` |
| `italia-nera/registri-analitici/registro-dominiale-d04-massoneria.md` | 20.306 | `186a02d273e36a8eadb5730261350456f96d93d07ea620025bf4b953c972dd17` |
| `italia-nera/registri-analitici/registro-dominiale-d05-istituzioni-religiose.md` | 22.727 | `06f14d969b35f85df61ac38a49086aa03fc41888ac673123421e67f55f95834b` |
| `italia-nera/registri-analitici/registro-dominiale-d06-economia-finanza.md` | 22.540 | `ba3b7d533824a0cf70e8684fbd57892c0f09f5454a4f5a4d3150b0b2600cb6eb` |
| `italia-nera/registri-analitici/registro-dominiale-d07-terrorismo.md` | 50.684 | `e7df970b1fce755f5e86587d5dbf812eb776e149f647dd8c1081451acec78361` |
| `italia-nera/registri-analitici/registro-dominiale-d08-media.md` | 12.863 | `5775a59963ff52d29395e386505c0ae769b17ad0d78bb26646edd8a1bfead7c1` |
| `italia-nera/registri-analitici/registro-dominiale-d09-forze-armate.md` | 43.968 | `881c56ea38d5bb95704463e76556d295a27ad931a1636404fb6c33acef3a89d9` |
| `italia-nera/registri-analitici/registro-dominiale-d10-magistratura.md` | 19.866 | `dc11c2d05c8139e562ec523b442652248bf8abe9379502b207f14527289f66a2` |
| `italia-nera/registri-analitici/registro-nodi-aginter-asse-asiatico-pacifico.md` | 59.680 | `01ffd5c34b82d49e4db7cb565c16870cef7205a2ebb3e00bc335ff07df705e7f` |
| `italia-nera/registri-analitici/registro-nodi-aginter-sudafrica-sudamerica.md` | 80.921 | `ac54ff77e71f9372f65a18c8a421c10dd1c3543803c370f70e08f4b6153bab58` |
| `italia-nera/registri-analitici/registro-nodi-aginter-sunniti.md` | 55.876 | `234c32956d7d62596364620b083ae0b882731ee264220202601be9dc67afcc65` |
| `italia-nera/registri-analitici/registro-nodi-antartide-aginter-golfo.md` | 17.243 | `82732cd494df7b66e9c5a60fc6742994f8510358be5695bfb174ebe30826e76d` |
| `italia-nera/registri-analitici/registro-nodi-corpus-guerra-fredda.md` | 77.959 | `5b901834df3f30f766bbc631a0befd8e24f659fc0a24acc6f519dcf75be6382b` |
| `italia-nera/registri-analitici/registro-nodi-paypal-apartheid.md` | 62.069 | `fff2ae0cbd67a8de1ebdcad950c523a6e5176282f51b27f569d574efebc5b3db` |
| `italia-nera/registri-analitici/registro-nodi-sessione-2-agosto.md` | 42.683 | `fb8cff3387c1d58404f461469047821b0e4db3caf8981d039e9db25a5ab3ee5e` |
| `italia-nera/registri-analitici/registro-sinaptico-generale.md` | 515.916 | `2104977cc6c5b5b9ea2f340044223dcf9383a97471aa3e094785766f5507f6ee` |
| `italia-nera/registri-analitici/registro-spaziale.md` | 30.531 | `da270bf3a9259c449f03ce1691ee0353c95e7e6ffafdd190e791f5996030b281` |
| `italia-nera/registri-analitici/registro-temporale.md` | 31.057 | `65665324c226534a20d33b1eb2953fe93de1144947e153ee55507f33c04ceb77` |
| `italia-nera/registri-analitici/registro-unico-dei-nodi-v63-nota.md` | 6.366 | `a22c3371f7c53b14a5ac6afbed54d0d042dd6179e14e900f71bd2bc22c2e5270` |
| `italia-nera/registri-analitici/v75-struttura-e-triangolazione-moro-che.md` | 68.369 | `6c5afaae04ec22cc9b07c4b3aa774434100237c16c721708c9cb9749e10ad649` |
| `italia-nera/registro-analitico-dei-nodi-cinque-documenti.md` | 25.523 | `b722a90762a44da25bf2e65183dd379e3478696f9aa04bfd13df01ab2d904a05` |
| `italia-nera/registro-analitico-dei-nodi-corpus-aginter.md` | 79.913 | `1945eaafca258aaa56fa01fce5ad0afaeeadab1d68c440afc1b1eab4a7a96c37` |
| `italia-nera/registro-v77-l-opera-simile-a-se-stessa.md` | 13.619.501 | `0462c33417891471f1353899cc10bc4dea5283460399528ef6bf254ea9af7f84` |
| `italia-nera/ricerche-approfondite/README.md` | 5.352 | `4bdd3b033986520a782039bd757f5f8b2fefa4826f1fc474111348b58cf633fe` |
| `italia-nera/ricerche-approfondite/architetto-del-caos-dugin-e-l-eurasiatismo.md` | 123.179 | `c75ed84d22d1cc417f46002dd11d2a3d708e5bf338090f629f4f040489f1b023` |
| `italia-nera/ricerche-approfondite/ayman-al-zawahiri-radici-e-reti.md` | 54.120 | `b31d44e791a22703ea539f81bc5c83e9df57ff404eba2a6139542276077d7969` |
| `italia-nera/ricerche-approfondite/internazionale-parallela-gli-accordi-bilaterali.md` | 16.637 | `60921953b3e5b56e3eb623908c2d4384bbc8db7b6108046f9e0225ba8ab9e03d` |
| `italia-nera/ricerche-approfondite/le-cercle-architettura-occulta.md` | 42.525 | `83ca7f21180ac0153ec274c48cd54f74646464981d7348d6ce729c03776d2ae7` |
| `italia-nera/ricerche-approfondite/nazisti-in-urss-l-esodo-tecnologico.md` | 73.994 | `d0522de8a19c8fc43eb8503db7b201359186feae27908e0dfabbdc6eb3d40dc6` |
| `italia-nera/ricerche-approfondite/network-finanziario-sud-africa.md` | 45.255 | `b49b88bfa806f1f491f13feb93c6a4d31872752209c889823b0c6b9edddb3d43` |
| `italia-nera/ricerche-approfondite/ordre-et-tradition-e-l-ecosistema-del-terrore.md` | 42.481 | `281d526a523305aad9451cf23af0bed9dc40a97d37aa74a3be5ae140c1f1f8c8` |
| `italia-nera/ricerche-approfondite/russia-unita-la-diplomazia-partitica.md` | 51.406 | `c17f8f22cff788bab2beb348239b34d821e6bf1072c2209515a3acc0f1a2b940` |
| `italia-nera/ricerche-approfondite/veritas-ubique-la-rete-di-aginter-press.md` | 45.969 | `2c33c77dd0f8aeaa9d7ae405ce29e191ec8ed8627724b0666325ee3e01950df1` |
| `italia-nera/scheda-di-consegna-aldo-moro-tutta-la-verita.md` | 4.200 | `67bcff5b9b826c64e487a0deb18d69b0e576c95167addfc27ba8224bfde10e67` |
| `italia-nera/scheda-ombra-kgb-e-riscrittura-dei-nodi.md` | 13.855 | `9a0069d16e1e05e75cb92896577ea3f775ee5d37eed80477b4e2d16dd215e250` |
| `italia-nera/schede-di-presa-in-consegna/README.md` | 9.688 | `ed6faf7af3f105493ca1637abda2175e093b9e09b2f2cd6ec37d9ea2b53d7a89` |
| `italia-nera/schede-di-presa-in-consegna/archivio-jprs-traduzioni-di-stampa-estera.md` | 27.879 | `e27f7e7e619245f49cad8d0b9542c8fe331f967c9335d0062f72850db08663ee` |
| `italia-nera/schede-di-presa-in-consegna/archivio-uno-documenti-cia-1946-1986.md` | 30.412 | `4a83cfedf3df6d05a7c22625da08f2d66f7d81c7631da7d4304dbe9f485a60c7` |
| `italia-nera/schede-di-presa-in-consegna/blocco-quarto.md` | 30.781 | `b21a1599c9ab18c8bb2572f6d93d2db3b85d2fb047fa890a1f4ec9c1736880ca` |
| `italia-nera/schede-di-presa-in-consegna/blocco-quinto.md` | 16.267 | `475e05ea3c741c7bbd99728813ea6962633763e7b747564c498b9b8268455f84` |
| `italia-nera/schede-di-presa-in-consegna/blocco-secondo-verbali-x-legislatura.md` | 53.805 | `e68430d43d7a1d493bf844b6b4955e7aeab6c90888abfa3aa734e8c38aa2a733` |
| `italia-nera/schede-di-presa-in-consegna/blocco-terzo.md` | 26.403 | `41830c4c2e62ae5dfb325851d65f187a5373a24a24094373488e776ece86ee6e` |
| `italia-nera/schede-di-presa-in-consegna/collezione-pre-1945-propaganda-fascista.md` | 19.686 | `e1806ea518d3485351dd0552c50f069b01241b365bb4e2c0e4c8e41e827d2422` |
| `italia-nera/schede-di-presa-in-consegna/scheda-nodo-wanda-vannacci-addendum-correttivo.md` | 15.365 | `4e7a27cbad73c545e9576b1a061b15b2e95ed4da8a583e28d7c5a649b6255321` |
| `italia-nera/schede-di-presa-in-consegna/scheda-nv01-msi-in-argentina-1952.md` | 7.051 | `f90aeb09bce1a37a97852747d4a26e6eca86fde2f67948e2ba151665a27228fb` |
| `italia-nera/schede-di-presa-in-consegna/schede-complete-ventotto.md` | 55.889 | `f0d0ce241d3dfad10f54db0260db10b4a3271c2c80b62350c49b181505ec0929` |
| `italia-nera/schede-di-presa-in-consegna/schede-unificate.md` | 958.058 | `25ae9aa833c0abb364c22599a8c456620676f3805c852234974576c8992dbfe4` |
| `italia-nera/schede-di-presa-in-consegna/triangolazione-schede-dossier-v63.md` | 29.941 | `c044e255c9840edd89fa0ea623a6fae1a6b8133923ae78d7338469431f8f877e` |
| `italia-nera/schede-di-presa-in-consegna/v63-scheda-diagnostica-computazionale.md` | 13.514 | `1ca7bbfe01113fc55140d03c83803b8a6a5acfc7444a5bd4a6400c02b3c7dbec` |
| `italia-nera/schede-di-presa-in-consegna/volume-02-tomo-i-allegati-doc-xxiii-2-quater.md` | 54.783 | `bbaf2754a3716d58cd8ad6cb12e07c8b11a82d872b903e05acba9418164a1eca` |
| `italia-nera/schede-estratte-lotto-primo.md` | 52.043 | `c7621a9212aeca6568c0f0127a855d7d36ebb37e1a14f3e228ebb7b52d5177c8` |
| `italia-nera/schede-estratte-lotto-secondo.md` | 62.516 | `0e6df5b9e16e1219b0962af74a234d743d96f121a998346a60f2de59bd493ab4` |
| `italia-nera/schede-nodo/README.md` | 3.367 | `aadc96b5bae7ea63fd1bcd0a6948f70cf050ec8286e352e5ac88467614bdc4cd` |
| `italia-nera/schede-nodo/nodi-criminalita-organizzata.md` | 169.192 | `d4658faa208cab4c913715ee999fbce9e19c7ed47deb7d81a4e23ea8ccbaee93` |
| `italia-nera/schede-nodo/nodi-dominio-decimo-sinaptiche.md` | 328.778 | `6447bd374d2246a9b5b7d4f56c2451373b34c2e613dbf73147be4458d8180d70` |
| `italia-nera/schede-nodo/nodi-dominio-sesto-sinaptiche.md` | 164.183 | `499035ea859a6e776d2c660351a469b8feabb0aed54dc80b18b4b83f9d076a33` |
| `italia-nera/schede-nodo/nodi-economico-finanziario-sinaptiche.md` | 167.564 | `49e04b73ee93b2904999a4688c8c707711f9c32c887ef2769adbce0e9fae5964` |
| `italia-nera/schede-nodo/nodi-intelligence-sinaptiche.md` | 634.216 | `fe0afbf02958b206920bf5e72ac626fe73a16d9965d7820792d240bcd699f807` |
| `italia-nera/schede-nodo/nodi-intelligence.md` | 132.706 | `ae57d44500b60e8ac722e7c5801050e62f59ef649a208803d64c24d6420b01b9` |
| `italia-nera/schede-nodo/nodi-religioso.md` | 158.734 | `78015fccf5a826445945be0d5c370283f72579059a09cf2f39ca1dfbf0fa68fb` |
| `italia-nera/schede-nodo/nodi-stampa-sinaptiche.md` | 84.077 | `03bed6b04ad471a49663706ff33f56c0e1d1718f2739f706b1b03e5a2c27a07b` |
| `italia-nera/schede-nodo/nodi-stampa.md` | 16.232 | `9a2bd007a989b4c0dbc6cbb582096342292e2d53f43e016a1f8da144bf706d7b` |
| `italia-nera/undici-nodi-ex-novo.md` | 9.968 | `1861b577eb501d0e881772765b01241105de33c066567bc8331c66b11241442c` |
| `italia-nera/v68-libro-secondo/README.md` | 2.734 | `73178a224837ca0fec23e0593fcd9945dc2aac2e2117f4710308e54fdf57bc42` |
| `italia-nera/v68-libro-secondo/tomo-decimo.md` | 1.963.725 | `98945ecb95cc42d1bc8203dd396f5c4df9081e7e8e4959415032a28b4059b065` |
| `italia-nera/v68-libro-secondo/tomo-nono.md` | 229.754 | `1c794bd234f0864daa8fffa600589715a97da4230fc189b6288fab848fdc34e4` |
| `italia-nera/v68-libro-secondo/tomo-ottavo.md` | 337.029 | `774e55ffaa846ad14fe47f0cac74d1c7b628577f0728c68caba2352e7de8ca69` |
| `italia-nera/v68-libro-secondo/tomo-quinto.md` | 326.129 | `127e4ba66650a88874330fefd445cab16d3db9772baf41bf24aae56c3e59ec29` |
| `italia-nera/v68-libro-secondo/tomo-secondo.md` | 488.925 | `34e75d16d659a68eb4399ad6fb2e889acde44f18af928fe4b44b17341349c11a` |
| `italia-nera/v68-libro-secondo/tomo-sesto.md` | 332.111 | `f16d11886540d06d12601047116b4bb9c2c32adf8acd9138cce8e4dcf771acff` |
| `italia-nera/v68-libro-secondo/tomo-settimo.md` | 554.860 | `fa40a37fae18c083c51ab754c7fc26fdb57b39b6e0619dd3972e0aa89dc5701c` |
| `italia-nera/v68-libro-secondo/tomo-terzo.md` | 512.433 | `0cc3d6d721a34d85ccc59efdda346c847a23bde46d9b0aeae976e9f4ab3818d5` |
| `italia-nera/v68-libro-terzo-il-cantiere-di-riserva.md` | 332.945 | `c9eefcff43d6baed371a976e6429c712ad25c8ff7192df1b5e5a71045f7f4d03` |

### Opera derivata — il romanzo

*«Ottanta anni di Pace»: i sette capitoli, il volume rilegato nelle tre forme, le note di revisione. Si ricava dal corpus e non ne fa parte; e' certificata a parte perche' contarla dentro l'opera sarebbe contare due volte cio' che l'opera ha prodotto.*

14 file · 1.203.660 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_romanzo/OTTANTA-ANNI-DI-PACE-prima-stesura.docx` | 75.549 | `7bb0028b0114e6241c9ec4c67213b1a9a6dfc9ba378f12f9afdd1c08a4a36aa1` |
| `_romanzo/OTTANTA-ANNI-DI-PACE-prima-stesura.md` | 135.652 | `45b1724d9fc87c37a6e20a37a169e64fd77a2a056f74e4314a72394336feab4d` |
| `_romanzo/OTTANTA-ANNI-DI-PACE-prima-stesura.pdf` | 803.987 | `a6324f9708bb92125865c072018b60958307c637a818b3afeb121e89d9465dd2` |
| `_romanzo/README.md` | 16.781 | `7a7c172f8fd18cfa292da70a374c593d36f2e966b9b5c3bc546e61411a71e383` |
| `_romanzo/capitolo-primo-l-elenco-che-arriva.md` | 15.907 | `3719b925083828c4b6c74cc1a3dece9466a2583fb12984547b9825c3b484180f` |
| `_romanzo/capitolo-quarto-le-lettere-scelte.md` | 15.570 | `20884d60c8f5c132b0ef8a8bb4cc42623cba5a1fbb71e37a65574a8b8bd903fd` |
| `_romanzo/capitolo-quinto-l-archivio.md` | 15.554 | `237a5908f72e712d9764908f32fa9cfc25853a5166624c3660bd60ad3bea7b4a` |
| `_romanzo/capitolo-secondo-l-uomo-prima-del-caso.md` | 15.086 | `c4fc2683f2a78bf5ba188675d388e6db0860c9af80d4c1bf6aa4b86503f2d1ed` |
| `_romanzo/capitolo-sesto-l-aritmetica.md` | 19.193 | `99a5abf47e7d45bc9d1a4364ed0fc08fe9ca7701779300da6e69afbfb54450cc` |
| `_romanzo/capitolo-settimo-ottocentotredici-volte-non-trovato.md` | 18.609 | `07ea9316eb13dabe1dbef5d9b64f448bf2afc5de0eaf2036bbda8ca3a65eedd4` |
| `_romanzo/capitolo-terzo-gli-anni-della-farnesina.md` | 19.412 | `88c97a022c5cce5c2117070779bd325f0d0fd57b6bb55e66912b26bf39c81ee1` |
| `_romanzo/nota-sulle-fonti.md` | 9.088 | `7e77efb47cb95731a25afbaf20380986aad0bd926671cdeb3f36a01e7d581cf3` |
| `_romanzo/note-di-revisione.md` | 33.331 | `89311a2d8e596300c841fb2d33e9401072b349cf2856adef36cb5d4d6566591c` |
| `_romanzo/registro-di-chiusura.md` | 9.941 | `76edf449864e2f5d16ff0b8779ad70ecdf42204f35013ba9bf85ddebd72d7149` |

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

*I pacchetti che si consegnano interi. L'archivio unificato raccoglie in una sola consegna il volume, i volumi singoli, le centoundici sorgenti, i generatori, le impronte e i grafici: 90,8 MiB, oltre il limite del canale, e per questo diviso in quattro parti complementari che estratte nella stessa cartella lo ricompongono. Non sono versionati: duplicherebbero cio' che il repository gia' contiene, e non entrano nei totali perche' sommarli conterebbe due volte gli stessi file. Sono elencati qui quelli che esistono al momento della rigenerazione: un archivio costruito su una edizione anteriore non viene ridichiarato, perche' la sua impronta resterebbe esatta mentre la descrizione che l'accompagna sarebbe scaduta.*

6 file · 211.848.970 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `OPERA_INTEGRALE_E_UNIFICATA.zip` | 95.230.730 | `9cfa74a81a34b0c80d0cc73ae4cc78537a4aa57322ff1a1aa4f81cebe3b99c79` |
| `OPERA_UNIFICATA_1-di-4_IL_VOLUME_PARTI_I-II.zip` | 24.794.565 | `3ed66d9423d7d99fdd5805d17418a723712c79cc690b856fa98c3b9278023f61` |
| `OPERA_UNIFICATA_2-di-4_IL_VOLUME_PARTE_III_E_DOCX.zip` | 19.230.744 | `ba5c6f43c41d12e005c3a6234ae65836a5abbd0b0de9d56063d94c926c11da76` |
| `OPERA_UNIFICATA_3-di-4_I_VOLUMI_SINGOLI.zip` | 15.202.368 | `a9bccd7b356caaa9ab010e9e7f07774f26ea2064f6656e520af1920d89a43b38` |
| `OPERA_UNIFICATA_4-di-4_SORGENTI_GENERATORI_IMPRONTE_GRAFICI.zip` | 5.460.206 | `22bdc0f53de76513f4e5eed6639ea6ba6b9d2486606e6e7f97ebedea8bbef139` |
| `OPERA_INTERA_CASO_MORO.zip` | 51.930.357 | `76c8763bc4282bb819cf416712c39feb993f938da1bb8ef02bcf327c2a5cd288` |

### Il volume diviso in tre parti

*Le 2.425 pagine dell'edizione integrale pesano 37,5 MiB e il canale di consegna ne accetta 30: il volume viaggia in tre parti, tagliate su confini di Libro e non a caso. La prima porta dal Portale al Libro dodicesimo, la seconda i Libri tredicesimo e quattordicesimo, la terza il Libro quindicesimo con le quattro Appendici e l'Apparato conclusivo. Ogni parte ripete la copertina, cosi' che nessuna arrivi anonima; a parte quelle due pagine le tre non si sovrappongono, e la numerazione del volume intero e' dichiarata nelle proprieta' di ciascun file. Non entrano nei totali: sono lo stesso volume, tagliato.*

3 file · 30.075.131 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `OPERA_INTEGRALE_1-di-3_LIBRI_I-XII.pdf` | 14.564.401 | `0ba64daace51ee69648bbb4e529f5e78c094b4ae16893ad967aa48ae0f6490da` |
| `OPERA_INTEGRALE_2-di-3_LIBRI_XIII-XIV.pdf` | 10.160.957 | `c5aa4b575afd0050a29503a0201ab866623de08c3e8378352c94e9cc8c21c09b` |
| `OPERA_INTEGRALE_3-di-3_LIBRI_XV-XVI_E_APPENDICI.pdf` | 5.349.773 | `608fb174c649700787e95825fa2f424360832a283a6de89f5ae185eb3bc49ca7` |

### Il pacchetto dei grafici

*Le nove infografiche della verifica, la nota di metodo e l'archivio compresso. Non sono versionate: viaggiano a parte, e per questo l'impronta conta di più.*

15 file · 2.138.177 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `10_le-due-numerazioni-sulla-stessa-retta.png` | 104.252 | `94870100455a3514766df6e89095fe914d1e378ae17b315c443aea622f02b9e7` |
| `11_scarto-dalla-retta.png` | 137.029 | `bd044e395e4454d0cbda18fe6b938110b796b01f3a41b1f3cc2260710ab01ae8` |
| `12_un-archivio-deriva.png` | 83.468 | `5c273ae8c02eca58ca5d142ace63eb81943862d10cbddee8be7f31c795b9fdaa` |
| `13_lo-scarto-congelato.png` | 124.284 | `c4f645fd1e408250148ccb3e356d5c789d1b2213677e008050626d887e551e0d` |
| `1_imbuto-della-verificabilita.png` | 67.753 | `c6b0424bf2293c248575a66f2c44c790edc3c671adc190a94e8e0bbedbad3625` |
| `2_tessere-sotto-la-soglia-documentata.png` | 75.207 | `1a5c989e77f1e2c1b719d9eb6eae074b824bc6eb5cec4135303e7aecbf3c2832` |
| `3_i-trentatre-per-sede-istituzionale.png` | 71.597 | `f61a057b4315fd6eacf9a9a9726498dd1abdaa0e69d2285911274d4bc35a7f5b` |
| `4_composizione-documentata-dei-962.png` | 77.397 | `068e589fa336ffa8f587711677f87f195c4c4b72273516e2785dbc2fbf2acbe3` |
| `5_distanza-fra-i-fatti-e-la-prova.png` | 60.499 | `fc6860ccc09b8d17e2c7ae4d2627e3414d60570f0c447d34f2d2b82eb8eaeef0` |
| `6_finestra-sei-mesi-materia-disponibile.png` | 97.589 | `29db330279ad0a1b9bb8ebb51c06926d629387032f0613caf91825873b62e4dd` |
| `7_quota-dei-trentatre-sul-totale.png` | 67.111 | `09247c55e134b965157c3ce1a034611a5771e72b831488d5aea924496d887c35` |
| `8_date-di-affiliazione-disponibili.png` | 67.109 | `6b6c451f03a59689c3a9a4b45eca4e572d6a8e67e2c99569984bbde57f29b4f6` |
| `9_finestra-e-i-due-dati-datati.png` | 58.109 | `ca23774f52b68d21c204dca2f3d1632ef6917b6460331fc8f81b76a4d169b55a` |
| `LEGGIMI.txt` | 4.671 | `8f7bcae0efeb1cf9532ec1cb81d258cd6fe1bde5d336d1a743bd871bb290ca5c` |
| `GRAFICI_VERIFICA_P2.zip` | 1.042.102 | `29659110553a69f3501aeddd54e5063778997182ad7e6be9b84770ede66ccb7f` |

---

## Il commit, che è un'altra cosa

L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git:

```
8b4266cbf1ca2762de7b266c10a696567de143ca
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
