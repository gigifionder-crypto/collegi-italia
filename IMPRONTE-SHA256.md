# Registro delle impronte SHA-256

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file pubblicato porta qui la propria impronta crittografica. Chi riceve un
volume — un editore, un archivio, un lettore — può accertare in un comando che il
file che ha in mano è **bit per bit** quello depositato, e non una copia alterata,
troncata o rimontata.

**Stato al commit `1b902e169149`** del ramo `claude/amnistiati-tribunale-speciale-a82lzn`.
Impronte calcolate sui file così come stanno nel repository.

---

## Come si verifica

Su Linux e su macOS, dalla cartella che contiene il file:

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

Per verificare tutto in un colpo solo, da questa cartella:

```
sha256sum --check IMPRONTE-SHA256.txt
```

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

Chi riceve questi volumi deve poter fare due cose distinte: **accertare** che li ha
ricevuti integri — e questo il registro glielo consente — e **verificare** ciò che
affermano, che è invece il lavoro che i gradi dichiarati, le sedi d'archivio nominate
e gli Stati Zero servono a rendere possibile. La prima cosa è meccanica. La seconda no.

---

## L'opera integrale

| File | Byte | SHA-256 |
|---|---:|---|
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf` | 27.778.565 | `39ee2bab1f7b34a96954b508e899d0224141b9e1338e3ee057fd186eef3c8b4e` |
| `UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.docx` | 8.043.958 | `41dc4eb842a907aedaa3356f5133e99959ef87133266b0181559b4941b36f85c` |

## I volumi autonomi

*Estratti dell'opera integrale, non testi diversi: ciascuno riporta un tratto del
corpus nella stessa composizione tipografica.*

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

## Il pacchetto dei grafici della verifica

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

## Il commit

L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git:

```
1b902e1691496040aeb1eaa872ad08d44d8370f9
```

Sono due garanzie diverse e vanno tenute distinte. Il commit fissa **lo stato del
repository** — quali file esistevano e con quale contenuto in quel momento.
L'impronta SHA-256 fissa **il singolo file** anche quando viaggia fuori dal
repository: in allegato a una PEC, su una chiave, dentro un deposito d'archivio.
Un file staccato dal repository perde il commit e conserva l'impronta.

---

*Le impronte si ricalcolano a ogni nuova edizione. Un registro che non cambia
quando cambiano i file non certifica nulla: va rigenerato con*
`python3 _verifiche/generatori/gen_impronte.py` *e ricommesso insieme ai volumi.*
