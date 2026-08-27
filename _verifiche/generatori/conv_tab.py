# -*- coding: utf-8 -*-
"""Convertitore DOCX consapevole delle tabelle. Il convertitore precedente
appiattiva ogni cella in un paragrafo, e un censimento di centotrentaquattro
schede diventava centotrentaquattro titoli: la tavola andava persa. Qui il
corpo si percorre in ordine di documento, e w:tbl diventa una tabella."""
import re, sys, zipfile
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def testo(el):
    fuori = []
    for n in el.iter():
        if n.tag == W + 't':
            fuori.append(n.text or '')
        elif n.tag in (W + 'tab',):
            fuori.append(' ')
        elif n.tag == W + 'br':
            fuori.append(' ')
    return re.sub(r'\s+', ' ', ''.join(fuori)).strip()

def grassetto(p):
    run = [r for r in p.iter(W + 'r') if testo(r)]
    if not run:
        return False
    return all(r.find(W + 'rPr/' + W + 'b') is not None for r in run)

def esc(s):
    return s.replace('|', '\\|')

APERTURA = re.compile(r'^(capitolo|parte|sezione|appendice|registro|apparato|nota|'
                      r'premessa|introduzione|conclusion|schedario|censimento|'
                      r'legenda|fonti|riga di chiusura|indice)\b', re.I)

def tabella(tbl):
    righe = []
    for tr in tbl.findall(W + 'tr'):
        righe.append([esc(testo(tc)) for tc in tr.findall(W + 'tc')])
    righe = [r for r in righe if any(c.strip() for c in r)]
    if not righe:
        return ''
    largh = max(len(r) for r in righe)
    def riga(r):
        r = r + [''] * (largh - len(r))
        return '| ' + ' | '.join(r) + ' |'
    out = [riga(righe[0]), '|' + '---|' * largh]
    out += [riga(r) for r in righe[1:]]
    return '\n'.join(out)

def converti(src, dst, titolo=None):
    z = zipfile.ZipFile(src)
    corpo = ET.fromstring(z.read('word/document.xml')).find(W + 'body')
    fuori, primo = [], True
    for el in corpo:
        if el.tag == W + 'tbl':
            t = tabella(el)
            if t:
                fuori += ['', t, '']
            continue
        if el.tag != W + 'p':
            continue
        t = testo(el)
        if not t:
            continue
        if primo:
            primo = False
            fuori += ['# ' + esc(titolo or t), '']
            if titolo:
                fuori += [esc(t), '']
            continue
        if APERTURA.match(t) or (grassetto(el) and len(t) < 95 and not t.endswith('.')):
            fuori += ['', '## ' + esc(t), '']
        else:
            fuori += [esc(t), '']
    md = re.sub(r'\n{3,}', '\n\n', '\n'.join(fuori)).strip() + '\n'
    open(dst, 'w', encoding='utf-8').write(md)
    return md

if __name__ == '__main__':
    md = converti(sys.argv[1], sys.argv[2],
                  sys.argv[3] if len(sys.argv) > 3 else None)
    print(f'{len(md.split())} parole · {md.count("|---")} tabelle')
