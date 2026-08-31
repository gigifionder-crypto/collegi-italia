#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla l'edizione breve dai capitoli sorgente elencati in manifesto.json.

L'ordine dell'edizione sta in manifesto.json, sorgente unica — come parti.json
per l'opera integrale. Ogni capitolo sorgente conserva la propria intestazione
originale; la numerazione del libro e' riassegnata QUI, in assemblaggio, e il
cambio rispetto all'edizione in tredici capitoli e' dichiarato in apertura.

Uso:
    python3 assembla_libro.py [FILE_USCITA]
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def corpo(testo: str):
    """Ritorna (titolo_senza_numero, corpo) di un file capitolo."""
    righe = testo.rstrip().split("\n")
    if righe and righe[0].startswith("## "):
        t = righe[0][3:].strip()
        t = re.sub(r"^\d+\.\s*", "", t)
        return t, "\n".join(righe[1:]).strip("\n")
    return None, testo.rstrip()


def main():
    uscita = Path(sys.argv[1]) if len(sys.argv) > 1 else \
        BASE.parent.parent / "una-guerra-senza-fine-edizione-breve.md"
    man = json.loads((BASE / "manifesto.json").read_text(encoding="utf-8"))

    mancanti = []
    for p in man["parti"]:
        for f in p["capitoli"]:
            if not (BASE / f).exists():
                mancanti.append(f)
    for f in man.get("coda", []):
        if not (BASE / f).exists():
            mancanti.append(f)
    if mancanti:
        print("MANCANTI: " + ", ".join(mancanti), file=sys.stderr)
        sys.exit(2)

    parti = [(BASE / "00-frontespizio.md").read_text(encoding="utf-8").rstrip(), ""]
    n = 0
    indice = []
    corpi = []
    for p in man["parti"]:
        corpi.append(f"\n\n# {p['parte']}\n")
        indice.append(f"\n**{p['parte']}**\n")
        for f in p["capitoli"]:
            n += 1
            titolo, testo = corpo((BASE / f).read_text(encoding="utf-8"))
            indice.append(f"{n}. {titolo}")
            corpi.append(f"\n## {n}. {titolo}\n\n{testo}\n")
    for f in man.get("coda", []):
        titolo, testo = corpo((BASE / f).read_text(encoding="utf-8"))
        corpi.append(f"\n## {titolo}\n\n{testo}\n")
        indice.append(f"\n*{titolo}*")

    parti.append("\n## Indice\n")
    parti.append("\n".join(indice) + "\n")
    parti.extend(corpi)

    testo = "\n".join(parti)
    uscita.write_text(testo, encoding="utf-8")
    print(f"{uscita}: {n} capitoli, {len(testo)} byte, "
          f"{len(testo.split())} parole circa")


if __name__ == "__main__":
    main()
