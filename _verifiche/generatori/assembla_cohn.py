#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Roy Cohn — mille blocchi mirati» dai lotti verificati del
workflow wf_09f55cfa-d6f.

Sorgente: i file verificato-C*.json (sezione, titolo_sezione, batch,
blocchi [{b,e,f}], correzioni). Assemblaggio deterministico: sezioni C1..C10
in ordine, lotti in ordine lessicografico, numerazione progressiva 1..N
assegnata QUI e mai più toccata (append, mai rinumerare).

Uso:
    python3 assembla_cohn.py DIR_LOTTI FILE_USCITA [--persi id1,id2]
"""
import json
import sys
from pathlib import Path

ORDINE = [f"C{i}" for i in range(1, 11)]
ROMANI = {f"C{i}": r for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"], 1)}

INTESTAZIONE = """# Roy Cohn — mille blocchi mirati

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository.
> Non è opera di storici di professione; ogni affermazione porta il suo grado
> di prova e va verificata sulle fonti primarie. La generazione è avvenuta con
> {n_lotti} lotti prodotti da agenti indipendenti e sottoposti ciascuno a
> verifica avversariale; le correzioni dei verificatori sono riportate
> integralmente in coda.

## Il metodo, e le due regole che qui pesano più di tutte

Quest'opera approfondisce il **Libro sedicesimo · XXIV** con mille **blocchi
mirati**: per ciascuno un **bersaglio** (una domanda operativa precisa),
un **esito** col grado in testa (A giudicato · B accertamento · C congettura ·
F fatto pubblico · Zero = assenza documentata con sede nominata), e una
**fonte** — o la sede del vuoto. Un blocco che trova il vuoto non si scarta:
è uno Stato Zero con sede, ed è prezioso.

**Prima regola, e non ammette eccezioni.** **Roy Cohn non fu mai condannato
in sede penale.** Fu incriminato più volte — le fonti divergono fra tre e
quattro, e la divergenza si riporta senza scioglierla — e fu **assolto ogni
volta**, con un processo conclusosi in *mistrial*. La radiazione dall'albo
del **23 giugno 1986** è una sanzione **professionale**, non penale, e come
tale è sempre qualificata. **Gli assolti restano assolti anche quando
l'assoluzione è ripetuta, e anche quando spiace.**

**Seconda regola.** Nessuna persona vivente è indicata come responsabile di
un reato fuori da un giudicato definitivo. Cause civili, transazioni e
decreti di consenso **non sono ammissioni di colpa** e sono descritti per
quello che sono. Un'incriminazione non è una condanna; un'archiviazione non
è una condanna; un'assoluzione chiude.

**E una terza, di fonte.** Le biografie, i documentari, le opere teatrali e
cinematografiche su Cohn sono numerose e spesso ottime: restano **fonti
secondarie**, e la finzione non è mai fonte. Un riscontro da motore di
ricerca vale al massimo B, e solo con l'indirizzo citato — perché **un URL
citato non è un URL letto**.

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-C*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if not d.get("blocchi"):
            print(f"VUOTO {f.name}", file=sys.stderr)
            continue
        lotti.append(d)
    lotti.sort(key=lambda d: (ORDINE.index(d.get("sezione", "C10"))
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
