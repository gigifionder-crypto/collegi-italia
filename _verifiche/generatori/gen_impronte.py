# -*- coding: utf-8 -*-
"""Registro delle impronte SHA-256: il file markdown per il repo e la pagina."""
import hashlib, os, subprocess, json

REPO = '/home/user/collegi-italia'
SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
G = os.path.join(SP, 'grafici-verifica-p2')

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for blocco in iter(lambda: f.read(1 << 20), b''):
            h.update(blocco)
    return h.hexdigest()

def _n(x):
    return f'{x:,}'.replace(',', '.')

def voce(base, nome, etichetta=None):
    p = os.path.join(base, nome)
    return {'nome': nome, 'etichetta': etichetta or nome,
            'byte': os.path.getsize(p), 'sha': sha(p)}

# ---- l'opera integrale, in doppia edizione
INTEGRALE = [voce(REPO, 'UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.pdf'),
             voce(REPO, 'UNA_GUERRA_SENZA_FINE_OPERA_INTEGRALE.docx')]

# ---- i volumi autonomi: estratti dell'opera, non testi diversi
_esclusi = {v['nome'] for v in INTEGRALE}
_tutti = sorted(f for f in os.listdir(REPO)
                if f.endswith(('.pdf', '.docx')) and f not in _esclusi)
VOLUMI = [voce(REPO, f) for f in _tutti]

# ---- il pacchetto dei grafici della verifica
GRAFICI = [voce(G, f) for f in sorted(os.listdir(G))] + \
          [voce(SP, 'GRAFICI_VERIFICA_P2.zip')]

COMMIT = subprocess.run(['git', '-C', REPO, 'rev-parse', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
RAMO = subprocess.run(['git', '-C', REPO, 'rev-parse', '--abbrev-ref', 'HEAD'],
                      capture_output=True, text=True).stdout.strip()

json.dump({'integrale': INTEGRALE, 'volumi': VOLUMI, 'grafici': GRAFICI,
           'commit': COMMIT, 'ramo': RAMO},
          open(os.path.join(SP, 'impronte.json'), 'w'), ensure_ascii=False, indent=1)
print(f'opera: {len(INTEGRALE)} · volumi: {len(VOLUMI)} · grafici: {len(GRAFICI)}')
print('commit:', COMMIT[:12], '· ramo:', RAMO)
print('totale byte:', _n(sum(v['byte'] for v in INTEGRALE + VOLUMI + GRAFICI)))


# =====================================================================
#  Il registro in markdown, per il repo
# =====================================================================
def righe_md(voci):
    return '\n'.join(f'| `{v["nome"]}` | {_n(v["byte"])} | `{v["sha"]}` |' for v in voci)

TESTA = '| File | Byte | SHA-256 |\n|---|---:|---|'

MD = f'''# Registro delle impronte SHA-256

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana, come ogni documento di quest'opera.*

Ogni file pubblicato porta qui la propria impronta crittografica. Chi riceve un
volume — un editore, un archivio, un lettore — può accertare in un comando che il
file che ha in mano è **bit per bit** quello depositato, e non una copia alterata,
troncata o rimontata.

**Stato al commit `{COMMIT[:12]}`** del ramo `{RAMO}`.
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

{TESTA}
{righe_md(INTEGRALE)}

## I volumi autonomi

*Estratti dell'opera integrale, non testi diversi: ciascuno riporta un tratto del
corpus nella stessa composizione tipografica.*

{TESTA}
{righe_md(VOLUMI)}

## Il pacchetto dei grafici della verifica

{TESTA}
{righe_md(GRAFICI)}

---

## Il commit

L'albero da cui questi file provengono è identificato dal proprio SHA-1 di Git:

```
{COMMIT}
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
'''

open(os.path.join(REPO, 'IMPRONTE-SHA256.md'), 'w', encoding='utf-8').write(MD)

# Il formato che sha256sum --check sa leggere, per la verifica in blocco.
TXT = ''.join(f'{v["sha"]}  {v["nome"]}\n' for v in INTEGRALE + VOLUMI)
open(os.path.join(REPO, 'IMPRONTE-SHA256.txt'), 'w', encoding='utf-8').write(TXT)
print('scritti IMPRONTE-SHA256.md e .txt')
