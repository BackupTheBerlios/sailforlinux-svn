# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\MainWindow.ui'
#
# Created: Tue Mar 06 17:47:54 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,625,453).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.TAB_Ranking = QtGui.QWidget()
        self.TAB_Ranking.setObjectName("TAB_Ranking")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.TAB_Ranking)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.label_2 = QtGui.QLabel(self.TAB_Ranking)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,0,0,1,1)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,0,4,1,1)

        self.L_Class = QtGui.QLabel(self.TAB_Ranking)
        self.L_Class.setObjectName("L_Class")
        self.gridlayout.addWidget(self.L_Class,0,2,1,1)

        self.CB_Regattas = QtGui.QComboBox(self.TAB_Ranking)
        self.CB_Regattas.setObjectName("CB_Regattas")
        self.gridlayout.addWidget(self.CB_Regattas,0,1,1,1)

        self.CB_Class = QtGui.QComboBox(self.TAB_Ranking)
        self.CB_Class.setObjectName("CB_Class")
        self.gridlayout.addWidget(self.CB_Class,0,3,1,1)

        self.T_DetailRanking = QtGui.QTableWidget(self.TAB_Ranking)
        self.T_DetailRanking.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.T_DetailRanking.setObjectName("T_DetailRanking")
        self.gridlayout.addWidget(self.T_DetailRanking,1,0,1,5)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.tabWidget.addTab(self.TAB_Ranking,"")

        self.TAB_Configuration = QtGui.QWidget()
        self.TAB_Configuration.setObjectName("TAB_Configuration")

        self.gridlayout1 = QtGui.QGridLayout(self.TAB_Configuration)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.groupBox_2 = QtGui.QGroupBox(self.TAB_Configuration)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.L_Regattas = QtGui.QListWidget(self.groupBox_2)
        self.L_Regattas.setObjectName("L_Regattas")
        self.vboxlayout2.addWidget(self.L_Regattas)
        self.gridlayout1.addWidget(self.groupBox_2,0,1,1,1)

        self.groupBox_3 = QtGui.QGroupBox(self.TAB_Configuration)
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridlayout2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridlayout2.addWidget(self.label,0,0,1,1)

        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridlayout2.addWidget(self.label_3,1,0,1,1)

        self.E_DNF = QtGui.QLineEdit(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.E_DNF.sizePolicy().hasHeightForWidth())
        self.E_DNF.setSizePolicy(sizePolicy)
        self.E_DNF.setMaxLength(2)
        self.E_DNF.setObjectName("E_DNF")
        self.gridlayout2.addWidget(self.E_DNF,0,1,1,1)

        self.SP_Discards = QtGui.QSpinBox(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SP_Discards.sizePolicy().hasHeightForWidth())
        self.SP_Discards.setSizePolicy(sizePolicy)
        self.SP_Discards.setMaximum(10)
        self.SP_Discards.setProperty("value",QtCore.QVariant(1))
        self.SP_Discards.setObjectName("SP_Discards")
        self.gridlayout2.addWidget(self.SP_Discards,1,1,1,1)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem1,0,2,1,1)
        self.gridlayout1.addWidget(self.groupBox_3,1,0,1,1)

        self.groupBox = QtGui.QGroupBox(self.TAB_Configuration)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.L_Classes = QtGui.QListWidget(self.groupBox)
        self.L_Classes.setObjectName("L_Classes")
        self.vboxlayout3.addWidget(self.L_Classes)
        self.gridlayout1.addWidget(self.groupBox,0,0,1,1)
        self.tabWidget.addTab(self.TAB_Configuration,"")
        self.vboxlayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,625,21))
        self.menubar.setObjectName("menubar")

        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuClasses = QtGui.QMenu(self.menubar)
        self.menuClasses.setObjectName("menuClasses")

        self.menuRegattas = QtGui.QMenu(self.menubar)
        self.menuRegattas.setObjectName("menuRegattas")

        self.menuRanking = QtGui.QMenu(self.menubar)
        self.menuRanking.setObjectName("menuRanking")
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

        self.actionAddClass = QtGui.QAction(MainWindow)
        self.actionAddClass.setObjectName("actionAddClass")

        self.actionDeleteClass = QtGui.QAction(MainWindow)
        self.actionDeleteClass.setObjectName("actionDeleteClass")

        self.actionAddRegatta = QtGui.QAction(MainWindow)
        self.actionAddRegatta.setObjectName("actionAddRegatta")

        self.actionDeleteRegatta = QtGui.QAction(MainWindow)
        self.actionDeleteRegatta.setObjectName("actionDeleteRegatta")

        self.actionNewRanking = QtGui.QAction(MainWindow)
        self.actionNewRanking.setObjectName("actionNewRanking")

        self.actionEditRanking = QtGui.QAction(MainWindow)
        self.actionEditRanking.setObjectName("actionEditRanking")

        self.actionDeleteRanking = QtGui.QAction(MainWindow)
        self.actionDeleteRanking.setObjectName("actionDeleteRanking")

        self.actionGeneral_Ranking = QtGui.QAction(MainWindow)
        self.actionGeneral_Ranking.setObjectName("actionGeneral_Ranking")

        self.actionDetail_Ranking = QtGui.QAction(MainWindow)
        self.actionDetail_Ranking.setObjectName("actionDetail_Ranking")

        self.actionPrint_General_Ranking = QtGui.QAction(MainWindow)
        self.actionPrint_General_Ranking.setObjectName("actionPrint_General_Ranking")

        self.actionPrint_Detail_Ranking = QtGui.QAction(MainWindow)
        self.actionPrint_Detail_Ranking.setObjectName("actionPrint_Detail_Ranking")

        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")

        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.menuData.addAction(self.actionExport)
        self.menuData.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuClasses.addAction(self.actionAddClass)
        self.menuClasses.addAction(self.actionDeleteClass)
        self.menuRegattas.addAction(self.actionAddRegatta)
        self.menuRegattas.addAction(self.actionDeleteRegatta)
        self.menuRanking.addAction(self.actionNewRanking)
        self.menuRanking.addAction(self.actionEditRanking)
        self.menuRanking.addAction(self.actionDeleteRanking)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuClasses.menuAction())
        self.menubar.addAction(self.menuRegattas.menuAction())
        self.menubar.addAction(self.menuRanking.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QtRanking", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Regatta", None, QtGui.QApplication.UnicodeUTF8))
        self.L_Class.setText(QtGui.QApplication.translate("MainWindow", "Class", None, QtGui.QApplication.UnicodeUTF8))
        self.T_DetailRanking.clear()
        self.T_DetailRanking.setColumnCount(0)
        self.T_DetailRanking.setRowCount(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_Ranking), QtGui.QApplication.translate("MainWindow", "Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Regattas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "DNF value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Discards", None, QtGui.QApplication.UnicodeUTF8))
        self.E_DNF.setText(QtGui.QApplication.translate("MainWindow", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Classes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_Configuration), QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClasses.setTitle(QtGui.QApplication.translate("MainWindow", "Classes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRegattas.setTitle(QtGui.QApplication.translate("MainWindow", "Regattas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRanking.setTitle(QtGui.QApplication.translate("MainWindow", "Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddClass.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteClass.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddRegatta.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteRegatta.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewRanking.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditRanking.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteRanking.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeneral_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDetail_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint_General_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Print General Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint_Detail_Ranking.setText(QtGui.QApplication.translate("MainWindow", "Print Detail Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))

