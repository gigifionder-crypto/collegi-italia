#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Il registro delle convergenze: quante volte l'opera ha trovato la stessa
forma, e su quali materiali.

PERCHE' ESISTE. Il corpus ripete in piu' capitoli che il proprio risultato
ricorrente -- «orientamento condiviso, ponti reali, nessun comando comune
provato» -- e' stato ottenuto N volte consecutive. Ma N era scritto a mano,
in capitoli diversi, e ha derivato: «quinta conferma» in un capitolo,
«sette prove» in due altri, «settima e ottava volta» in un terzo, «otto
prove» in un quarto. Ciascun numero era esatto quando fu scritto, e ha
smesso di esserlo appena e' stata aggiunta una conferma altrove.

Il rilievo non e' mio: viene dalla campagna Roy Cohn, sezione C9 («e' stabile
fra i capitoli il numero delle prove di unione?» -- F, no). L'errore non e'
di ricerca ma di CONTABILITA', e la cura di un errore di contabilita' non e'
riscrivere i numeri: e' smettere di scriverli a mano.

IL CRITERIO, dichiarato e applicato meccanicamente. Un documento conta come
conferma se contiene almeno una delle formule del risultato (sotto, FORMULE).
Sono escluse per costruzione: i tomi ricomposti e l'edizione breve (che
ripetono testo gia' contato), il romanzo, gli indici e i registri di
servizio. L'appartenenza e' dunque una proprieta' del TESTO, verificabile da
chiunque riesegua lo script; l'ordine e' la data del commit che ha
introdotto il documento; il numero e' la posizione in quell'ordine.

CHE COSA IL REGISTRO NON DICE. Non dice che le conferme siano indipendenti
fra loro -- alcune insistono su materiali contigui -- ne' che siano di pari
peso. Conta le volte in cui la stessa forma e' stata trovata, e questo e'
tutto cio' che un conteggio puo' fare.

Uso:  python3 registro_convergenze.py [FILE_USCITA]
"""
import os
import re
import subprocess
import sys
import glob
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
REPO = BASE.parent.parent

FORMULE = [
    r'nessun comando comune',
    r'nessuna regia accertata',
    r'orientamento condiviso, ponti reali',
    r'convergenza (?:di interesse )?(?:è |e )?accertata, il concerto no',
    r'convergenza senza concerto',
]
RE_FORM = re.compile('|'.join(FORMULE), re.I)

# Escluse per costruzione, e la ragione e' scritta accanto a ciascuna.
ESCLUSI = [
    ('_tomi/', 'tomi ricomposti: ripetono testo gia\' contato'),
    ('_integrale/', 'tomi dell\'edizione integrale: ricompongono il corpus, '
     'e contarli sarebbe contare due volte ogni documento che portano'),
    ('_romanzo/', 'romanzo: non e\' ricerca'),
    ('edizione-breve/', 'edizione breve: distilla testo gia\' contato'),
    ('una-guerra-senza-fine-edizione', 'edizione breve assemblata'),
    ('aldo-moro-ottanta-anni-senza-pace.md',
     'Opera monografica assemblata: contiene i capitoli gia\' contati'),
    ('_monografia/', 'sorgenti della monografia: narrano testo gia\' contato'),
    ('_meta/', 'registri di servizio'),
    ('_diffusione', 'materiali di diffusione'),
    ('_pubblicazione', 'materiali di pubblicazione'),
    ('_paper-', 'estratti accademici'),
    ('_livelli-', 'estratti per livelli'),
    ('tomo-1-', 'estratti territoriali'),
    ('tomo-2-', 'estratti territoriali'),
    ('ue-27/', 'estratti per paese'),
    ('INDICE', 'indice: descrive, non accerta'),
    ('GUIDA-ALLA-LETTURA', 'guida: descrive, non accerta'),
    # E se stesso, perche' cita le formule nel proprio criterio: un registro
    # che si conti fra le proprie voci non e' una misura, e' un'eco.
    ('il-registro-delle-convergenze.md', 'questo registro: si conterebbe da se\''),
]


def escluso(rel):
    for pref, _ in ESCLUSI:
        if rel.startswith(pref) or pref in rel:
            return True
    return False


def commit(rel):
    """Timestamp del commit che ha introdotto il file. Verificabile in git."""
    out = subprocess.run(
        ['git', 'log', '--diff-filter=A', '--format=%at|%ad', '--date=short',
         '--', rel], cwd=REPO, capture_output=True, text=True).stdout.strip()
    if not out:
        return (0, '')
    ts, d = out.split('\n')[-1].split('|')
    return (int(ts), d)


def main():
    uscita = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 \
        else REPO / 'il-registro-delle-convergenze.md'

    trovati = []
    for f in glob.glob(str(REPO / '**' / '*.md'), recursive=True):
        rel = os.path.relpath(f, REPO)
        if escluso(rel):
            continue
        testo = open(f, encoding='utf-8', errors='ignore').read()
        occ = RE_FORM.findall(testo)
        if occ:
            ts, d = commit(rel)
            trovati.append((ts, d, rel, len(occ)))
    trovati.sort()

    # i numeri scritti a mano che il registro sostituisce
    mano = []
    for f in glob.glob(str(REPO / '**' / '*.md'), recursive=True):
        rel = os.path.relpath(f, REPO)
        # Stesse esclusioni di servizio, piu' questo registro: se si
        # scandisse da se' si conterebbe le proprie citazioni.
        if (rel.startswith('_tomi/') or rel.startswith('_integrale/')
                or rel.startswith('_romanzo/')
                or rel.startswith('_meta/')
                or rel == 'il-registro-delle-convergenze.md'
                or rel == 'aldo-moro-ottanta-anni-senza-pace.md'
                or rel.startswith('_monografia/')
                or rel.startswith('una-guerra-senza-fine-edizione')):
            continue
        for m in re.finditer(
                r'((?:second|terz|quart|quint|sest|settim|ottav|non|decim)\w*'
                r'\s+(?:prov\w+|conferm\w+)\s+consecutiv\w+'
                r'|(?:due|tre|quattro|cinque|sei|sette|otto|nove|dieci|undici)'
                r'\s+prove\s+consecutive)', open(f, encoding='utf-8',
                                                errors='ignore').read(), re.I):
            mano.append((rel, m.group(1)))

    o = [f"""# Il registro delle convergenze — quante volte, e su che cosa

> **Dichiarazione.** Questo registro è **generato automaticamente** da
> `_verifiche/generatori/registro_convergenze.py`. **Non è un accertamento:
> è una misura riproducibile.** Chiunque abbia il repository può rieseguirlo
> e ottenere gli stessi numeri.

## Perché esiste

Il corpus ripete in più capitoli che il proprio risultato ricorrente —
**«orientamento condiviso, ponti reali, nessun comando comune provato»** —
è stato ottenuto un certo numero di volte consecutive. Quel numero era
**scritto a mano**, in capitoli diversi, e ha derivato.

Il rilievo non è di chi scrive: viene dalla campagna *Roy Cohn*, sezione
C9, che ha chiesto se il numero fosse stabile fra i capitoli e ha risposto
**no**, elencando le divergenze. **È un errore di contabilità, non di
ricerca** — e la cura di un errore di contabilità non è riscrivere i
numeri: è **smettere di scriverli a mano**.

## Il criterio, dichiarato e applicato meccanicamente

Un documento conta come conferma **se il suo testo contiene almeno una
delle formule del risultato**:

{chr(10).join('- `' + f + '`' for f in FORMULE)}

L'appartenenza è dunque una proprietà **del testo**, non un giudizio di chi
compila: chiunque riesegua lo script ottiene la stessa lista. L'**ordine** è
la data del commit che ha introdotto il documento nel repository,
verificabile in `git log --diff-filter=A`. Il **numero** è la posizione in
quell'ordine.

Sono esclusi per costruzione i tomi ricomposti e l'edizione breve, che
ripetono testo già contato; il romanzo, che non è ricerca; gli indici e le
guide, che descrivono invece di accertare.

## Che cosa questo registro **non** dice

**Non dice che le conferme siano indipendenti fra loro.** Alcune insistono
su materiali contigui, e chi le legge deve pesarle, non sommarle. **Non
dice che siano di pari valore probatorio.** Conta le volte in cui la stessa
forma è stata trovata su materiali dichiarati — e questo è tutto ciò che un
conteggio può fare. Un numero alto non rende la forma più vera: la rende
più **ricorrente**, che è un'altra cosa e va detta con un'altra parola.

## Il conto

**{len(trovati)} documenti** dell'opera portano il risultato.

| n. | data d'ingresso | documento | occorrenze |
|---:|---|---|---:|
"""]
    for i, (_, d, rel, n) in enumerate(trovati, 1):
        o.append(f"| {i} | {d} | [`{rel}`]({rel}) | {n} |\n")

    o.append("\n## I numeri scritti a mano che questo registro sostituisce\n\n"
             "Restano nei loro capitoli, dove furono scritti, perché **una "
             "correzione sta accanto all'errore e non al suo posto**. "
             "Ciascuno era esatto il giorno in cui fu scritto, e ha smesso "
             "di esserlo il giorno dopo.\n\n")
    if mano:
        o.append("| documento | formula |\n|---|---|\n")
        for rel, frase in sorted(set(mano)):
            o.append(f"| [`{rel}`]({rel}) | «{frase}» |\n")
    o.append(f"\n**Il numero corrente è {len(trovati)}, e non va più "
             "trascritto: va letto qui.** Chi aggiunge una conferma non deve "
             "aggiornare nessun capitolo — deve solo scrivere la formula, e "
             "il registro la conta.\n")

    uscita.write_text("".join(o), encoding='utf-8')
    print(f"{uscita}: {len(trovati)} conferme, "
          f"{len(set(mano))} numeri scritti a mano rilevati")


if __name__ == '__main__':
    main()
