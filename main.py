from PyQt5 import QtWidgets
from masaustu import Ui_MainWindow
import sys

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def app():
    app2 = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app2.exec_())
app()
