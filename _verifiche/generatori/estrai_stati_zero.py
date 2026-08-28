#!/usr/bin/env python3
"""Il registro di chiusura: estrae dagli Stati Zero del corpus quelli che
portano la sede nominata, che sono i soli validi per la regola del libro.

Criterio dichiarato. Entra una proposizione se (a) contiene la formula
«Stato Zero» o «Stati Zero» al singolare o plurale in funzione di
registrazione, e (b) nomina una sede: un archivio, una biblioteca, un fondo,
un portale, un dominio. Le proposizioni di metodo — quelle che parlano
*della* categoria invece di registrarne una — escono per parola-spia.
"""
import re, glob, os, json, collections

REPO='/home/user/collegi-italia'
ESCLUSI=('_romanzo/','italia-nera/','_diffusione-opera/','_meta/','tomo-1-puglia/',
         'tomo-2-nazionale/','ue-27/','_paper-accademico/','_livelli-piramide/',
         '_pubblicazione-finale/','_diffusione/')

SEDI = [
 ('Archivio storico della Camera dei deputati', r'Archivio storico della Camera'),
 ('Archivio storico del Senato', r'Archivio storico del Senato'),
 ('Archivio centrale dello Stato', r'Archivio centrale dello Stato'),
 ('Archivio storico diplomatico della Farnesina', r'Archivio [Ss]torico [Dd]iplomatico'),
 ('Archivio Flamigni', r'[Ff]lamigni'),
 ('Fondo Aldo Moro', r'Fondo (Aldo )?Moro'),
 ('Edizione Nazionale delle Opere', r'Edizione Nazionale'),
 ('Commissione parlamentare', r'Commissione (parlamentare|d.inchiesta|Moro)'),
 ('Fondo PIDE-DGS (Portogallo)', r'PIDE-?DGS'),
 ('Arquivo Histórico-Diplomático (Portogallo)', r'Arquivo'),
 ('Archivi spagnoli', r'Archivo|AGA|Alcal'),
 ('Archivi vaticani e Santa Sede', r'Archivio Apostolico|Segreteria di Stato|Vaticano'),
 ('Nazioni Unite', r'Nazioni Unite|Assemblea generale'),
 ('Archivi statunitensi (NARA, FRUS, CIA)', r'NARA|FRUS|CREST|FOIA|Department of State'),
 ('Emeroteca', r'[Ee]meroteca'),
 ('Portali telematici', r'\.it\b|\.org\b|\.gov\b|portale'),
]
SPIA_METODO = ('la disciplina degli stati zero','uno stato zero opera','ciò che gli stati zero',
               'gli stati zero come','statuto dello stato zero','scala degli stati zero',
               'gli stati zero non','tipologia','definizione')

def frasi(t):
    t=re.sub(r'\s+',' ',t)
    return re.split(r'(?<=[.;])\s+(?=[A-ZÈÉÀÌÒÙ«])', t)

voci=[]
for path in sorted(glob.glob(os.path.join(REPO,'**','*.md'), recursive=True)):
    rel=os.path.relpath(path,REPO)
    if rel.startswith(ESCLUSI) or rel.startswith('.'): continue
    for f in frasi(open(path,encoding='utf-8').read()):
        if len(f)<70 or len(f)>620: continue
        b=f.lower()
        if 'stato zero' not in b and 'stati zero' not in b: continue
        if any(s in b for s in SPIA_METODO): continue
        sedi=[nome for nome,rx in SEDI if re.search(rx,f)]
        if not sedi: continue
        voci.append({'file':rel,'sedi':sedi,'frase':re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',f).strip()})

# dedup per incipit
visti,out=set(),[]
for v in voci:
    k=v['frase'][:90]
    if k in visti: continue
    visti.add(k); out.append(v)

json.dump(out, open('/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad/stati_zero.json','w'), ensure_ascii=False, indent=1)
print(f'Stati Zero con sede nominata: {len(out)}')
print('per sede:')
for s,n in collections.Counter(x for v in out for x in v['sedi']).most_common():
    print(f'  {n:4}  {s}')
print(f'\ndocumenti sorgente: {len({v["file"] for v in out})}')
