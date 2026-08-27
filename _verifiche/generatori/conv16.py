#!/usr/bin/env python3
"""Converte i DOCX del lotto nel markdown del repo.
Non usano pStyle: la gerarchia sta nel grassetto. Ma il grassetto fa due
mestieri — intestazione e capoverso in rilievo — e vanno distinti, altrimenti
i capoversi finiscono nell'indice del volume."""
import xml.etree.ElementTree as ET, io, re, sys, zipfile
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
ns={'w':W[1:-1]}
APERTURA=re.compile(r'^(capitolo|parte|sezione|appendice|registro|apparato|nota|premessa|'
                    r'introduzione|conclusion|riga di chiusura|indice)\b', re.I)

def paragrafi(docx):
    z=zipfile.ZipFile(docx)
    root=ET.parse(io.BytesIO(z.read('word/document.xml'))).getroot()
    out=[]
    for p in root.findall('.//w:p',ns):
        txt=''.join(t.text or '' for t in p.findall('.//w:t',ns)).strip()
        if not txt: continue
        pezzi=[]
        for r in p.findall('.//w:r',ns):
            t=''.join(x.text or '' for x in r.findall('w:t',ns))
            if not t.strip(): continue
            rPr=r.find('w:rPr',ns)
            pezzi.append(rPr is not None and rPr.find('w:b',ns) is not None)
        out.append((txt, bool(pezzi) and all(pezzi)))
    return out

def esc(t):
    return t.replace('*','\\*').replace('`',"'").replace('_','\\_')

def converti(docx):
    ps=paragrafi(docx)
    righe=[]; titolo=None; front=True
    for t,b in ps:
        if titolo is None:
            titolo=t; righe += ['# '+esc(t), '']; continue
        if not b:
            front=False
            righe += [esc(t), '']; continue
        # da qui in poi: paragrafo in grassetto
        if APERTURA.match(t) or (len(t) < 95 and not t.endswith('.')):
            front=False
            righe += ['', '## '+esc(t), '']
        elif front:
            # occhiello del frontespizio: resta, in corsivo, senza entrare nell'indice
            righe += ['*'+esc(t)+'*', '']
        else:
            # capoverso in rilievo: grassetto in linea, non intestazione
            righe += ['**'+esc(t)+'**', '']
    md=re.sub(r'\n{3,}','\n\n','\n'.join(righe)).strip()+'\n'
    return md, titolo

if __name__=='__main__':
    md,tit=converti(sys.argv[1])
    open(sys.argv[2],'w',encoding='utf-8').write(md)
    h2=md.count('\n## ')
    print(f'{sys.argv[2].split("/")[-1]:<46}{len(md.split()):>7} parole · {h2:>3} sezioni')
