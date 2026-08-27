# -*- coding: utf-8 -*-
"""Da rapporto in PDF a markdown.

L'estrazione predefinita di pypdf restituisce una parola per riga: il PDF porta
la spaziatura come geometria e non come testo, e il paragrafo va perduto. La
modalita' `layout` lo conserva, e da li' si lavora: si toglie il filo di testa
che si ripete a ogni pagina, si ricuce il paragrafo spezzato dal salto e si
riconoscono le aperture di capitolo. Nessuna parola viene aggiunta o tolta."""
import collections, re, sys
from pypdf import PdfReader

def _righe(pagina):
    t = pagina.extract_text(extraction_mode='layout') or ''
    return [r.rstrip() for r in t.split('\n')]

def _filo(pagine):
    """Il filo di testa: la riga non vuota che ricorre in testa a piu' di meta'
    delle pagine. Se non ce n'e' una, non se ne toglie nessuna."""
    teste = collections.Counter()
    for rr in pagine:
        for r in rr[:3]:
            if r.strip():
                teste[r.strip()] += 1
                break
    if not teste:
        return None
    testa, quante = teste.most_common(1)[0]
    return testa if quante > len(pagine) / 2 else None

def _paragrafi(rr, filo):
    """Le righe di una pagina diventano paragrafi: riga vuota separa, riga piena
    prosegue. Gli spazi interni multipli sono giustificazione, non testo."""
    fuori, buf = [], []
    for r in rr:
        s = re.sub(r'\s+', ' ', r).strip()
        if filo and s == filo:
            continue
        if not s:
            if buf:
                fuori.append(' '.join(buf)); buf = []
        else:
            buf.append(s)
    if buf:
        fuori.append(' '.join(buf))
    return fuori

APERTURA = re.compile(
    r'^(?:CAPITOLO\s+[IVXLC]+|PARTE\s+[IVXLC]+|Capitolo\s+\d+|Parte\s+\w+|'
    r'Sezione\s+\w+|Appendice\b|Introduzione\b|Conclusion\w*\b|Premessa\b|'
    r'Bibliografia\b|Fonti\b|Allegato\b|\d+(?:\.\d+)*\.?\s+[A-ZÀ-Ù])')

def _titolo(p, prossimo=''):
    """Due strade per essere un titolo. La prima: aprire come un titolo, essere
    corto e non chiudere come una frase. La seconda, per i rapporti che i titoli
    non li numerano: essere corto, cominciare per maiuscola, non chiudere con un
    punto e avere davanti a se' un paragrafo lungo — perche' un titolo senza
    testo sotto non e' un titolo, e' una riga di elenco."""
    if p.startswith(('http', '- ')) or 'http' in p[:40]:
        return False
    n = len(p.split())
    if APERTURA.match(p) and n <= 22 and not p.endswith('.'):
        return True
    return (n <= 16 and not p.endswith(('.', ',', ';', ':'))
            and p[:1].isupper() and len(prossimo.split()) > 30)


def _bibliografia(p):
    """Un elenco di riferimenti estratto da PDF arriva come muro unico: si
    rimette una voce per riga, senza toccarne il testo."""
    voci = re.split(r'(?<=\s)(?=\d{1,3}\.\s+\S)', p)
    return voci if len(voci) > 3 else None

def converti(src, dst, titolo, sottotitolo='', cautela=''):
    r = PdfReader(src)
    pagine = [_righe(p) for p in r.pages]
    filo = _filo(pagine)
    corpo = []
    for rr in pagine:
        for p in _paragrafi(rr, filo):
            # una pagina che riprende in minuscolo continua il paragrafo di prima
            if corpo and re.match(r'^[a-zà-ù,;)]', p) and not corpo[-1].endswith(('.', ':', '?', '!')):
                corpo[-1] = corpo[-1] + ' ' + p
            else:
                corpo.append(p)
    righe = ['# ' + titolo, '',
             "*Documento dell'opera «Italia Nera», acquisito il 27 agosto 2026. "
             "Prodotto con sistemi di intelligenza artificiale sotto direzione e "
             "responsabilità umana.*", '']
    if cautela:
        righe += ['> ' + cautela, '']
    if sottotitolo:
        righe += ['*' + sottotitolo + '*', '']
    # Un'apertura di capitolo puo' arrivare incollata al testo che introduce,
    # perche' il PDF non le separa: si stacca, senza toccare una parola.
    STACCA = re.compile(r'^((?:Capitolo\s+\d+|CAPITOLO\s+[IVXLC]+)\s*[:—-]?\s*'
                        r'[^.]{4,120}?)\s+(?=[A-ZÀ-Ù][a-zà-ù])')
    staccati = []
    for p in corpo:
        m = STACCA.match(p) if len(p.split()) > 25 else None
        if m and len(m.group(1).split()) <= 22:
            staccati += [m.group(1).strip(), p[m.end(1):].strip()]
        else:
            staccati.append(p)
    corpo = staccati

    in_bib = False
    for i, p in enumerate(corpo):
        prossimo = corpo[i + 1] if i + 1 < len(corpo) else ''
        if _titolo(p, prossimo):
            in_bib = bool(re.match(r'(Bibliografia|Fonti|Note|Riferimenti)\b', p, re.I))
            righe += ['', '## ' + p.rstrip(':'), '']
            continue
        voci = _bibliografia(p) if in_bib else None
        if voci:
            righe += [''] + [v.strip() for v in voci if v.strip()] + ['']
        else:
            righe += [p, '']
    md = re.sub(r'\n{3,}', '\n\n', '\n'.join(righe)).strip() + '\n'
    open(dst, 'w', encoding='utf-8').write(md)
    return md

if __name__ == '__main__':
    md = converti(sys.argv[1], sys.argv[2], sys.argv[3],
                  sys.argv[4] if len(sys.argv) > 4 else '')
    print(f'{len(md.split())} parole · {md.count(chr(10) + "## ")} sezioni')
