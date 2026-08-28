#!/usr/bin/env python3
"""Estrae dal romanzo ogni proposizione che porta un grado dichiarato, e
prepara il riscontro contro il corpus. Il libro prescrive che ogni
affermazione porti il grado e, per gli esiti negativi, la sede: qui la
prescrizione si applica al libro."""
import re, os, glob, json

ROM='/home/user/collegi-italia/_romanzo'
ORDINE=[('I','capitolo-primo-l-elenco-che-arriva.md'),
        ('II','capitolo-secondo-l-uomo-prima-del-caso.md'),
        ('III','capitolo-terzo-gli-anni-della-farnesina.md'),
        ('IV','capitolo-quarto-le-lettere-scelte.md'),
        ('V','capitolo-quinto-l-archivio.md'),
        ('VI','capitolo-sesto-l-aritmetica.md'),
        ('VII','capitolo-settimo-ottocentotredici-volte-non-trovato.md')]

# un grado dichiarato: **A** **B** **C** **F** oppure la formula Stato Zero
GRADO = re.compile(r'\*\*(A|B|C|F)\*\*|[Ss]tat[oi] Zero')

# Un blocco e' voce prestata se apre in corsivo e chiude in corsivo. Il test
# ingenuo — apre in corsivo — da' cinque falsi positivi su sette capitoli,
# perche' i blocchi che chiudono con un grassetto dentro il corsivo terminano
# in tre asterischi. Il test va sul principio e sulla fine, non sul principio.
def voce(b):
    return bool(re.match(r'^\*[^*]', b)) and b.rstrip().endswith('*')

def blocchi(t):
    r=t.split('\n')
    for i,x in enumerate(r):
        if x.strip()=='---' and i>5:
            t='\n'.join(r[i+1:]); break
    out=[]
    for b in re.split(r'\n\s*\n', t):
        b=b.strip()
        if not b or b.startswith('#'): continue
        out.append(re.sub(r'\s+',' ',b))
    return out

righe=[]
for num,nome in ORDINE:
    for b in blocchi(open(os.path.join(ROM,nome),encoding='utf-8').read()):
        if b.startswith('*') and not b.startswith('**'):   # voce prestata: non porta gradi
            continue
        for m in GRADO.finditer(b):
            righe.append({'parte':num,'grado':m.group(1) or 'Stato Zero','testo':b})
            break

print(f'proposizioni con grado dichiarato: {len(righe)}')
import collections
print('per grado :', dict(collections.Counter(r['grado'] for r in righe)))
print('per parte :', dict(collections.Counter(r['parte'] for r in righe)))
print()
# la voce prestata non deve MAI portare gradi: controllo
sospetti=[]
for num,nome in ORDINE:
    for b in blocchi(open(os.path.join(ROM,nome),encoding='utf-8').read()):
        if b.startswith('*') and not b.startswith('**') and GRADO.search(b):
            sospetti.append((num,b[:150]))
print(f'gradi trovati DENTRO la voce prestata: {len(sospetti)}')
for n,b in sospetti: print(f'  [{n}] {b}')

json.dump(righe, open('/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/gradi.json','w'), ensure_ascii=False, indent=1)
