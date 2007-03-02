# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/regatta_dialog.ui'
#
# Created: Fri Mar  2 23:43:09 2007
#      by: PyQt4 UI code generator 4.1.1
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

    def retranslateUi(self, RegattaDialog):
        RegattaDialog.setWindowTitle(QtGui.QApplication.translate("RegattaDialog", "Regatta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RegattaDialog", "Class", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RegattaDialog", "Insert new regatta", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("RegattaDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("RegattaDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

