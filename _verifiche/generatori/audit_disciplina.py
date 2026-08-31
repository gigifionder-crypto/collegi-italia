#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L'audit della disciplina — la prescrizione dell'opera applicata all'opera.

Quattro controlli deterministici su tutti i capitoli di parti.json. Il
criterio di ciascuno e' dichiarato accanto al risultato; nessuno di essi
e' un accertamento, tutti sono misure riproducibili.

  A. DICHIARAZIONE IN APERTURA — la regola vuole la dichiarazione di
     generazione IA nell'apertura di ogni documento, non in calce.
  B. CAPITOLI SENZA GRADI — un capitolo che non gradua nulla afferma
     senza dichiarare su che cosa poggia.
  C. ATTRIBUZIONI PERICOLOSE — formule che attribuiscono responsabilita'
     penale, cercate insieme al contesto che le qualifica. Il controllo
     produce falsi positivi per costruzione: e' fatto per essere letto,
     non per essere creduto.
  D. STATI ZERO SENZA SEDE — la regola vuole che uno Stato Zero nomini
     la sede interrogata. Il controllo guarda il capoverso, non la frase.

Uso:  python3 audit_disciplina.py [FILE_USCITA]
"""
import json, re, sys, pathlib

BASE = pathlib.Path(__file__).resolve().parent
REPO = BASE.parent.parent

RE_DICH = re.compile(r"intelligenza\s+artificiale|sistemi di intelligenza artificiale", re.I)
RE_GRADO = re.compile(r'\*\*(A|B|C|F|A/B|B/F|F/B|B/C|C/F|A/F)\*\*|'
                      r'[Ll]ivello\s+[ABCF]\b|[Ss]tat[oi]\s+[Zz]ero')
RE_ZERO = re.compile(r'[Ss]tat[oi]\s+[Zz]ero')
RE_SEDE = re.compile(r'\bsede\b|\bsedi\b|archivio|Archivio|fascicolo|atti d|commissione|'
                     r'Commissione|procura|Procura|registro|biblioteca', re.I)
RE_METODO = re.compile(r'uno Stato Zero richiede|Stato Zero = assenza|'
                       r'la formula «Stato Zero»|il grado «Stato Zero»')
# formule che attribuiscono responsabilita' penale
RE_ATTRIB = re.compile(
    r'(è|fu|era)\s+(il\s+)?(mandante|colpevole|responsabile)\b|'
    r'\bha ordinato l.omicidio\b|\bordinò (il sequestro|l.omicidio)\b|'
    r'\bfu lui a\b', re.I)
# contesto che qualifica: nella stessa proposizione o nel capoverso
RE_QUALIF = re.compile(
    r'non è|non fu|nessun|non risulta|Stato Zero|congettura|\bC\b|'
    r'non accertat|non prov|ipotesi|si sostiene|secondo|presunt|'
    r'giudicato|condannat[oi] in via definitiva|sentenza definitiva', re.I)


def capoversi(t):
    for b in t.split('\n\n'):
        b = ' '.join(b.split())
        if b and not b.startswith('|'):
            yield b


def main():
    uscita = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 \
        else REPO / '_verifiche/audit-disciplina.md'
    parti = json.loads((BASE / 'parti.json').read_text(encoding='utf-8'))['parti']

    senza_dich, senza_gradi, attrib, zero_senza_sede = [], [], [], []
    tot_zero = 0
    n = 0

    for p in parti:
        f = REPO / p['file']
        if not f.exists():
            continue
        n += 1
        t = f.read_text(encoding='utf-8')
        testa = '\n'.join(t.split('\n')[:30])

        if not RE_DICH.search(testa):
            senza_dich.append(p)

        if not RE_GRADO.search(t):
            senza_gradi.append(p)

        for cp in capoversi(t):
            if RE_METODO.search(cp):
                continue
            if RE_ZERO.search(cp):
                tot_zero += 1
                if not RE_SEDE.search(cp):
                    zero_senza_sede.append((p, cp[:300]))
            m = RE_ATTRIB.search(cp)
            if m and not RE_QUALIF.search(cp):
                attrib.append((p, cp[:400]))

    o = []
    o.append(f"""# L'audit della disciplina — la prescrizione applicata all'opera

> **Dichiarazione.** Questo audit è **generato automaticamente** da
> `_verifiche/generatori/audit_disciplina.py` su tutti i capitoli
> elencati in `parti.json`. **Non è un accertamento: è una misura
> riproducibile**, e produce falsi positivi per costruzione. È fatto per
> essere letto, non per essere creduto.
>
> **Perché esiste.** Quest'opera prescrive quattro cose a chiunque scriva
> di questo caso: dichiarare la propria natura in apertura, graduare ogni
> affermazione portante, non attribuire responsabilità penale fuori dai
> giudicati, e nominare la sede di ogni assenza. **La sesta volta che il
> corpus ha registrato "un controllo che fallisce prima della cosa
> controllata" ha imposto questa conseguenza: la prescrizione va applicata
> per prima a chi la scrive.**

## Il conto

| controllo | esito |
|---|---:|
| capitoli esaminati | **{n}** |
| **A** — senza dichiarazione nell'apertura | **{len(senza_dich)}** |
| **B** — senza alcun grado dichiarato | **{len(senza_gradi)}** |
| **C** — attribuzioni penali senza contesto qualificante | **{len(attrib)}** |
| **D** — Stati Zero senza sede nel capoverso (su {tot_zero} capoversi con Stato Zero) | **{len(zero_senza_sede)}** |
""")

    o.append("\n## A — Capitoli senza dichiarazione nell'apertura\n")
    o.append("*Criterio: la formula «intelligenza artificiale» non compare nelle prime trenta righe. "
             "I capitoli anteriori alla regola la portano altrove o non la portano: il conto li registra "
             "senza distinguerli, perché la distinzione è storica e il controllo è meccanico.*\n")
    if senza_dich:
        for p in senza_dich:
            o.append(f"- **{p['etichetta']}** — `{p['file']}`")
    else:
        o.append("*Nessuno. Tutti i capitoli portano la dichiarazione in apertura.*")

    o.append("\n\n## B — Capitoli senza alcun grado dichiarato\n")
    o.append("*Criterio: nessuna occorrenza di un grado in grassetto, di «Livello X» o di «Stato Zero». "
             "Un capitolo può legittimamente non graduare — un portale, un indice, un apparato — e "
             "l'elenco va letto sapendolo.*\n")
    if senza_gradi:
        for p in senza_gradi:
            o.append(f"- **{p['etichetta']}** — `{p['file']}`")
    else:
        o.append("*Nessuno.*")

    o.append("\n\n## C — Attribuzioni penali senza contesto qualificante\n")
    o.append("*Criterio: un capoverso che contiene una formula di attribuzione — «è il mandante», "
             "«fu responsabile», «ordinò l'omicidio» — **e nessuna** delle parole che la qualificano "
             "(negazione, grado, «non accertato», «congettura», «giudicato», «condannato in via "
             "definitiva»). **È il controllo più importante dei quattro**, ed è quello con più falsi "
             "positivi: una formula può essere qualificata nel capoverso precedente. Ogni riga va "
             "letta, non contata.*\n")
    if attrib:
        for p, cp in attrib:
            o.append(f"\n- **{p['etichetta']}** — `{p['file']}`\n  > {cp}")
    else:
        o.append("*Nessuna. Nessun capoverso dell'opera attribuisce responsabilità penale senza "
                 "una parola che la qualifichi.*")

    o.append("\n\n## D — Stati Zero senza sede nel capoverso\n")
    o.append("*Criterio: un capoverso che porta «Stato Zero» e nessuna parola di sede — archivio, "
             "fascicolo, atti, commissione, procura, registro, biblioteca. La regola vuole la sede "
             "nominata; il controllo la cerca nel capoverso e non nella frase, perché spesso sta nella "
             "proposizione successiva.*\n")
    if zero_senza_sede:
        o.append(f"\n*Primi cinquanta su {len(zero_senza_sede)}.*\n")
        for p, cp in zero_senza_sede[:50]:
            o.append(f"\n- **{p['etichetta']}** — `{p['file']}`\n  > {cp}")
    else:
        o.append("*Nessuno.*")

    o.append(f"""

---

## Come si legge questo audit

**I quattro numeri non sono voti.** Il controllo C con zero risultati non
significa che l'opera non attribuisca mai indebitamente: significa che
**nessun capoverso lo fa nella forma che il controllo sa riconoscere**. Il
controllo D con molti risultati non significa che quegli Stati Zero siano
privi di sede: significa che **la sede non sta nel loro capoverso**, e in
molti casi sta due righe più in là.

**Ciò che l'audit fa davvero è una cosa sola, e la fa bene: rende
riproducibile una verifica che finora era stata affidata alla lettura.**
Chiunque abbia il repository può rieseguirlo, e ogni riga che questo
elenco produce è un indirizzo dove andare a guardare.

**È la sola forma di controllo che un'opera possa applicare a sé stessa
senza mentire: non dichiararsi conforme, ma pubblicare l'elenco dei propri
punti da controllare.**
""")

    testo = '\n'.join(o) + '\n'
    uscita.parent.mkdir(parents=True, exist_ok=True)
    uscita.write_text(testo, encoding='utf-8')
    print(f"{uscita}: {n} capitoli | A={len(senza_dich)} B={len(senza_gradi)} "
          f"C={len(attrib)} D={len(zero_senza_sede)}/{tot_zero}")


if __name__ == '__main__':
    main()
