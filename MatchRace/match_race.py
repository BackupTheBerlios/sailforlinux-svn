#!/usr/bin/env python2.4

import sys,copy, random, re, os
from reportlab.platypus import *
from reportlab.lib.styles import PropertySet, getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.flowables import PageBreak
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import units

from PyQt4 import QtGui, QtCore, uic, Qt

from MainWin import Ui_D_MainWin

class MainWin(Ui_D_MainWin):
    
    matchRaceList = []
    skipperList = []
    ROWSKIPPER = 5
    
    def AddSkipperToList(self):
        skipper =  self.T_SkipperName.text()
        if skipper == '':
            self.ShowWarning("The skipper name is not valid.\n Please insert a valid skipper name.")
            return
        y = self.T_SkipperList.rowCount()
        for pos in range(0,y):
            PrecSkipper = self.T_SkipperList.item(pos,0).text()
            if skipper == PrecSkipper:
                self.ShowWarning("The skipper name is duplicated.\n Please insert a unique skipper name.")
                return        
        sk = QtGui.QTableWidgetItem(skipper)
        self.T_SkipperList.insertRow(y)
        self.T_SkipperList.setItem(y,0,sk)
        self.T_SkipperName.setText("")
        
    def GenerateMatchRace(self):
        self.matchRaceList = []
        self.skipperList = []
        n = self.T_SkipperList.rowCount()
        if n == 0:
            self.ShowWarning("The skipper list is empty.\n Please insert some skipper.")
            return
        if self.T_MatchRaceList.rowCount() > 1:
            self.ClearMatchRaceList()
        for pos in range(0,n):
            self.skipperList.append(str(self.T_SkipperList.item(pos,0).text()))
        for n in range(0,len(self.skipperList)):
            for m in range(n+1, len(self.skipperList)):
                self.matchRaceList.append((self.skipperList[n], self.skipperList[m]))
        self.RandomizeMatchRace(self.matchRaceList)
       
    def RandomizeMatchRace(self, mr):
        defMatchRaceList = []
        tmpMatchRachList = copy.deepcopy(mr)
        random.shuffle(tmpMatchRachList)
        f = -1
        l = -1
        defMatchRaceList.append(tmpMatchRachList[0])
        tmpMatchRachList.remove(tmpMatchRachList[0])
        while len(defMatchRaceList) != 0:
            found = 0
            for c in range(0,len(tmpMatchRachList)):
                d = len(defMatchRaceList) - 1
                if (tmpMatchRachList[c][0] != defMatchRaceList[d][0] and \
                       tmpMatchRachList[c][1] != defMatchRaceList[d][1]) and \
                      (tmpMatchRachList[c][1] != defMatchRaceList[d][0] and \
                        tmpMatchRachList[c][0] != defMatchRaceList[d][1]):
                    defMatchRaceList.append(tmpMatchRachList[c])
                    tmpMatchRachList.remove(tmpMatchRachList[c])
                    found = 1
                if found == 1:
                    break
            if len(tmpMatchRachList) == 0:
                break
            if found == 0:
                if len(tmpMatchRachList) == 1 :
                    p = 0
                else:
                    p = random.randint(0,len(tmpMatchRachList)-1)
                defMatchRaceList.append(tmpMatchRachList[p])
                tmpMatchRachList.remove(tmpMatchRachList[p])
        y = 0
        match_a = {}
        match_b = {}
        for matchrace in defMatchRaceList:
            self.T_MatchRaceList.insertRow(self.T_MatchRaceList.rowCount())        
            match_a[y] = QtGui.QTableWidgetItem(matchrace[0])
            match_b[y] = QtGui.QTableWidgetItem(matchrace[1])
            if self.R_Live.isChecked():
                print "live"
            match_a[y].setTextAlignment(QtCore.Qt.AlignHCenter)
            match_b[y].setTextAlignment(QtCore.Qt.AlignHCenter)
            self.T_MatchRaceList.setItem(y,0,match_a[y])
            self.T_MatchRaceList.setItem(y,1,match_b[y])
            y = y + 1
            
    def BuildMatchRaceList(self):
        mr = self.T_MatchRaceList.rowCount()
        if mr > 13:
            data = [["","Sk. A","Sk. B", "Ris", "", "", "Sk. A", "Sk. B", "Ris"]]
            incr = 2
        else:
            incr = 1
            data = [["","Sk. A","Sk. B", "Ris"]]
        for c in range(0,mr,incr):
            sa1 = str(self.T_MatchRaceList.item(c,0).text())
            sb2 = str(self.T_MatchRaceList.item(c,1).text())
            if mr > 13:
                d = c + 1
                try:
                    sa3 = str(self.T_MatchRaceList.item(d,0).text())
                    sb4 = str(self.T_MatchRaceList.item(d,1).text())                
                except:
                    sa3 = ""
                    sb4 = ""
            if self.R_OffLine.isChecked():
                sa1 = sa1
                sb2 = sb2
                if mr > 13:
                    sa3 = sa3
                    sb4 = sb4
                
            p = c + 1
            pc1 = "Reg. %3d"%p
            if mr > 13:
                p = c + 2
                pc2 = "Reg. %3d"%p
            if mr > 13:
                data.append([pc1, sa1, sb2, "", "",pc2,sa3,sb4,""])
            else:
                data.append([pc1, sa1, sb2, ""])
        return data
    
    def AddSkipperTable(self):
        n = self.T_SkipperList.count()
        sklist = []
        subsklist = []
        row = 0
        for sk in range(0,n):
            self.T_SkipperList.setCurrentRow(sk)
            subsklist.append(str(self.T_SkipperList.currentItem().text()) + " - ")
            row = row + 1
            if row == self.ROWSKIPPER:
                sklist.append(subsklist)
                subsklist = []
                row = 0
        if len(subsklist) < self.ROWSKIPPER and len(subsklist) > 0:
            m = len(subsklist)
            for c in range(m, self.ROWSKIPPER):
                subsklist.append('')
            sklist.append(subsklist)
        return sklist
            
    def SaveMatchRaceList(self):
        mr = self.T_MatchRaceList.rowCount()
        if mr == 0:
            self.ShowWarning("Nothing to save\n")
            return
        mrlist = self.BuildMatchRaceList()
        fileName = QtGui.QFileDialog.getSaveFileName(None,"Save As...",
                                                        ".",
                                                        "*.pdf",
                                                        "*.pdf"
                                                        )
        if fileName == '':
            return
        ext = str(fileName[-4:])
        if ext.upper() != ".pdf".upper():
            fileName = fileName+".pdf"
        doc = SimpleDocTemplate(fileName, pagesize=landscape(A4), leftMargin=units.mm*20, topMargin=units.mm*10, bottomMargin=units.mm*10)
        styleSheet = getSampleStyleSheet()
        styNormal = styleSheet['Normal']
        styNormal.spaceBefore = 6
        styNormal.spaceAfter = 20
        rowheight= units.mm*10
        colwidth = units.mm*25
        # first the columns, after the rows
        t = Table(mrlist, colwidth, rowheight)
        flowables = []
        if self.R_OffLine.isChecked():
            psk = Paragraph("""Skipper List\n\n""", styleSheet['Heading1'])
            flowables.append(psk)
            skipperTable = self.AddSkipperTable()
            rows = len(skipperTable)
            cols = len(skipperTable[0])
            skt = Table(skipperTable, units.mm*55, units.mm*10,)
            flowables.append(skt)
            SK_GRID_STYLE = TableStyle(
                    [('GRID', (0,0), (cols,rows), 0.25, colors.black),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('SIZE',(0,0),(-1,-1),units.mm*7),
                    ]
                )
            skt.setStyle(SK_GRID_STYLE)
            
        rowst = len(mrlist)
        colst = len(mrlist[0])
        GRID_STYLE = TableStyle(
                [('GRID', (0,0), (colst,rowst), 0.75, colors.black),
                ('GRID', (0,1), (colst,6), 0.25, colors.black),
                ('GRID', (4,0),(4,rowst), 0.25, colors.black),
                ('LINEABOVE',(4,0),(4,rowst), 0.0, colors.white),
                ('LINEABOVE',(0,0),(3,rowst), 0.0, colors.black),
                ('LINEABOVE',(5,0),(colst,rowst), 0.0, colors.black),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('SIZE',(0,0),(-1,-1),units.mm*7),
                ]
            )
        t.setStyle(GRID_STYLE)
        p = Paragraph("""\n\nMatch Race program\n""", styleSheet['Heading1'])
        flowables.append(p)
        flowables.append(t)
        doc.build (flowables)        
        
    def ClearMatchRaceList(self):
        self.T_MatchRaceList.clear()
        self.T_MatchRaceList.setRowCount = 0
        rows = self.T_MatchRaceList.rowCount() 
        for i in range(rows, 0, -1):
            self.T_MatchRaceList.removeRow(i)
        self.T_MatchRaceList.removeRow(0)
        self.T_MatchRaceList.setRowCount = 0
        self.T_MatchRaceList.setHorizontalHeaderLabels(["Skipper A","Skipper B","Winner"])
    
    def DeleteSkipper(self):
        self.T_SkipperList.removeRow(self.T_SkipperList.currentRow())
        
    def ClearSkipper(self):
        self.T_SkipperList.clear()
        self.T_SkipperList.setRowCount = 0
        rows = self.T_SkipperList.rowCount() 
        for i in range(rows, 0, -1):
            self.T_SkipperList.removeRow(i)
        self.T_SkipperList.removeRow(0)
        self.T_SkipperList.setRowCount = 0
        self.T_SkipperList.setHorizontalHeaderLabels(["Skipper","Points","Rank"])

    def CalcRanking(self):
        SkipperList  = {}
        rows = self.T_SkipperList.rowCount() 
        for y in range(0,rows):
            sk = self.T_SkipperList.item(y,0).text()
            SkipperList[str(sk)] = 0
        rows = self.T_MatchRaceList.rowCount()
        for y in range(0,rows):
            try:
                v = str(self.T_MatchRaceList.item(y,2).text())
                SkipperList[v] = SkipperList[v] + 1
            except:
                msg = "Race %d had not a winner"%(y+1)
                self.ShowError(msg)
                return
                
        it = SkipperList.items()
        it = [(v, k) for (k, v) in it]
        it.sort()
        it = [(k, v) for (v, k) in it]
        it.reverse()
        self.ClearSkipper()
        y = 0
        
        for item in it:            
            self.T_SkipperList.insertRow(y)
            sk = QtGui.QTableWidgetItem(item[0])
            self.T_SkipperList.setItem(y,0,sk)
            sk = QtGui.QTableWidgetItem(str(item[1]))
            sk.setTextAlignment(QtCore.Qt.AlignCenter)
            self.T_SkipperList.setItem(y,1,sk)
            y = y + 1

    def ShowWarning(self, msg):
        QtGui.QMessageBox.warning(None, self.tr("Error"),
            self.tr(msg),
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.Escape)

        
    def ShowError(self, msg):
        QtGui.QMessageBox.critical(None, self.tr("Error"),
            self.tr(msg),
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.Escape)
            
            
            
    def UpdateFileName(self):
        txt = self.E_FileName.text()
        d = os.getcwd()
        s = os.sep
        fname = d+s+txt
        if txt[-4:] != 'pdf':
            fname = fname+'.pdf'
        self.E_FileName.setText(fname)
            
# End Class        
        
        
app = QtGui.QApplication(sys.argv)
window = QtGui.QDialog()

ui = MainWin()
ui.setupUi(window)

# Custom signal connection
QtCore.QObject.connect(ui.B_AddSkipper, QtCore.SIGNAL("clicked()"), ui.AddSkipperToList)
QtCore.QObject.connect(ui.B_Generate, QtCore.SIGNAL("clicked()"), ui.GenerateMatchRace)
QtCore.QObject.connect(ui.B_Save, QtCore.SIGNAL("clicked()"), ui.SaveMatchRaceList)
QtCore.QObject.connect(ui.B_ClearMatchRace, QtCore.SIGNAL("clicked()"), ui.ClearMatchRaceList)
QtCore.QObject.connect(ui.B_DelSkipper, QtCore.SIGNAL("clicked()"), ui.DeleteSkipper)
QtCore.QObject.connect(ui.B_ClearSkipper, QtCore.SIGNAL("clicked()"), ui.ClearSkipper)
QtCore.QObject.connect(ui.B_Ranking, QtCore.SIGNAL("clicked()"), ui.CalcRanking)
QtCore.QObject.connect(ui.E_FileName, QtCore.SIGNAL("lostFocus()"), ui.UpdateFileName)

window.show()
sys.exit(app.exec_())