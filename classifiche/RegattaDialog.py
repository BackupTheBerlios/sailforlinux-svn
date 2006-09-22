# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Sat Sep 23 00:32:56 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_RegattaDialog(object):
    def setupUi(self, RegattaDialog):
        RegattaDialog.setObjectName("RegattaDialog")
        RegattaDialog.resize(QtCore.QSize(QtCore.QRect(0,0,286,103).size()).expandedTo(RegattaDialog.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegattaDialog.sizePolicy().hasHeightForWidth())
        RegattaDialog.setSizePolicy(sizePolicy)

        self.gridlayout = QtGui.QGridLayout(RegattaDialog)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.label_3 = QtGui.QLabel(RegattaDialog)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)

        self.T_DialogRegattaValue = QtGui.QLineEdit(RegattaDialog)
        self.T_DialogRegattaValue.setObjectName("T_DialogRegattaValue")
        self.gridlayout.addWidget(self.T_DialogRegattaValue,0,1,1,1)

        self.label = QtGui.QLabel(RegattaDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.C_RegattaClass = QtGui.QComboBox(RegattaDialog)
        self.C_RegattaClass.setObjectName("C_RegattaClass")
        self.gridlayout.addWidget(self.C_RegattaClass,1,1,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.okButton = QtGui.QPushButton(RegattaDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(RegattaDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout,2,0,1,2)

        self.retranslateUi(RegattaDialog)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),RegattaDialog.accept)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),RegattaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RegattaDialog)

    def tr(self, string):
        return QtGui.QApplication.translate("RegattaDialog", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, RegattaDialog):
        RegattaDialog.setWindowTitle(self.tr("Regatta"))
        self.label_3.setText(self.tr("Class"))
        self.label.setText(self.tr("Insert new regatta"))
        self.okButton.setText(self.tr("OK"))
        self.cancelButton.setText(self.tr("Cancel"))
