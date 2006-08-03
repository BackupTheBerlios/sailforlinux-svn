# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Mon Jul 24 21:56:59 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,200,97).size()).expandedTo(Dialog.minimumSizeHint()))

        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0,10,191,79))
        self.widget.setObjectName("widget")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)

        self.T_DialogValue = QtGui.QLineEdit(self.widget)
        self.T_DialogValue.setObjectName("T_DialogValue")
        self.vboxlayout1.addWidget(self.T_DialogValue)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.okButton = QtGui.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.hboxlayout1.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),Dialog.accept)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def tr(self, string):
        return QtGui.QApplication.translate("Dialog", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(self.tr("Dialog"))
        self.label.setText(self.tr("Enter"))
        self.okButton.setText(self.tr("OK"))
        self.cancelButton.setText(self.tr("Cancel"))
