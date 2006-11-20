# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Mon Nov 20 23:38:39 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_D_Naca(object):
    def setupUi(self, D_Naca):
        D_Naca.setObjectName("D_Naca")
        D_Naca.resize(QtCore.QSize(QtCore.QRect(0,0,774,664).size()).expandedTo(D_Naca.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(D_Naca.sizePolicy().hasHeightForWidth())
        D_Naca.setSizePolicy(sizePolicy)

        self.vboxlayout = QtGui.QVBoxLayout(D_Naca)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        spacerItem = QtGui.QSpacerItem(20,100,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.vboxlayout1.addItem(spacerItem)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.groupBox = QtGui.QGroupBox(D_Naca)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.L_ProfileList = QtGui.QListWidget(self.groupBox)
        self.L_ProfileList.setObjectName("L_ProfileList")
        self.vboxlayout3.addWidget(self.L_ProfileList)
        self.vboxlayout2.addWidget(self.groupBox)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.La_ProfileType = QtGui.QLabel(D_Naca)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.La_ProfileType.sizePolicy().hasHeightForWidth())
        self.La_ProfileType.setSizePolicy(sizePolicy)
        self.La_ProfileType.setFrameShape(QtGui.QFrame.Box)
        self.La_ProfileType.setFrameShadow(QtGui.QFrame.Raised)
        self.La_ProfileType.setObjectName("La_ProfileType")
        self.gridlayout.addWidget(self.La_ProfileType,0,1,1,1)

        self.label = QtGui.QLabel(D_Naca)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.label_3 = QtGui.QLabel(D_Naca)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)

        self.La_Radius = QtGui.QLabel(D_Naca)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.La_Radius.sizePolicy().hasHeightForWidth())
        self.La_Radius.setSizePolicy(sizePolicy)
        self.La_Radius.setFrameShape(QtGui.QFrame.Box)
        self.La_Radius.setFrameShadow(QtGui.QFrame.Raised)
        self.La_Radius.setObjectName("La_Radius")
        self.gridlayout.addWidget(self.La_Radius,1,1,1,1)
        self.vboxlayout2.addLayout(self.gridlayout)
        self.hboxlayout.addLayout(self.vboxlayout2)

        self.groupBox_2 = QtGui.QGroupBox(D_Naca)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout4.setMargin(9)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.T_CoordTable = QtGui.QTableView(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_CoordTable.sizePolicy().hasHeightForWidth())
        self.T_CoordTable.setSizePolicy(sizePolicy)
        self.T_CoordTable.setObjectName("T_CoordTable")
        self.vboxlayout4.addWidget(self.T_CoordTable)
        self.hboxlayout.addWidget(self.groupBox_2)

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setMargin(0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.groupBox_3 = QtGui.QGroupBox(D_Naca)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridlayout1.addWidget(self.lineEdit_2,3,1,1,1)

        self.CB_Scale = QtGui.QCheckBox(self.groupBox_3)
        self.CB_Scale.setObjectName("CB_Scale")
        self.gridlayout1.addWidget(self.CB_Scale,1,0,1,1)

        self.label_5 = QtGui.QLabel(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5,0,0,1,1)

        self.label_6 = QtGui.QLabel(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridlayout1.addWidget(self.label_6,2,0,1,1)

        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridlayout1.addWidget(self.lineEdit,1,1,1,1)

        self.CB_Print = QtGui.QCheckBox(self.groupBox_3)
        self.CB_Print.setObjectName("CB_Print")
        self.gridlayout1.addWidget(self.CB_Print,3,0,1,1)
        self.vboxlayout5.addWidget(self.groupBox_3)

        self.groupBox_4 = QtGui.QGroupBox(D_Naca)
        self.groupBox_4.setObjectName("groupBox_4")

        self.gridlayout2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.B_Print = QtGui.QPushButton(self.groupBox_4)
        self.B_Print.setObjectName("B_Print")
        self.gridlayout2.addWidget(self.B_Print,0,0,1,1)
        self.vboxlayout5.addWidget(self.groupBox_4)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout5.addItem(spacerItem1)
        self.hboxlayout.addLayout(self.vboxlayout5)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)

        self.cancelButton = QtGui.QPushButton(D_Naca)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(D_Naca)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),D_Naca.accept)
        QtCore.QMetaObject.connectSlotsByName(D_Naca)

    def tr(self, string):
        return QtGui.QApplication.translate("D_Naca", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, D_Naca):
        D_Naca.setWindowTitle(self.tr("PyNaca"))
        self.groupBox.setTitle(self.tr("Lista dei profili"))
        self.label.setText(self.tr("Tipo profilo"))
        self.label_3.setText(self.tr("Raggio del bordo d\'attacco"))
        self.groupBox_2.setTitle(self.tr("Coordinate delle curve del profilo"))
        self.groupBox_3.setTitle(self.tr("Opzioni"))
        self.CB_Scale.setText(self.tr("Scala"))
        self.label_5.setText(self.tr("Dimensioni corda in mm"))
        self.label_6.setText(self.tr("Unità di misura righello in mm"))
        self.CB_Print.setText(self.tr("Stampa righello"))
        self.groupBox_4.setTitle(self.tr("Azioni"))
        self.B_Print.setText(self.tr("Stampa"))
        self.cancelButton.setText(self.tr("Quit"))
