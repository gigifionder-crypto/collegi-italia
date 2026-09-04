#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembla l'OPERA MONOGRAFICA INTEGRALE E OMNICOMPRENSIVA.

Non e' l'edizione ridotta: qui entrano TUTTE le 154 parti registrate in
parti.json -- oltre due milioni di parole -- con l'apparato monografico come
guida di lettura.

Perche' in tomi. Duemilioni di parole fanno circa quattromilacinquecento
pagine: un solo PDF sarebbe di novanta megabyte, inconsegnabile e illeggibile.
Le opere integrali si pubblicano in volumi da sempre, e per la stessa ragione.
NESSUNA PARTE SI SPEZZA fra due tomi: un documento e' un'unita', e tagliarlo a
meta' per far quadrare un conto di pagine sarebbe far prevalere la contabilita'
sul contenuto. Le parti che da sole superano il bersaglio fanno tomo da se'.

Uso: python3 assembla_integrale.py [CARTELLA_USCITA]
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO = BASE.parent
USCITA = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "_integrale"
USCITA.mkdir(parents=True, exist_ok=True)

BERSAGLIO = 240_000        # parole per tomo, indicativo
ROMANI = ("primo secondo terzo quarto quinto sesto settimo ottavo nono decimo "
          "undicesimo dodicesimo tredicesimo quattordicesimo quindicesimo "
          "sedicesimo diciassettesimo diciottesimo").split()

# Titoli generici ripetuti in testa a molti sorgenti: sotto l'occhiello della
# parte sono ridondanti. E' la stessa regola della filiera integrale storica.
GENERICI = [re.compile(r"^#\s*Aldo Moro\s*$"),
            re.compile(r"^#\s*Aldo Moro\s+—\s+Una guerra senza fine\s*$")]


def declassa(md: str) -> str:
    """Abbassa di due livelli i titoli della parte, e toglie il solo titolo
    generico d'apertura. Nulla di specifico viene rimosso: cio' che il
    documento dice di se' resta, un gradino piu' in basso."""
    righe = md.rstrip().split("\n")
    for i, r in enumerate(righe):
        if not r.strip():
            continue
        if r.startswith("# ") and any(g.match(r.strip()) for g in GENERICI):
            righe.pop(i)
        break
    fuori = []
    for r in righe:
        m = re.match(r"^(#{1,4})\s+(.*)$", r)
        fuori.append(f"{'#' * min(len(m.group(1)) + 2, 6)} {m.group(2)}" if m else r)
    return "\n".join(fuori).strip("\n")


def gruppo(etichetta: str) -> str:
    return etichetta.split(" · ")[0]


RE_NUM = re.compile(r"^([IVXLC]+|\d+)\.\s+(.*)$")


def numerale(etichetta: str) -> str:
    pezzi = etichetta.split(" · ")
    return pezzi[1] if len(pezzi) > 1 else ""


def scomponi(p: dict):
    """Separa il titolo del Libro dal numerale e dal titolo della parte.

    I titoli del corpus hanno forma «Libro quinto — Il vettore e il ceppo —
    IV. L'incrocio Feltrinelli-Hyperion»: il Libro porta un titolo proprio, piu'
    ricco della sola etichetta, e ripeterlo su ogni capitolo sarebbe rumore.
    Ritorna (titolo_del_libro, numerale, titolo_della_parte).
    """
    pezzi = [x.strip() for x in p["titolo"].split(" — ")]
    for i, z in enumerate(pezzi):
        m = RE_NUM.match(z)
        if m and i > 0:
            return (" — ".join(pezzi[:i]), m.group(1),
                    " — ".join([m.group(2)] + pezzi[i + 1:]))
    et = p["etichetta"]
    for sep in (" — ", " - "):
        if p["titolo"].startswith(et + sep):
            return gruppo(et), numerale(et), p["titolo"][len(et) + len(sep):]
    return gruppo(et), numerale(et), p["titolo"]


def testa(tomo_n, tomo_tit, sommario, nota):
    return f"""# OPERA NERA

## Il Secolo Nero dell'Italia più Bella

### Opera integrale e omnicomprensiva · Tomo {tomo_n} — {tomo_tit}

> «NON SIAMO PADRONI NEMMENO IN CASA NOSTRA»
>
> — **Sigmund Freud**

> **Dichiarazione, in testa e non in coda.** Quest'opera è stata generata da
> un'intelligenza artificiale (Claude, Anthropic) su richiesta del titolare del
> repository. Ogni affermazione porta il suo grado di prova — **A** giudicato
> definitivo, **B** accertamento qualificato, **C** congettura o fonte
> secondaria, **F** fatto pubblico, **Stato Zero** assenza documentata con sede
> nominata e interrogata. Nessuna persona è indicata come responsabile di un
> reato fuori da un giudicato definitivo. Gli assolti restano assolti. Le
> divergenze si riportano, non si scelgono.

---

## Sommario del tomo

{sommario}

## Nota su questo tomo

{nota}
"""


def main():
    man = json.loads((BASE / "opera.json").read_text(encoding="utf-8"))
    parti = json.loads((REPO / "_verifiche" / "generatori" / "parti.json")
                       .read_text(encoding="utf-8"))["parti"]

    # Il registro ripete dieci numerali del Libro dodicesimo: la terza
    # campagna riparti' da IV e riuso' IV-XIII, gia' assegnati alla seconda.
    # Non si rinumera il registro -- appende e non rinumera, e' la sua regola --
    # ma un rinvio deve essere univoco: alla seconda occorrenza di un numerale
    # si aggiunge «bis» in composizione, e alla terza «ter». Non si aggiunge
    # nulla che affermi qualcosa: «bis» dice soltanto «la seconda volta che
    # questo numero compare nel registro», che e' esattamente il fatto.
    ORD = ("", " bis", " ter", " quater")
    conta, ripetute = {}, []
    for p in parti:
        et = p["etichetta"]
        conta[et] = conta.get(et, 0) + 1
        p["sigla"] = et + ORD[min(conta[et] - 1, 3)]
        if conta[et] > 1:
            ripetute.append(p["sigla"])

    pesate = []
    for p in parti:
        f = REPO / p["file"]
        if not f.exists():
            sys.exit(f"MANCANTE: {p['file']}")
        testo = f.read_text(encoding="utf-8")
        pesate.append({**p, "parole": len(testo.split()), "testo": testo})

    # Ripartizione in tomi: si riempie fino al bersaglio e si chiude al
    # confine di una parte, mai dentro.
    tomi, corrente, peso = [], [], 0
    for p in pesate:
        # Si chiude il tomo solo se ha gia' corpo: altrimenti una parte enorme
        # che arriva presto lascerebbe dietro di se' un tomo-mozzicone.
        if corrente and peso >= BERSAGLIO * 0.4 and peso + p["parole"] > BERSAGLIO:
            tomi.append(corrente); corrente, peso = [], 0
        corrente.append(p); peso += p["parole"]
    if corrente:
        tomi.append(corrente)

    scritti = []

    # --- Tomo I: la guida ------------------------------------------------
    pezzi = []
    for f in [man["prologo"]] + [man["proemio"]]:
        pezzi.append((BASE / f).read_text(encoding="utf-8").rstrip())
    for L in man["libri"]:
        pezzi.append((BASE / L["narrazione"]).read_text(encoding="utf-8").rstrip())
    for c in man["chiusura"]:
        pezzi.append((BASE / c).read_text(encoding="utf-8").rstrip())
    # Gli apparati sono strumenti di lettura, non documenti: stanno con la guida.
    BREVE = REPO / "_verifiche" / "edizione-breve"
    pezzi.append("# Apparati")
    for c in man["apparati"]:
        f_app = BREVE / "opera" / c
        if not f_app.exists():
            f_app = BREVE / c
        pezzi.append(f_app.read_text(encoding="utf-8").rstrip())

    reg = (REPO / "il-registro-savona.md").read_text(encoding="utf-8")
    i = reg.find("## Gli archi")
    guida = "\n\n---\n\n".join(pezzi).replace("<!--REGISTRO-SAVONA-->", reg[i:].rstrip())
    # Nella guida il titolo e l'epigrafe sono quelli del proemio: si tolgono,
    # perche' la testa del tomo li porta gia'.
    guida = re.sub(r"^#\s+ALDO MORO\s*\n+##[^\n]*\n+###[^\n]*\n+(>\s?[^\n]*\n)+", "", guida, count=1)

    voci = []
    for L in man["libri"]:
        t = (BASE / L["narrazione"]).read_text(encoding="utf-8").split("\n", 1)[0][2:].strip()
        voci.append(f"- **{t}**")
    nota_g = (
        "**Questo tomo è la guida, e gli altri sono il corpus.** Contiene "
        "l'apparato monografico per intero — il prologo sulla scala di "
        "triangolazione, il proemio con i sei nomi, i sette libri narrativi con "
        "i loro referti, il congedo e il quadro sinottico delle piste. "
        "**Non contiene documenti: contiene il modo di leggerli.**\n\n"
        "**E una differenza dall'edizione ridotta va dichiarata qui.** In quella, "
        "dopo ogni libro narrativo seguiva una scelta di capitoli documentari. "
        "**Qui non c'è una scelta: c'è tutto**, nei tomi che seguono, "
        "nell'ordine in cui il corpus lo registra. I raccordi che nell'edizione "
        "ridotta annunciavano una selezione qui non hanno oggetto, e "
        "**sono stati tolti invece di essere lasciati a puntare al vuoto**.")
    testo = testa("I", "La guida e il metodo", "\n".join(voci), nota_g) + "\n\n---\n\n" + guida
    f = USCITA / "tomo-01-la-guida.md"
    f.write_text(testo + "\n", encoding="utf-8")
    scritti.append({"tomo": 1, "titolo": "La guida e il metodo", "file": f.name,
                    "parti": 0, "parole": len(testo.split())})

    # --- Tomi del corpus --------------------------------------------------
    for n, blocco in enumerate(tomi, start=2):
        e_primo, e_ultimo = blocco[0]["sigla"], blocco[-1]["sigla"]
        tit = e_primo if e_primo == e_ultimo else f"{e_primo} — {e_ultimo}"
        # Il titolo del Libro e' il piu' ricco fra quelli che le sue parti
        # dichiarano: prenderlo dalla prima parte darebbe a volte il piu' povero.
        # Nessun titolo al libro, nessun titolo al capitolo: ogni parte porta
        # in testa la sola etichetta con cui `parti.json` la registra, cioe'
        # la sua numerazione. Il titolo che il documento da' a se' stesso non
        # e' toccato: resta la prima riga del documento, un gradino piu' in
        # basso. Non si cancella cio' che una fonte dice di se'.
        voci, corpo, visti = [], [], {}
        for p in blocco:
            et = p["sigla"]
            visti[et] = visti.get(et, 0) + 1
            if visti[et] > 1:
                sys.exit(f"SIGLA RIPETUTA NELLO STESSO TOMO: {et} — "
                         "due capitoli con la stessa numerazione renderebbero "
                         "ambiguo il rinvio del sommario.")
            # Stesso testo nel titolo e nella voce di sommario: e' cio' che
            # permette al rinvio di agganciare.
            corpo.append(f"# {et}\n\n{declassa(p['testo'])}")
            voci.append(f"- {et}")
        nota = (f"**Questo tomo porta {len(blocco)} parti del corpus, "
                f"{sum(x['parole'] for x in blocco):,} parole, nell'ordine in cui "
                "`parti.json` le registra — sorgente unica dell'ordine, come per "
                "ogni edizione di quest'opera.**\n\n"
                "**Nessuna parte è spezzata fra due tomi.** Un documento è "
                "un'unità: tagliarlo a metà per far quadrare un conto di pagine "
                "farebbe prevalere la contabilità sul contenuto. Le parti che da "
                "sole superano il bersaglio fanno tomo da sé, e i tomi sono "
                "perciò diseguali — **è la conseguenza voluta della regola, non "
                "un difetto della ripartizione**.\n\n"
                "**I libri e i capitoli non portano titolo: portano la loro "
                "numerazione.** È una scelta d'edizione — l'opera si chiama "
                "*Opera Nera* e non intitola le sue parti — e ha una "
                "conseguenza che va detta: **un titolo è già un'interpretazione**, "
                "e un'opera che distingue il fatto dalla sua lettura fa bene a "
                "non anteporne una a ogni documento. *Ciò che il documento dice "
                "di sé non è toccato*: il titolo che ciascuna parte si dà resta "
                "la sua prima riga, un gradino più in basso nella gerarchia, "
                "insieme al solo titolo generico dell'opera, tolto perché "
                "ridondante sotto l'occhiello che lo precede.\n\n"
                "**Un avvertimento sull'ordine, perche' altrimenti sembra un "
                "disordine.** Le parti si susseguono come `parti.json` le "
                "registra, e quel registro **appende e non rinumera**: una "
                "campagna aggiunta dopo entra in coda, anche se il suo Libro "
                "d'appartenenza era stato aperto molto prima. Percio' un tomo "
                "puo' passare da un'Appendice a un Libro gia' incontrato. "
                "**Non e' un errore di ripartizione: e' la storia del corpus "
                "leggibile nel suo ordine**, ed e' preferita a una "
                "risistemazione che cancellerebbe l'ordine in cui il lavoro "
                "e' realmente cresciuto.*").replace(",", ".")
        bis = [x for x in voci if x.endswith((" bis", " ter", " quater"))]
        if bis:
            nota += ("\n\n**Una parola sulle sigle «bis».** In questo tomo "
                     f"{len(bis)} capitoli portano un numerale gia' usato in un "
                     "altro capitolo del medesimo Libro: la terza campagna "
                     "riparti' da IV e riuso' i numeri della seconda. **Il "
                     "registro non e' stato rinumerato** — appende e non "
                     "rinumera, ed e' la regola di tutta l'opera — ma un rinvio "
                     "deve essere univoco, e alla seconda occorrenza di un "
                     "numerale si e' aggiunto «bis» in composizione. "
                     "*«bis» non afferma nulla: dice soltanto che quel numero "
                     "compare per la seconda volta nel registro.*")
        testo = testa(ROMANI[n - 1].capitalize(), tit, "\n".join(voci), nota) + \
            "\n\n---\n\n" + "\n\n".join(corpo)
        f = USCITA / f"tomo-{n:02d}-{re.sub(r'[^a-z0-9]+', '-', tit.lower()).strip('-')}.md"
        f.write_text(testo + "\n", encoding="utf-8")
        scritti.append({"tomo": n, "titolo": tit, "file": f.name,
                        "parti": len(blocco), "parole": len(testo.split())})

    (USCITA / "manifesto-tomi.json").write_text(
        json.dumps({"tomi": scritti}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tot = sum(t["parole"] for t in scritti)
    print(f"{len(scritti)} tomi · {sum(t['parti'] for t in scritti)} parti · "
          f"{tot:,} parole".replace(",", "."))
    for t in scritti:
        print(f"  Tomo {t['tomo']:2d}  {t['parole']:8,d} parole  {t['parti']:3d} parti  "
              f"{t['titolo']}".replace(",", "."))


if __name__ == "__main__":
    main()
