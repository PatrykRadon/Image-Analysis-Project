from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from mainView import Ui_mainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    myapp = Ui_mainWindow()
    myapp.setupUi(window)
    window.show()
    sys.exit(app.exec_())
