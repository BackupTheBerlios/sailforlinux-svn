#!/usr/bin/env python2.4

# ReportLab include
from reportlab.platypus import *
#from reportlab import rl_config
from reportlab.lib.styles import PropertySet, getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus.paragraph import Paragraph
#from reportlab.lib.utils import fp_str
#from reportlab.pdfbase import pdfmetrics
from reportlab.platypus.flowables import PageBreak

class Export:
    def __init__(self):
        pass
    
    def ExportAsPDF(self, DataGrid, FileName):
        doc = SimpleDocTemplate(FileName)
        styleSheet = getSampleStyleSheet()
        styNormal = styleSheet['Normal']
        styNormal.spaceBefore = 6
        styNormal.spaceAfter = 6
        data = []
        cols = DataGrid.columnCount()
        subdata = []
        subdata.append("Skipper")
        for c in range(1,cols-1):
            subdata.append("Race %d"%c)
        subdata.append("Total")
        data.append(subdata)
        rows = DataGrid.rowCount()
        for y in range(0,rows):
            subdata = []
            for x in range(0,cols):
                txt = str(DataGrid.item(y,x).text())
                subdata.append(txt)
            data.append(subdata)
        cw = []
        for c in range(0,cols):
            cw.append(50)    
        rowheight= 100
        colwidth = 30
        #prima le colonne, poi le righe
        t = Table(data, cw, colwidth)
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
                            
        
    def ExportAsHTML(self, DataGrid, FileName):     
        print FileName
        print type(DataGrid)
 
 