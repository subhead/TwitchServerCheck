# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ping_gui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerPing(object):
    def setupUi(self, ServerPing):
        ServerPing.setObjectName("ServerPing")
        ServerPing.resize(461, 341)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("free-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ServerPing.setWindowIcon(icon)
        self.txtOutput = QtWidgets.QTextBrowser(ServerPing)
        self.txtOutput.setGeometry(QtCore.QRect(10, 10, 351, 321))
        self.txtOutput.setObjectName("txtOutput")
        self.btnPing = QtWidgets.QPushButton(ServerPing)
        self.btnPing.setGeometry(QtCore.QRect(370, 280, 81, 21))
        self.btnPing.setObjectName("btnPing")
        self.btnExit = QtWidgets.QPushButton(ServerPing)
        self.btnExit.setGeometry(QtCore.QRect(370, 310, 81, 23))
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(ServerPing)
        QtCore.QMetaObject.connectSlotsByName(ServerPing)

    def retranslateUi(self, ServerPing):
        _translate = QtCore.QCoreApplication.translate
        ServerPing.setWindowTitle(_translate("ServerPing", "Server Ping"))
        self.btnPing.setText(_translate("ServerPing", "Ping"))
        self.btnExit.setText(_translate("ServerPing", "Exit"))

