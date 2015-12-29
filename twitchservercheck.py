import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
from gui.ping_gui_v4 import Ui_ServerPing


TWITCH_API_SERVER_LIST = "https://api.twitch.tv/kraken/ingests/"



class ServerPingLogic(Ui_ServerPing):
    
    def __init__(self, dialog):
        Ui_ServerPing.__init__(self)
        self.setupUi(dialog)
        self.btnPing.clicked.connect(self.getServerList)
        self.btnExit.clicked.connect(self.exit_app)
        #self.btnCopy.clicked.connect(pyperclip.copy(self.txtOutput.text().ascii()))
      
    def exit_app(self):
        QtCore.QCoreApplication.instance().quit()    
        
    def getServerList(self):
        #self.txtOutput.append('Using: ' + TWITCH_API_SERVER_LIST)
        api = requests.get(TWITCH_API_SERVER_LIST)
        
        text = json.loads(api.text)
        json.dumps(text)
        
        i = 0
        
        try:           
            for z in text['ingests']:
                if z["availability"] == 1.0:
                    avail = "Online"
                    textcolor = QtCore.Qt.green
                else:
                    avail = "Offline"
                    textcolor = QtCore.Qt.red                
                
                self.listWidget.addItem(z['name'] + ' Status: ' + avail)
                self.listWidget.item(i).setForeground(textcolor)
                i += 1
        except:
            print(sys.exc_info())
                        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = ServerPingLogic(dialog)
    dialog.show()
    sys.exit(app.exec_())