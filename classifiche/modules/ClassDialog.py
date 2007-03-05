# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/class_dialog.ui'
#
# Created: Sun Mar  4 01:09:43 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_ClassDialog(object):
    def setupUi(self, ClassDialog):
        ClassDialog.setObjectName("ClassDialog")
        ClassDialog.resize(QtCore.QSize(QtCore.QRect(0,0,196,97).size()).expandedTo(ClassDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ClassDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(16,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label = QtGui.QLabel(ClassDialog)
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)

        self.T_DialogClassValue = QtGui.QLineEdit(ClassDialog)
        self.T_DialogClassValue.setObjectName("T_DialogClassValue")
        self.vboxlayout2.addWidget(self.T_DialogClassValue)
        self.vboxlayout1.addLayout(self.vboxlayout2)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.okButton = QtGui.QPushButton(ClassDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout1.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(ClassDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout1)

        spacerItem1 = QtGui.QSpacerItem(16,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(ClassDialog)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),ClassDialog.reject)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),ClassDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ClassDialog)

    def retranslateUi(self, ClassDialog):
        ClassDialog.setWindowTitle(QtGui.QApplication.translate("ClassDialog", "Class", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ClassDialog", "Insert new class", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("ClassDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("ClassDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

