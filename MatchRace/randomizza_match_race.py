#!/usr/bin/env python

import os, sys, random, copy

from reportlab.platypus import *
#from reportlab import rl_config
from reportlab.lib.styles import PropertySet, getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus.paragraph import Paragraph
#from reportlab.lib.utils import fp_str
#from reportlab.pdfbase import pdfmetrics
from reportlab.platypus.flowables import PageBreak


li = ('a','b','c','d','e')
a = []
for m in range(0,len(li)):
    for n in range(m+1, len(li)):
        a.append((li[m],li[n]))

#a = [('a','b'),('a','c'),('a','d'),('b','c'),('b','d'), ('c','d') ]
random.shuffle(a)
na = []
f = -1
l = -1

na.append(a[0])
a.remove(a[0])

while len(a) != 0:
    found = 0
    for c in range(0,len(a)):
        d = len(na) - 1
        print d
        print "Match ", a[c]
        if (a[c][0] != na[d][0] and a[c][1] != na[d][1]) and (a[c][1] != na[d][0] and a[c][0] != na[d][1]):
            print "Rimuovo il match ", a[c]
            na.append(a[c])
            a.remove(a[c])
            found = 1
        if found == 1:
            break
    if found == 0:
        p = random.randint(0,len(a)-1)
        na.append(a[c])
        a.remove(a[c])

fname = "output_"+str(len(li))+"_skipper.pdf"
doc = SimpleDocTemplate(fname)
styleSheet = getSampleStyleSheet()
styNormal = styleSheet['Normal']
styNormal.spaceBefore = 6
styNormal.spaceAfter = 6
   
data =[['','Skipper', 'Skipper', 'Risultato'],
        ['1','10', '11', '12'],
        ['2','20', '21', '22'],
        ['3','30', '31', '32']]
        
rowheight= 100
colwidth = 30
#prima le colonne, poi le righe
t = Table(data, [80,100,100,40], colwidth)
GRID_STYLE = TableStyle(
    [('GRID', (0,0), (3,0), 0.75, colors.black),
     ('GRID', (0,1), (4,4), 0.25, colors.black),
     ('ALIGN', (0,0), (-1,-1), 'CENTER'),
     ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
     ('SIZE',(0,0),(1,2),16),
     ]
    )
t.setStyle(GRID_STYLE)
p = Paragraph("""Basics about column sizing and cell contents\n""", styleSheet['Heading1'])
flowables = [p,t]

doc.build (flowables)

