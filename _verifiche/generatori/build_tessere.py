# -*- coding: utf-8 -*-
"""Compone la pagina della verifica, con i sei grafici incorporati come data URI."""
import base64, os
SP = '/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
G = os.path.join(SP, 'grafici-verifica-p2')

def fig(nome, didascalia):
    b = base64.b64encode(open(os.path.join(G, nome), 'rb').read()).decode()
    return (f'<figure class="g">\n'
            f'<img src="data:image/png;base64,{b}" alt="{didascalia}">\n'
            f'<figcaption>{didascalia}</figcaption>\n</figure>')

F = ['Giuseppe Santovito', 'Raffaele Giudice', 'Donato Lo Prete', 'Vito Miceli',
     'Walter Pelosi', 'Umberto Ortolani', 'Michele Sindona', 'Pietro Musumeci',
     'Giovanni Torrisi', 'Roberto Calvi', 'Elio Cioppa', 'Giulio Grassini',
     'Antonio Cornacchia', 'Carmelo Spagnuolo', 'Antonio Varisco', 'Antonio Viezzer',
     "Federico Umberto D'Amato", 'Mino Pecorelli', 'Maurizio Costanzo', 'Franco Di Bella']
C = ['Sergio Di Donato', 'Vincenzo Rizzuti', 'Camillo Guglielmi', 'Giuseppe Siracusano',
     'Stefano Giovannone', 'Antonino Geraci', 'Mario Salacone', 'Achille Gallucci',
     'Francesco Malfatti di Montetretto', 'Mario Semprini', 'Antonio Esposito',
     'Franco Ferracuti']

COLL = [
 ('1.612', 'Michele Sindona, come <em>numero di tessera</em>',
  'Licio Gelli, come «1612 (Fascicolo)»',
  'tabella dei protagonisti · riga 11 dei trentatré'),
 ('519', 'Roberto Calvi, come <em>numero di fascicolo</em>',
  'Walter Pelosi, come «Fascicolo 519/1607»',
  'riga 16 · riga 8 dei trentatré'),
 ('527', 'Giuseppe Santovito, come <em>numero di fascicolo</em>',
  'Giuseppe Santovito, come «Tessera 527»',
  'riga 2 dei trentatré · sezione sui servizi'),
 ('530 / 519', 'Roberto Calvi, <em>fascicolo</em> 530',
  'Roberto Calvi, <em>fascicolo</em> 519 — la stessa persona, due valori',
  'scheda di apertura · riga 16 dei trentatré'),
 ('1.612 / 1.711', 'Licio Gelli, <em>fascicolo</em> 1612',
  'Licio Gelli, <em>tessera</em> 1711 — e il 1612 è già di Sindona',
  'tabella dei protagonisti · sezione sulla Commissione'),
]

righe = '\n'.join(
    f'<tr><td class="num">{n}</td><td>{a}</td><td>{b}</td><td class="dove">{d}</td></tr>'
    for n, a, b, d in COLL)


FIG1 = fig("1_imbuto-della-verificabilita.png",
  "I quattro campi della tabella e quanti nomi reggono in ciascuno. Il numero di tessera — il campo su cui il testo chiede di costruire il calcolo delle percentuali — è l&rsquo;unico per cui non esiste un solo riscontro indipendente.")
FIG2 = fig("2_tessere-sotto-la-soglia-documentata.png",
  "Quattro dei trentatré valori dichiarati come numero di tessera cadono sotto la soglia documentata; un quinto vi si posa esattamente sopra. Gli altri ventotto stanno nell&rsquo;intervallo plausibile.")
FIG3 = fig("3_i-trentatre-per-sede-istituzionale.png",
  "Ripartizione delle trentatré righe per sede istituzionale attribuita nel 1978: quindici nei servizi informativi riformati l&rsquo;anno prima, ventidue in apparati che rispondono all&rsquo;esecutivo.")
FIG4 = fig("4_composizione-documentata-dei-962.png",
  "La composizione riportata dalle fonti sui lavori della Commissione Anselmi. Il grafico del Libro quarto registra 44 parlamentari: la cifra documentata è 59, e l&rsquo;errore è annotato accanto anziché cancellato.")
FIG5 = fig("5_distanza-fra-i-fatti-e-la-prova.png",
  "La finestra richiesta dura 419 giorni. Gli elenchi furono sequestrati 1.097 giorni dopo via Fani, e la relazione di maggioranza depositata 2.310 giorni dopo.")
FIG6 = fig("6_finestra-sei-mesi-materia-disponibile.png",
  "La finestra dei sei mesi misurata sul corpus: la documentazione si addensa sui tre mesi del sequestro e si dirada ai due estremi. Novembre 1978 non ha una sola data.")
LISTA_F = "".join("<li>%s</li>" % n for n in F)
LISTA_C = "".join("<li>%s</li>" % n for n in C)

HTML = f'''<title>Le tessere impossibili</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Spectral:ital,wght@0,300;0,400;0,600;1,400&display=swap">
<style>
:root{{
  --paper:#ffffff; --cream:#f6efe1; --cream-deep:#f0e5d0; --surface:#fffdf8;
  --ink:#1F3864; --ink-soft:#42598a; --ink-faint:#7d8fb2;
  --navy:#1F3864; --navy-soft:#3d5c96; --brick:#8a2d2d;
  --rule:#ddd4c1; --rule-soft:#e9e0ce; --band:#f4ecdb;
}}
*{{box-sizing:border-box;}}
body{{
  margin:0; background:var(--paper);
  background-image:linear-gradient(168deg,#ffffff 0%,#ffffff 24%,var(--cream) 76%,var(--cream-deep) 100%);
  background-attachment:fixed; min-height:100vh; color:var(--ink);
  font-family:"Spectral",Georgia,"Times New Roman",serif;
  font-size:17px; line-height:1.62; -webkit-font-smoothing:antialiased;
}}
.wrap{{max-width:53rem;margin:0 auto;padding:0 1.5rem 5rem;}}
p{{margin:0 0 1.05em;}}
em{{font-style:italic;}}
.cond{{font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;}}

header.top{{padding:4rem 0 2.2rem;border-bottom:1px solid var(--rule);}}
.eyebrow{{
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  text-transform:uppercase;letter-spacing:.16em;font-size:.72rem;font-weight:600;
  color:var(--ink-faint);margin:0 0 1.1rem;
}}
h1{{
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-weight:700;font-size:clamp(2.6rem,7vw,4.2rem);line-height:1.02;
  letter-spacing:-.01em;margin:0 0 1.1rem;color:var(--navy);text-wrap:balance;
}}
.stand{{font-size:1.16rem;line-height:1.55;color:var(--ink-soft);max-width:38rem;margin:0;}}

h2{{
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-weight:700;font-size:1.62rem;line-height:1.16;margin:3.4rem 0 .35rem;
  color:var(--navy);text-wrap:balance;
}}
h2 .n{{display:block;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;
  font-weight:600;color:var(--ink-faint);margin-bottom:.5rem;}}
h3{{font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-weight:600;font-size:1.06rem;letter-spacing:.01em;margin:2.1rem 0 .5rem;color:var(--navy-soft);}}
.lead{{color:var(--ink-soft);max-width:38rem;}}

.regola{{
  margin:2.6rem 0;padding:1.5rem 1.6rem;background:var(--band);
  border-left:3px solid var(--navy);
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-weight:600;font-size:1.22rem;line-height:1.34;letter-spacing:.005em;color:var(--navy);
}}
.regola span{{display:block;font-weight:400;font-size:.85rem;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ink-faint);margin-top:.7rem;}}

figure.g{{margin:1.9rem 0 2.3rem;padding:0;}}
figure.g img{{display:block;width:100%;height:auto;border:1px solid var(--rule-soft);background:var(--surface);}}
figure.g figcaption{{
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-size:.86rem;line-height:1.45;color:var(--ink-soft);margin-top:.6rem;max-width:40rem;
}}

.tabwrap{{overflow-x:auto;margin:1.6rem 0 2.2rem;border:1px solid var(--rule-soft);background:var(--surface);}}
table{{border-collapse:collapse;width:100%;min-width:44rem;
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;font-size:.9rem;}}
thead th{{
  text-align:left;font-weight:600;font-size:.72rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--ink-faint);padding:.8rem .9rem;border-bottom:1px solid var(--rule);
}}
td{{padding:.72rem .9rem;border-bottom:1px solid var(--rule-soft);vertical-align:top;color:var(--ink);}}
tbody tr:last-child td{{border-bottom:none;}}
td.num{{font-weight:700;color:var(--brick);white-space:nowrap;font-variant-numeric:tabular-nums;}}
td.dove{{color:var(--ink-faint);font-size:.82rem;white-space:nowrap;}}

.gradi{{display:grid;gap:1.1rem;margin:1.7rem 0 2.2rem;}}
@media(min-width:44rem){{.gradi{{grid-template-columns:repeat(3,1fr);align-items:start;}}}}
.grado{{background:var(--surface);border:1px solid var(--rule-soft);border-top:3px solid var(--navy);padding:1.05rem 1.1rem 1.2rem;}}
.grado.c{{border-top-color:var(--navy-soft);}}
.grado.g{{border-top-color:var(--brick);}}
.grado .k{{
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  display:flex;align-items:baseline;gap:.55rem;margin-bottom:.15rem;
}}
.grado .lettera{{font-size:1.5rem;font-weight:700;color:var(--navy);line-height:1;}}
.grado.g .lettera{{color:var(--brick);}}
.grado .conta{{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint);font-weight:600;}}
.grado .che{{
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-size:.87rem;line-height:1.38;color:var(--ink-soft);margin:.35rem 0 .8rem;
}}
.grado ul{{margin:0;padding:0;list-style:none;
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;font-size:.86rem;line-height:1.5;}}
.grado li{{padding:.13rem 0;border-top:1px solid var(--rule-soft);}}
.grado li:first-child{{border-top:none;}}

.chiusa{{margin-top:3.6rem;padding-top:1.6rem;border-top:1px solid var(--rule);
  font-family:"Barlow Semi Condensed","Liberation Sans",system-ui,sans-serif;
  font-size:.83rem;line-height:1.6;color:var(--ink-faint);max-width:40rem;}}
.chiusa a{{color:var(--navy-soft);}}
</style>

<div class="wrap">

<header class="top">
  <p class="eyebrow">Ottanta anni senza Pace · verifica di un elenco · 26 agosto 2026</p>
  <h1>Le tessere impossibili</h1>
  <p class="stand">Trentatré nomi, trentatré numeri di tessera, una tabella che si dichiara
  «graniticamente confermata». I nomi in gran parte reggono. I numeri, no: quattro cadono
  sotto una soglia che gli atti parlamentari escludono, e cinque valori sono assegnati
  due volte. Questa è la verifica, campo per campo.</p>
</header>

<h2><span class="n">I</span>Il campo su cui non c'è riscontro</h2>
<p class="lead">Un elenco si verifica per campi separati, non in blocco. Il nome è un campo,
il ruolo ricoperto nella primavera del 1978 è un altro, l'appartenenza agli elenchi
sequestrati è un terzo, il numero di tessera è un quarto. Il testo li presenta insieme e
chiede di crederli insieme. Presi uno alla volta, si comportano in modo molto diverso.</p>

{FIG1}

<p>Il divario fra la terza barra e la quarta è tutto il problema. Venti nomi su trentatré
hanno un'appartenenza corroborata da fonti che non discendono da questo testo. Nessuno dei
trentatré ha un numero di tessera che io possa confermare altrove. E il numero di tessera
è precisamente il campo su cui poggia l'analisi quantitativa che il testo propone.</p>

<h2><span class="n">II</span>Quattro numeri che quel campo non poteva contenere</h2>
<p class="lead">Non si tratta di cifre invertite. Nelle audizioni della Commissione
parlamentare d'inchiesta è verbalizzato che la numerazione delle tessere sequestrate a
Castiglion Fibocchi presenta ampi vuoti e che <strong>nessuna tessera aveva numero
inferiore al 1.600</strong>. È il dato da cui la Commissione ricavò l'ipotesi che
l'archivio della Giole fosse solo una piramide inferiore.</p>

{FIG2}

<p>Il testo conosce quella soglia — la cita esso stesso, e cita la tessera 1711 di Gelli.
Poi assegna 158, 163, 811 e 1592 come numeri di tessera. Corregge perfino un nome
(«Santovito non è 163, è Salacone») senza accorgersi che la correzione lascia il 163
esattamente dov'era: sotto una soglia che non ammette nulla.</p>

<h2><span class="n">III</span>Lo stesso numero, due volte</h2>
<p class="lead">L'altra prova sta dentro il testo e non richiede archivi. Cinque valori
compaiono in due posizioni incompatibili: assegnati a due persone diverse, oppure alla
stessa persona con due significati diversi, oppure alla stessa persona con due valori
diversi.</p>

<div class="tabwrap">
<table>
<thead><tr><th>Il numero</th><th>Il testo lo assegna a</th><th>E anche a</th><th>Dove</th></tr></thead>
<tbody>
{righe}
</tbody>
</table>
</div>

<p>Un archivio non si comporta così. Un numero di fascicolo identifica una posizione e una
sola; un numero di tessera identifica un iscritto e uno solo. Cinque collisioni in un
documento che si presenta come collazione d'archivio non sono sviste di trascrizione: sono
il segno che i numeri non provengono da un archivio.</p>

<h2><span class="n">IV</span>I trentatré, per grado di riscontro</h2>
<p class="lead">Questa è la classificazione per grado, secondo la scala del corpus. Il
confine fra il primo gruppo e il secondo è il confine della mia conoscenza, non quello
dell'archivio: soltanto l'allegato Anselmi può spostarlo, in un senso o nell'altro.</p>

<div class="gradi">
  <div class="grado">
    <div class="k"><span class="lettera">F</span><span class="conta">venti nomi</span></div>
    <p class="che">Appartenenza agli elenchi corroborata da fonti indipendenti da questo
    testo. Il <em>numero</em> resta non corroborato anche qui.</p>
    <ul>{LISTA_F}</ul>
  </div>
  <div class="grado c">
    <div class="k"><span class="lettera">C</span><span class="conta">dodici nomi</span></div>
    <p class="che">Persona reale e ruolo del 1978 verificabili; appartenenza che non so
    corroborare fuori da questo testo. Sono due affermazioni di rango diverso, e il testo
    le presenta appaiate.</p>
    <ul>{LISTA_C}</ul>
  </div>
  <div class="grado g">
    <div class="k"><span class="lettera">G</span><span class="conta">un nome</span></div>
    <p class="che">Posizione definita in sede giudiziaria. Il precedente esiste: l'appartenenza
    di Publio Fiori fu esclusa da una sentenza del Tribunale di Roma nel 2001.</p>
    <ul><li>Gustavo Selva</li></ul>
  </div>
</div>

{FIG3}

<h2><span class="n">V</span>La prova arriva molto dopo i fatti</h2>
<p class="lead">C'è un vincolo cronologico che nessuna verifica dei singoli numeri può
aggirare, e che vale anche nell'ipotesi in cui tutti e trentatré risultassero esatti.</p>

{FIG5}

<p>Nel 1978 la composizione della loggia non era un oggetto conoscibile. Fu rivelata tre
anni dopo e ordinata sei anni dopo. Una lista del 1981 documenta chi vi risultava nel 1981.
Che sia la stessa cosa di «chi vi era iscritto nella primavera del 1978» è un'ipotesi
ragionevole, non un fatto accertato — e il testo stesso registra i 49 affiliati posti in
sonno e i 22 transitati ad altre logge, che sono esattamente i casi in cui le due cose
divergono.</p>

{FIG6}

<h2><span class="n">VI</span>Il denominatore regge, il numeratore no</h2>

{FIG4}

<p>Il denominatore, quindi, esiste ed è solido: 962 nominativi, con una composizione nota.
Manca il numeratore. Una percentuale calcolata su numeri di tessera che la fonte primaria
esclude non sarebbe un'analisi quantitativa: sarebbe un errore travestito da aritmetica.</p>

<h2><span class="n">VII</span>Che cosa serve, e dove chiederlo</h2>
<p>Una cosa sola, e non è ricavabile in rete: <strong>l'allegato alla Doc. XXIII n. 2 —
Relazione della Commissione parlamentare d'inchiesta sulla Loggia P2, 12 luglio 1984</strong>,
dove i numeri stanno scritti accanto ai nomi. La relazione è pubblica; l'allegato nominativo
va richiesto all'Archivio storico della Camera dei deputati. Finché non è sul tavolo, nessun
numero di questo elenco va pubblicato come certificato.</p>

<div class="regola">
  L'appartenenza a un'organizzazione non è prova di condotta.
  <span>terza regola dell'opera — e ultima riga del testo verificato</span>
</div>

<p>Vale anche nel caso migliore. Se l'allegato confermasse tutti e trentatré i numeri, si
sarebbe accertata l'appartenenza di trentatré persone a una loggia, e nient'altro. Nessuna
condotta, nessuna responsabilità, nessun concorso. La distanza fra le due cose è l'intera
ragione per cui questa verifica esiste.</p>

<p class="chiusa">
Verifica prodotta con sistemi di intelligenza artificiale sotto direzione e responsabilità
umana, come ogni documento di quest'opera. Le classificazioni per grado sono dichiarate e
rivedibili; le correzioni sono annotate accanto all'errore e non lo sostituiscono. I sei
grafici sono generati dai dati citati nelle rispettive note.<br><br>
Fonti documentali:
<a href="https://it.wikisource.org/wiki/Relazione_della_Commissione_parlamentare_di_inchiesta_sulla_Loggia_P2/Capitolo_II._L%27organizzazione_e_la_consistenza/II_-_Autenticit%C3%A0_e_attendibilit%C3%A0_delle_liste">Relazione Anselmi, Cap. II — Autenticità e attendibilità delle liste</a> ·
<a href="https://www.archivioantimafia.org/p2/commissione_parlamentare/01.%20Relazioni%20Minoranza%20(0-005)/000-relazione-anselmi.pdf">Relazione Anselmi (PDF)</a> ·
<a href="https://it.wikipedia.org/wiki/Appartenenti_alla_P2">Appartenenti alla P2</a> ·
<a href="https://www.ilfattoquotidiano.it/2021/03/17/p2-quarantanni-fa-la-scoperta-degli-iscritti-alla-loggia-di-licio-gelli-ecco-perche-gli-elenchi-con-962-nomi-non-erano-completi/6134635/">Il Fatto Quotidiano, 17 marzo 2021</a> ·
<a href="https://it.wikipedia.org/wiki/Comitato_esecutivo_per_i_servizi_di_informazione_e_sicurezza">CESIS</a>
</p>

</div>
'''

out = os.path.join(SP, 'tessere.html')
open(out, 'w', encoding='utf-8').write(HTML)
print(out, os.path.getsize(out) // 1024, 'KB')
