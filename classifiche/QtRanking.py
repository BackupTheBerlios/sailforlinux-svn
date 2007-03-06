#!/usr/bin/python2.4 

# system include
import sys, os, re, string, ConfigParser
sys.path.append('modules')

# PyQt4 include
from PyQt4 import QtGui, QtCore

# qtclass include
from MainWindow import Ui_MainWindow

#QtRanking Include
from QtRankingIO import *
from QtExport import *

class MainWindow(Ui_MainWindow):
    def __init__(self):
        pass
    
    def FinalizeGui(self):
        # Signal Connection
        QtCore.QObject.connect(ui.CB_Regattas, QtCore.SIGNAL("activated(int)"), self.LoadRegattaClasses)
        QtCore.QObject.connect(ui.CB_Class, QtCore.SIGNAL("activated(int)"), self.LoadRanking)
        

    def LoadRegattaClasses(self):
        reg = ui.CB_Regattas.currentText()
        file = './saved_data/'+re.sub(' ','_',str(reg))+'.cla'
        data = ConfigParser.ConfigParser()
        data.readfp(open(file))
        cl = data.get("info", "class").split(',')
        ui.CB_Class.clear()
        ui.CB_Class.addItems(cl)
        self.LoadRanking()
    
    def LoadRanking(self):
        reg = ui.CB_Regattas.currentText()
        file = './saved_data/'+re.sub(' ','_',str(reg))+'.cla'
        rank = QtRankIO.LoadRegattaRanking(file,ui.CB_Class.currentText())
        self.FillResultTable('D', rank)
        
        
    def FillResultTable(self, type, data):
    
        def ClearRankTable(type):
            if type == 'D':
                ClearTable(ui.T_DetailRanking)
            if type == 'G':
                ClearTable(ui.T_GeneralRanking)


        def ClearTable(Item):
            Item.clear()
            Item.setRowCount = 0
            Item.setColumnCount = 0
            rows = Item.rowCount()
            cols = Item.columnCount()
            for i in range(cols, 0, -1):
                Item.removeColumn(i)
            for i in range(rows, 0, -1):
                Item.removeRow(i)
            Item.removeRow(0)
            Item.removeColumn(0)
            Item.setRowCount = 0
            Item.setColumnCount = 0
            
            
        def UpdateTable(table, header, data):
            for sk in header:
                table.insertColumn(0)
            x = 0
            for sk in data:
                table.insertRow(table.rowCount())
                pt = QtGui.QTableWidgetItem(sk)
                pt.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(x,0,pt)
                y = 1
                for p in data[sk]:
                    pt = QtGui.QTableWidgetItem(p)
                    pt.setTextAlignment(QtCore.Qt.AlignCenter)
                    table.setItem(x,y,pt)
                    y += 1
                x += 1
            table.setHorizontalHeaderLabels(TableHeader)
            table.resizeColumnsToContents()
            
        if type == 'D':
            header = 'Race'
        if type == 'G':
            header = 'Regatta'
        TableBody = {}
        TableHeader = ["Skipper"]
        c = 1
        for sk in data:
            for p in data[sk]:
                TableHeader.append('%s %d'%(header, c))
                c += 1
            TableHeader.append('Tot')
            break
        for sk in data:
            TableBody[sk] = []
            tot = 0
            for r in data[sk]:
                TableBody[sk].append(str(r))
                if r == 'DNF':
                    r = 10
                tot += int(r)
            TableBody[sk].append(str(tot))
        if type == 'D':
            ClearRankTable('D')
            UpdateTable(ui.T_DetailRanking, TableHeader, TableBody)
        if type == 'G':
            ClearRankTable('G')
            UpdateTable(ui.T_GeneralRanking, TableHeader, TableBody)
            
        

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = MainWindow()
#translator = QtCore.QTranslator()
#translator.load(QtCore.QString(ui.i18npath+'i18n_'+ui.lang))
#QtGui.qApp.installTranslator(translator)
ui.setupUi(window)  
QtRankIO = QtRankingIO()
QtRankIO.LoadData(ui)
ui.FinalizeGui()
window.show()
sys.exit(app.exec_())
