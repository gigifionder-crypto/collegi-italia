# Gli strumenti ricevuti

*Nota prodotta con sistemi di intelligenza artificiale sotto direzione e
responsabilità umana.*

Questa cartella conserva gli script **arrivati insieme al materiale**, non scritti
per quest'opera. Sono conservati **come ricevuti**: non corretti, non adattati,
non eseguiti.

## `estrai_nodi.py`

Lo strumento con cui i nodi sono stati estratti dai registri integrali V63 e V55.
Vale la pena conservarlo perché **rende ispezionabile il metodo**: dice, in
codice, che cosa conta come nodo — un paragrafo che apre con `**▶ nome**` e porta
fra parentesi quadre i tag e il grado nella forma `Savona A|B|C` — e come i nomi
vengono normalizzati per il confronto (scomposizione Unicode, rimozione dei
segni diacritici, minuscole). Un elenco di nodi si può contestare; una regola di
estrazione si può leggere e riprodurre.

**Non è eseguibile qui**, e non è un difetto da correggere: punta a `/mnt/project`
e a `/home/claude/staging`, cioè all'ambiente in cui fu scritto, e ai due file
`ITALIA_NERA_REGISTRO_INTEGRALE_V63.docx` e
`ITALIA_NERA_Registro_Analitico_Nodi_V55_INTEGRALE.docx`. Correggere quei
percorsi lo renderebbe un altro script, e questa cartella conserva quello vero.
