#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Il registro di chiusura dell'opera — condizione prima del capitolo XXXII.

Estrae da tutti i capitoli registrati in parti.json ogni cella dichiarata,
e la classifica secondo la sola distinzione che conta per la chiusura:

  INTERROGATA  — porta la formula «Stato Zero», che per regola del corpus
                 significa «ho cercato lì e non c'è». La data di
                 interrogazione e' la data del commit che ha introdotto il
                 documento che la dichiara: verificabile in git.

  NON INTERROGATA — porta la formula «cella aperta» senza Stato Zero,
                 che per regola significa «non ho guardato». Non ha data,
                 e per ciascuna il registro dice che manca.

Il criterio e' dichiarato e grossolano per costruzione: conta le formule,
non le interpreta. Un conteggio automatico non e' un accertamento — e'
una misura riproducibile, ed e' esattamente ciò che serve per dire se
un'opera abbia esaurito le proprie sedi.

Uso:  python3 registro_chiusura.py [FILE_USCITA]
"""
import json, re, subprocess, sys, pathlib, collections

BASE = pathlib.Path(__file__).resolve().parent
REPO = BASE.parent.parent

RE_ZERO = re.compile(r'[Ss]tat[oi]\s+[Zz]ero')
RE_APERTA = re.compile(r'[Cc]ell[ae]\s+apert[ae]')
RE_SEDE = re.compile(r'[Ss]ede\s*[:—\-]|sede nominata|sedi nominate|sede da interrogare')
RE_ROB = re.compile(r'robustezza\s+(alta|media|modesta|bassa)')
# proposizioni di metodo: parlano *della* categoria, non ne registrano una
RE_METODO = re.compile(
    r'(uno Stato Zero richiede|la formula «Stato Zero»|il grado «Stato Zero»|'
    r'che cos.è uno Stato Zero|Stato Zero = assenza)')


def data_commit(f):
    try:
        d = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--format=%ad', '--date=short', '--', f],
            cwd=REPO, capture_output=True, text=True, timeout=30).stdout.strip()
        return d.split('\n')[-1] if d else ''
    except Exception:
        return ''


def frasi(testo):
    """Spezza in proposizioni grossolane, conservando i capoversi corti."""
    for blocco in testo.split('\n\n'):
        b = ' '.join(blocco.split())
        if not b or b.startswith('|'):
            continue
        for p in re.split(r'(?<=[.;:])\s+(?=[A-ZÈÉÀÌÒÙ«*])', b):
            p = p.strip()
            if 20 < len(p) < 900:
                yield p


def main():
    uscita = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 \
        else REPO / 'il-registro-di-chiusura.md'
    parti = json.loads((BASE / 'parti.json').read_text(encoding='utf-8'))['parti']

    interrogate, non_interrogate = [], []
    per_file = collections.OrderedDict()

    for p in parti:
        f = REPO / p['file']
        if not f.exists():
            continue
        testo = f.read_text(encoding='utf-8')
        data = data_commit(p['file'])
        zz, aa = [], []
        for fr in frasi(testo):
            if RE_METODO.search(fr):
                continue
            ha_zero = bool(RE_ZERO.search(fr))
            ha_aperta = bool(RE_APERTA.search(fr))
            if ha_zero:
                rob = RE_ROB.search(fr)
                zz.append((fr, rob.group(1) if rob else '',
                           bool(RE_SEDE.search(fr))))
            elif ha_aperta:
                aa.append((fr, bool(RE_SEDE.search(fr))))
        if zz or aa:
            per_file[p['file']] = dict(etichetta=p['etichetta'], data=data,
                                       zero=zz, aperte=aa)
            interrogate += zz
            non_interrogate += aa

    n_z, n_a = len(interrogate), len(non_interrogate)
    con_sede = sum(1 for _, _, s in interrogate if s)
    senza_data = sum(1 for v in per_file.values() if not v['data'])

    out = []
    out.append(f"""# Il registro di chiusura — ogni cella, e la sua data

> **Dichiarazione.** Questo registro è **generato automaticamente** da
> `_verifiche/generatori/registro_chiusura.py` su tutti i capitoli
> elencati in `parti.json`, sorgente unica dell'opera. **Non è un
> accertamento: è una misura riproducibile.** Chiunque abbia il
> repository può rieseguirlo e ottenere gli stessi numeri.
>
> **Il criterio, dichiarato e volutamente grossolano.** Il registro conta
> **formule**, non le interpreta. Una proposizione che porta «Stato Zero»
> è classificata **interrogata**, perché nella regola di quest'opera
> quella formula significa *ho cercato lì e non c'è*. Una proposizione che
> porta «cella aperta» senza Stato Zero è classificata **non
> interrogata**, perché quella formula significa *non ho guardato*. Le
> proposizioni di metodo — quelle che parlano *della* categoria invece di
> registrarne una — escono per parola-spia.
>
> **La data di interrogazione** è la data del commit che ha introdotto nel
> repository il documento che dichiara la cella. È verificabile in
> `git log --diff-filter=A`. Non è la data in cui la ricerca fu condotta:
> è la data in cui il suo esito fu messo per iscritto, ed è il solo dato
> che un archivio possa certificare.

## Il conto

| voce | numero |
|---|---:|
| capitoli dell'opera che dichiarano celle | **{len(per_file)}** |
| proposizioni **interrogate** (Stato Zero) | **{n_z}** |
| di esse, con **sede nominata** nella stessa proposizione | **{con_sede}** |
| proposizioni **non interrogate** (cella aperta) | **{n_a}** |
| capitoli senza data di commit ricavabile | **{senza_data}** |

**La lettura del conto, e va fatta con onestà.** Il numero delle
proposizioni interrogate è alto perché l'opera dichiara i propri vuoti
sistematicamente: è la sua disciplina, non un merito. Il numero che conta
per la chiusura è il secondo: **{n_a} proposizioni dichiarano
esplicitamente di non essere state interrogate.** Sono quelle che il
capitolo · XXXII chiama celle aperte, e sono l'unica cosa che separa
quest'opera dalla condizione prima del proprio criterio di chiusura.

**Che cosa questo registro non fa.** Non giudica se una sede fosse
interrogabile, non pesa il rendimento atteso di una cella, non distingue
la cella grande dalla piccola. Fa una cosa sola, ed è la sola che serviva:
**mette una data accanto a ciò che è stato cercato, e dichiara l'assenza
di data accanto a ciò che non lo è stato.**

---

## Le celle non interrogate, per capitolo

*Sono le proposizioni che dichiarano di non aver guardato. Chi voglia
chiudere l'opera deve guardarle — o dichiarare, con la sua data, di aver
guardato e non trovato.*
""")

    for f, v in per_file.items():
        if not v['aperte']:
            continue
        out.append(f"\n### {v['etichetta']} — `{f}`")
        out.append(f"*Introdotto nel repository il {v['data'] or '(data non ricavabile)'}.*\n")
        for fr, sede in v['aperte']:
            marchio = '**sede indicata**' if sede else '**sede non indicata**'
            out.append(f"- {marchio} · {fr}")

    out.append("""
---

## Le celle interrogate, per capitolo

*Sono le proposizioni che dichiarano di aver cercato e non trovato. La
data accanto a ciascun capitolo è la data in cui quell'esito fu messo per
iscritto.*
""")

    for f, v in per_file.items():
        if not v['zero']:
            continue
        out.append(f"\n### {v['etichetta']} — `{f}`")
        out.append(f"*Interrogato e messo per iscritto il {v['data'] or '(data non ricavabile)'}.*\n")
        for fr, rob, sede in v['zero']:
            note = []
            if rob:
                note.append(f'robustezza {rob}')
            note.append('sede indicata' if sede else 'sede non indicata nella proposizione')
            out.append(f"- *({'; '.join(note)})* · {fr}")

    out.append(f"""
---

## La condizione prima, e se sia soddisfatta

Il capitolo · XXXII fissa tre condizioni congiunte perché l'opera possa
dirsi finita. La prima è: **ogni cella porta una data di interrogazione.**

**Non è soddisfatta**, e questo registro dice esattamente di quanto:
**{n_a} proposizioni dichiarano di non essere state interrogate**,
distribuite su {sum(1 for v in per_file.values() if v['aperte'])} capitoli.

**Ma la condizione è ora misurabile, e prima non lo era.** Un'opera che
non sappia contare le proprie celle aperte non può chiuderle; questa ora
le conta, le elenca e le indirizza. **Il registro si rigenera con un
comando**, e ogni volta che una cella viene interrogata il numero scende
di uno.

**È la forma più onesta di chiusura che una ricerca documentale possa
assumere: non dire di aver finito, ma dire esattamente quanto manca.**
""")

    testo = '\n'.join(out) + '\n'
    uscita.write_text(testo, encoding='utf-8')
    print(f"{uscita}: {len(per_file)} capitoli, {n_z} interrogate "
          f"({con_sede} con sede), {n_a} non interrogate, {len(testo)} byte")


if __name__ == '__main__':
    main()
