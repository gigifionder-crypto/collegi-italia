#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla la chiusura delle celle aperte, e ne ricava il registro delle
consegne.

Sorgente: i lotti verificati della campagna di chiusura (verificato-L*.json),
ciascuno con celle {domanda, capitolo, esito, testo, fonte, destinatario}.

L'esito puo' essere uno solo di tre, e la distinzione fra i primi due e' la
sola cosa che tenga in piedi il registro:

  chiusa            ho raggiunto la sede: risposta col grado in testa
  stato-zero        ho interrogato la sede nominata e non c'e'
  non-interrogabile la sede esiste ma da qui non si raggiunge

Il terzo esito non e' un fallimento. E' la conversione di una cella
indefinita in una CONSEGNA definita, e da esso questo script ricava il
secondo documento: le celle non interrogabili raggruppate per DESTINATARIO,
ciascuna con la richiesta esatta da rivolgergli. E' lo strumento che il
capitolo · XXXII chiama «chiusura per consegna» e che l'opera non aveva.

Uso:
    python3 assembla_celle.py DIR_LOTTI FILE_CAPITOLO [FILE_CONSEGNE]
"""
import collections
import json
import sys
from pathlib import Path

ESITI = ["chiusa", "stato-zero", "non-interrogabile"]
NOME = {
    "chiusa": "Chiuse — la sede ha risposto",
    "stato-zero": "Stato Zero — ho bussato, e non c'e'",
    "non-interrogabile": "Non interrogabili da qui — e diventano consegne",
}

INTESTAZIONE = """# La chiusura delle celle aperte

> **Dichiarazione.** Questo documento è stato generato da un'intelligenza
> artificiale (Claude, Anthropic) su richiesta del titolare del repository.
> Non è opera di storici di professione; ogni affermazione porta il suo grado
> di prova e va verificata sulle fonti primarie. Ogni lotto è stato prodotto
> da un agente indipendente e sottoposto a un verificatore avversariale il
> cui primo mandato era **declassare a «non interrogabile» ogni Stato Zero
> che non avesse davvero bussato**. Le correzioni sono riportate in coda.

## Che cosa è stato chiuso, e che cosa vuol dire chiudere

Il registro di chiusura dell'opera contava **ottanta** proposizioni non
interrogate. Rileggendo l'elenco si è visto che il criterio contava come
cella aperta ogni frase che contenesse la formula: titoli di sezione, frasi
di metodo, e perfino una negazione — *«il solo blocco dell'intera opera che
**non ha** celle aperte»*. Stretto il criterio con la regola stessa del
corpus — **una cella senza sede nominata non è una cella** — il conto è
sceso a **trentasei**, e le quarantaquattro differenze restano contate come
menzioni, non cancellate.

Questo documento interroga quelle trentasei. Ogni cella esce con **uno solo
di tre esiti**, e non ne esiste un quarto.

**Chiusa** significa che sono arrivato alla sede, o a una fonte che risponde,
e la risposta porta il suo grado in testa.

**Stato Zero** significa che ho interrogato la sede nominata e la risposta
non c'è. Vale solo se ho davvero bussato, e con quale robustezza è
dichiarato ogni volta.

**Non interrogabile** significa che la sede esiste ma da qui non si
raggiunge: un archivio fisico, un fascicolo giudiziario aperto, quattro
bobine di microfilm, un fondo disperso, un dominio che non risponde.

**E qui sta il punto dell'intera campagna.** La differenza fra *«ho bussato
e non c'è»* e *«non ho bussato»* è la sola cosa che tenga in piedi un
registro di celle: confonderle è l'errore più grave che si possa commettere,
perché trasforma un'ignoranza in un accertamento. Per questo il primo
controllo di ogni verificatore era proprio quello, e per questo le
declassazioni da Stato Zero a non interrogabile sono contate qui sotto una
per una.

**Un «non interrogabile» non è un fallimento.** È la conversione di una
cella indefinita in una **consegna definita**: la sede ha un nome, il
destinatario ha un nome, e la richiesta è scritta. Il capitolo · XXXII
chiama questo «chiusura per consegna» e la elenca fra le tre chiusure
legittime dell'opera. Il documento gemello di questo — il registro delle
consegne — è il primo strumento che l'opera abbia mai avuto per eseguirla.

"""

INTESTAZIONE_CONSEGNE = """# Il registro delle consegne

> **Dichiarazione.** Questo registro è **generato automaticamente** da
> `_verifiche/generatori/assembla_celle.py` a partire dalle celle che la
> campagna di chiusura ha classificato **non interrogabili da qui**. Non è
> un atto: è la lista, ordinata per destinatario, di ciò che andrebbe
> chiesto e a chi. **Nessuna di queste richieste è stata inviata**, e
> nessuna può esserlo senza una decisione del titolare del repository.

## Perché questo documento esiste

Il capitolo · XXXII fissa tre chiusure legittime per quest'opera. La terza è
**la chiusura per consegna**: trasmettere le celle aperte a chi ha i poteri
di aprirle — l'autorità che tiene il fascicolo, le commissioni, gli archivi,
le famiglie.

Era registrata come possibilità e non era mai stata eseguita, per una ragione
semplice: **le celle non erano indirizzate**. Una cella che dice «l'archivio
direbbe» non si può consegnare a nessuno; una cella che dice *quale*
archivio, *quale* fondo, *quale* segnatura e *quale* domanda, sì.

Questo registro contiene le seconde. Per ciascuna: il destinatario con il suo
nome istituzionale, la sede esatta, la domanda da rivolgere, e il capitolo
del corpus da cui la cella viene.

**Una nota che vale per tutte.** Nessuna di queste richieste chiede a
qualcuno di confermare una tesi. Chiedono tutte la stessa cosa — **un
documento** — e la risposta «non esiste» è una risposta buona quanto l'altra,
perché trasforma una cella aperta in uno Stato Zero con sede interrogata, che
è esattamente ciò di cui quest'opera ha più bisogno.

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("verificato-L*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"ILLEGGIBILE {f.name}: {e}", file=sys.stderr)
            continue
        if d.get("celle"):
            lotti.append(d)
    lotti.sort(key=lambda d: d.get("lotto", ""))
    return lotti


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cartella = Path(sys.argv[1])
    uscita = Path(sys.argv[2])
    consegne = Path(sys.argv[3]) if len(sys.argv) > 3 else \
        uscita.parent / "il-registro-delle-consegne.md"

    lotti = carica(cartella)
    if not lotti:
        sys.exit("nessun lotto verificato in " + str(cartella))

    tutte = [(l, c) for l in lotti for c in l["celle"]]
    conta = collections.Counter(c["esito"] for _, c in tutte)
    n_corr = sum(len(l.get("correzioni", [])) for l in lotti)

    # --- il capitolo ---
    p = [INTESTAZIONE, "## Il conto\n\n| esito | celle |\n|---|---:|\n"]
    for e in ESITI:
        p.append(f"| {NOME[e]} | **{conta.get(e, 0)}** |\n")
    p.append(f"| *totale* | *{len(tutte)}* |\n\n"
             f"Interventi dei verificatori avversariali: **{n_corr}**.\n")

    for e in ESITI:
        gruppo = [(l, c) for l, c in tutte if c["esito"] == e]
        if not gruppo:
            continue
        p.append(f"\n## {NOME[e]}\n")
        for l, c in gruppo:
            p.append(
                f"\n**{c['domanda'].strip()}**\n"
                f"— {c['testo'].strip()}\n"
                f"— *Fonte* · {c.get('fonte', '').strip()}\n"
            )
            if c.get("destinatario"):
                p.append(f"— *Destinatario* · {c['destinatario'].strip()}\n")
            if c.get("capitolo"):
                p.append(f"— *Cella registrata in* · {c['capitolo'].strip()}\n")

    p.append("\n## Il registro delle correzioni\n\n")
    for l in lotti:
        for c in l.get("correzioni", []):
            p.append(f"- [{l.get('lotto', '?')}] {c.strip()}\n")
    uscita.write_text("".join(p), encoding="utf-8")

    # --- le consegne, per destinatario ---
    per_dest = collections.defaultdict(list)
    for l, c in tutte:
        if c["esito"] == "non-interrogabile":
            per_dest[(c.get("destinatario") or "destinatario non nominato").strip()].append((l, c))

    q = [INTESTAZIONE_CONSEGNE,
         f"## Il conto\n\n**{sum(len(v) for v in per_dest.values())} celle** "
         f"da consegnare, a **{len(per_dest)} destinatari**. "
         "Nessuna inviata.\n"]
    for dest in sorted(per_dest, key=lambda d: (-len(per_dest[d]), d)):
        voci = per_dest[dest]
        q.append(f"\n## {dest}\n\n*{len(voci)} "
                 f"{'richiesta' if len(voci) == 1 else 'richieste'}.*\n")
        for l, c in voci:
            q.append(f"\n**{c['domanda'].strip()}**\n"
                     f"— {c['testo'].strip()}\n"
                     f"— *Sede* · {l.get('sede', '').strip()}\n")
            if c.get("capitolo"):
                q.append(f"— *Cella registrata in* · {c['capitolo'].strip()}\n")
    q.append("\n---\n\n**Nessuna di queste richieste è stata inviata.** "
             "La decisione di inviarle non appartiene a chi ha generato "
             "questo registro.\n")
    consegne.write_text("".join(q), encoding="utf-8")

    print(f"{uscita}: {len(tutte)} celle, {len(lotti)} lotti, "
          f"{n_corr} correzioni — " +
          ", ".join(f"{e}={conta.get(e, 0)}" for e in ESITI))
    print(f"{consegne}: {sum(len(v) for v in per_dest.values())} consegne "
          f"a {len(per_dest)} destinatari")


if __name__ == "__main__":
    main()
