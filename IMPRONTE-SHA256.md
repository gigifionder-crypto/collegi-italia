# Registro delle impronte SHA-256 — tutta l'opera

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file dell'opera porta qui la propria impronta crittografica: non i soli
volumi rilegati, ma **tutti i 209 file** — le sorgenti in markdown, gli
apparati, i tracker di lavorazione, il dossier di invio, i generatori, il
pacchetto dei grafici. Chi riceve un file può accertare in un comando che è
**bit per bit** quello depositato, e non una copia alterata, troncata o rimontata.

**Stato al commit `a34bf3dc6cdd`** del ramo `claude/amnistiati-tribunale-speciale-a82lzn`.

---

## L'impronta dell'opera intera

Una stringa sola per tutto il lavoro. È l'impronta del manifesto, cioè del file
che elenca i 198 file versionati con la loro impronta ciascuno:

```
4672f939f1d09aedc041b100bc1ab70075b694fdb8faa2d7c5f1e6760c5f543a
```

Non è ricorsiva — il manifesto non contiene sé stesso — ed è riproducibile da
chiunque, in un comando:

```
sha256sum IMPRONTE-SHA256.txt
```

Se quella stringa coincide, **l'intero corpus versionato è quello depositato**:
non un file di meno, non un file di più, nessun file diverso. Se differisce,
il confronto riga per riga dice quale.

### I due file che restano fuori, e perché

Il manifesto elenca ogni file versionato **tranne due**: sé stesso e questo
registro. Non è una svista ed è l'unica esclusione. Un registro non può
certificare sé stesso: i suoi file cambiano a ogni rigenerazione, e l'impronta
che vi si scrivesse dentro sarebbe falsa nell'istante stesso in cui viene
scritta. La catena si chiude comunque, e senza circoli: i 198 file
sono certificati dal manifesto, il manifesto è certificato dalla stringa qui
sopra, e questo registro non ha bisogno di esserlo perché **è interamente
ricavabile dal manifesto** — chi vuole controllarlo lo rigenera.

---

## Come si verifica

Tutti i file versionati in un colpo solo, dalla radice del repository:

```
sha256sum --check IMPRONTE-SHA256.txt
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
| I volumi rilegati | 28 | 56.474.748 |
| I documenti del corpus | 43 | 6.018.748 |
| Il Libro dodicesimo e i suoi originali | 15 | 1.115.047 |
| Le verifiche e i generatori | 9 | 155.904 |
| L'apparato editoriale | 28 | 1.490.636 |
| Il dossier di invio dell'opera | 27 | 1.267.571 |
| Il dossier di diffusione anteriore | 5 | 22.024 |
| La pubblicazione finale | 13 | 123.536.718 |
| I livelli della piramide | 8 | 54.505 |
| Il paper accademico | 7 | 396.324 |
| Tomo I — Puglia | 8 | 27.135.817 |
| Tomo II — nazionale | 5 | 3.833.161 |
| L'estensione ai ventisette | 2 | 349.771 |
| Il pacchetto dei grafici | 11 | 1.268.605 |
| **Totale** | **209** | **223.119.579** |

---

## Le impronte, sezione per sezione

### I volumi rilegati

*Le edizioni tipografiche in DOCX e PDF: è la forma in cui l'opera viaggia fuori dal repository.*

28 file · 56.474.748 byte

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
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.docx` | 8.043.958 | `41dc4eb842a907aedaa3356f5133e99959ef87133266b0181559b4941b36f85c` |
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf` | 27.778.565 | `39ee2bab1f7b34a96954b508e899d0224141b9e1338e3ee057fd186eef3c8b4e` |

### I documenti del corpus

*Le sorgenti in markdown del Portale, dei quattordici Libri e delle tre Appendici, con gli indici e gli apparati.*

43 file · 6.018.748 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `.gitignore` | 97 | `7dac985ee724aa40946e756bf4b4eeb4149ab170c7a3c9c28557832694357e78` |
| `GUIDA-ALLA-LETTURA.md` | 22.317 | `62b5db321abf9413a22151da0ff2a7d10c7a78c9afc4b001116c7f04160dfd5e` |
| `INDICE-DOCUMENTI-BRANCH.md` | 69.184 | `1cd87f7e211616b93864ff61080c22b9ca9024da2adb0dbbecd8d728a162e056` |
| `README.md` | 1.841 | `e546510b9cea21ad289c0fcf4d20e723675f556b69c9e502f5a3e598bcad912b` |
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
| `il-meridiano-e-la-valle-mille-blocchi.md` | 504.216 | `f966f97e815ee946ffc7dcc5abfae49511dcb615e369517547ce593e19c0a278` |
| `kissinger-mille-blocchi-il-codice-e-la-sua-trasmissione.md` | 2.400.306 | `754eea844fde0a471f13b549805f85814c2fd507dc1a7a84f2769af06ec5beaa` |
| `le-pene-oltre-confine-mitterrand-mulinaris.md` | 12.314 | `620e2299da71f18efc52bc13f7f4743211f1709a523c843eb1bf37fbfd5b8138` |
| `manuale-investigativo-nuovo-caso-moro.md` | 104.736 | `8669efe737f67785354604348850f5843185efbbc266a5cb2ce124ea8004a74b` |
| `metodologie-del-dossier-sinaptogenesi-e-strumenti.md` | 15.749 | `2b6f198ec9cf61b850bcf1aa392f7c65e61d4b5c6df8bf7a90305797cda54cf9` |
| `note-bibliografiche-opera-integrale.md` | 131.027 | `fe0c3de45a90e4123da4b5a91d3212af1a6be3881d3f5ae8e32439c4f6b7977f` |
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

15 file · 1.115.047 byte

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
| `moro-ministro-esteri/triangolazione-seconda-campagna.md` | 39.418 | `574b3a22479712cd9288b97ba5e2d76daa98ee5380cda9411917547f23cd5864` |
| `moro-ministro-esteri/volume.html` | 560.334 | `aef519447a3d02869ee9ee70dce6c61bce7a73577bf3cfbc282b57f9cadaf96f` |

### Le verifiche e i generatori

*Le schede di verifica e gli script che ricompongono l'opera, i grafici, le note e questo stesso registro.*

9 file · 155.904 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_verifiche/generatori/b_integrale.js` | 18.783 | `8c170c8d156f789e856038afa6053e911dcdf8adcd397366f4ad28fe0e2e1fd7` |
| `_verifiche/generatori/build_impronte.py` | 11.119 | `502132b99e37460a77a7cf8fba0c6e6715213faf9ea585a8ac3b7a5a9fe58832` |
| `_verifiche/generatori/build_tessere.py` | 25.343 | `795feb08d704126b151de3fe52429e6ebd0dc269f3cc908c9151974b94023de4` |
| `_verifiche/generatori/gen_figs.py` | 36.305 | `e77d2d595c8e2811241e8f20262f12707ff38df49bd1d463e1ae6b8d175edcb7` |
| `_verifiche/generatori/gen_impronte.py` | 5.991 | `43c0e72df59b31af348f0e7495a22d5822666678a904455c8b0aef71272c2c5c` |
| `_verifiche/generatori/gen_note.py` | 11.211 | `425117297d8049ad0db79528c01499483aaa3ec40b3fd315ade9be4e5705b439` |
| `_verifiche/generatori/gen_verifica_p2.py` | 19.504 | `4f2ccd98963d24d8056fcffaf0bdf54fdb10ebdf3d2f3715228b3b0d3804da90` |
| `_verifiche/generatori/p_integrale.js` | 17.168 | `e6cc7a61c5bd2412c9e076dc742aa119d265e911c2a8be803d89bbf70169bed0` |
| `_verifiche/verifica-elenco-trentatre-nomi-p2.md` | 10.480 | `9e6f006abf38a98db9c2d3212a42f60ba244ed0e077de2a1fa683d90ca29ae85` |

### L'apparato editoriale

*I tracker di lavorazione, il registro delle anomalie, il parcheggio delle decisioni sospese.*

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

### Il dossier di invio dell'opera

*Proposte editoriali, lettere istituzionali, registro dei canali PEC, checklist di spedizione.*

27 file · 1.267.571 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.docx` | 20.326 | `9de0e634426c0858df09651df91f6bc492eaed9cd4d5056db92f505792bf6b61` |
| `_diffusione-opera/ALLEGATO_CAPITOLO_CAMPIONE.pdf` | 179.489 | `d3313336dfb423b6affdd1da96a96621825e32ca864e5d01f3162ca17afe795d` |
| `_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.docx` | 11.122 | `3dd1698f7e8e28502b5f276f13b76353207f905ef540ec6253506fc153f16f77` |
| `_diffusione-opera/ALLEGATO_CURRICULUM_DA_COMPILARE.pdf` | 68.194 | `1679e644e4cb2b997f51bdff063861e673db3c1a31bdc12d0a26b96da5e885d7` |
| `_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.docx` | 12.441 | `bc17d247537bafb1592522f41dc512e823728321cace97c623dd8d009b9df629` |
| `_diffusione-opera/ALLEGATO_SCHEDA_DELL_OPERA.pdf` | 83.574 | `da083701451198a7a637c4ef26bdca86360ab1b1b436b1d50750aab872bf3b72` |
| `_diffusione-opera/CHECKLIST_DI_INVIO.docx` | 16.717 | `8c2a49fe51da6c1da0ffe5fc34607540b60a4876c9ed969dbae54cfe90ceaae8` |
| `_diffusione-opera/CHECKLIST_DI_INVIO.pdf` | 253.683 | `cf18fd83d2c0c44d3077b7dca2c134ffeab878e47a184eb305df15177d31ee2b` |
| `_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.docx` | 14.486 | `8be32daee50c816defecc858c4158e2b47551685dc1216f65dd9dab5a7777441` |
| `_diffusione-opera/LETTERA_FONDAZIONE_ALDO_MORO.pdf` | 116.297 | `491f01810ea65860f0280518cf00e88613b0a103caa285be3e7e4c738901840d` |
| `_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.docx` | 14.346 | `f8d6c5125ea24fb820f48ddeb46b453b43a88be4f79f12849a13a20ca6512859` |
| `_diffusione-opera/PROPOSTE_CHIARELETTERE_BOMPIANI.pdf` | 121.064 | `f5b631c51dda261ffec8d0767b5db101f0a3f2b0b067307a691b8e9180ef8de3` |
| `_diffusione-opera/README.md` | 5.894 | `15fdb4e0141aacb9cb9ad3266f27da27b5f2f7710353e597d15822d892d85162` |
| `_diffusione-opera/RELAZIONE_SUL_PROGETTO.docx` | 19.324 | `88a58414ef650e5e6f75be537c1440a9ed363f68a31d2a4db4d0c3cb0b3d19cc` |
| `_diffusione-opera/RELAZIONE_SUL_PROGETTO.pdf` | 188.220 | `9d2644e9d3065f25384b652f9ad28460982f3689416a80510fa7ed929c667403` |
| `_diffusione-opera/capitolo-campione.md` | 23.221 | `d7c27e0665b89564d9965bf2cc6df402c365a5329a62d2ff9a663193a30b610d` |
| `_diffusione-opera/checklist-di-invio.md` | 12.083 | `7452685bc08372ab0a8ef6f0d13ce26a2799b0ea74cd0fac7eeb84faf876b390` |
| `_diffusione-opera/curriculum-modello.md` | 3.886 | `79eae88d23ad05d9f280445583e3a80f589890332e1fc8724634033fd38f5a83` |
| `_diffusione-opera/lettera-fondazione-aldo-moro.md` | 11.221 | `4a959a542a6e04b88caebf19a38e25cd6cfa2411a44d6c53e9c439a4575e977c` |
| `_diffusione-opera/mappa-dei-destinatari.md` | 7.354 | `bb0a4fea47582bf82a5d0f7fb7918597e5dfc00b11869dd7e64aae7217b2c545` |
| `_diffusione-opera/pec-archivio-flamigni.md` | 8.788 | `30629e30ed1efcac5f5cd02c9045533799c158ec45ea89255e20f0d37f1726fc` |
| `_diffusione-opera/proposta-editrice-laterza.md` | 7.269 | `9a66fe93f89ef6424713389e43f0845a4d89c866bbf677012dc2e3ddfd5f3578` |
| `_diffusione-opera/proposte-chiarelettere-bompiani.md` | 12.025 | `315d094a4056ce3eb09dfd6e2832f160ad9c3b22874c802c7b16d436819c2cec` |
| `_diffusione-opera/proposte-mulino-carocci-einaudi.md` | 15.347 | `144b4d6ad806405c0df77f3a510cb5c0d6307066c5ca4ce06f21979e90e55053` |
| `_diffusione-opera/registro-pec-e-canali.md` | 14.921 | `937f9f84cd4db8ba931666440aeeb1c6da9b7ef53fec7dd8a4e364f725676a3f` |
| `_diffusione-opera/relazione-al-centro-flamigni.md` | 20.353 | `5d9f5244bb68dd0a9bb523ccfbb4fd620cd2579d5374e9e8be96cd2bf8ff4921` |
| `_diffusione-opera/scheda-dell-opera.md` | 5.926 | `e4def6e69e6095b55a7e1bbbef22794006a1dee7bc60a8504ea1ab39d4ec8fa3` |

### Il dossier di diffusione anteriore

*L'elenco dei destinatari e i materiali della prima campagna.*

5 file · 22.024 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `_diffusione/README.md` | 1.856 | `63b5ab1a66ba350f723c29b5ff0d3c0af83320cd56497aa8eafd49589623866b` |
| `_diffusione/elenco-destinatari.md` | 4.103 | `c02f7dc18d09fd3b8b58a25ed86fcf6c6cd42bbfa16186d36ae15a9c0da0eb86` |
| `_diffusione/lettera-accompagnamento.md` | 3.121 | `49c50e451c5daa0c7a162253632c270d6da1f03688b396801f1a3b22c83f3404` |
| `_diffusione/pec-invio.md` | 6.474 | `cf08d9428ee20b2747556389d5d15179d97327ba9d4be6182f9567c57f7df636` |
| `_diffusione/prompt-ricerca-destinatari.md` | 6.470 | `39309785a6a97c45618fc8d5d1b519426bb6fad86f657113c52a1383d64da3f0` |

### La pubblicazione finale

*L'impaginato conclusivo con il proprio indice generale.*

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

### I livelli della piramide

*Le riduzioni progressive dell'opera, dall'abstract strutturato in giù.*

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

### Il paper accademico

*La versione per la sede accademica, anche in inglese.*

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

### Tomo I — Puglia

*Il nucleo regionale.*

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

### Tomo II — nazionale

*L'estensione alle altre regioni.*

5 file · 3.833.161 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `tomo-2-nazionale/README.md` | 2.815 | `fc7fd8bcf9e826bb38b30802276629f531eb95c5a4f6d23a86f6353417a94b8e` |
| `tomo-2-nazionale/blocco-regionale/tomo-ii-blocco-regionale.docx` | 1.294.873 | `b182fd23caf8c76cef187cbb2587b5f13742c0a77d7baebd2ae1b7fec6a7077c` |
| `tomo-2-nazionale/blocco-regionale/versioni-precedenti/tomo-ii-blocco-regionale_tranche-4-ocse2026.docx` | 1.087.394 | `88d68670f2215f0ce9df52426706453a21ebdecc5a5cd2774f2b3e45ce59b873` |
| `tomo-2-nazionale/blocco-regionale/versioni-precedenti/tomo-ii-blocco-regionale_v-651fd061.docx` | 1.098.941 | `5743fe688060e99798f173f8242479bce197ae4804703b34c45f218e04c6566f` |
| `tomo-2-nazionale/opera-unificata-nazionale-e-ue27.docx` | 349.138 | `d11dd0a0a77fa37e776a5410522199111f542be59aa3ec6229bf7eaada08a3b1` |

### L'estensione ai ventisette

*L'opera unificata nazionale e UE-27.*

2 file · 349.771 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `ue-27/README.md` | 633 | `e7e8f06c0b412b7e5bf1e209c1e53912c01f786e8f0c73a89b32616a0cb03132` |
| `ue-27/opera-unificata-nazionale-e-ue27.docx` | 349.138 | `d11dd0a0a77fa37e776a5410522199111f542be59aa3ec6229bf7eaada08a3b1` |

### Il pacchetto dei grafici

*Le nove infografiche della verifica, la nota di metodo e l'archivio compresso. Non sono versionate: viaggiano a parte, e per questo l'impronta conta di più.*

11 file · 1.268.605 byte

| File | Byte | SHA-256 |
|---|---:|---|
| `1_imbuto-della-verificabilita.png` | 67.753 | `c6b0424bf2293c248575a66f2c44c790edc3c671adc190a94e8e0bbedbad3625` |
| `2_tessere-sotto-la-soglia-documentata.png` | 75.207 | `1a5c989e77f1e2c1b719d9eb6eae074b824bc6eb5cec4135303e7aecbf3c2832` |
| `3_i-trentatre-per-sede-istituzionale.png` | 71.597 | `f61a057b4315fd6eacf9a9a9726498dd1abdaa0e69d2285911274d4bc35a7f5b` |
| `4_composizione-documentata-dei-962.png` | 77.397 | `068e589fa336ffa8f587711677f87f195c4c4b72273516e2785dbc2fbf2acbe3` |
| `5_distanza-fra-i-fatti-e-la-prova.png` | 60.499 | `fc6860ccc09b8d17e2c7ae4d2627e3414d60570f0c447d34f2d2b82eb8eaeef0` |
| `6_finestra-sei-mesi-materia-disponibile.png` | 97.589 | `29db330279ad0a1b9bb8ebb51c06926d629387032f0613caf91825873b62e4dd` |
| `7_quota-dei-trentatre-sul-totale.png` | 67.111 | `09247c55e134b965157c3ce1a034611a5771e72b831488d5aea924496d887c35` |
| `8_date-di-affiliazione-disponibili.png` | 67.109 | `6b6c451f03a59689c3a9a4b45eca4e572d6a8e67e2c99569984bbde57f29b4f6` |
| `9_finestra-e-i-due-dati-datati.png` | 58.109 | `ca23774f52b68d21c204dca2f3d1632ef6917b6460331fc8f81b76a4d169b55a` |
| `LEGGIMI.txt` | 3.419 | `19db10c11567fbd2ce60657d9f225484c24c06960fe47fda973df834ee5f7113` |
| `GRAFICI_VERIFICA_P2.zip` | 622.815 | `060e7c4e5c65b048de6904ef74eb34eff6f41d1d0da0d3826720a0e32d655b49` |

---

## Il commit, che è un'altra cosa

L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git:

```
a34bf3dc6cdd8d7a8dead480722b57d3d9a19361
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
