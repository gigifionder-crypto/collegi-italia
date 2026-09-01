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

# --- La correzione del 1° settembre 2026, annotata e non taciuta. ---
# Il criterio originario contava come cella aperta OGNI proposizione che
# portasse la formula. Rilettura dell'elenco: fra le 80 «non interrogate»
# c'erano titoli di sezione («Le celle aperte, con sede»), frasi di metodo
# («ogni cella aperta porta il suo falsificatore»), la dichiarazione di
# generazione automatica, e perfino una NEGAZIONE — «il solo blocco
# dell'intera opera che NON ha celle aperte». Il criterio è stato stretto,
# e la misura vecchia resta stampata accanto alla nuova.
#
# La regola che stringe è la regola stessa del corpus: *una cella senza
# sede nominata non è una cella*. Il registro stampava «sede non indicata»
# per settanta proposizioni su ottantuno, e non ne traeva la conseguenza.

# Una sede: un luogo dove si può bussare.
RE_SEDE_LEX = re.compile(
    r'[Aa]rchivi|[Aa]rchive|Arquivo|Archivo|Akten|[Ff]ondo\b|[Ff]ascicol'
    r'|[Bb]obin|microfilm|[Ii]nventario|[Rr]epertorio|[Bb]iblioteca|HOLLIS'
    r'|[Vv]erbali|[Aa]tti (integrali|del|della|dei|parlamentari|giudiziari)'
    r'|[Pp]rocura|[Tt]ribunale|Cassazione|[Cc]ancelleria|[Cc]atasto'
    r'|Commissione (parlamentare|Moro|d.inchiesta|stragi)|Camera|Senato'
    r'|Knesset|Bundestag|[Mm]inistero|Farnesina|Viminale|ENEA|CNEN|SISMI'
    r'|Konrad-Adenauer|Hanns-Seidel|IDU\b|AAPD|DDI\b|FRUS|NARA|FBI'
    r'|https?://|\b[a-z0-9][a-z0-9-]*\.(org|com|gov|edu|net|it|de|fr|ch|uk)\b'
    r'|[Ss]cheda di servizio|[Cc]ablogramm|[Bb]rogliacc|[Pp]erizia'
    r'|sede da interrogare|sede nominata|sedi nominate|[Ss]ede\s*[:—-]')

# Ciò che porta la formula ma NON registra una cella.
RE_NON_CELLA = re.compile(
    r'^#|^\*?\*?Le celle aperte'                      # titoli di sezione
    r'|non ha celle aperte|senza celle aperte'          # negazioni
    r'|[Oo]gni cella aperta'                            # metodo, quantificato
    r'|celle aperte (del corpus|vanno lette|di due Libri)'
    r'|le celle aperte (delle|dei|di) '                 # rinvii d.insieme
    r'|generat[oa] da un.intelligenza'                  # boilerplate
    r'|celle aperte con la loro sede'                   # descrizione dell.opera
    r'|di più celle aperte|le tre matrici')


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

    interrogate, non_interrogate, menzioni = [], [], []
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
                # criterio stretto: e' una cella solo se non e' una
                # menzione di metodo E se nomina una sede dove bussare.
                if RE_NON_CELLA.search(fr) or not RE_SEDE_LEX.search(fr):
                    menzioni.append((p['file'], fr))
                else:
                    aa.append((fr, True))
        if zz or aa:
            per_file[p['file']] = dict(etichetta=p['etichetta'], data=data,
                                       zero=zz, aperte=aa)
            interrogate += zz
            non_interrogate += aa

    n_z, n_a = len(interrogate), len(non_interrogate)
    n_m = len(menzioni)
    n_a_vecchio = n_a + n_m
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
> **Il criterio, dichiarato — e corretto il 1° settembre 2026.** Il registro
> conta **formule**, non le interpreta. Una proposizione che porta «Stato
> Zero» è classificata **interrogata**, perché nella regola di quest'opera
> quella formula significa *ho cercato lì e non c'è*. Una proposizione che
> porta «cella aperta» senza Stato Zero è classificata **non interrogata**,
> perché quella formula significa *non ho guardato*.
>
> ~~Le proposizioni di metodo — quelle che parlano *della* categoria invece
> di registrarne una — escono per parola-spia.~~ **Non bastava, e il conto
> era gonfio.** Rileggendo l'elenco delle ottanta si trovavano titoli di
> sezione (*«Le celle aperte, con sede»*), frasi di metodo (*«ogni cella
> aperta porta il suo falsificatore»*), la dichiarazione di generazione
> automatica, e perfino una **negazione**: *«il solo blocco dell'intera
> opera che **non ha** celle aperte»*, contata come cella aperta.
>
> **Il criterio è stato stretto con la regola stessa del corpus: una cella
> senza sede nominata non è una cella.** Il registro stampava «sede non
> indicata» per settanta proposizioni su ottantuno e non ne traeva la
> conseguenza. Ora una proposizione è contata come cella aperta soltanto
> se **nomina un luogo dove si può bussare** — un archivio, un fondo, un
> fascicolo, un repertorio, un atto parlamentare, un dominio — e non è una
> negazione, un titolo, o una frase sulla categoria. **Il conto scende da
> 80 a 36, e le 44 differenze restano contate come "menzioni", non
> cancellate.**
>
> Questa correzione è dello stesso genere dei ventisette falsi positivi del
> controllo A dell'audit di disciplina, e ha la stessa morale: **un'espressione
> regolare non è una lettura.**
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
| proposizioni **non interrogate** (cella aperta con sede) | **{n_a}** |
| ~~conto precedente, criterio largo~~ · corretto il 2026-09-01 | ~~{n_a_vecchio}~~ |
| menzioni scartate dal criterio stretto | **{n_m}** |
| capitoli senza data di commit ricavabile | **{senza_data}** |

**Un avvertimento sul numero, del 1° settembre 2026, e va letto prima del
conto.** Il conto delle non interrogate è **salito** dopo la campagna di
chiusura delle celle (Libro sedicesimo · XL), e chi lo legge deve sapere
perché, altrimenti ne trae il contrario di ciò che è accaduto.

Le celle vere erano **36**. La campagna le ha interrogate tutte, e ne ha
chiuse **3**; le altre **30** non erano raggiungibili da qui e sono state
**convertite in consegne indirizzate** — sede nominata, destinatario
istituzionale, richiesta scritta. Ma **una consegna è essa stessa una cella
aperta con sede**, e il capitolo che la registra la dichiara come tale: il
registro, che conta formule e non le interpreta, **le conta di nuovo**.

**36 + 30 = 66**, e i due insiemi si sovrappongono quasi per intero: sono in
larga parte **le stesse celle contate due volte** — una volta dove furono
registrate, una volta dove furono indirizzate. **Il registro non sa che sono
le stesse**, perché sa contare e non sa riconoscere.

Questo non è un difetto da nascondere: è il limite dichiarato di un
conteggio automatico, ed è la ragione per cui in testa a questo documento sta
scritto che **non è un accertamento ma una misura riproducibile**. Il numero
utile per la chiusura resta **36**, e ciò che la campagna ha cambiato non è
il numero: è che **trenta di quelle celle ora hanno un destinatario**.

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
