# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Thu Aug 03 16:51:32 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_DMainWin(object):
    def setupUi(self, DMainWin):
        DMainWin.setObjectName("DMainWin")
        DMainWin.resize(QtCore.QSize(QtCore.QRect(0,0,900,706).size()).expandedTo(DMainWin.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(DMainWin)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.groupBox = QtGui.QGroupBox(DMainWin)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.L_Classi = QtGui.QListWidget(self.groupBox)
        self.L_Classi.setViewMode(QtGui.QListView.ListMode)
        self.L_Classi.setObjectName("L_Classi")
        self.vboxlayout2.addWidget(self.L_Classi)

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
        self.vboxlayout2.addLayout(self.hboxlayout2)
        self.vboxlayout1.addWidget(self.groupBox)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.hboxlayout1.addLayout(self.vboxlayout1)

        spacerItem1 = QtGui.QSpacerItem(20,327,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)

        self.groupBox_3 = QtGui.QGroupBox(DMainWin)
        self.groupBox_3.setObjectName("groupBox_3")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.T_GeneralRanking = QtGui.QTableWidget(self.groupBox_3)
        self.T_GeneralRanking.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.T_GeneralRanking.setTabKeyNavigation(False)
        self.T_GeneralRanking.setAlternatingRowColors(True)
        self.T_GeneralRanking.setObjectName("T_GeneralRanking")
        self.vboxlayout3.addWidget(self.T_GeneralRanking)
        self.hboxlayout1.addWidget(self.groupBox_3)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.groupBox_2 = QtGui.QGroupBox(DMainWin)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
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

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.B_AddRegatta = QtGui.QPushButton(self.groupBox_2)
        self.B_AddRegatta.setObjectName("B_AddRegatta")
        self.hboxlayout4.addWidget(self.B_AddRegatta)

        self.B_CancelRegatta = QtGui.QPushButton(self.groupBox_2)
        self.B_CancelRegatta.setObjectName("B_CancelRegatta")
        self.hboxlayout4.addWidget(self.B_CancelRegatta)
        self.vboxlayout5.addLayout(self.hboxlayout4)
        self.vboxlayout4.addWidget(self.groupBox_2)

        spacerItem2 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout4.addItem(spacerItem2)
        self.hboxlayout3.addLayout(self.vboxlayout4)

        spacerItem3 = QtGui.QSpacerItem(20,326,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem3)

        self.groupBox_4 = QtGui.QGroupBox(DMainWin)
        self.groupBox_4.setObjectName("groupBox_4")

        self.vboxlayout6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout6.setMargin(9)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.T_DetailRanking = QtGui.QTableWidget(self.groupBox_4)
        self.T_DetailRanking.setAlternatingRowColors(True)
        self.T_DetailRanking.setObjectName("T_DetailRanking")
        self.hboxlayout5.addWidget(self.T_DetailRanking)

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setMargin(0)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.B_AddSkipper = QtGui.QPushButton(self.groupBox_4)
        self.B_AddSkipper.setObjectName("B_AddSkipper")
        self.vboxlayout7.addWidget(self.B_AddSkipper)

        self.B_DeleteSkipper = QtGui.QPushButton(self.groupBox_4)
        self.B_DeleteSkipper.setObjectName("B_DeleteSkipper")
        self.vboxlayout7.addWidget(self.B_DeleteSkipper)

        self.B_AddRace = QtGui.QPushButton(self.groupBox_4)
        self.B_AddRace.setObjectName("B_AddRace")
        self.vboxlayout7.addWidget(self.B_AddRace)

        self.B_DeleteRace = QtGui.QPushButton(self.groupBox_4)
        self.B_DeleteRace.setObjectName("B_DeleteRace")
        self.vboxlayout7.addWidget(self.B_DeleteRace)

        self.B_CalcRanking = QtGui.QPushButton(self.groupBox_4)
        self.B_CalcRanking.setObjectName("B_CalcRanking")
        self.vboxlayout7.addWidget(self.B_CalcRanking)

        self.B_Legenda = QtGui.QPushButton(self.groupBox_4)
        self.B_Legenda.setObjectName("B_Legenda")
        self.vboxlayout7.addWidget(self.B_Legenda)

        spacerItem4 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout7.addItem(spacerItem4)
        self.hboxlayout5.addLayout(self.vboxlayout7)
        self.vboxlayout6.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.B_SaveData = QtGui.QPushButton(self.groupBox_4)
        self.B_SaveData.setObjectName("B_SaveData")
        self.hboxlayout6.addWidget(self.B_SaveData)

        self.B_ExportPDF = QtGui.QPushButton(self.groupBox_4)
        self.B_ExportPDF.setObjectName("B_ExportPDF")
        self.hboxlayout6.addWidget(self.B_ExportPDF)

        self.B_ExportHTML = QtGui.QPushButton(self.groupBox_4)
        self.B_ExportHTML.setObjectName("B_ExportHTML")
        self.hboxlayout6.addWidget(self.B_ExportHTML)
        self.vboxlayout6.addLayout(self.hboxlayout6)
        self.hboxlayout3.addWidget(self.groupBox_4)
        self.vboxlayout.addLayout(self.hboxlayout3)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setMargin(0)
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.vboxlayout9 = QtGui.QVBoxLayout()
        self.vboxlayout9.setMargin(0)
        self.vboxlayout9.setSpacing(6)
        self.vboxlayout9.setObjectName("vboxlayout9")

        spacerItem5 = QtGui.QSpacerItem(20,31,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.vboxlayout9.addItem(spacerItem5)

        self.okButton = QtGui.QPushButton(DMainWin)
        self.okButton.setObjectName("okButton")
        self.vboxlayout9.addWidget(self.okButton)
        self.vboxlayout8.addLayout(self.vboxlayout9)

        spacerItem6 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout8.addItem(spacerItem6)
        self.hboxlayout.addLayout(self.vboxlayout8)

        self.retranslateUi(DMainWin)
        self.L_Classi.setCurrentRow(-1)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),DMainWin.accept)
        QtCore.QMetaObject.connectSlotsByName(DMainWin)

    def tr(self, string):
        return QtGui.QApplication.translate("DMainWin", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, DMainWin):
        DMainWin.setWindowTitle(self.tr("QtRank"))
        self.groupBox.setTitle(self.tr("Classes"))
        self.B_AddClass.setText(self.tr("Add"))
        self.B_CancelClass.setText(self.tr("Cancel"))
        self.groupBox_3.setTitle(self.tr("General ranking"))
        self.T_GeneralRanking.setColumnCount(1)
        self.T_GeneralRanking.clear()
        self.T_GeneralRanking.setColumnCount(1)
        self.T_GeneralRanking.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(self.tr("Skipper"))
        self.T_GeneralRanking.setHorizontalHeaderItem(0,headerItem)
        self.groupBox_2.setTitle(self.tr("Regattas"))
        self.B_AddRegatta.setText(self.tr("Add"))
        self.B_CancelRegatta.setText(self.tr("Cancel"))
        self.groupBox_4.setTitle(self.tr("Detail Ranking"))
        self.T_DetailRanking.setColumnCount(1)
        self.T_DetailRanking.clear()
        self.T_DetailRanking.setColumnCount(1)
        self.T_DetailRanking.setRowCount(0)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(self.tr("Skipper"))
        self.T_DetailRanking.setHorizontalHeaderItem(0,headerItem1)
        self.B_AddSkipper.setText(self.tr("Add Skipper"))
        self.B_DeleteSkipper.setText(self.tr("Delete Skipper"))
        self.B_AddRace.setText(self.tr("Add Race"))
        self.B_DeleteRace.setText(self.tr("Delete Race"))
        self.B_CalcRanking.setText(self.tr("Update Rank"))
        self.B_Legenda.setText(self.tr("Legenda"))
        self.B_SaveData.setText(self.tr("Save Data"))
        self.B_ExportPDF.setText(self.tr("Export as PDF"))
        self.B_ExportHTML.setText(self.tr("Export as HTML"))
        self.okButton.setText(self.tr("Quit"))
