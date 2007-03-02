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
    

    
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = MainWindow()
#translator = QtCore.QTranslator()
#translator.load(QtCore.QString(ui.i18npath+'i18n_'+ui.lang))
#QtGui.qApp.installTranslator(translator)
ui.setupUi(window)  
QtRankIO = QtRankingIO()
QtRankIO.LoadData(ui)

window.show()
sys.exit(app.exec_())
