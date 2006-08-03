#!/usr/bin/env python2.4

import sys, os, re

def calcola_totali(punteggi):
    tot = 0
    scarto = max(punteggi)
    if scarto == '999': scarto='20'
    scart = 0
    for p in punteggi:
        if p == '999': p = '20'
        tot = tot + int(p)
    tot = tot - int(scarto)
        
    return tot

lista = os.listdir('.')

for file in lista:
    risultati = {}
    totali = {}
    if (file[-4:] == '.cla' and file[0:4] != 'gene'):
        FI = open(file,'r')
        FD = FI.read()
        FI.close()
        righe = re.split('\n',FD)
        for riga in righe:
            skipper,punti = re.split('=', riga)
            risultati[skipper] = re.split(',',punti)
            print skipper, risultati[skipper]
        fname = file+'.html'
        FO = open(fname,'w')
        FO.write("""
        <table border="1"  cellspacing="0" cellpadding="2">
        <th>Skipper</th>
        """)
        d = 1
        for c in risultati[skipper]:
            FO.write("<th>%d°<br>Manche</th>"%d)
            d = d + 1
        FO.write("<th>Totale</th>")
        for skip in risultati:
            totali[skip] = calcola_totali(risultati[skip])
        totord = [(v, k) for (k, v) in totali.iteritems()]
        totord.sort()
        for s in totord:
            FO.write("<tr><td>%s</td>"%s[1])
            scarto = max(risultati[s[1]])
            if scarto == '999': scarto = '20'
            scartato = 0
            for p in risultati[s[1]]:
                if p == '999': p='20'
                if (p == scarto and scartato == 0) :
                    FO.write("""<td bgcolor="#ff0000" align="center">%s</td>"""%p)
                    scartato = 1
                else:
                    FO.write("""<td align="center">%s</td>"""%p)
            FO.write("""<td align="center">%s</td></tr>\n"""%s[0])
        FO.write("</table>")
        FO.close()        
        
        
        
        


