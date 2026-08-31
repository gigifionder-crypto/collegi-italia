#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Il Mediterraneo conteso — mille ricerche» dai lotti verificati
del workflow wf_f9ab33aa-27e.

Sorgente: i file verificato-M*.json (sezione, titolo_sezione, batch,
blocchi [{b,e,f}], correzioni). Assemblaggio deterministico: sezioni M1..M10
in ordine, lotti in ordine lessicografico, numerazione progressiva 1..N
assegnata QUI e mai più toccata (append, mai rinumerare).

Uso:
    python3 assembla_mediterraneo.py DIR_LOTTI FILE_USCITA [--persi id1,id2]
"""
import json
import sys
from pathlib import Path

ORDINE = [f"M{i}" for i in range(1, 11)]
ROMANI = {f"M{i}": r for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"], 1)}

INTESTAZIONE = """# Il Mediterraneo conteso — mille ricerche

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository,
> nell'ambito del corpus documentale sul caso Moro. Non è opera di storici di
> professione; ogni affermazione porta il suo grado di prova e va verificata
> sulle fonti primarie. La generazione è avvenuta con {n_lotti} lotti prodotti
> da agenti indipendenti e sottoposti ciascuno a verifica avversariale; le
> correzioni dei verificatori sono riportate integralmente in coda.

## Il metodo

Quest'opera esplora, su richiesta del titolare, **la politica mediterranea e
mediorientale italo-francese e le sue opposizioni** — fino alla pista
mediorientale nel caso Moro e alla lettura speculare del titolare, sviluppata
nel modo più forte che le fonti consentano. Mille **ricerche**, ciascuna con
tre campi: il **bersaglio** (una domanda puntuale), l'**esito** (col grado in
testa: A giudicato · B accertamento · C congettura · F fatto pubblico ·
Zero = assenza documentata con sede nominata), la **fonte** (o la sede del
vuoto). Un riscontro da motore di ricerca vale al massimo B: un URL citato
non è un URL letto.

Due regole hanno qui un peso speciale. La prima: **nessuno Stato, governo o
servizio è indicato come mandante, complice od operatore del sequestro fuori
da un giudicato definitivo — e un giudicato in tal senso non esiste**; le
ostilità politiche documentate sono ostilità politiche, mai responsabilità
operative. La seconda: **il calendario si verifica sempre** — il Likud
governa dal maggio 1977; l'Iran è dello Scià fino al gennaio-febbraio 1979 e
il finanziamento iraniano a gruppi palestinesi è un fenomeno essenzialmente
post-1979; ogni catena causale è messa alla prova delle date, come il corpus
fece con Feltrinelli.

Le sei vittime — Oreste Leonardi, Domenico Ricci, Giulio Rivera, Francesco
Zizzi, Raffaele Iozzino, Aldo Moro — stanno in testa a tutto, come sempre.

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-M*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if not d.get("blocchi"):
            print(f"VUOTO {f.name}", file=sys.stderr)
            continue
        lotti.append(d)
    lotti.sort(key=lambda d: (ORDINE.index(d.get("sezione", "M10"))
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
    n_ric = sum(len(l["blocchi"]) for l in lotti)
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
        f"Ricerche assemblate: **{n_ric}**, in {len(lotti)} lotti "
        f"verificati. Interventi dei verificatori avversariali: "
        f"**{n_corr}**, riportati integralmente qui sotto.\n"
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
    print(f"{uscita}: {n} ricerche, {len(lotti)} lotti, "
          f"{n_corr} correzioni, persi {len(persi)}")


if __name__ == "__main__":
    main()
