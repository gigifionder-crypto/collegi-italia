#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla l'Opera monografica unica da opera.json.

Ogni libro: narrazione (versi + prosa) -> raccordo -> capitoli documentari
-> referto. Il referto sta DOPO i documenti perche' e' un referto su cio'
che si e' letto, non una promessa su cio' che si leggera'.

La numerazione dei capitoli e' continua e assegnata qui, in assemblaggio:
i sorgenti conservano il nome con cui furono scritti.
"""
import json
import re
import sys
from pathlib import Path

MONO = Path(__file__).resolve().parent
BREVE = MONO.parent / "_verifiche" / "edizione-breve"
USCITA = Path(sys.argv[1]) if len(sys.argv) > 1 else \
    MONO.parent / "novanta-secondi-e-quarantotto-anni.md"

RE_REFERTO = re.compile(r"\n(## Referto del [^\n]+)\n", re.M)


def spezza_narrazione(testo: str):
    """Ritorna (titolo, corpo_narrativo, referto) di un libro della monografia."""
    testo = testo.rstrip()
    titolo = testo.split("\n", 1)[0][2:].strip()
    m = RE_REFERTO.search(testo)
    if not m:
        return titolo, testo, ""
    corpo = testo[:m.start()].rstrip()
    referto = testo[m.start():].strip()
    # via l'eventuale riga di separazione prima del referto
    corpo = re.sub(r"\n-{3,}\s*$", "", corpo).rstrip()
    return titolo, corpo, referto


def capitolo(path: Path):
    """Ritorna (titolo_senza_numero, corpo) di un capitolo documentario."""
    testo = path.read_text(encoding="utf-8").rstrip()
    righe = testo.split("\n")
    if righe and righe[0].startswith("## "):
        t = re.sub(r"^\d+\.\s*", "", righe[0][3:].strip())
        return t, "\n".join(righe[1:]).strip("\n")
    return path.stem, testo


def main():
    man = json.loads((MONO / "opera.json").read_text(encoding="utf-8"))

    mancanti = [f for L in man["libri"] for f in [L["narrazione"]]
                if not (MONO / f).exists()]
    mancanti += [c for L in man["libri"] for c in L["capitoli"]
                 if not (BREVE / c).exists()]
    mancanti += [c for c in man["chiusura"] if not (MONO / c).exists()]
    mancanti += [c for c in man["apparati"] if not (BREVE / c).exists()]
    for k in ("prologo", "registro_savona"):
        if man.get(k) and not (MONO / man[k]).exists():
            mancanti.append(man[k])
    if mancanti:
        sys.exit("MANCANTI: " + ", ".join(mancanti))

    pezzi = [(MONO / man["proemio"]).read_text(encoding="utf-8").rstrip()]
    indice = []
    n = 0

    if man.get("prologo"):
        pro = (MONO / man["prologo"]).read_text(encoding="utf-8").rstrip()
        reg = (MONO / man["registro_savona"]).read_text(encoding="utf-8")
        # si inietta il registro generato dal marcatore in poi: l'elenco non
        # si scrive a mano, si conta.
        i = reg.find("## Gli archi")
        if i < 0:
            sys.exit("registro Savona senza la sezione degli archi")
        pro = pro.replace("<!--REGISTRO-SAVONA-->", reg[i:].rstrip())
        if "<!--REGISTRO-SAVONA-->" in pro:
            sys.exit("marcatore del registro non sostituito")
        indice.append(("libro", pro.split("\n", 1)[0][2:].strip(), None))
        pezzi.append(pro)

    for L in man["libri"]:
        titolo, corpo, referto = spezza_narrazione(
            (MONO / L["narrazione"]).read_text(encoding="utf-8"))
        indice.append(("libro", titolo, None))
        pezzi.append(corpo)
        pezzi.append("## I documenti di questo libro\n\n" + L["raccordo"].strip())
        for c in L["capitoli"]:
            n += 1
            t, testo = capitolo(BREVE / c)
            indice.append(("cap", t, n))
            pezzi.append(f"## {n}. {t}\n\n{testo}")
        if referto:
            pezzi.append(referto)

    for c in man["chiusura"]:
        testo = (MONO / c).read_text(encoding="utf-8").rstrip()
        indice.append(("libro", testo.split("\n", 1)[0][2:].strip(), None))
        pezzi.append(testo)

    pezzi.append("# Apparati")
    indice.append(("libro", "Apparati", None))
    for c in man["apparati"]:
        t, testo = capitolo(BREVE / c)
        indice.append(("app", t, None))
        pezzi.append(f"## {t}\n\n{testo}")

    corpo = "\n\n---\n\n".join(pezzi)

    voci = []
    for tipo, t, num in indice:
        if tipo == "libro":
            voci.append(f"\n**{t}**\n")
        elif tipo == "cap":
            voci.append(f"{num}. {t}")
        else:
            voci.append(f"· {t}")
    sommario = "\n\n## Sommario\n" + "\n".join(voci) + "\n"

    marca = "\n## Proemio · I sei nomi"
    corpo = corpo.replace(marca, sommario + marca, 1) if marca in corpo \
        else sommario + corpo

    USCITA.write_text(corpo + "\n", encoding="utf-8")
    print(f"{USCITA.name} — {len(man['libri'])} libri, {n} capitoli, "
          f"{len(man['apparati'])} apparati, {len(corpo.split())} parole")


if __name__ == "__main__":
    main()
