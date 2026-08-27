import re, os, json, unicodedata

P = '/mnt/project'
OUT = '/home/claude/staging/nodi_registrati.json'

FILES = [
    ('V63', 'ITALIA_NERA_REGISTRO_INTEGRALE_V63.docx'),
    ('V55', 'ITALIA_NERA_Registro_Analitico_Nodi_V55_INTEGRALE.docx'),
]

entry_re = re.compile(
    r'\*\*▶\s*(?P<nome>.+?)\*\*.*?\[(?P<tags>[^\]\|]*?)\|\s*Savona\s*(?P<sav>[ABC])\s*\]'
)
entry_re_loose = re.compile(r'\*\*▶\s*(?P<nome>.+?)\*\*')

def norm_key(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

nodes = {}
order = []

for src, fname in FILES:
    with open(os.path.join(P, fname), encoding='utf-8', errors='replace') as f:
        lines = f.read().split('\n')
    for i, l in enumerate(lines):
        if '▶' not in l:
            continue
        m = entry_re.search(l)
        if m:
            nome = m.group('nome')
            tags = m.group('tags')
            sav = m.group('sav')
        else:
            m2 = entry_re_loose.search(l)
            if not m2:
                continue
            nome = m2.group('nome')
            tags, sav = '', ''
        card = '[CARD]' in nome
        nome = nome.replace('[CARD]', '').strip(' *').strip()
        doms = re.findall(r'D(?:10|[1-9])', tags)
        k = norm_key(nome)
        if k not in nodes:
            nodes[k] = {'nome': nome, 'card': card, 'domini': [], 'savona': sav, 'fonti': []}
            order.append(k)
        n = nodes[k]
        for d in doms:
            if d not in n['domini']:
                n['domini'].append(d)
        if card:
            n['card'] = True
        if sav and (not n['savona'] or 'ABC'.index(sav) < 'ABC'.index(n['savona'])):
            n['savona'] = sav
        if src not in n['fonti']:
            n['fonti'].append(src)

# statistiche
per_dom = {f'D{i}': 0 for i in range(1, 11)}
senza_tag = 0
solo_v55 = 0
for k in order:
    n = nodes[k]
    if not n['domini']:
        senza_tag += 1
    else:
        per_dom[n['domini'][0]] += 1
    if n['fonti'] == ['V55']:
        solo_v55 += 1

print(f'nodi unici registrati: {len(nodes)}')
print(f'senza tag di dominio: {senza_tag}   presenti solo in V55: {solo_v55}')
for d in [f'D{i}' for i in range(1, 11)]:
    print(f'  {d}: {per_dom[d]} (dominio primario)')
mult = sum(1 for k in order if len(nodes[k]['domini']) > 1)
card = sum(1 for k in order if nodes[k]['card'])
print(f'nodi multi-dominio: {mult}   nodi cardinali [CARD]: {card}')

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump({'ordine': order, 'nodi': nodes}, f, ensure_ascii=False)
print('salvato:', OUT)

# campione nodi senza tag (per diagnosi parser)
st = [nodes[k]['nome'] for k in order if not nodes[k]['domini']][:10]
print('campione senza-tag:', '; '.join(st))
