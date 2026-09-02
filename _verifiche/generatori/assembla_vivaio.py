#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla «Il vivaio nero e il rifugio latinoamericano» dai SEI lotti
REDATTI E NON VERIFICATI della campagna wf_1d7f1001-c05, interrotta dal
limite settimanale prima che un solo critico avversariale girasse.

Questo assemblatore fa due cose che nessun altro dell'opera fa, e le
dichiara entrambe nel documento che produce:

  1. marca l'intero capitolo come NON PASSATO DALLA VERIFICA AVVERSARIALE;
  2. applica al posto del critico mancante UN SOLO controllo, il piu'
     meccanico e il piu' urgente -- la qualificazione dei gradi A -- e
     annota ogni intervento accanto al blocco, mai al suo posto.

Uso: python3 assembla_vivaio.py DIR_BOZZE FILE_USCITA
"""
import json
import re
import sys
from pathlib import Path

ORDINE = [f"N{i}" for i in range(1, 9)]
ROMANI = {f"N{i}": r for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"], 1)}

# Un blocco ha davvero aperto qualcosa se lo dichiara con un percorso o una riga.
APERTO = re.compile(r'APERTO E LETTO|sed -n|grep -n|righe \d+-\d+', re.I)
# Un grado A "nudo": comincia con A e non porta gia' la doppia qualificazione.
A_NUDO = re.compile(r'^A\b(?!\s*\(categoria)')

INTESTAZIONE = """# Il vivaio nero e il rifugio latinoamericano — sei lotti non verificati

> **Dichiarazione, e va letta prima di ogni riga.** Questo documento è stato
> generato da un'intelligenza artificiale (Claude, Anthropic). **A differenza
> di ogni altro capitolo di quest'opera, NON È PASSATO DALLA VERIFICA
> AVVERSARIALE.** La campagna che lo ha prodotto è stata interrotta dal limite
> settimanale di utilizzo **dopo la redazione di sei lotti su otto e prima che
> un solo critico girasse**: otto agenti su quattordici hanno terminato con
> errore, e fra essi **tutti e sei i verificatori**.
>
> **Il lettore sappia dunque che il controllo indipendente su questi
> settantasette blocchi non è stato eseguito**, ed è dichiarato mancante
> invece che presunto. I due lotti non redatti — **N7, il legame con
> Badalamenti, e N8, le sedi e le consegne** — **non ci sono**, e non sono
> stati sostituiti con testo di ripiego.

## Che cosa è stato fatto al posto del critico, e che cosa no

Al posto della verifica avversariale, chi ha condotto la campagna ha applicato
**un solo controllo**, scelto perché è il più meccanico e il più urgente fra i
sette del mandato: **la qualificazione dei gradi A**.

La regola è quella dell'opera: **una condanna vale A solo se definitiva, e
solo se la definitività è stata accertata su una sede aperta.** In questa
campagna **nessuna pagina esterna è stata aperta** — la rete della macchina
nega ogni dominio documentale — e dunque **ogni A che poggi su un motore di
ricerca porta la via di questa sessione, che è C.**

Molti blocchi lo dichiaravano già da sé, nella forma
**«A (categoria: giudicato) / C (via di questa sessione)»**, che è quella
giusta. **Dove mancava, è stata aggiunta, e l'aggiunta è marcata.** Tre blocchi
dichiarano invece **«APERTO E LETTO»** con percorso e numeri di riga su fonti
parlamentari già dentro il corpus: quelli conservano il proprio grado.

**Gli altri sei controlli del mandato non sono stati eseguiti** — assoluzioni
non dichiarate, appartenenza trattata come condotta, etichette all'ingrosso,
Stati Zero fabbricati, autoriscontro, verifica indipendente di due
affermazioni per lotto. **Chi legge li esegua da sé.**

## Che cosa la campagna ha comunque stabilito

**La premessa che l'ha generata è smentita, ed è il suo risultato principale.**
La richiesta diceva «ex SS come gli Ertl». **Hans Ertl non era SS**: alpinista,
cineoperatore, collaboratore di Leni Riefenstahl, poi operatore delle truppe di
propaganda della **Wehrmacht** presso Rommel. E sua figlia **Monika Ertl** fu
**guerrigliera dell'Esercito di liberazione nazionale boliviano**, e il 1º
aprile 1971 uccise ad Amburgo il colonnello **Roberto Quintanilla Pereira**.

**Un padre propagandista del Reich e una figlia che uccide per Che Guevara: se
una famiglia non basta a produrre una linea, un'etichetta non basta a produrre
una rete.** È la stessa regola che l'opera aveva già scritto per un vivaio che
produsse un fondatore delle Brigate Rosse, un saggista eurasiatista e uno
storico medievista.

"""


def carica(cartella: Path):
    lotti = []
    for f in sorted(cartella.glob("bozza-N*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        if d.get("blocchi"):
            lotti.append(d)
    lotti.sort(key=lambda d: ORDINE.index(d["sezione"])
               if d["sezione"] in ORDINE else 99)
    return lotti


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cartella, uscita = Path(sys.argv[1]), Path(sys.argv[2])
    lotti = carica(cartella)
    if not lotti:
        sys.exit("nessuna bozza in " + str(cartella))

    interventi = []
    parti = [INTESTAZIONE]
    n = 0
    for lotto in lotti:
        sez = lotto["sezione"]
        parti.append(f"\n## {ROMANI.get(sez, sez)}. "
                     f"{lotto.get('titolo_sezione', sez)}\n")
        for b in lotto["blocchi"]:
            n += 1
            e = b["e"].strip()
            f = b.get("f", "")
            nota = ""
            if A_NUDO.match(e) and not APERTO.search(f):
                nota = ("\n— *Qualificazione del compilatore, aggiunta al "
                        "posto del critico mancante* · **A è la categoria "
                        "dell'atto; la via di questa sessione è C**, perché "
                        "la fonte è un motore di ricerca e nessuna pagina è "
                        "stata aperta. Il grado non sale finché la sede non "
                        "è interrogata.")
                interventi.append(f"{sez} · blocco {n}")
            parti.append(
                f"\n**{n} · {b['b'].strip()}**\n"
                f"— {e}\n"
                f"— *Fonte* · {f.strip()}\n" + (nota + "\n" if nota else ""))

    parti.append("\n## Registro di chiusura\n\n")
    parti.append(
        f"Blocchi assemblati: **{n}**, in **{len(lotti)} lotti su otto**. "
        f"**Lotti verificati: zero.**\n\n"
        f"**Stato Zero di lavorazione** (sede: questo registro): i lotti "
        f"**N7** — *Badalamenti, e la ricerca esplicita del legame* — e "
        f"**N8** — *le sedi e le consegne* — **non sono stati redatti**, "
        f"perché il limite settimanale ha interrotto la campagna. Non sono "
        f"stati sostituiti, e la numerazione non è stata rifatta.\n\n"
        f"**Qualificazioni di grado aggiunte dal compilatore: "
        f"{len(interventi)}**, tutte della stessa specie — un A nudo "
        f"riportato alla propria via di sessione. Elenco:\n\n")
    for i in interventi:
        parti.append(f"- {i}\n")
    parti.append(
        "\n**E una avvertenza finale, che vale più dell'elenco.** "
        "Un capitolo non verificato non è un capitolo peggiore degli altri: "
        "**è un capitolo di cui non si sa se sia peggiore.** La differenza è "
        "tutta lì, ed è la ragione per cui questa pagina esiste invece di un "
        "silenzio.\n")

    uscita.write_text("".join(parti), encoding="utf-8")
    print(f"{uscita}: {n} blocchi, {len(lotti)}/8 lotti, "
          f"0 verificati, {len(interventi)} qualificazioni aggiunte")


if __name__ == "__main__":
    main()
