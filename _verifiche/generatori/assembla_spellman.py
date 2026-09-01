#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Spellman — cento blocchi mirati» dai lotti verificati del
workflow wf_a86f5e74-edb.

Sorgente: i file verificato-S*.json (sezione, titolo_sezione,
batch, blocchi [{b,e,f}], correzioni). Assemblaggio deterministico: sezioni
in ordine fisso, lotti in ordine lessicografico, numerazione progressiva
1..N assegnata QUI e mai più toccata (append, mai rinumerare).

Uso:
    python3 assembla_spellman.py DIR_LOTTI FILE_USCITA [--persi id1,id2]
"""
import json
import sys
from pathlib import Path

ORDINE = [f"S{i}" for i in range(1, 9)]
ROMANI = {f"S{i}": r for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"], 1)}

INTESTAZIONE = """# Spellman — cento blocchi mirati

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository.
> Non è opera di storici di professione; ogni affermazione porta il suo grado
> di prova e va verificata sulle fonti primarie. La generazione è avvenuta con
> {n_lotti} lotti prodotti da agenti indipendenti e sottoposti ciascuno a
> verifica avversariale; le correzioni sono riportate integralmente in coda.

## Perché questa campagna esiste

Il corpus conta oltre sette milioni di parole, e **«Spellman» vi ricorreva
zero volte** — mentre un suo capitolo colloca **l'arcidiocesi di New York fra
i clienti dello studio di Roy Cohn**. Era la lacuna più grossa dell'opera, e
questa campagna doveva **misurarla**, non riempirla a ogni costo.

## I due recinti, che valgono più di ogni risultato

**Il calendario.** Francis Joseph Spellman muore il **2 dicembre 1967**. Via
Fani è del 16 marzo 1978: **3.757 giorni dopo**. Nessun atto, nessuna
condotta, nessuna decisione di Spellman può essere contemporanea al caso Moro.

**Le allegazioni non provate su una persona morta.** Su Spellman circolano da
decenni allegazioni relative alla vita privata, mai accertate in alcuna sede.
**Questo documento non le ripete come fatti e non vi costruisce sopra alcuna
inferenza.** Ne accerta al massimo lo **statuto probatorio**, e poi tace.
**Una persona morta non può difendersi, e una diceria con un grado accanto
resta una diceria: il grado non la nobilita.**

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if not d.get("blocchi"):
            print(f"VUOTO {f.name}", file=sys.stderr)
            continue
        lotti.append(d)
    lotti.sort(key=lambda d: (ORDINE.index(d.get("sezione", ""))
                              if d.get("sezione") in ORDINE else 99,
                              d.get("batch", "")))
    return lotti


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cartella, uscita = Path(sys.argv[1]), Path(sys.argv[2])
    persi = []
    if len(sys.argv) > 4 and sys.argv[3] == "--persi":
        persi = [x for x in sys.argv[4].split(",") if x]

    lotti = carica(cartella)
    n_bl = sum(len(l["blocchi"]) for l in lotti)
    n_corr = sum(len(l.get("correzioni", [])) for l in lotti)

    parti = [INTESTAZIONE.format(n_lotti=len(lotti))]
    n = 0
    sez_corr = None
    for lotto in lotti:
        sez = lotto.get("sezione", "?")
        if sez != sez_corr:
            sez_corr = sez
            parti.append(f"\n## {ROMANI.get(sez, sez)}. "
                         f"{lotto.get('titolo_sezione', sez)}\n")
        for bl in lotto["blocchi"]:
            n += 1
            parti.append(
                f"\n**{n} · {bl['b'].strip()}**\n"
                f"— {bl['e'].strip()}\n"
                f"— *Fonte* · {bl['f'].strip()}\n"
            )

    parti.append("\n## Registro di chiusura\n\n")
    parti.append(
        f"Blocchi assemblati: **{n_bl}**, in {len(lotti)} lotti verificati. "
        f"Interventi dei verificatori avversariali: **{n_corr}**, riportati "
        "integralmente qui sotto — la verifica è parte dell'opera.\n"
    )
    if persi:
        parti.append(
            f"\n**Stato Zero di lavorazione** (sede: questo registro): i "
            f"lotti {', '.join(persi)} sono andati persi e non sostituiti "
            "con testo non verificato — append, mai rinumerare.\n"
        )
    parti.append("\n### Il registro delle correzioni\n\n")
    for lotto in lotti:
        for c in lotto.get("correzioni", []):
            parti.append(f"- [{lotto.get('batch', '?')}] {c.strip()}\n")

    uscita.write_text("".join(parti), encoding="utf-8")
    print(f"{uscita}: {n} blocchi, {len(lotti)} lotti, "
          f"{n_corr} correzioni, persi {len(persi)}")


if __name__ == "__main__":
    main()
