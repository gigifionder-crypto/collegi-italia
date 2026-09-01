#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «L'Ogaden e Belgrado — cento blocchi» dai lotti verificati del
workflow wf_49bbde8c-00d.

Sorgente: i file verificato-{O1,O2,B1,B2}-b*.json (sezione, titolo_sezione,
batch, blocchi [{b,e,f}], correzioni). Assemblaggio deterministico: sezioni
in ordine fisso, lotti in ordine lessicografico, numerazione progressiva
1..N assegnata QUI e mai più toccata (append, mai rinumerare).

Uso:
    python3 assembla_ogaden.py DIR_LOTTI FILE_USCITA [--persi id1,id2]
"""
import json
import sys
from pathlib import Path

ORDINE = ["O1", "O2", "B1", "B2"]
ROMANI = {"O1": "I", "O2": "II", "B1": "III", "B2": "IV"}

INTESTAZIONE = """# L'Ogaden e Belgrado — cento blocchi

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository.
> Non è opera di storici di professione; ogni affermazione porta il suo grado
> di prova e va verificata sulle fonti primarie. La generazione è avvenuta con
> {n_lotti} lotti prodotti da agenti indipendenti e sottoposti ciascuno a
> verifica avversariale; le correzioni dei verificatori sono riportate
> integralmente in coda.

## Perché questi due materiali, e perché insieme

Il critico di completezza del **Mediterraneo conteso** chiuse i suoi rilievi
con venti lacune. Le prime due erano queste: **la guerra dell'Ogaden**, che
nel 1977-78 rovescia gli allineamenti del Corno d'Africa mentre l'Italia vi
ha interessi antichi, e **la riunione di Belgrado della CSCE**, il primo
seguito di Helsinki, che si svolge negli stessi mesi.

Stanno insieme in un solo documento per una ragione di metodo, non di
argomento: **sono i due grandi fatti internazionali contemporanei ai
cinquantacinque giorni**, e servono a mettere alla prova, l'ennesima volta,
lo strumento più economico e più letale di quest'opera — **il calendario**.

**La regola che governa l'intero documento.** La contemporaneità **non è**
un nesso. Che due cose accadano negli stessi mesi non stabilisce fra loro
alcun rapporto: né di causa, né di concerto, né di conoscenza reciproca.
Un blocco che accerti una sincronia e **si fermi lì** ha fatto il suo
lavoro; un blocco che dalla sincronia inferisca un legame ha commesso
l'errore che questo documento esiste per non commettere.

**E la premessa che il documento doveva verificare, non presupporre.** La
campagna fu chiesta con la formula «la CSCE di Belgrado che cade dentro i
cinquantacinque giorni». Se la formula è sbagliata, la sezione III lo dice
con la data: **una premessa smentita è un risultato**, e si scrive.

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
