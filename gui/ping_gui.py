# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ping_gui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerPing(object):
    def setupUi(self, ServerPing):
        ServerPing.setObjectName("ServerPing")
        ServerPing.resize(394, 242)
        self.txtOutput = QtWidgets.QTextBrowser(ServerPing)
        self.txtOutput.setGeometry(QtCore.QRect(10, 10, 256, 221))
        self.txtOutput.setObjectName("txtOutput")
        self.btnPing = QtWidgets.QPushButton(ServerPing)
        self.btnPing.setGeometry(QtCore.QRect(280, 10, 101, 21))
        self.btnPing.setObjectName("btnPing")
        self.btnCopy = QtWidgets.QPushButton(ServerPing)
        self.btnCopy.setGeometry(QtCore.QRect(280, 40, 101, 23))
        self.btnCopy.setObjectName("btnCopy")
        self.btnExit = QtWidgets.QPushButton(ServerPing)
        self.btnExit.setGeometry(QtCore.QRect(280, 70, 101, 23))
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(ServerPing)
        QtCore.QMetaObject.connectSlotsByName(ServerPing)

    def retranslateUi(self, ServerPing):
        _translate = QtCore.QCoreApplication.translate
        ServerPing.setWindowTitle(_translate("ServerPing", "Server Ping"))
        self.btnPing.setText(_translate("ServerPing", "Ping"))
        self.btnCopy.setText(_translate("ServerPing", "Copy to clipboard"))
        self.btnExit.setText(_translate("ServerPing", "Exit"))

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ui_sp = QtWidgets.QDialog()
	ui = Ui_ServerPing()
	ui.setupUi(ui_sp)
	ui_sp.show()
	sys.exit(app.exec_())

