#!/usr/bin/env python3
"""Rilega la prima stesura del romanzo in un solo manoscritto.

Decisione editoriale dichiarata: l'avvertenza sulla voce, che in ciascun
capitolo sciolto sta per intero perché ciascun capitolo circolava da solo,
qui compare **una volta sola** in apertura del volume. A ciascun capitolo
resta un richiamo di una riga. La dichiarazione di generazione con sistemi
di intelligenza artificiale resta in apertura, com'è regola del corpus.
"""
import re, sys, os

REPO = '/home/user/collegi-italia'
ROM = os.path.join(REPO, '_romanzo')
ORDINE = [
    ('I',   'capitolo-primo-l-elenco-che-arriva.md'),
    ('II',  'capitolo-secondo-l-uomo-prima-del-caso.md'),
    ('III', 'capitolo-terzo-gli-anni-della-farnesina.md'),
    ('IV',  'capitolo-quarto-le-lettere-scelte.md'),
    ('V',   'capitolo-quinto-l-archivio.md'),
    ('VI',  'capitolo-sesto-l-aritmetica.md'),
    ('VII', 'capitolo-settimo-ottocentotredici-volte-non-trovato.md'),
]

RICHIAMO = ("> *In corsivo la prosopopea dichiarata — non sono parole di Aldo Moro. "
            "In tondo l'apparato, coi gradi. L'avvertenza per esteso è in apertura del volume.*")

def corpo(testo):
    """Toglie il titolo, la riga di generazione e l'avvertenza; restituisce
    titolo e corpo dal primo separatore in poi."""
    righe = testo.split('\n')
    titolo = righe[0].lstrip('# ').strip()
    # il corpo comincia dopo il primo '---' isolato che segue l'avvertenza
    for i, r in enumerate(righe):
        if r.strip() == '---' and i > 5:
            return titolo, '\n'.join(righe[i+1:]).strip()
    raise SystemExit(f'separatore non trovato in: {titolo}')

FRONTE = """# Ottanta anni di Pace

## Romanzo evidence-based in sette parti — prima stesura

*Documento prodotto con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana. La dichiarazione sta in apertura, non in calce.*

---

> **Avvertenza sulla voce, da leggere prima del libro.** In corsivo parla Aldo
> Moro. **Non sono sue parole.** È **prosopopea dichiarata**: un artificio
> letterario che presta a un uomo morto nel 1978 un ragionamento che non ha mai
> fatto, su fatti che non ha mai conosciuto. Nessuna riga in corsivo va citata
> come sua.
>
> La voce prestata ragiona **sulla prova** — che fu la materia insegnata da Aldo
> Moro nell'università di Bari per vent'anni — e **mai sui fatti**: non sul
> proprio sequestro, non sulla propria morte, e nelle due parti in cui l'oggetto
> è lui stesso — la seconda, che è il ritratto, e la terza, che è il suo
> ministero — non su di sé. Nella seconda la voce si ferma dove dovrebbe parlare
> di sé, e lo dichiara.
>
> In tondo parla l'apparato, e ogni sua affermazione porta il grado: **A**
> giudicato, **B** accertamento, **C** congettura, **F** fatto pubblico. Quando
> una ricerca è stata condotta senza esito, l'esito negativo è registrato come
> **Stato Zero** ed è valido soltanto se la sede consultata è nominata.
>
> **L'appartenenza a un'organizzazione non è prova di condotta.** Nessuna riga di
> questo libro indica alcuno come responsabile di un reato al di fuori di un
> giudicato definitivo.

---

> **Che libro è questo.** Non è un libro sul caso Moro: è un libro **su che cosa
> succede quando si prova a verificarlo**. La scelta non è di gusto. Un romanzo
> ha bisogno di scene, e le scene del 1978 il corpus non le ha — due sole
> indicazioni di ora in oltre un milione di parole, nessuna stanza, nessun volto
> — e in un libro fondato sulle prove quelle scene non si possono inventare. Le
> scene della verifica invece ci sono tutte, e sono documentate perché sono
> accadute.

> **Che cosa questa stesura è.** La **prima stesura completa**: sette parti su
> sette, circa quattordicimila parole delle settantacinquemila previste. La
> struttura c'è per intero; ciò che manca non è più impianto ma ampiezza. Il
> corpus da cui il libro si ricava resta depositato a parte, ed è quindici volte
> più esteso di quanto qui si legga.

> **Una decisione editoriale, dichiarata.** Ciascun capitolo, finché circolava
> sciolto, portava per intero l'avvertenza sulla voce. Rilegati, la portano una
> volta sola — qui sopra — e a ciascuno resta un richiamo di una riga. Nulla
> della disciplina è stato tolto: è stato spostato, e questa nota dice dove.

> **Le riparazioni restano visibili.** Due cifre di questo lavoro sono state
> ritirate da chi le aveva scritte, e la ritrattazione sta nel testo che le
> conteneva: una probabilità che dipendeva da un parametro non dichiarato (parte
> sesta) e un conteggio che dipendeva da un perimetro non dichiarato (parte
> settima). Non sono state emendate in silenzio, e la ragione è nel libro: **la
> correzione silenziosa produce un testo migliore e un lavoro peggiore.**

---

## Indice

| | parte | |
|---|---|---|
"""

def main():
    fuori = [FRONTE]
    voci, corpi = [], []
    for num, nome in ORDINE:
        t = open(os.path.join(ROM, nome), encoding='utf-8').read()
        titolo, c = corpo(t)
        breve = titolo.split('—', 1)[1].strip() if '—' in titolo else titolo
        voci.append(f'| **{num}** | {breve} | |')
        corpi.append((num, breve, c))
    fuori.append('\n'.join(voci))
    fuori.append('\n')
    for num, breve, c in corpi:
        fuori.append(f'\n---\n\n# Parte {num} — {breve}\n\n{RICHIAMO}\n\n{c}\n')
    fuori.append("""
---

## Colophon

Prima stesura completa, 28 agosto 2026. Sette parti, sette capitoli.

Il corpus da cui il libro si ricava è depositato nel medesimo branch e porta il
proprio registro di impronte SHA-256. Le parti di questo libro rinviano ad esso
per l'apparato integrale: la certificazione dei numeri, la relazione della
campagna di ricerca, il registro degli ingressi e il perimetro negativo per
esteso.

Lo spoglio da cui nasce la parte terza è riproducibile: il criterio è scritto in
`_verifiche/generatori/spoglio_farnesina.py`, e la rilegatura di questo volume in
`_verifiche/generatori/rilega_romanzo.py`. È la regola che la parte settima
enuncia — *una misura non è il numero, è il numero più la regola che lo produce* —
applicata a sé stessa.
""")
    testo = '\n'.join(fuori)
    dest = os.path.join(ROM, 'OTTANTA-ANNI-DI-PACE-prima-stesura.md')
    open(dest, 'w', encoding='utf-8').write(testo)
    print(f'{dest}\nparole: {len(testo.split())}\nparti: {len(ORDINE)}')

if __name__ == '__main__':
    main()
