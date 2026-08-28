#!/usr/bin/env python3
"""Lettura di seguito, misurata. Tre misure sulla prima stesura rilegata:
1) equilibrio delle due voci per capitolo (corsivo = prosopopea, tondo = apparato);
2) ritmo: lunghezza dei paragrafi e delle sezioni;
3) ripetizione fra capitoli, per contenimento di 8-grammi (lo strumento del corpus).
"""
import re, os, itertools, collections

ROM='/home/user/collegi-italia/_romanzo'
ORDINE=[('I','capitolo-primo-l-elenco-che-arriva.md'),
        ('II','capitolo-secondo-l-uomo-prima-del-caso.md'),
        ('III','capitolo-terzo-gli-anni-della-farnesina.md'),
        ('IV','capitolo-quarto-le-lettere-scelte.md'),
        ('V','capitolo-quinto-l-archivio.md'),
        ('VI','capitolo-sesto-l-aritmetica.md'),
        ('VII','capitolo-settimo-ottocentotredici-volte-non-trovato.md')]

def corpo(t):
    r=t.split('\n')
    for i,x in enumerate(r):
        if x.strip()=='---' and i>5: return '\n'.join(r[i+1:]).strip()
    return t

def paragrafi(c):
    out=[]
    for b in re.split(r'\n\s*\n', c):
        b=b.strip()
        if not b or b.startswith('|') or b.startswith('#') or b=='---': continue
        out.append(re.sub(r'\s+',' ',b))
    return out

def voce(p):
    """corsivo se il paragrafo si apre e chiude con asterisco singolo"""
    return 'corsivo' if re.match(r'^\*[^*]', p) and p.rstrip().endswith('*') else 'tondo'

def parole(s): return re.findall(r"[a-zàèéìòùA-ZÀÈÉÌÒÙ']+", s.lower())

def ngrammi(s,n=8):
    w=parole(s)
    return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}

cap={}
print('=== 1. EQUILIBRIO DELLE DUE VOCI ===\n')
print(f"{'':4} {'parole':>7} {'corsivo':>8} {'tondo':>7} {'quota cors.':>12} {'sezioni':>8} {'par.':>5}")
for num,nome in ORDINE:
    c=corpo(open(os.path.join(ROM,nome),encoding='utf-8').read())
    ps=paragrafi(c)
    pc=[p for p in ps if voce(p)=='corsivo']; pt=[p for p in ps if voce(p)=='tondo']
    wc=sum(len(parole(p)) for p in pc); wt=sum(len(parole(p)) for p in pt)
    sez=len(re.findall(r'^## ', c, re.M))
    cap[num]={'testo':c,'w':wc+wt,'corsivo':wc,'tondo':wt,'par':ps,'sez':sez}
    print(f"{num:4} {wc+wt:7} {wc:8} {wt:7} {wc/(wc+wt):11.0%} {sez:8} {len(ps):5}")

print('\n=== 2. RITMO ===\n')
print(f"{'':4} {'par. medio':>11} {'più lungo':>10} {'sez. media':>11} {'sez. più lunga':>15}")
for num,_ in ORDINE:
    d=cap[num]; lp=[len(parole(p)) for p in d['par']]
    sm=d['w']/d['sez'] if d['sez'] else 0
    # lunghezza per sezione
    sez=re.split(r'^## ', d['testo'], flags=re.M)[1:]
    ls=[len(parole(s)) for s in sez]
    print(f"{num:4} {sum(lp)//len(lp):11} {max(lp):10} {sm:11.0f} {max(ls) if ls else 0:15}")

print('\n=== 3. RIPETIZIONE FRA CAPITOLI (contenimento di 8-grammi) ===\n')
ng={n:ngrammi(cap[n]['testo']) for n,_ in ORDINE}
righe=[]
for a,b in itertools.combinations([n for n,_ in ORDINE],2):
    com=ng[a]&ng[b]
    if com:
        q=len(com)/min(len(ng[a]),len(ng[b]))
        righe.append((q,a,b,com))
righe.sort(reverse=True, key=lambda r:r[0])
if not righe:
    print('nessun 8-grammo condiviso fra capitoli.')
for q,a,b,com in righe[:8]:
    print(f'{a} ~ {b}: {len(com)} 8-grammi condivisi ({q:.2%})')
    for g in list(com)[:3]: print('   «'+' '.join(g)+'»')

print('\n=== 4. FORMULE RICORRENTI (locuzioni della voce, oltre 2 capitoli) ===\n')
FORM=['del resto','di regola','onde','vi è','ne discende','ne segue','conviene',
      'i miei studenti','agli studenti','non si negozia','per esteso','la sede nominata',
      'non è una prova','grado b','stato zero','si registra e non si scioglie']
for f in FORM:
    # confine di parola: senza di esso «onde» conta dentro «risponde», e la
    # misura diventa un'altra cosa da quella che si voleva misurare.
    rx=r'(?<![a-zàèéìòù])'+re.escape(f)+r'(?![a-zàèéìòù])'
    pres={n:len(re.findall(rx, cap[n]['testo'], re.I)) for n,_ in ORDINE}
    dove=[f'{n}×{v}' for n,v in pres.items() if v]
    if len(dove)>2: print(f'«{f}»  →  '+'  '.join(dove))
