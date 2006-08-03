# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Sun Jul 16 23:14:59 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_D_MainWin(object):
    def setupUi(self, D_MainWin):
        D_MainWin.setObjectName("D_MainWin")
        D_MainWin.resize(QtCore.QSize(QtCore.QRect(0,0,991,715).size()).expandedTo(D_MainWin.minimumSizeHint()))

        font = QtGui.QFont(D_MainWin.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        D_MainWin.setFont(font)

        self.widget = QtGui.QWidget(D_MainWin)
        self.widget.setGeometry(QtCore.QRect(10,10,971,691))
        self.widget.setObjectName("widget")

        self.vboxlayout = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.L_SkipperList = QtGui.QListWidget(self.groupBox)
        self.L_SkipperList.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape(0)))
        self.L_SkipperList.setObjectName("L_SkipperList")
        self.vboxlayout1.addWidget(self.L_SkipperList)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.T_SkipperName = QtGui.QLineEdit(self.groupBox)
        self.T_SkipperName.setObjectName("T_SkipperName")
        self.vboxlayout2.addWidget(self.T_SkipperName)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.B_AddSkipper = QtGui.QPushButton(self.groupBox)
        self.B_AddSkipper.setObjectName("B_AddSkipper")
        self.hboxlayout1.addWidget(self.B_AddSkipper)

        self.B_Generate = QtGui.QPushButton(self.groupBox)
        self.B_Generate.setObjectName("B_Generate")
        self.hboxlayout1.addWidget(self.B_Generate)

        self.b_ClearSkipper = QtGui.QPushButton(self.groupBox)
        self.b_ClearSkipper.setObjectName("b_ClearSkipper")
        self.hboxlayout1.addWidget(self.b_ClearSkipper)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        self.vboxlayout1.addLayout(self.vboxlayout2)
        self.hboxlayout.addWidget(self.groupBox)

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.groupBox_3 = QtGui.QGroupBox(self.widget)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName("groupBox_3")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout4.setMargin(9)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.R_Live = QtGui.QRadioButton(self.groupBox_3)
        self.R_Live.setObjectName("R_Live")
        self.vboxlayout4.addWidget(self.R_Live)

        self.R_OffLine = QtGui.QRadioButton(self.groupBox_3)
        self.R_OffLine.setChecked(True)
        self.R_OffLine.setObjectName("R_OffLine")
        self.vboxlayout4.addWidget(self.R_OffLine)
        self.vboxlayout3.addWidget(self.groupBox_3)

        spacerItem2 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem2)
        self.hboxlayout.addLayout(self.vboxlayout3)

        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout5.setMargin(9)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

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
        self.vboxlayout5.addWidget(self.T_MatchRaceList)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem3)

        self.b_ClearMatchRace = QtGui.QPushButton(self.groupBox_2)
        self.b_ClearMatchRace.setObjectName("b_ClearMatchRace")
        self.hboxlayout2.addWidget(self.b_ClearMatchRace)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem4)
        self.vboxlayout5.addLayout(self.hboxlayout2)
        self.hboxlayout.addWidget(self.groupBox_2)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem5 = QtGui.QSpacerItem(131,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem5)

        self.B_Save = QtGui.QPushButton(self.widget)
        self.B_Save.setObjectName("B_Save")
        self.hboxlayout3.addWidget(self.B_Save)

        self.okButton = QtGui.QPushButton(self.widget)
        self.okButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.okButton.setObjectName("okButton")
        self.hboxlayout3.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout3)

        self.retranslateUi(D_MainWin)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),D_MainWin.accept)
        QtCore.QObject.connect(self.b_ClearSkipper,QtCore.SIGNAL("clicked()"),self.L_SkipperList.clear)
        QtCore.QMetaObject.connectSlotsByName(D_MainWin)
        D_MainWin.setTabOrder(self.T_SkipperName,self.B_AddSkipper)
        D_MainWin.setTabOrder(self.B_AddSkipper,self.L_SkipperList)
        D_MainWin.setTabOrder(self.L_SkipperList,self.B_Generate)
        D_MainWin.setTabOrder(self.B_Generate,self.B_Save)
        D_MainWin.setTabOrder(self.B_Save,self.T_MatchRaceList)
        D_MainWin.setTabOrder(self.T_MatchRaceList,self.okButton)

    def tr(self, string):
        return QtGui.QApplication.translate("D_MainWin", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, D_MainWin):
        D_MainWin.setWindowTitle(self.tr("Dialog"))
        self.groupBox.setTitle(self.tr("Skipper"))
        self.B_AddSkipper.setText(self.tr("Add"))
        self.B_Generate.setText(self.tr("&Generate"))
        self.B_Generate.setShortcut(self.tr("Ctrl+G"))
        self.b_ClearSkipper.setText(self.tr("Clear"))
        self.groupBox_3.setTitle(self.tr("Options"))
        self.R_Live.setText(self.tr("Live"))
        self.R_OffLine.setText(self.tr("OffLine"))
        self.groupBox_2.setTitle(self.tr("Match Race"))
        self.T_MatchRaceList.setColumnCount(2)
        self.T_MatchRaceList.clear()
        self.T_MatchRaceList.setColumnCount(2)
        self.T_MatchRaceList.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(self.tr("Skipper A"))
        self.T_MatchRaceList.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(self.tr("Skipper B"))
        self.T_MatchRaceList.setHorizontalHeaderItem(1,headerItem1)
        self.b_ClearMatchRace.setText(self.tr("C&lear"))
        self.b_ClearMatchRace.setShortcut(self.tr("Ctrl+L"))
        self.B_Save.setText(self.tr("&Save"))
        self.B_Save.setShortcut(self.tr("Ctrl+S"))
        self.okButton.setText(self.tr("&Quit"))
        self.okButton.setShortcut(self.tr("Ctrl+Q"))
