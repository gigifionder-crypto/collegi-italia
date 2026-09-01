#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Spellman: ogni strumento» dai dieci confutatori.

Sorgente: verificato-I*.json, ciascuno con {strumento, esiti [{b,e,f}],
correzioni, sopravvive}. La forma e' diversa dalle altre campagne perche'
la campagna lo era: dieci LENTI indipendenti sullo stesso punto, non dieci
sezioni di una materia.

Uso: python3 assembla_strumenti.py DIR_LOTTI FILE_USCITA [FILE_SINTESI]
"""
import json
import sys
from pathlib import Path

INTESTAZIONE = """# Spellman: ogni strumento

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository.
> Non è opera di storici di professione; ogni esito porta il suo grado.
> **Nessuna persona è qui indicata come responsabile di un reato fuori da un
> giudicato definitivo.** Ogni lente è stata sottoposta a un **confutatore**
> il cui mandato era **rompere, non migliorare**; le correzioni sono riportate.

## La forma di questa campagna, che è diversa da tutte le altre

Le altre campagne dividono **una materia in sezioni**. Questa divide **il
metodo in strumenti**: dieci arnesi che quest'opera ha costruito nel tempo,
puntati **uno per uno, senza consultarsi, sullo stesso identico punto**.

Il punto è questo, e nient'altro. Il **Libro sedicesimo · XXIV** registra fra
i clienti dello studio di Roy Cohn **«l'arcidiocesi di New York»**. Il corpus
**non ha mai affermato un rapporto fra Cohn e Francis Spellman**: nomina un
**ente**, non un **prelato**. E una misura meccanica ha accertato che il
cognome «Spellman» ricorreva **zero volte** in tutti i file dell'opera.

**Un ente nominato, un prelato mai nominato, e una lacuna misurata.**

## I due recinti

**Il calendario.** Spellman muore il **2 dicembre 1967**, **3.757 giorni**
prima di via Fani. Non può essere agente in fatti posteriori.

**Le allegazioni non provate su una persona morta.** Non si ripetono come
fatti, non ci si costruisce sopra inferenze; se ne accerta al massimo lo
**statuto probatorio**. **Una diceria con un grado accanto resta una diceria.**

## Perché ogni verdetto ha una metà negativa

A ciascuna lente è stato imposto di dichiarare **due cose**: che cosa il
proprio strumento, **da solo**, stabilisce — e **che cosa non stabilisce**.
La seconda metà era obbligatoria, e i confutatori avevano ordine di
**scriverla loro** se mancava o era debole.

**È la parte che, in una campagna su una lacuna, contiene il risultato.**

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-I*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if d.get("esiti"):
            lotti.append(d)
    return lotti


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cartella, uscita = Path(sys.argv[1]), Path(sys.argv[2])
    sintesi = Path(sys.argv[3]) if len(sys.argv) > 3 else None

    lotti = carica(cartella)
    if not lotti:
        sys.exit("nessuno strumento verificato in " + str(cartella))
    n_es = sum(len(l["esiti"]) for l in lotti)
    n_corr = sum(len(l.get("correzioni", [])) for l in lotti)

    p = [INTESTAZIONE,
         f"## Il conto\n\n**{len(lotti)} strumenti**, **{n_es} esiti**, "
         f"**{n_corr} interventi dei confutatori** "
         f"({n_corr / max(len(lotti), 1):.1f} per strumento).\n"]

    n = 0
    for l in lotti:
        p.append(f"\n## {l.get('strumento', '?')}\n")
        for e in l["esiti"]:
            n += 1
            p.append(f"\n**{n} · {e['b'].strip()}**\n"
                     f"— {e['e'].strip()}\n"
                     f"— *Fonte* · {e['f'].strip()}\n")
        if l.get("sopravvive"):
            p.append(f"\n> **Che cosa sopravvive alla confutazione.** "
                     f"{l['sopravvive'].strip()}\n")

    p.append("\n## Il registro delle confutazioni\n\n")
    for l in lotti:
        for c in l.get("correzioni", []):
            p.append(f"- [{l.get('strumento', '?').split()[0]}] {c.strip()}\n")

    if sintesi and sintesi.exists():
        p.append("\n---\n\n" + sintesi.read_text(encoding="utf-8"))

    uscita.write_text("".join(p), encoding="utf-8")
    print(f"{uscita}: {n} esiti, {len(lotti)} strumenti, {n_corr} confutazioni"
          + (", sintesi inclusa" if sintesi and sintesi.exists() else ""))


if __name__ == "__main__":
    main()
