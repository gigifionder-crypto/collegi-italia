# -*- coding: utf-8 -*-
"""Compone in PDF gli allegati del dossier, con la tipografia del corpus."""
import io, os, re, subprocess, html

SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
REPO = '/home/user/collegi-italia'
CH = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

CSS = """
@page{size:A4;margin:24mm 22mm 24mm 22mm;}
body{font-family:"Barlow Semi Condensed","Liberation Sans",sans-serif;font-size:11pt;
     line-height:1.55;color:#111;margin:0;}
h1{font-size:19pt;color:#1F3864;margin:0 0 4mm;line-height:1.2;}
h2{font-size:14.5pt;color:#1F3864;margin:8mm 0 3mm;line-height:1.25;page-break-after:avoid;}
h3{font-size:11.6pt;color:#333;font-style:italic;margin:6mm 0 2.5mm;page-break-after:avoid;}
p{margin:0 0 3.2mm;text-align:justify;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:anywhere;}
blockquote{margin:4mm 0;padding:1.5mm 0 1.5mm 5mm;border-left:2.4pt solid #1F3864;color:#222;
     text-align:justify;font-size:10.4pt;page-break-inside:avoid;hyphens:auto;-webkit-hyphens:auto;}
ul,ol{margin:0 0 3.2mm;padding-left:6mm;}
/* una voce da spuntare ha gia il proprio segno: il pallino la raddoppierebbe */
li.spunta{list-style:none;margin-left:-4.6mm;}
li{margin:0 0 1.6mm;text-align:justify;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:anywhere;}
table{border-collapse:collapse;width:100%;margin:3mm 0 4mm;font-size:9.6pt;}
th{background:#1F3864;color:#fff;text-align:left;padding:1.8mm 2.4mm;}
/* se la tabella scavalca la pagina, l'intestazione la segue e nessuna riga
   viene tagliata a meta: una riga orfana senza intestazione non si legge */
thead{display:table-header-group;}
tr{page-break-inside:avoid;}
td{border-bottom:.5pt solid #bbb;padding:1.6mm 2.4mm;vertical-align:top;text-align:justify;}
/* la colonna delle etichette non si giustifica: due parole distanziate a forza
   sono peggio di due parole */
td:first-child{text-align:left;}
/* una tabella con celle da riempire a mano diventa un modulo: righe alte e
   colonne vuote rigate, cosi si puo stampare e compilare */
table.modulo td{height:9mm;vertical-align:bottom;}
table.modulo td:empty{border-bottom:.5pt solid #888;}
hr{border:0;border-top:.5pt solid #aaa;margin:6mm 0;}
em{font-style:italic;} strong{font-weight:700;}
code{font-family:"Liberation Mono",monospace;font-size:9.2pt;color:#1F3864;
     overflow-wrap:anywhere;}
"""

def inline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    return s

def to_html(md):
    righe = md.split('\n')
    out, i = [], 0
    def blocco(pred):
        buf = []
        nonlocal i
        while i < len(righe) and pred(righe[i]):
            buf.append(righe[i]); i += 1
        return buf
    while i < len(righe):
        r = righe[i]
        if not r.strip(): i += 1; continue
        if re.match(r'^---\s*$', r): out.append('<hr>'); i += 1; continue
        m = re.match(r'^(#{1,3}) (.+)$', r)
        if m:
            n = len(m.group(1)); out.append('<h%d>%s</h%d>' % (n, inline(m.group(2)), n)); i += 1; continue
        if r.lstrip().startswith('|'):
            t = blocco(lambda x: x.lstrip().startswith('|'))
            t = [x for x in t if not re.match(r'^\s*\|?[\s:|]*-[\s:|-]*\|?\s*$', x)]
            celle = [[c.strip() for c in x.strip().strip('|').split('|')] for x in t]
            # la prima riga di una tabella markdown e' l'intestazione. Se e'
            # dichiarata vuota — «| | |» — non va stampata come riga bianca:
            # si toglie, e la tabella resta senza fascia di testa.
            if celle and not any(celle[0]):
                celle, testa = celle[1:], False
            else:
                testa = True
            if not celle:
                continue
            vuote = sum(1 for riga in celle[1:] for c in riga if not c)
            modulo = vuote >= 2
            h = ['<table class="modulo">' if modulo else '<table>']
            for j, riga in enumerate(celle):
                intesta = (j == 0 and testa)
                tag = 'th' if intesta else 'td'
                if intesta:
                    h.append('<thead>')
                elif j == (1 if testa else 0):
                    h.append('<tbody>')
                h.append('<tr>' + ''.join('<%s>%s</%s>' % (tag, inline(c), tag) for c in riga) + '</tr>')
                if intesta:
                    h.append('</thead>')
            h.append('</tbody>')
            out.append('\n'.join(h) + '</table>'); continue
        if r.startswith('>'):
            t = blocco(lambda x: x.startswith('>'))
            out.append('<blockquote><p>%s</p></blockquote>' % inline(' '.join(x.lstrip('> ').strip() for x in t))); continue
        if re.match(r'^\s*[-*] ', r) or re.match(r'^\s*\d{1,2}\. ', r):
            ordinato = bool(re.match(r'^\s*\d{1,2}\. ', r))
            voci = []
            while i < len(righe) and (re.match(r'^\s*[-*] ', righe[i]) or re.match(r'^\s*\d{1,2}\. ', righe[i])):
                v = re.sub(r'^\s*([-*]|\d+\.) ', '', righe[i]); i += 1
                while i < len(righe) and righe[i].strip() and not re.match(r'^\s*([-*] |\d{1,2}\. |#|>|\||---)', righe[i]):
                    v += ' ' + righe[i].strip(); i += 1
                casella = v.lstrip().startswith('[ ]')
                voci.append('<li%s>%s</li>' % (' class="spunta"' if casella else '',
                                               inline(v.replace('[ ]', '☐'))))
            tag = 'ol' if ordinato else 'ul'
            out.append('<%s>%s</%s>' % (tag, ''.join(voci), tag)); continue
        par = r
        i += 1
        while i < len(righe) and righe[i].strip() and not re.match(r'^\s*([-*] |\d{1,2}\. |#|>|\||---\s*$)', righe[i]):
            par += ' ' + righe[i].strip(); i += 1
        out.append('<p>%s</p>' % inline(par))
    return '\n'.join(out)

LAVORI = [
    ('_diffusione-opera/pec-unica-formale.md',  'PEC_UNICA_FORMALE'),
    ('_diffusione-opera/capitolo-campione.md',   'ALLEGATO_CAPITOLO_CAMPIONE'),
    ('_diffusione-opera/scheda-dell-opera.md',   'ALLEGATO_SCHEDA_DELL_OPERA'),
    ('_diffusione-opera/curriculum-modello.md',  'ALLEGATO_CURRICULUM_DA_COMPILARE'),
    ('_diffusione-opera/checklist-di-invio.md',   'CHECKLIST_DI_INVIO'),
    ('_diffusione-opera/relazione-al-centro-flamigni.md', 'RELAZIONE_SUL_PROGETTO'),
    ('_diffusione-opera/lettera-fondazione-aldo-moro.md',  'LETTERA_FONDAZIONE_ALDO_MORO'),
    ('_diffusione-opera/proposte-chiarelettere-bompiani.md', 'PROPOSTE_CHIARELETTERE_BOMPIANI'),
]

def main():
    for sorgente, nome in LAVORI:
        md = io.open(os.path.join(REPO, sorgente), encoding='utf-8').read()
        pagina = ('<!doctype html><meta charset="utf-8"><style>%s</style>\n%s'
                  % (CSS, to_html(md)))
        hp = os.path.join(SP, nome + '.html')
        io.open(hp, 'w', encoding='utf-8').write(pagina)
        pdf = os.path.join(REPO, '_diffusione-opera', nome + '.pdf')
        subprocess.run([CH, '--headless', '--no-sandbox', '--disable-gpu',
                        '--print-to-pdf=' + pdf, '--no-pdf-header-footer',
                        'file://' + hp], capture_output=True)
        from pypdf import PdfReader
        print('  %-36s %2d pagine' % (nome + '.pdf', len(PdfReader(pdf).pages)))

if __name__ == '__main__':
    main()
