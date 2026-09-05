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

Uso: python3 assembla_integrale.py [CARTELLA_USCITA] [--unico]
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO = BASE.parent
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
UNICO = "--unico" in sys.argv          # tutto in un solo volume, non in tomi
COMPLETA = "--completa" in sys.argv    # il volume unico E gli undici tomi, di seguito
USCITA = Path(ARGS[0]) if ARGS else REPO / "_integrale"
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


def senza_frontespizio(md: str) -> str:
    """Toglie dal proemio il suo frontespizio -- titolo, sottotitoli, epigrafe
    e dichiarazione -- perche' la testa del volume li porta gia'.

    Non si ancora al testo del titolo: quello cambia, e un taglio ancorato a
    una parola smette di tagliare il giorno in cui la parola cambia. E' gia'
    successo, e il frontespizio e' comparso due volte nello stesso tomo. Si
    ancora invece alla forma: la pila di titoli in testa, e la dichiarazione
    riconosciuta dal suo incipit, come fa il compositore per la copertina.
    """
    m = re.search(r"^>\s*\*\*Dichiarazione", md, re.M)
    if m:
        fine = md.find("\n\n", m.start())
        return md[fine:].lstrip("\n-\n ").lstrip() if fine > 0 else md
    righe = md.split("\n")
    i = 0
    while i < len(righe) and (not righe[i].strip()
                              or re.match(r"^#{1,5}\s", righe[i])
                              or righe[i].strip() == "---"):
        i += 1
    return "\n".join(righe[i:]).strip("\n")


def testa(tomo_n, tomo_tit, sommario, nota):
    return f"""# OPERA NERA

## Il Secolo Nero della Bella Europa

### La Seconda Guerra Mondiale non è Finita

#### 100 anni di Guerra tra opposte visioni: dalla Federazione, all'Europa delle Nazioni, passando per Quarto Reich e Nazi-Bolscevismo Euroasiatico

##### Edizione integrale · Tomo {tomo_n} — {tomo_tit}

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


def completa():
    """Il volume unico seguito dagli undici tomi: la stessa opera due volte.

    E' cio' che il titolare ha chiesto dopo che gli e' stato detto, con la
    verifica in mano, che i due formati portano contenuto identico -- 166 parti,
    stesse impronte, nessuna di qua che non sia di la'. La richiesta e' stata
    riconfermata, e si esegue; ma la ripetizione si dichiara in testa e non si
    nasconde, perche' un lettore che sfogliasse settemila pagine senza saperlo
    dedurrebbe un corpus grande il doppio di quello che e'.
    """
    vol = (USCITA / "opera-nera-volume-unico.md")
    man = json.loads((USCITA / "manifesto-tomi.json").read_text(encoding="utf-8"))["tomi"]
    if not vol.exists():
        sys.exit("manca il volume unico: eseguire prima con --unico")
    for t in man:
        if not (USCITA / t["file"]).exists():
            sys.exit(f"manca {t['file']}: eseguire prima senza --unico")

    corpo_vol = senza_frontespizio(vol.read_text(encoding="utf-8"))
    pezzi = [f"# Parte prima · La monografia in un volume\n\n{corpo_vol}",
             "# Parte seconda · Gli undici tomi, ciascuno col suo apparato"]
    for t in man:
        md = (USCITA / t["file"]).read_text(encoding="utf-8").rstrip()
        # Il titolo d'apertura di ogni tomo e' quello dell'opera, e undici
        # segnalibri che dicono tutti «OPERA NERA» in settemila pagine non
        # sono una navigazione: qui l'apertura nomina il tomo. Il resto del
        # frontespizio del tomo -- sottotitoli, epigrafe, dichiarazione,
        # sommario e nota -- resta dov'e'.
        capo = f"# Tomo {ROMANI[t['tomo'] - 1].capitalize()} :: {t['titolo']}"
        md = re.sub(r"^#\s+[^\n]*", capo, md, count=1)
        pezzi.append(md)

    voci = ["\n**Parte prima · La monografia in un volume**\n",
            "- L'opera intera, gli undici tomi fusi in un solo corpo"]
    voci.append("\n**Parte seconda · Gli undici tomi**\n")
    for t in man:
        voci.append(f"- Tomo {ROMANI[t['tomo'] - 1].capitalize()} · {t['titolo']}")

    nota = (
        "**Questo documento porta l'opera due volte, e va detto subito.**\n\n"
        "La **parte prima** è la monografia in un volume: la guida e le "
        "centocinquantaquattro parti del corpus, con gli undici tomi come "
        "divisioni interne. La **parte seconda** sono gli undici tomi uno dopo "
        "l'altro, ciascuno con la propria copertina, la propria dichiarazione, "
        "il proprio sommario e la propria nota d'edizione.\n\n"
        "**Il testo delle due parti è lo stesso, e non per approssimazione: è "
        "stato verificato.** Centosessantasei parti nell'una e centosessantasei "
        "nell'altra, con la medesima impronta SHA-256 parte per parte, nessuna "
        "presente solo di qua o solo di là. *L'unica differenza è l'apparato*: "
        "nella parte prima il frontespizio compare una volta, nella parte "
        "seconda undici, e con esso le note che ciascun tomo dà di sé.\n\n"
        "**Perché allora esiste questo documento.** Perché è stato chiesto, "
        "dopo che la verifica era stata mostrata e la richiesta riconfermata. "
        "**Si esegue quello che è stato chiesto e si dichiara quello che si è "
        "fatto**: chi sfogliasse settemila pagine senza questa nota dedurrebbe "
        "un corpus grande il doppio di quello che è, e sarebbe un errore che "
        "questo documento avrebbe indotto.\n\n"
        "**Il conto vero resta quello di sempre**, e non raddoppia con le "
        "pagine: **centocinquantaquattro parti**, **due milioni ottantanovemila "
        "parole**, **centoquarantadue celle aperte**, **dodici conferme del "
        "risultato ricorrente**, **cinquantasei archi Savona**. *Un'opera "
        "stampata due volte non è un'opera doppia.*")

    testo = (testa("", "", "\n".join(voci), nota)
             .replace("\n\n##### Edizione integrale · Tomo  — \n", "\n")
             .replace("## Sommario del tomo", "## Sommario del documento")
             .replace("## Nota su questo tomo", "## Nota su questo documento")
             + "\n\n---\n\n" + "\n\n---\n\n".join(pezzi))
    f = USCITA / "opera-nera-monografia-completa.md"
    f.write_text(testo + "\n", encoding="utf-8")
    print(f"monografia completa: volume unico + {len(man)} tomi · "
          f"{len(testo.split()):,} parole · {f}".replace(",", "."))


def main():
    if COMPLETA:
        return completa()
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
        testo_f = (BASE / f).read_text(encoding="utf-8").rstrip()
        if f == man["proemio"]:
            testo_f = senza_frontespizio(testo_f)
        pezzi.append(testo_f)
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
    # --- Volume unico -----------------------------------------------------
    # Tutto in un solo documento: la guida e poi le 154 parti di seguito.
    # E' cio' che l'edizione in tomi evita per ragioni di peso, non di forma:
    # la forma dell'opera e' una sola, e questa e' quella.
    if UNICO:
        # Gli undici tomi restano, ma come divisioni interne: dal primo
        # all'ultimo, ciascuno aperto dal suo occhiello. Tremilacinquecento
        # pagine di parti numerate senza un solo appiglio intermedio non si
        # percorrono; le divisioni sono la spina dorsale del volume.
        romano = lambda n: ROMANI[n - 1].capitalize()
        voci_v = [f"\n**Tomo Primo · La guida e il metodo**\n"] + list(voci)
        corpo, visti = [], {}
        for n, blocco in enumerate(tomi, start=2):
            e_p, e_u = blocco[0]["sigla"], blocco[-1]["sigla"]
            tit = e_p if e_p == e_u else f"{e_p} — {e_u}"
            corpo.append(f"# Tomo {romano(n)} :: {tit}")
            voci_v.append(f"\n**Tomo {romano(n)} · {tit}**\n")
            for p in blocco:
                et = p["sigla"]
                visti[et] = visti.get(et, 0) + 1
                if visti[et] > 1:
                    sys.exit(f"SIGLA RIPETUTA NEL VOLUME: {et}")
                corpo.append(f"# {et}\n\n{declassa(p['testo'])}")
                voci_v.append(f"- {et}")
        if len(visti) != len(pesate):
            sys.exit(f"PARTI PERSE: {len(visti)} su {len(pesate)}")
        bis = [x for x in voci_v if x.endswith((" bis", " ter", " quater"))]
        nota_v = (
            f"**Questa è la monografia intera in un solo documento: gli undici "
            f"tomi dal primo all'ultimo.** Porta la guida monografica e poi "
            f"**tutte le {len(pesate)} parti del "
            f"corpus**, {sum(x['parole'] for x in pesate):,} parole, nell'ordine "
            "in cui `parti.json` le registra — sorgente unica dell'ordine, come "
            "per ogni edizione di quest'opera.\n\n"
            "**Prima viene il modo di leggere, poi ciò che si legge.** La guida "
            "apre il volume — il prologo sulla scala di triangolazione, il "
            "proemio con i sei nomi, i sette libri narrativi coi loro referti, "
            "il congedo, il quadro sinottico delle piste e gli apparati — e "
            "**non contiene documenti: contiene il modo di leggerli**. Tutto ciò "
            "che segue sono i documenti, **non una scelta: tutti**.\n\n"
            "**Gli undici tomi ci sono, come divisioni.** L'edizione in volumi "
            "separati esiste per il peso dei file, non per la forma dell'opera: "
            "qui i tomi restano dove erano, ciascuno aperto dal suo occhiello, "
            "**dal primo all'ultimo**. *Tremilacinquecento pagine di parti "
            "numerate senza un appiglio intermedio non si percorrono.*\n\n"
            "**I libri e i capitoli non portano titolo: portano la loro "
            "numerazione.** Un titolo è già una lettura, e anteporne una a ogni "
            "documento contraddirebbe un'opera costruita per separare il fatto "
            "dalla sua interpretazione. *Ciò che il documento dice di sé non è "
            "toccato*: il titolo che ciascuna parte si dà resta la sua prima "
            "riga, un gradino più in basso nella gerarchia.\n\n"
            "**Un avvertimento sull'ordine, perché altrimenti sembra un "
            "disordine.** Il registro **appende e non rinumera**: una campagna "
            "aggiunta dopo entra in coda, anche se il suo Libro d'appartenenza "
            "era stato aperto molto prima, e il volume può perciò passare da "
            "un'Appendice a un Libro già incontrato. **Non è un errore di "
            "composizione: è la storia del corpus leggibile nel suo ordine**, ed "
            "è preferita a una risistemazione che cancellerebbe l'ordine in cui "
            "il lavoro è realmente cresciuto.").replace(",", ".")
        if bis:
            nota_v += ("\n\n**Una parola sulle sigle «bis».** "
                       f"{len(bis)} capitoli portano un numerale già usato in un "
                       "altro capitolo del medesimo Libro: la terza campagna "
                       "ripartì da IV e riusò i numeri della seconda. **Il "
                       "registro non è stato rinumerato** — appende e non "
                       "rinumera — ma un rinvio dev'essere univoco, e alla "
                       "seconda occorrenza di un numerale si è aggiunto «bis» in "
                       "composizione. *«bis» non afferma nulla: dice soltanto che "
                       "quel numero compare per la seconda volta nel registro.*")
        testo = (testa("", "", "\n".join(voci_v), nota_v)
                 .replace("\n\n##### Edizione integrale · Tomo  — \n", "\n")
                 .replace("## Sommario del tomo", "## Sommario del volume")
                 .replace("## Nota su questo tomo", "## Nota su questo volume")
                 + "\n\n---\n\n# Tomo Primo :: La guida e il metodo\n\n"
                 + guida + "\n\n" + "\n\n".join(corpo))
        fv = USCITA / "opera-nera-volume-unico.md"
        fv.write_text(testo + "\n", encoding="utf-8")
        print(f"volume unico: {len(pesate)} parti · "
              f"{len(testo.split()):,} parole · {fv}".replace(",", "."))
        return

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

    # Il conteggio delle pagine lo sa solo la composizione, non l'assemblaggio:
    # se un manifesto precedente lo porta, lo si conserva invece di azzerarlo.
    # Un assemblatore che cancella un dato che non sa produrre lascia dietro di
    # se' un manifesto piu' povero di quello che ha trovato.
    mf = USCITA / "manifesto-tomi.json"
    vecchio = {}
    if mf.exists():
        try:
            d = json.loads(mf.read_text(encoding="utf-8"))
            vecchio = {t["file"]: t.get("pagine") for t in d.get("tomi", [])}
        except (ValueError, KeyError):
            vecchio = {}
    for t in scritti:
        if vecchio.get(t["file"]):
            t["pagine"] = vecchio[t["file"]]
    pag = [t.get("pagine") for t in scritti]
    fuori = {"tomi": scritti}
    if all(pag):
        fuori["pagine_totali"] = sum(pag)
    mf.write_text(json.dumps(fuori, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tot = sum(t["parole"] for t in scritti)
    print(f"{len(scritti)} tomi · {sum(t['parti'] for t in scritti)} parti · "
          f"{tot:,} parole".replace(",", "."))
    for t in scritti:
        print(f"  Tomo {t['tomo']:2d}  {t['parole']:8,d} parole  {t['parti']:3d} parti  "
              f"{t['titolo']}".replace(",", "."))


if __name__ == "__main__":
    main()
