#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Il parallelo delle due piste — mille studi sincronici» dai lotti
verificati del workflow wf_7a759335-124.

Sorgente: i file verificato-*.json scritti dai verificatori avversariali nella
directory dei lotti (uno per lotto: sezione, titolo_sezione, batch, studi,
correzioni). L'assemblaggio è deterministico: sezioni S1..S8 in ordine, lotti
in ordine lessicografico, numerazione progressiva 1..N assegnata QUI e mai più
toccata (append, mai rinumerare).

Uso:
    python3 assembla_parallelo.py DIR_LOTTI FILE_USCITA [--persi id1,id2]

Il registro delle correzioni dei verificatori viene riportato integralmente in
coda: è la traccia d'audit della verifica avversariale, non un'appendice
facoltativa.
"""
import json
import sys
from pathlib import Path

ORDINE_SEZIONI = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]

INTESTAZIONE = """# Il parallelo delle due piste — mille studi sincronici

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository,
> nell'ambito del corpus documentale sul caso Moro. Non è opera di storici di
> professione; ogni affermazione porta il suo grado di prova e va verificata
> sulle fonti primarie. La generazione è avvenuta con {n_lotti} lotti prodotti
> da agenti indipendenti e sottoposti ciascuno a verifica avversariale; le
> correzioni dei verificatori sono riportate integralmente in coda.

**Libro diciassettesimo dell'opera integrale.**

## Il metodo

Quest'opera esegue una sola istruzione: sugli **stessi soggetti** — le stesse
persone, gli stessi eventi, gli stessi aspetti — porre fianco a fianco due
letture, senza scegliere fra loro.

La colonna **Assodata** dice che cosa risulta nella pista accertata: giudicati,
accertamenti qualificati, fatti pubblici, ciascuno col suo grado in testa
(A giudicato · B accertamento · C congettura · F fatto pubblico · Zero =
assenza documentata con sede nominata).

La colonna **Speculare** legge lo stesso soggetto dentro la pista proposta dal
titolare del corpus — la congettura dell'isomorfismo: il ceppo Feltrinelli, lo
snodo Superclan/Hyperion come possibile terminale informativo di apparati
atlantici, le Brigate Rosse usate (a loro insaputa o no) per depistare, in
movimento speculare alla trama nera. Questa colonna è sviluppata **nel modo più
forte che le fonti consentano** — è la colonna che questa opera ha il compito
di approfondire — ma porta anch'essa il grado in testa, e il grado non si
gonfia: di norma C o Zero, B dove esiste testimonianza o atto qualificato.

Seguono, per ogni studio, la **divergenza** (dove esattamente le due letture si
separano) e il **decisore** (quale documento concreto, se emergesse,
deciderebbe fra le due). Il decisore è la parte che conta: un parallelo senza
falsificatori sarebbe letteratura.

Le regole del corpus valgono per entrambe le colonne: l'appartenenza a
un'organizzazione non è prova di condotta; nessun nome è indicato come
responsabile fuori da un giudicato definitivo; gli assolti restano assolti, i
prosciolti restano prosciolti; il rifiuto di un campione di DNA è un diritto e
non prova nulla; le divergenze si riportano, non si risolvono; il doppio
sospetto non è un grado di prova.

Le sei vittime — Oreste Leonardi, Domenico Ricci, Giulio Rivera, Francesco
Zizzi, Raffaele Iozzino, Aldo Moro — stanno in testa a tutto, come sempre.

"""


def carica_lotti(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-*.json")):
        try:
            dati = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001 — un lotto illeggibile va segnalato, non nascosto
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if not dati.get("studi"):
            print(f"VUOTO {f.name}", file=sys.stderr)
            continue
        lotti.append(dati)
    lotti.sort(key=lambda d: (ORDINE_SEZIONI.index(d.get("sezione", "S8"))
                              if d.get("sezione") in ORDINE_SEZIONI else 99,
                              d.get("batch", "")))
    return lotti


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cartella = Path(sys.argv[1])
    uscita = Path(sys.argv[2])
    persi = []
    if len(sys.argv) > 4 and sys.argv[3] == "--persi":
        persi = [x for x in sys.argv[4].split(",") if x]

    lotti = carica_lotti(cartella)
    n_studi = sum(len(l["studi"]) for l in lotti)
    n_correzioni = sum(len(l.get("correzioni", [])) for l in lotti)

    parti = [INTESTAZIONE.format(n_lotti=len(lotti))]
    numero = 0
    sezione_corrente = None
    romani = {"S1": "I", "S2": "II", "S3": "III", "S4": "IV",
              "S5": "V", "S6": "VI", "S7": "VII", "S8": "VIII"}
    for lotto in lotti:
        sez = lotto.get("sezione", "?")
        if sez != sezione_corrente:
            sezione_corrente = sez
            titolo = lotto.get("titolo_sezione", sez)
            parti.append(f"\n## {romani.get(sez, sez)}. {titolo}\n")
        for st in lotto["studi"]:
            numero += 1
            parti.append(
                f"\n**{numero} · {st['soggetto'].strip()}**\n"
                f"— *Assodata* · {st['assodata'].strip()}\n"
                f"— *Speculare* · {st['speculare'].strip()}\n"
                f"— *Divergenza* · {st['divergenza'].strip()}\n"
                f"— *Deciderebbe* · {st['decisore'].strip()}\n"
            )

    parti.append("\n## Registro di chiusura\n\n")
    parti.append(
        f"Studi assemblati: **{n_studi}**, in {len(lotti)} lotti verificati. "
        f"Interventi dei verificatori avversariali: **{n_correzioni}**, "
        "riportati integralmente qui sotto — la verifica è parte dell'opera, "
        "non un retroscena.\n"
    )
    if persi:
        parti.append(
            f"\n**Stato Zero di lavorazione** (sede: questo registro): i lotti "
            f"{', '.join(persi)} sono andati persi in generazione o verifica e "
            "non sono stati sostituiti con testo non verificato. I loro "
            "soggetti restano nel catalogo per un'integrazione futura — "
            "append, mai rinumerare.\n"
        )

    parti.append("\n### Il registro delle correzioni\n\n")
    for lotto in lotti:
        for c in lotto.get("correzioni", []):
            parti.append(f"- [{lotto.get('batch', '?')}] {c.strip()}\n")

    uscita.write_text("".join(parti), encoding="utf-8")
    print(f"{uscita}: {numero} studi, {len(lotti)} lotti, "
          f"{n_correzioni} correzioni, persi {len(persi)}")


if __name__ == "__main__":
    main()
