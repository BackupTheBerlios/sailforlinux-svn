# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/legenda_dialog.ui'
#
# Created: Sun Mar  4 01:09:44 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_LegendaDialog(object):
    def setupUi(self, LegendaDialog):
        LegendaDialog.setObjectName("LegendaDialog")
        LegendaDialog.resize(QtCore.QSize(QtCore.QRect(0,0,411,527).size()).expandedTo(LegendaDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(LegendaDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.T_Legenda = QtGui.QTableWidget(LegendaDialog)
        self.T_Legenda.setObjectName("T_Legenda")
        self.vboxlayout.addWidget(self.T_Legenda)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(131,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.okButton = QtGui.QPushButton(LegendaDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(LegendaDialog)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),LegendaDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(LegendaDialog)

    def retranslateUi(self, LegendaDialog):
        LegendaDialog.setWindowTitle(QtGui.QApplication.translate("LegendaDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.T_Legenda.clear()
        self.T_Legenda.setColumnCount(2)
        self.T_Legenda.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("LegendaDialog", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.T_Legenda.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("LegendaDialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.T_Legenda.setHorizontalHeaderItem(1,headerItem1)
        self.okButton.setText(QtGui.QApplication.translate("LegendaDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

