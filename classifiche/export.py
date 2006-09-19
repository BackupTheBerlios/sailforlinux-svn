#!/usr/bin/env python2.4

import string


# ReportLab include
from reportlab.platypus import *
#from reportlab import rl_config
from reportlab.lib.styles import PropertySet, getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.pagesizes import landscape, A4
#from reportlab.lib.utils import fp_str
#from reportlab.pdfbase import pdfmetrics
from reportlab.platypus.flowables import PageBreak
from reportlab.lib import units

class Export:
    def __init__(self):
        pass
    
        
    def ExtractData(self, DataSource):
        DataDest = []
        cols = DataSource.columnCount()
        subdata = []
        subdata.append("Skipper")
        for c in range(1,cols-1):
            subdata.append("Race %d"%c)
        subdata.append("Total")
        DataDest.append(subdata)
        rows = DataSource.rowCount()
        for y in range(0,rows):
            subdata = []
            for x in range(0,cols):
                txt = str(DataSource.item(y,x).text())
                subdata.append(txt)
            DataDest.append(subdata)
        return DataDest
    
    def ExtractRegattaInfo(self, RegattaSource):
        reg = str(RegattaSource).split(' ')
        for r in range(0,len(reg)):
            reg[r] = reg[r].capitalize()
        classe = reg[-1]
        reg[-1] = ''
        race = string.join(reg)
        return ([race,classe])

        
    def ExportAsPDF(self, DataGrid, FileName, Regatta):
        doc = SimpleDocTemplate(FileName, pagesize=landscape(A4), leftMargin=units.mm*20, topMargin=units.mm*10, bottomMargin=units.mm*10)
        styleSheet = getSampleStyleSheet()
        styNormal = styleSheet['Normal']
        styNormal.spaceBefore = 6
        styNormal.spaceAfter = 6
        data = self.ExtractData(DataGrid)
        cw = []
        cw.append(100)
        cols = DataGrid.columnCount()
        rows = DataGrid.rowCount()
        for c in range(0,cols-1):
            cw.append(50)    
        rowheight= 100
        colwidth = 30
        #prima le colonne, poi le righe
        t = Table(data, cw, colwidth)
        # cols deve essere diminuito di uno, non so perche'.
        cols -= 1
        GRID_STYLE = TableStyle(
            [('GRID', (0,0), (cols,rows), 0.75, colors.black),
            ('GRID', (0,1), (cols,rows), 0.25, colors.black),
            ('ALIGN', (0,0), (1,-1), 'CENTER'),
            ('ALIGN', (1,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('SIZE',(0,0),(cols,0),16),
            ('SIZE',(0,1),(cols,rows),14)
            ]
            )
        (race, classe) = self.ExtractRegattaInfo(Regatta)
        t.setStyle(GRID_STYLE)
        p = Paragraph("""Classifica '%s' classe %s\n"""%(race , classe), styleSheet['Heading1'])
        flowables = [p,t]
        
        doc.build (flowables)
                            
        
    def ExportAsHTML(self, DataGrid, FileName, Regatta):     
        data = self.ExtractData(DataGrid)
        
        
 
 