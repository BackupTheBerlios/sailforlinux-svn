# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main_win.ui'
#
# Created: Sun Mar  4 01:09:42 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_DMainWin(object):
    def setupUi(self, DMainWin):
        DMainWin.setObjectName("DMainWin")
        DMainWin.resize(QtCore.QSize(QtCore.QRect(0,0,914,813).size()).expandedTo(DMainWin.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(DMainWin)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.groupBox = QtGui.QGroupBox(DMainWin)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.L_Classi = QtGui.QListWidget(self.groupBox)
        self.L_Classi.setViewMode(QtGui.QListView.ListMode)
        self.L_Classi.setObjectName("L_Classi")
        self.vboxlayout3.addWidget(self.L_Classi)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.B_AddClass = QtGui.QPushButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_AddClass.sizePolicy().hasHeightForWidth())
        self.B_AddClass.setSizePolicy(sizePolicy)
        self.B_AddClass.setObjectName("B_AddClass")
        self.hboxlayout2.addWidget(self.B_AddClass)

        self.B_CancelClass = QtGui.QPushButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_CancelClass.sizePolicy().hasHeightForWidth())
        self.B_CancelClass.setSizePolicy(sizePolicy)
        self.B_CancelClass.setObjectName("B_CancelClass")
        self.hboxlayout2.addWidget(self.B_CancelClass)
        self.vboxlayout3.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem)

        self.B_ExportClassRank = QtGui.QPushButton(self.groupBox)
        self.B_ExportClassRank.setObjectName("B_ExportClassRank")
        self.hboxlayout3.addWidget(self.B_ExportClassRank)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem1)
        self.vboxlayout3.addLayout(self.hboxlayout3)
        self.vboxlayout2.addWidget(self.groupBox)

        spacerItem2 = QtGui.QSpacerItem(276,75,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem2)
        self.hboxlayout1.addLayout(self.vboxlayout2)

        spacerItem3 = QtGui.QSpacerItem(20,342,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem3)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.groupBox_2 = QtGui.QGroupBox(DMainWin)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout5.setMargin(9)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.L_Regattas = QtGui.QListWidget(self.groupBox_2)
        self.L_Regattas.setObjectName("L_Regattas")
        self.vboxlayout5.addWidget(self.L_Regattas)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.B_AddRegatta = QtGui.QPushButton(self.groupBox_2)
        self.B_AddRegatta.setObjectName("B_AddRegatta")
        self.hboxlayout5.addWidget(self.B_AddRegatta)

        self.B_CancelRegatta = QtGui.QPushButton(self.groupBox_2)
        self.B_CancelRegatta.setObjectName("B_CancelRegatta")
        self.hboxlayout5.addWidget(self.B_CancelRegatta)
        self.vboxlayout5.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem4)

        self.B_SaveRegattaRank = QtGui.QPushButton(self.groupBox_2)
        self.B_SaveRegattaRank.setObjectName("B_SaveRegattaRank")
        self.hboxlayout6.addWidget(self.B_SaveRegattaRank)

        self.B_ExportRegattaRank = QtGui.QPushButton(self.groupBox_2)
        self.B_ExportRegattaRank.setObjectName("B_ExportRegattaRank")
        self.hboxlayout6.addWidget(self.B_ExportRegattaRank)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem5)
        self.vboxlayout5.addLayout(self.hboxlayout6)
        self.vboxlayout4.addWidget(self.groupBox_2)
        self.hboxlayout4.addLayout(self.vboxlayout4)

        spacerItem6 = QtGui.QSpacerItem(20,341,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem6)
        self.vboxlayout1.addLayout(self.hboxlayout4)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setMargin(0)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.groupBox_3 = QtGui.QGroupBox(DMainWin)
        self.groupBox_3.setObjectName("groupBox_3")

        self.vboxlayout7 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout7.setMargin(9)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.T_GeneralRanking = QtGui.QTableWidget(self.groupBox_3)
        self.T_GeneralRanking.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.T_GeneralRanking.setTabKeyNavigation(False)
        self.T_GeneralRanking.setAlternatingRowColors(True)
        self.T_GeneralRanking.setObjectName("T_GeneralRanking")
        self.vboxlayout7.addWidget(self.T_GeneralRanking)
        self.vboxlayout6.addWidget(self.groupBox_3)

        self.groupBox_4 = QtGui.QGroupBox(DMainWin)
        self.groupBox_4.setObjectName("groupBox_4")

        self.vboxlayout8 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout8.setMargin(9)
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setMargin(0)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.T_DetailRanking = QtGui.QTableWidget(self.groupBox_4)
        self.T_DetailRanking.setAlternatingRowColors(True)
        self.T_DetailRanking.setObjectName("T_DetailRanking")
        self.hboxlayout7.addWidget(self.T_DetailRanking)

        self.vboxlayout9 = QtGui.QVBoxLayout()
        self.vboxlayout9.setMargin(0)
        self.vboxlayout9.setSpacing(6)
        self.vboxlayout9.setObjectName("vboxlayout9")

        self.B_AddSkipper = QtGui.QPushButton(self.groupBox_4)
        self.B_AddSkipper.setObjectName("B_AddSkipper")
        self.vboxlayout9.addWidget(self.B_AddSkipper)

        self.B_DeleteSkipper = QtGui.QPushButton(self.groupBox_4)
        self.B_DeleteSkipper.setObjectName("B_DeleteSkipper")
        self.vboxlayout9.addWidget(self.B_DeleteSkipper)

        self.B_AddRace = QtGui.QPushButton(self.groupBox_4)
        self.B_AddRace.setObjectName("B_AddRace")
        self.vboxlayout9.addWidget(self.B_AddRace)

        self.B_DeleteRace = QtGui.QPushButton(self.groupBox_4)
        self.B_DeleteRace.setObjectName("B_DeleteRace")
        self.vboxlayout9.addWidget(self.B_DeleteRace)

        self.B_CalcRanking = QtGui.QPushButton(self.groupBox_4)
        self.B_CalcRanking.setObjectName("B_CalcRanking")
        self.vboxlayout9.addWidget(self.B_CalcRanking)

        self.B_Legenda = QtGui.QPushButton(self.groupBox_4)
        self.B_Legenda.setObjectName("B_Legenda")
        self.vboxlayout9.addWidget(self.B_Legenda)

        spacerItem7 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout9.addItem(spacerItem7)
        self.hboxlayout7.addLayout(self.vboxlayout9)
        self.vboxlayout8.addLayout(self.hboxlayout7)
        self.vboxlayout6.addWidget(self.groupBox_4)
        self.hboxlayout.addLayout(self.vboxlayout6)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setSpacing(6)
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem8)

        self.B_Quit = QtGui.QPushButton(DMainWin)
        self.B_Quit.setObjectName("B_Quit")
        self.hboxlayout8.addWidget(self.B_Quit)
        self.vboxlayout.addLayout(self.hboxlayout8)

        self.retranslateUi(DMainWin)
        self.L_Classi.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(DMainWin)

    def retranslateUi(self, DMainWin):
        DMainWin.setWindowTitle(QtGui.QApplication.translate("DMainWin", "QtRank", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DMainWin", "Classes", None, QtGui.QApplication.UnicodeUTF8))
        self.B_AddClass.setText(QtGui.QApplication.translate("DMainWin", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.B_CancelClass.setText(QtGui.QApplication.translate("DMainWin", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.B_ExportClassRank.setText(QtGui.QApplication.translate("DMainWin", "Export Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DMainWin", "Regattas", None, QtGui.QApplication.UnicodeUTF8))
        self.B_AddRegatta.setText(QtGui.QApplication.translate("DMainWin", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.B_CancelRegatta.setText(QtGui.QApplication.translate("DMainWin", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.B_SaveRegattaRank.setText(QtGui.QApplication.translate("DMainWin", "Save Data", None, QtGui.QApplication.UnicodeUTF8))
        self.B_ExportRegattaRank.setText(QtGui.QApplication.translate("DMainWin", "Export Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("DMainWin", "General ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.T_GeneralRanking.setColumnCount(1)
        self.T_GeneralRanking.clear()
        self.T_GeneralRanking.setColumnCount(1)
        self.T_GeneralRanking.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("DMainWin", "Skipper", None, QtGui.QApplication.UnicodeUTF8))
        self.T_GeneralRanking.setHorizontalHeaderItem(0,headerItem)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("DMainWin", "Detail Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.T_DetailRanking.setColumnCount(1)
        self.T_DetailRanking.clear()
        self.T_DetailRanking.setColumnCount(1)
        self.T_DetailRanking.setRowCount(0)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("DMainWin", "Skipper", None, QtGui.QApplication.UnicodeUTF8))
        self.T_DetailRanking.setHorizontalHeaderItem(0,headerItem1)
        self.B_AddSkipper.setText(QtGui.QApplication.translate("DMainWin", "Add Skipper", None, QtGui.QApplication.UnicodeUTF8))
        self.B_DeleteSkipper.setText(QtGui.QApplication.translate("DMainWin", "Delete Skipper", None, QtGui.QApplication.UnicodeUTF8))
        self.B_AddRace.setText(QtGui.QApplication.translate("DMainWin", "Add Race", None, QtGui.QApplication.UnicodeUTF8))
        self.B_DeleteRace.setText(QtGui.QApplication.translate("DMainWin", "Delete Race", None, QtGui.QApplication.UnicodeUTF8))
        self.B_CalcRanking.setText(QtGui.QApplication.translate("DMainWin", "Update Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.B_Legenda.setText(QtGui.QApplication.translate("DMainWin", "Legenda", None, QtGui.QApplication.UnicodeUTF8))
        self.B_Quit.setText(QtGui.QApplication.translate("DMainWin", "Quit", None, QtGui.QApplication.UnicodeUTF8))

