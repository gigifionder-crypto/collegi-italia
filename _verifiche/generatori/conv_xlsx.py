# -*- coding: utf-8 -*-
"""Da tavola .xlsx a documento markdown: un foglio, una sezione; una riga, una
riga di tabella. I fogli che non sono tabelle (una colonna sola, prosa) si
rendono in prosa, perche' incolonnarli li renderebbe illeggibili."""
import openpyxl, re, sys, os

def esc(v):
    if v is None: return ''
    s = str(v).replace('\r\n', ' ').replace('\n', ' ').strip()
    return s.replace('|', '\\|')

def foglio(ws):
    righe = [[esc(c) for c in r] for r in ws.iter_rows(values_only=True)]
    righe = [r for r in righe if any(r)]
    if not righe: return ''
    largh = max(len(r) for r in righe)
    if largh == 1:                       # prosa, non tabella
        return '\n\n'.join(r[0] for r in righe if r[0])
    testa = righe[0] + [''] * (largh - len(righe[0]))
    out = ['| ' + ' | '.join(testa) + ' |',
           '|' + '---|' * largh]
    for r in righe[1:]:
        r = r + [''] * (largh - len(r))
        out.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(out)

def converti(src, dst, titolo, sottotitolo):
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    parti = [f'# {titolo}', '',
             '*Tavola dell\'opera «Italia Nera», acquisita il 27 agosto 2026. '
             'Prodotta con sistemi di intelligenza artificiale sotto direzione e '
             'responsabilità umana.*', '']
    if sottotitolo:
        parti += [sottotitolo, '']
    for ws in wb.worksheets:
        corpo = foglio(ws)
        if not corpo: continue
        parti += ['', f'## {ws.title}', '', corpo, '']
    wb.close()
    open(dst, 'w', encoding='utf-8').write('\n'.join(parti).rstrip() + '\n')
    return sum(1 for _ in open(dst, encoding='utf-8'))

if __name__ == '__main__':
    print(converti(sys.argv[1], sys.argv[2], sys.argv[3],
                   sys.argv[4] if len(sys.argv) > 4 else ''))
