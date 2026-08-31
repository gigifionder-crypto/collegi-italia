#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «La caccia al rifugio — mille tentativi di ricerca» dai lotti
verificati del workflow wf_b52894a3-88b.

Sorgente: i file verificato-K*.json (sezione, titolo_sezione, batch,
blocchi [{b,e,f}], correzioni). Assemblaggio deterministico: sezioni K1..K10
in ordine, lotti in ordine lessicografico, numerazione progressiva 1..N
assegnata QUI e mai più toccata (append, mai rinumerare).

Uso:
    python3 assembla_caccia.py DIR_LOTTI FILE_USCITA [--persi id1,id2]
"""
import json
import sys
from pathlib import Path

ORDINE = [f"K{i}" for i in range(1, 11)]
ROMANI = {f"K{i}": r for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"], 1)}

INTESTAZIONE = """# La caccia al rifugio — mille tentativi di ricerca

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository,
> nell'ambito del corpus documentale sul caso Moro. Non è opera di storici di
> professione; ogni affermazione porta il suo grado di prova e va verificata
> sulle fonti primarie. La generazione è avvenuta con {n_lotti} lotti prodotti
> da agenti indipendenti e sottoposti ciascuno a verifica avversariale; le
> correzioni dei verificatori sono riportate integralmente in coda.

## Il metodo

Quest'opera risponde a una domanda del titolare: **come cercarono, le forze
di polizia, il rifugio di Aldo Moro — e perché non lo trovarono.** La
risposta è data nella forma più onesta che il corpus conosca: non una tesi,
ma un migliaio di **tentativi di ricerca**, ciascuno con tre campi — il
**bersaglio** (una domanda operativa precisa), l'**esito** (col grado in
testa: A giudicato · B accertamento · C congettura · F fatto pubblico ·
Zero = assenza documentata con sede nominata), la **fonte** (o la sede del
vuoto). Un riscontro trovato via motore di ricerca vale al massimo B: un
URL citato non è un URL letto. Un tentativo che trova il vuoto non si
scarta: è uno Stato Zero con sede, ed è prezioso.

Dieci sezioni: la rete del primo giorno; i numeri della caccia; via Gradoli
e le sue tre occasioni; le segnalazioni cadute; la Duchessa e il diversivo;
i comitati e gli esperti; i servizi in riforma; la guerra psicologica
(Pieczenik, Ferracuti, la linea «non è lui»); le tecniche mancate; il
confronto con come i covi si trovavano prima e dopo.

Le regole del corpus valgono per ogni riga: l'appartenenza a
un'organizzazione non è prova di condotta; per gli iscritti P2 vale il
perimetro della relazione Anselmi, non di più; nessuna persona è indicata
come responsabile fuori da un giudicato definitivo; le divergenze si
riportano, non si scelgono.

Le sei vittime — Oreste Leonardi, Domenico Ricci, Giulio Rivera, Francesco
Zizzi, Raffaele Iozzino, Aldo Moro — stanno in testa a tutto, come sempre.

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-K*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if not d.get("blocchi"):
            print(f"VUOTO {f.name}", file=sys.stderr)
            continue
        lotti.append(d)
    lotti.sort(key=lambda d: (ORDINE.index(d.get("sezione", "K10"))
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
    n_tent = sum(len(l["blocchi"]) for l in lotti)
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
        f"Tentativi assemblati: **{n_tent}**, in {len(lotti)} lotti "
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
    print(f"{uscita}: {n} tentativi, {len(lotti)} lotti, "
          f"{n_corr} correzioni, persi {len(persi)}")


if __name__ == "__main__":
    main()
