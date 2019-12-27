# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(973, 397)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(760, 20, 191, 331))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.menu_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setObjectName("menu_layout")
        self.run_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.run_button.setObjectName("run_button")
        self.menu_layout.addWidget(self.run_button, 1, 1, 1, 1)
        self.folder_widget = QtWidgets.QTreeWidget(self.gridLayoutWidget_2)
        self.folder_widget.setObjectName("folder_widget")
        self.folder_widget.headerItem().setText(0, "1")
        self.menu_layout.addWidget(self.folder_widget, 0, 1, 1, 1)
        self.plot_view = QtWidgets.QWidget(self.centralwidget)
        self.plot_view.setGeometry(QtCore.QRect(20, 20, 711, 331))
        self.plot_view.setObjectName("plot_view")
        self.graphics_view = QtWidgets.QGraphicsView(self.plot_view)
        self.graphics_view.setGeometry(QtCore.QRect(0, 0, 341, 331))
        self.graphics_view.setObjectName("graphics_view")
        self.plot_view_2 = QtWidgets.QGraphicsView(self.plot_view)
        self.plot_view_2.setGeometry(QtCore.QRect(370, 0, 341, 331))
        self.plot_view_2.setObjectName("plot_view_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QMenuBar(mainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 973, 22))
        self.menu_bar.setObjectName("menu_bar")
        mainWindow.setMenuBar(self.menu_bar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Animal detector"))
        self.run_button.setText(_translate("mainWindow", "Check"))


