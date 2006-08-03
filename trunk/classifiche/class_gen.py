#!/usr/bin/env python2.4

import sys, os, re

def calcola_totali(punteggi):
    tot = 0
    scarto = max(punteggi)
    scart = 0
    for p in punteggi:
        tot = tot + int(p)
    return tot

lista = os.listdir('.')
risultati = {}
totali = {}

for file in lista:
    if (file[-4:] == '.cla' and file[0:4] == 'gene'):
        FI = open(file,'r')
        FD = FI.read()
        FI.close()
        righe = re.split('\n',FD)
        for riga in righe:
            skipper,punti = re.split('=', riga)
            risultati[skipper] = re.split(',',punti)
        fname = file+'.html'
        FO = open(fname,'w')
        FO.write("""
        <table border="1" cellspacing="0" cellpadding="2">
        <th>Skipper</th>
        """)
        d = 1
        for c in risultati[skipper]:
            FO.write("<th>%d°<br>Regata</th>"%d)
            d = d + 1
        FO.write("<th>Totale</th>")
        for skip in risultati:
            totali[skip] = calcola_totali(risultati[skip])
        totord = [(v, k) for (k, v) in totali.iteritems()]
        totord.sort()
        for s in totord:
            FO.write("<tr><td>%s</td>"%s[1])
            for p in risultati[s[1]]:
                FO.write("""<td align="center">%s</td>"""%p)
            FO.write("""<td align="center">%s</td></tr>\n"""%s[0])


        FO.write("</table>")
        FO.close()        
        
        
        
        


