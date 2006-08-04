# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Fri Aug 04 17:44:39 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_D_MainWin(object):
    def setupUi(self, D_MainWin):
        D_MainWin.setObjectName("D_MainWin")
        D_MainWin.resize(QtCore.QSize(QtCore.QRect(0,0,718,578).size()).expandedTo(D_MainWin.minimumSizeHint()))

        font = QtGui.QFont(D_MainWin.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        D_MainWin.setFont(font)

        self.vboxlayout = QtGui.QVBoxLayout(D_MainWin)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.groupBox = QtGui.QGroupBox(D_MainWin)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.T_SkipperList = QtGui.QTableWidget(self.groupBox)
        self.T_SkipperList.setObjectName("T_SkipperList")
        self.vboxlayout1.addWidget(self.T_SkipperList)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.T_SkipperName = QtGui.QLineEdit(self.groupBox)
        self.T_SkipperName.setObjectName("T_SkipperName")
        self.hboxlayout1.addWidget(self.T_SkipperName)

        self.B_AddSkipper = QtGui.QPushButton(self.groupBox)
        self.B_AddSkipper.setObjectName("B_AddSkipper")
        self.hboxlayout1.addWidget(self.B_AddSkipper)

        self.B_DelSkipper = QtGui.QPushButton(self.groupBox)
        self.B_DelSkipper.setObjectName("B_DelSkipper")
        self.hboxlayout1.addWidget(self.B_DelSkipper)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.B_Generate = QtGui.QPushButton(self.groupBox)
        self.B_Generate.setObjectName("B_Generate")
        self.hboxlayout2.addWidget(self.B_Generate)

        self.B_ClearSkipper = QtGui.QPushButton(self.groupBox)
        self.B_ClearSkipper.setObjectName("B_ClearSkipper")
        self.hboxlayout2.addWidget(self.B_ClearSkipper)

        spacerItem = QtGui.QSpacerItem(40,26,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.hboxlayout.addWidget(self.groupBox)

        self.groupBox_2 = QtGui.QGroupBox(D_MainWin)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName("groupBox_3")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.R_Live = QtGui.QRadioButton(self.groupBox_3)
        self.R_Live.setObjectName("R_Live")
        self.vboxlayout3.addWidget(self.R_Live)

        self.R_OffLine = QtGui.QRadioButton(self.groupBox_3)
        self.R_OffLine.setChecked(True)
        self.R_OffLine.setObjectName("R_OffLine")
        self.vboxlayout3.addWidget(self.R_OffLine)
        self.vboxlayout2.addWidget(self.groupBox_3)

        self.T_MatchRaceList = QtGui.QTableWidget(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_MatchRaceList.sizePolicy().hasHeightForWidth())
        self.T_MatchRaceList.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.T_MatchRaceList.font())
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.T_MatchRaceList.setFont(font)
        self.T_MatchRaceList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.T_MatchRaceList.setObjectName("T_MatchRaceList")
        self.vboxlayout2.addWidget(self.T_MatchRaceList)

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.B_ClearMatchRace = QtGui.QPushButton(self.groupBox_2)
        self.B_ClearMatchRace.setObjectName("B_ClearMatchRace")
        self.hboxlayout3.addWidget(self.B_ClearMatchRace)

        self.B_Ranking = QtGui.QPushButton(self.groupBox_2)
        self.B_Ranking.setObjectName("B_Ranking")
        self.hboxlayout3.addWidget(self.B_Ranking)
        self.vboxlayout4.addLayout(self.hboxlayout3)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.E_FileName = QtGui.QLineEdit(self.groupBox_2)
        self.E_FileName.setObjectName("E_FileName")
        self.hboxlayout4.addWidget(self.E_FileName)

        self.B_Save = QtGui.QPushButton(self.groupBox_2)
        self.B_Save.setObjectName("B_Save")
        self.hboxlayout4.addWidget(self.B_Save)
        self.vboxlayout4.addLayout(self.hboxlayout4)
        self.vboxlayout2.addLayout(self.vboxlayout4)
        self.hboxlayout.addWidget(self.groupBox_2)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem1 = QtGui.QSpacerItem(300,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem1)

        self.okButton = QtGui.QPushButton(D_MainWin)
        self.okButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.okButton.setObjectName("okButton")
        self.hboxlayout5.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout5)

        self.retranslateUi(D_MainWin)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),D_MainWin.accept)
        QtCore.QMetaObject.connectSlotsByName(D_MainWin)
        D_MainWin.setTabOrder(self.T_SkipperName,self.B_AddSkipper)
        D_MainWin.setTabOrder(self.B_AddSkipper,self.B_Generate)
        D_MainWin.setTabOrder(self.B_Generate,self.B_Save)
        D_MainWin.setTabOrder(self.B_Save,self.T_MatchRaceList)
        D_MainWin.setTabOrder(self.T_MatchRaceList,self.okButton)

    def tr(self, string):
        return QtGui.QApplication.translate("D_MainWin", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, D_MainWin):
        D_MainWin.setWindowTitle(self.tr("Dialog"))
        self.groupBox.setTitle(self.tr("Skipper"))
        self.T_SkipperList.clear()
        self.T_SkipperList.setColumnCount(2)
        self.T_SkipperList.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(self.tr("Skipper"))
        self.T_SkipperList.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(self.tr("Rank"))
        self.T_SkipperList.setHorizontalHeaderItem(1,headerItem1)
        self.B_AddSkipper.setText(self.tr("Add skipper"))
        self.B_DelSkipper.setText(self.tr("Delete skipper"))
        self.B_Generate.setText(self.tr("&Generate"))
        self.B_Generate.setShortcut(self.tr("Ctrl+G"))
        self.B_ClearSkipper.setText(self.tr("Clear"))
        self.groupBox_2.setTitle(self.tr("Match Race"))
        self.groupBox_3.setTitle(self.tr("Options"))
        self.R_Live.setText(self.tr("Live"))
        self.R_OffLine.setText(self.tr("OffLine"))
        self.T_MatchRaceList.setColumnCount(3)
        self.T_MatchRaceList.clear()
        self.T_MatchRaceList.setColumnCount(3)
        self.T_MatchRaceList.setRowCount(0)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(self.tr("Skipper A"))
        self.T_MatchRaceList.setHorizontalHeaderItem(0,headerItem2)

        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(self.tr("Skipper B"))
        self.T_MatchRaceList.setHorizontalHeaderItem(1,headerItem3)

        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(self.tr("Winner"))
        self.T_MatchRaceList.setHorizontalHeaderItem(2,headerItem4)
        self.B_ClearMatchRace.setText(self.tr("C&lear"))
        self.B_ClearMatchRace.setShortcut(self.tr("Ctrl+L"))
        self.B_Ranking.setText(self.tr("Ranking"))
        self.B_Save.setText(self.tr("&Save"))
        self.B_Save.setShortcut(self.tr("Ctrl+S"))
        self.okButton.setText(self.tr("&Quit"))
        self.okButton.setShortcut(self.tr("Ctrl+Q"))
