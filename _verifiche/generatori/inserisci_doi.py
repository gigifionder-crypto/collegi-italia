#!/usr/bin/env python3
"""Inserisce il DOI del deposito nei documenti del dossier di invio.

    python3 _verifiche/generatori/inserisci_doi.py 10.5281/zenodo.1234567
    python3 _verifiche/generatori/inserisci_doi.py 10.5281/zenodo.1234567 --scrivi

Senza --scrivi non tocca nulla e mostra che cosa farebbe. È deliberato: la
sostituzione è irreversibile quanto il deposito che la precede, e un DOI
sbagliato inserito in nove documenti è più difficile da correggere che da
evitare.
"""
import sys, os, re, glob

REPO = '/home/user/collegi-italia'
DOSSIER = os.path.join(REPO, '_diffusione-opera')
SEGNAPOSTO = '{{DOI}}'

# Un DOI Zenodo: prefisso 10.5281, suffisso zenodo.<cifre>. La forma si controlla
# perché l'errore tipico non e' inventarsi un DOI: e' incollarlo con uno spazio,
# con l'URL davanti, o con la virgola finale di una frase.
RE_DOI = re.compile(r'^10\.5281/zenodo\.\d+$')

def normalizza(v):
    v = v.strip().strip('.,;)»"\'')
    for pref in ('https://doi.org/', 'http://doi.org/', 'doi:', 'DOI:', 'https://zenodo.org/records/'):
        if v.startswith(pref):
            v = v[len(pref):]
    return v.strip()

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    doi = normalizza(sys.argv[1])
    scrivi = '--scrivi' in sys.argv

    if not RE_DOI.match(doi):
        print(f'DOI non riconosciuto: «{doi}»')
        print('Forma attesa: 10.5281/zenodo.<cifre>. Sono accettati e ripuliti')
        print('anche i formati https://doi.org/…, doi:…, e l\'URL del record.')
        return 1

    testo = f'https://doi.org/{doi}'
    trovati = []
    for p in sorted(glob.glob(os.path.join(DOSSIER, '*.md'))):
        s = open(p, encoding='utf-8').read()
        n = s.count(SEGNAPOSTO)
        if n:
            trovati.append((p, n, s))

    if not trovati:
        print('Nessun segnaposto trovato. O il DOI è già stato inserito, o i')
        print('documenti sono cambiati: in entrambi i casi, controllare prima di')
        print('procedere.')
        return 1

    tot = sum(n for _p, n, _s in trovati)
    print(f'DOI: {doi}')
    print(f'Da sostituire con: {testo}')
    print(f'Documenti: {len(trovati)} · occorrenze: {tot}\n')
    for p, n, _s in trovati:
        print(f'  {n}×  {os.path.relpath(p, REPO)}')

    if not scrivi:
        print('\nProva a vuoto: nulla è stato modificato.')
        print('Per eseguire davvero, ripetere il comando con --scrivi.')
        return 0

    for p, _n, s in trovati:
        open(p, 'w', encoding='utf-8').write(s.replace(SEGNAPOSTO, testo))
    print(f'\nFatto: {tot} occorrenze in {len(trovati)} documenti.')
    print('\nRestano da fare, e non li fa questo script:')
    print('  1. ricomporre gli allegati del dossier (b_dossier.js, p_dossier.py)')
    print('  2. riallineare il registro delle impronte (gen_impronte.py, build_impronte.py)')
    print('  3. spuntare la prima voce della checklist di invio')
    print('\nE il controllo che conta: aprire una delle lettere e leggere la riga')
    print('del deposito. Un DOI giusto in una frase sbagliata resta una frase')
    print('sbagliata, e nessuno script se ne accorge.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
