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
        QtCore.QObject.connect(ui.CB_Classes, QtCore.SIGNAL("activated(int)"), self.LoadClassRanking)
        QtCore.QObject.connect(ui.CB_Regattas, QtCore.SIGNAL("activated(int)"), self.LoadRegattaRanking)

    def LoadClassRanking(self):
        print "Cambio classe"

    def LoadRegattaRanking(self):
        print ui.CB_Regattas.currentText()
        #La funzione deve prendere i dati nell'header [info] , caricarli nel box delle classifiche e caricare la classifica giusta nella tabella

        
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
