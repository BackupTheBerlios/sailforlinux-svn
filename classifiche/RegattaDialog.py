# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Mon Sep 11 17:27:21 2006
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_RegattaDialog(object):
    def setupUi(self, RegattaDialog):
        RegattaDialog.setObjectName("RegattaDialog")
        RegattaDialog.resize(QtCore.QSize(QtCore.QRect(0,0,216,325).size()).expandedTo(RegattaDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(RegattaDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label = QtGui.QLabel(RegattaDialog)
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)

        self.T_DialogRegattaValue = QtGui.QLineEdit(RegattaDialog)
        self.T_DialogRegattaValue.setObjectName("T_DialogRegattaValue")
        self.vboxlayout2.addWidget(self.T_DialogRegattaValue)

        self.label_3 = QtGui.QLabel(RegattaDialog)
        self.label_3.setObjectName("label_3")
        self.vboxlayout2.addWidget(self.label_3)

        self.T_DialogClassValue = QtGui.QLineEdit(RegattaDialog)
        self.T_DialogClassValue.setObjectName("T_DialogClassValue")
        self.vboxlayout2.addWidget(self.T_DialogClassValue)

        self.label_2 = QtGui.QLabel(RegattaDialog)
        self.label_2.setObjectName("label_2")
        self.vboxlayout2.addWidget(self.label_2)

        self.T_DialogSkipperValue = QtGui.QLineEdit(RegattaDialog)
        self.T_DialogSkipperValue.setObjectName("T_DialogSkipperValue")
        self.vboxlayout2.addWidget(self.T_DialogSkipperValue)

        self.labelrace = QtGui.QLabel(RegattaDialog)
        self.labelrace.setObjectName("labelrace")
        self.vboxlayout2.addWidget(self.labelrace)

        self.T_DialogRaceValue = QtGui.QLineEdit(RegattaDialog)
        self.T_DialogRaceValue.setObjectName("T_DialogRaceValue")
        self.vboxlayout2.addWidget(self.T_DialogRaceValue)
        self.vboxlayout1.addLayout(self.vboxlayout2)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.okButton = QtGui.QPushButton(RegattaDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout1.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(RegattaDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout1)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(RegattaDialog)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),RegattaDialog.accept)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),RegattaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RegattaDialog)

    def tr(self, string):
        return QtGui.QApplication.translate("RegattaDialog", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, RegattaDialog):
        RegattaDialog.setWindowTitle(self.tr("Regatta"))
        self.label.setText(self.tr("Insert new regatta"))
        self.label_3.setText(self.tr("Class"))
        self.label_2.setText(self.tr("Number of Skipper"))
        self.labelrace.setText(self.tr("Number of Race"))
        self.okButton.setText(self.tr("OK"))
        self.cancelButton.setText(self.tr("Cancel"))
