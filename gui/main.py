from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from mainView import Ui_mainWindow
import warnings
class MainWindow(QMainWindow):
    def addObj(self, obj):
        self.obj = obj

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.obj.resize(self.size())

if __name__ == "__main__":
    warnings.simplefilter("ignore")
    app = QApplication(sys.argv)
    window = MainWindow()
    my_app = Ui_mainWindow()
    my_app.setupUi(window)
    window.addObj(my_app)

    window.show()
    sys.exit(app.exec_())
