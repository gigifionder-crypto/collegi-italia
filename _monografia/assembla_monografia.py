#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla la monografia dai file numerati di _monografia/.

Ordine = ordine dei nomi file. Nessuna rinumerazione: i titoli stanno
gia' nei sorgenti. L'indice e' generato dai titoli di primo livello.
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
USCITA = Path(sys.argv[1]) if len(sys.argv) > 1 else \
    BASE.parent / "novanta-secondi-e-quarantotto-anni.md"

files = sorted(p for p in BASE.glob("*.md"))
if not files:
    sys.exit("nessun sorgente")

testi = []
indice = []
for i, p in enumerate(files):
    t = p.read_text(encoding="utf-8").rstrip()
    if i:  # il titolo del primo sorgente e' il titolo del libro, non una voce
        for riga in t.split("\n"):
            if riga.startswith("# "):
                indice.append(riga[2:].strip())
                break
    testi.append(t)

corpo = "\n\n---\n\n".join(testi)

# l'indice va dopo il blocco di dichiarazione del proemio: lo si inserisce
# prima del primo titolo "## " del proemio.
voci = "\n".join(f"- **{v}**" for v in indice)
sommario = f"\n\n## Sommario\n\n{voci}\n"

marca = "\n## Proemio · I sei nomi"
if marca in corpo:
    corpo = corpo.replace(marca, sommario + marca, 1)
else:
    corpo = sommario + corpo

USCITA.write_text(corpo + "\n", encoding="utf-8")
parole = len(corpo.split())
print(f"{USCITA}  —  {len(files)} sorgenti, {len(indice)} titoli, {parole} parole")
