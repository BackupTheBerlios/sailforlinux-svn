# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Mar  2 22:45:53 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,934,731).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.centralwidget)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.CB_Classi = QtGui.QComboBox(self.centralwidget)
        self.CB_Classi.setObjectName("CB_Classi")
        self.vboxlayout.addWidget(self.CB_Classi)

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)

        self.CB_Regattas = QtGui.QComboBox(self.centralwidget)
        self.CB_Regattas.setObjectName("CB_Regattas")
        self.vboxlayout.addWidget(self.CB_Regattas)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2,"")
        self.hboxlayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,934,33))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuClasses = QtGui.QMenu(self.menubar)
        self.menuClasses.setObjectName("menuClasses")

        self.menuRegattas = QtGui.QMenu(self.menubar)
        self.menuRegattas.setObjectName("menuRegattas")

        self.menuRanking = QtGui.QMenu(self.menubar)
        self.menuRanking.setObjectName("menuRanking")

        self.menuExport = QtGui.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")

        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")

        self.actionAdd_2 = QtGui.QAction(MainWindow)
        self.actionAdd_2.setObjectName("actionAdd_2")

        self.actionDelete_2 = QtGui.QAction(MainWindow)
        self.actionDelete_2.setObjectName("actionDelete_2")

        self.actionNew_2 = QtGui.QAction(MainWindow)
        self.actionNew_2.setObjectName("actionNew_2")

        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")

        self.actionDelete_3 = QtGui.QAction(MainWindow)
        self.actionDelete_3.setObjectName("actionDelete_3")

        self.actionGeneral_Ranking = QtGui.QAction(MainWindow)
        self.actionGeneral_Ranking.setObjectName("actionGeneral_Ranking")

        self.actionDetail_Ranking = QtGui.QAction(MainWindow)
        self.actionDetail_Ranking.setObjectName("actionDetail_Ranking")

        self.actionPrint_General_Ranking = QtGui.QAction(MainWindow)
        self.actionPrint_General_Ranking.setObjectName("actionPrint_General_Ranking")

        self.actionPrint_Detail_Ranking = QtGui.QAction(MainWindow)
        self.actionPrint_Detail_Ranking.setObjectName("actionPrint_Detail_Ranking")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuClasses.addAction(self.actionAdd)
        self.menuClasses.addAction(self.actionDelete)
        self.menuRegattas.addAction(self.actionAdd_2)
        self.menuRegattas.addAction(self.actionDelete_2)
        self.menuRanking.addAction(self.actionNew_2)
        self.menuRanking.addAction(self.actionEdit)
        self.menuRanking.addAction(self.actionDelete_3)
        self.menuExport.addAction(self.actionGeneral_Ranking)
        self.menuExport.addAction(self.actionDetail_Ranking)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.actionPrint_General_Ranking)
        self.menuExport.addAction(self.actionPrint_Detail_Ranking)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuClasses.menuAction())
        self.menubar.addAction(self.menuRegattas.menuAction())
        self.menubar.addAction(self.menuRanking.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Classes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Regatta", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "General Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Detail ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClasses.setTitle(QtGui.QApplication.translate("MainWindow", "Classes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRegattas.setTitle(QtGui.QApplication.translate("MainWindow", "Regattas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRanking.setTitle(QtGui.QApplication.translate("MainWindow", "Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_2.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_2.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_2.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_3.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeneral_Ranking.setText(QtGui.QApplication.translate("MainWindow", "General Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDetail_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Detail Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint_General_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Print General Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint_Detail_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Print Detail Ranking", None, QtGui.QApplication.UnicodeUTF8))

