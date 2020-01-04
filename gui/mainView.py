# -*- coding: utf-8 -*-

import sys
from ImgPredictor import load_file
from PyQt5 import QtCore, QtGui, QtWidgets
# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_mainWindow(object):

    def __init__(self):
        self.data = []
        self.types = ["jpg File", "jpeg File"]
        self.path = ""
        self.plot_view_size = [20, 20, 780, 380]
        self.graphic_view_size = [-80, -60, 920, 460]
        self.folder_widget_size = [820, 20, 400, 360]
        self.window_size = [0, 0, 1240, 420]


    def setupUi(self, mainWindow):

        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_dialog.setText("Error")
        self.error_dialog.setInformativeText('File must be one of the following types: ' + str(self.types))
        self.error_dialog.setWindowTitle("Error")

        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(self.window_size[2], self.window_size[3])
        self.central_widget = QtWidgets.QWidget(mainWindow)
        self.central_widget.setObjectName("central_widget")

        self.file_widget = QtWidgets.QWidget(self.central_widget)
        self.file_widget.setGeometry(QtCore.QRect(*self.folder_widget_size))
        self.file_widget.setObjectName("file_widget")

        self.menu_layout = QtWidgets.QGridLayout(self.file_widget)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setObjectName("menu_layout")

        self.file_model = QtWidgets.QFileSystemModel()
        self.file_model.setRootPath("~home")
        self.file_model.setFilter(QtCore.QDir.NoDotAndDotDot
                                  | QtCore.QDir.AllEntries
                                  | QtCore.QDir.Dirs
                                  | QtCore.QDir.Files)
        self.folder_view = QtWidgets.QTreeView(self.file_widget)
        self.folder_view.setObjectName("folder_view")
        self.folder_view.setModel(self.file_model)
        self.folder_view.hideColumn(1)
        self.folder_view.hideColumn(2)
        self.folder_view.hideColumn(3)
        self.folder_view.clicked.connect(self.fileClicked)
        self.menu_layout.addWidget(self.folder_view, 0, 1, 1, 1)

        self.plot_widget = QtWidgets.QWidget(self.central_widget)
        self.plot_widget.setGeometry(QtCore.QRect(*self.plot_view_size))
        self.plot_widget.setObjectName("plot_widget")

        self.graphics_view = QtWidgets.QLabel(self.plot_widget)
        self.graphics_view.setGeometry(QtCore.QRect(*self.graphic_view_size))
        self.graphics_view.setObjectName("graphics_view")

        mainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(mainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 973, 22))
        self.menu_bar.setObjectName("menu_bar")
        mainWindow.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(mainWindow)
        self.status_bar.setObjectName("status_bar")
        mainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Animal detector"))

    def fileClicked(self, index):
        if self.file_model.type(index) in self.types:
            self.path = self.file_model.filePath(index)
            self.pix_map = QtGui.QPixmap.fromImage(load_file(self.path))
            self.pix_map = self.pix_map.scaled(self.graphic_view_size[2],self.graphic_view_size[3], QtCore.Qt.KeepAspectRatio)
            self.graphics_view.setPixmap(self.pix_map)
        elif self.file_model.isDir(index):
            pass
        else:
            self.path = ""
            self.error_dialog.exec_()
