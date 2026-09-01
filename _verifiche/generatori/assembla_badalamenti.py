#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Badalamenti — cento blocchi mirati» dai lotti verificati del
workflow wf_344d651a-a78.

Sorgente: i file verificato-B*.json (sezione, titolo_sezione,
batch, blocchi [{b,e,f}], correzioni). Assemblaggio deterministico: sezioni
in ordine fisso, lotti in ordine lessicografico, numerazione progressiva
1..N assegnata QUI e mai più toccata (append, mai rinumerare).

Uso:
    python3 assembla_badalamenti.py DIR_LOTTI FILE_USCITA [--persi id1,id2]
"""
import json
import sys
from pathlib import Path

ORDINE = [f"B{i}" for i in range(1, 9)]
ROMANI = {f"B{i}": r for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"], 1)}

INTESTAZIONE = """# Badalamenti — cento blocchi mirati

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository.
> Non è opera di storici di professione; ogni affermazione porta il suo grado
> di prova. **Nessuna persona è qui indicata come responsabile di un reato
> fuori da un giudicato definitivo.** La generazione è avvenuta con {n_lotti}
> lotti verificati da critici avversariali; le correzioni sono in coda.

## Perché questa campagna esiste

Al titolare era stata data una risposta su Gaetano Badalamenti **interamente
di grado C** — sintesi di motore di ricerca, nessuna pagina aperta. Su un uomo
che ha giudicati a carico questo non basta. La campagna doveva **alzare il
grado dove si può, e dove non si può dire perché.**

## I recinti

**La differenza che la campagna esiste per tenere.** Badalamenti fu Cosa
Nostra **siciliana**, capo di Cinisi. **Non fu membro di alcuna delle Cinque
Famiglie di New York.** Il rapporto con la mafia americana fu **operativo** —
traffico, canali, crew — **non di affiliazione**. Un rapporto d'affari non è
un'appartenenza, e un tramite non è un grado gerarchico.

**I giudicati si usano, e solo quelli.** Dove esistono si nominano con gli
estremi e si graduano **A se definitivi, B se no**. Dove non esistono, **non
si supplisce con la fama: la fama non è un grado.**

**Il 9 maggio 1978.** Peppino Impastato fu ucciso a Cinisi nella notte fra
l'8 e il 9 maggio 1978; il corpo di Aldo Moro fu trovato in via Caetani il 9
maggio 1978. **La contemporaneità non è un nesso**, e nessun documento lega i
due delitti. È però lecito, e utile, accertare una cosa diversa: che
l'omicidio di Cinisi fu inizialmente trattato come atto terroristico, e che
vi fu un depistaggio poi esaminato in sede qualificata. **Quello è un fatto
sulla ricezione e sulle indagini, non un legame fra i due delitti.**

**E Impastato è una vittima**, e va nominato come tale: trent'anni, fondatore
di Radio Aut, **eletto cinque giorni dopo la propria morte**.

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
