#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Misura una campagna di blocchi verificati e ne scrive il referto.

Nasce dal rilievo del critico del «Mediterraneo conteso»: una parte dei
blocchi poggiava su fonti interne al corpus, cioe' su se stessa. Il rilievo
fu accolto e annotato, ma restava misurato una volta sola e a mano. Questo
script lo misura sempre, e per ogni campagna allo stesso modo.

Non interpreta: conta. Le quattro misure sono:

  1. la distribuzione dei gradi in testa all'esito;
  2. la sede della fonte: esterna, mista, o SOLO interna al corpus
     (l'autoriscontro: un'eco, non una fonte);
  3. la dichiarazione del non letto, che e' la regola «un URL citato non e'
     un URL letto» resa visibile e contabile;
  4. il carico dei verificatori avversariali, correzione per correzione.

Tutto e' riportato anche per sezione, perche' l'autoriscontro non si
distribuisce a caso: si concentra dove il corpus aveva gia' scritto.

Uso:
    python3 audit_campagna.py DIR_LOTTI [--nome "Titolo"] [--out FILE.md]
"""
import argparse
import collections
import glob
import json
import re
import sys
from pathlib import Path

# Una sede interna: un file del corpus, o un rimando esplicito all'opera.
INTERNA = re.compile(
    r'\.md\b|questo corpus|del corpus|Libro sedicesimo|Libro \w+ ·'
    r'|GUIDA-ALLA-LETTURA|INDICE\b')

# Una sede esterna: un indirizzo, un dominio nudo, un repertorio giudiziario,
# un fondo archivistico, un atto parlamentare, una testata.
ESTERNA = re.compile(
    r'https?://'
    r'|\b[a-z0-9][a-z0-9-]*\.(org|com|gov|edu|net|it|uk|ch|fr|de|info)\b'
    r'|FBI|National Archives|HOLLIS|Harvard|Columbia|Yale|Princeton'
    r'|New York Times|Washington Post|Village Voice|Corriere|Repubblica'
    r'|\d{3}\s+U\.S\.|F\.2d|F\.Supp|Supreme Court|S\.D\.N\.Y|Second Circuit'
    r'|Appellate Division|Congress|Senate|GPO|Library of Congress'
    r'|Roosevelt Library|Gazzetta|Commissione parlamentare|CIA|Dipartimento'
    r'|sentenza|Corte|archivio|Archives|fondo |bobin|microfilm|fascicolo'
    r'|inventario|openlibrary|OSCE|FRUS',
    re.I)

NON_LETTO = re.compile(
    r'non apert|non lett|citat[oi],? non|mai apert|mai lett|egress'
    r'|non spogliat|non consultat|non interrogat|non raggiung|non scaric',
    re.I)

CELLA = re.compile(r'^(Cella aperta|Non Stato Zero)', re.I)
ZERO = re.compile(r'^(Stato\s+)?Zero\b', re.I)


def grado(esito: str) -> str:
    """Il grado in testa all'esito, o la categoria che lo sostituisce."""
    e = esito.strip()
    if CELLA.match(e):
        return 'cella aperta con sede'
    if ZERO.match(e):
        return 'Stato Zero'
    for g in ('B/C', 'F/B', 'A', 'B', 'C', 'F'):
        if re.match(re.escape(g) + r'\b', e):
            return g
    return 'senza grado in testa'


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if d.get("blocchi"):
            lotti.append(d)
    return lotti


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cartella")
    ap.add_argument("--nome", default="")
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    lotti = carica(Path(a.cartella))
    if not lotti:
        sys.exit("nessun lotto verificato in " + a.cartella)

    gradi = collections.Counter()
    sede = collections.Counter()
    per_sez = collections.defaultdict(lambda: collections.Counter())
    titoli = {}
    tot = non_letto = 0
    n_corr = 0

    for d in lotti:
        s = d.get("sezione", "?")
        titoli[s] = d.get("titolo_sezione", s)
        n_corr += len(d.get("correzioni", []))
        for b in d["blocchi"]:
            tot += 1
            g = grado(b.get("e", ""))
            gradi[g] += 1
            per_sez[s]["tot"] += 1
            f = b.get("f", "")
            i, e = bool(INTERNA.search(f)), bool(ESTERNA.search(f))
            k = ("solo interna" if i and not e else
                 "mista" if i and e else "esterna")
            sede[k] += 1
            per_sez[s][k] += 1
            if NON_LETTO.search(f):
                non_letto += 1
                per_sez[s]["non letto"] += 1

    nome = a.nome or Path(a.cartella).name
    p = lambda n: f"{n} ({100 * n / tot:.1f}%)"  # noqa: E731

    r = [f"### Referto di campagna — {nome}\n\n",
         f"Blocchi misurati: **{tot}**, in {len(lotti)} lotti verificati. "
         f"Interventi dei verificatori avversariali: **{n_corr}** "
         f"({n_corr / tot:.2f} per blocco).\n\n",
         "**I gradi in testa all'esito.**\n\n",
         "| grado | blocchi | quota |\n|---|---:|---:|\n"]
    for g, n in gradi.most_common():
        r.append(f"| {g} | {n} | {100 * n / tot:.1f}% |\n")

    r.append(
        "\n**La sede della fonte.** Una fonte *esterna* nomina un indirizzo, "
        "un repertorio, un fondo o un atto fuori dal corpus; una *mista* ne "
        "nomina uno e vi affianca un rimando interno; una **solo interna** "
        "rimanda unicamente a documenti di quest'opera — ed e' "
        "l'**autoriscontro**, che non e' un riscontro: e' un'eco.\n\n"
        f"- sede esterna nominata: **{p(sede['esterna'])}**\n"
        f"- sede mista: **{p(sede['mista'])}**\n"
        f"- **solo interna al corpus: {p(sede['solo interna'])}**\n\n"
        f"**La dichiarazione del non letto.** {p(non_letto)} dei blocchi "
        "dichiarano nella fonte che una sede citata non e' stata aperta. "
        "Non e' una debolezza: e' la regola «un URL citato non e' un URL "
        "letto» resa contabile.\n\n"
        "**Per sezione**, perche' l'autoriscontro non si distribuisce a "
        "caso.\n\n"
        "| sezione | blocchi | solo interna | quota | non letto |\n"
        "|---|---:|---:|---:|---:|\n")
    for s in sorted(per_sez, key=lambda x: (len(x), x)):
        c = per_sez[s]
        r.append(f"| {s} — {titoli.get(s, s)} | {c['tot']} | "
                 f"{c['solo interna']} | "
                 f"{100 * c['solo interna'] / c['tot']:.0f}% | "
                 f"{c['non letto']} |\n")

    testo = "".join(r)
    if a.out:
        Path(a.out).write_text(testo, encoding="utf-8")
        print(f"scritto {a.out}: {tot} blocchi, {len(lotti)} lotti")
    else:
        print(testo)


if __name__ == "__main__":
    main()
