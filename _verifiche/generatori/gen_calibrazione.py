# -*- coding: utf-8 -*-
"""Il controllo di calibrazione, in un grafico."""
import importlib.util, os, sys
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.ticker as mticker
SP='/tmp/claude-0/-home-user-collegi-italia/b56982bd-6563-5c45-a8f3-3901ea39a5a4/scratchpad'
spec=importlib.util.spec_from_file_location('g', os.path.join(SP,'gen_verifica_p2.py'))
g=importlib.util.module_from_spec(spec); _o=sys.stdout; sys.stdout=open(os.devnull,'w')
try: spec.loader.exec_module(g)
finally: sys.stdout=_o
OUT,NAVY,INK,MUT,ROSSO = g.OUT,g.NAVY,g.INK,g.MUT,g.ROSSO
VERDE='#2f6b3a'

TESTO=[('Giudice',1592,504),('Lo Prete',1600,512),('Guglielmi',1602,514),
 ('Miceli',1605,491),('Pelosi',1607,519),('Siracusano',1608,520),
 ('Ortolani',1609,494),('Sindona',1612,501),('Torrisi',1619,531),
 ('Giovannone',1620,532),('Calvi',1624,530),('Grassini',1629,515),
 ('Santovito',1630,527),('Spagnuolo',1632,543),('Varisco',1633,537),
 ('Gallucci',1634,546),('Viezzer',1635,539),('Malfatti',1636,540),
 ('Semprini',1637,544)]
ATT=[('Berlusconi',1816,625),('Costanzo',1819,626)]

fig,ax=plt.subplots(figsize=(6.8,4.2),dpi=120)
g._fondo(fig); ax.set_facecolor('none'); ax.patch.set_alpha(0); ax.set_zorder(2)

ax.axhline(1088,color=ROSSO,linewidth=1.1,linestyle=(0,(5,3)),zorder=3,alpha=.75)
ax.text(1592,1082,'scarto congelato a 1.088',fontsize=7.6,color=ROSSO,ha='left',va='top')

for n,t,f in TESTO:
    s=t-f; piatto=(s==1088)
    ax.scatter([t],[s],s=52,color=ROSSO if piatto else '#c98a8a',
               edgecolor='white',linewidth=1.0,zorder=5 if piatto else 4)
SFALSA={'Berlusconi':(-46,-30,'right'),'Costanzo':(-4,40,'right')}
for n,t,f in ATT:
    ax.scatter([t],[t-f],s=72,color=VERDE,marker='D',edgecolor='white',linewidth=1.0,zorder=6)
    dx,dy,ha=SFALSA[n]
    ax.annotate(f'{n}\n{g._it(t)} · {g._it(f)} = {g._it(t-f)}',xy=(t,t-f),xytext=(t+dx,t-f+dy),
                fontsize=7.2,color=VERDE,ha=ha,va='center',linespacing=1.35,
                arrowprops=dict(arrowstyle='-',color=VERDE,linewidth=0.7,shrinkA=0,shrinkB=5))
ax.plot([a[1] for a in ATT],[a[1]-a[2] for a in ATT],color=VERDE,linewidth=1.4,zorder=5)

ax.set_xlim(1580,1878); ax.set_ylim(1050,1265)
ax.set_xlabel('numero di tessera',fontsize=8,color=MUT,labelpad=4)
ax.set_ylabel('scarto  (tessera − fascicolo)',fontsize=8,color=MUT,labelpad=4)
for a in (ax.xaxis,ax.yaxis): a.set_major_formatter(mticker.FuncFormatter(lambda v,_: g._it(v)))
ax.xaxis.grid(True,color='#d9d3c6',linewidth=0.7,zorder=1)
ax.yaxis.grid(True,color='#d9d3c6',linewidth=0.7,zorder=1); ax.set_axisbelow(True)
for s_ in ('top','right'): ax.spines[s_].set_visible(False)
for s_ in ('bottom','left'): ax.spines[s_].set_color('#c9ccd2'); ax.spines[s_].set_linewidth(0.8)
ax.tick_params(labelsize=7.0,colors=MUT,length=0)
fig.text(0.012,0.965,"Un archivio deriva, una sottrazione no",
         fontsize=12.2,color=NAVY,fontweight='bold',va='top')
fig.text(0.012,0.012,'\n'.join([
 "In verde le due sole coppie che la ricerca ha trovato attestate in fonti pubblicate: Berlusconi e",
 "Costanzo. Le loro tessere distano tre posizioni, i loro fascicoli una: lo scarto cambia di due. È così",
 "che si comporta un archivio con due registri, ciascuno coi propri vuoti.",
 "In rosso le coppie del testo esaminato: otto di esse hanno lo scarto identico, 1.088, su quarantadue",
 "posizioni di tessera. Uno scarto che non deriva mai non è un secondo registro: è una sottrazione."]),
 fontsize=6.5,color=MUT,va='bottom')
fig.subplots_adjust(left=0.115,right=0.985,top=0.885,bottom=0.335)
fig.savefig(os.path.join(OUT,'12_un-archivio-deriva.png')); plt.close(fig)
print('   12_un-archivio-deriva.png')
