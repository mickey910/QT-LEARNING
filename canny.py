# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\影像處理\QT\canny.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1285, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filename = QtWidgets.QLabel(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(120, 10, 321, 20))
        self.filename.setObjectName("filename")
        self.zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in.setGeometry(QtCore.QRect(850, 10, 71, 24))
        self.zoom_in.setObjectName("zoom_in")
        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out.setGeometry(QtCore.QRect(950, 10, 71, 24))
        self.zoom_out.setObjectName("zoom_out")
        self.img_shap = QtWidgets.QLabel(self.centralwidget)
        self.img_shap.setGeometry(QtCore.QRect(490, 40, 531, 20))
        self.img_shap.setObjectName("img_shap")
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(20, 10, 80, 24))
        self.openfile.setObjectName("openfile")
        self.img_processing = QtWidgets.QPushButton(self.centralwidget)
        self.img_processing.setGeometry(QtCore.QRect(20, 40, 101, 24))
        self.img_processing.setObjectName("img_processing")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 70, 1161, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        #self.scrollAreaWidgetContents = QtWidgets.QWidget()
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1157, 667))
        #self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_img = QtWidgets.QLabel()
        self.label_img.setGeometry(QtCore.QRect(562, 280, 61, 41))
        self.label_img.setObjectName("label_img")
        self.scrollArea.setWidget(self.label_img)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 21))
        self.menubar.setObjectName("menubar")
        self.menuopenimg = QtWidgets.QMenu(self.menubar)
        self.menuopenimg.setObjectName("menuopenimg")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuopenimg.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filename.setText(_translate("MainWindow", "filename"))
        self.zoom_in.setText(_translate("MainWindow", "zoom in"))
        self.zoom_out.setText(_translate("MainWindow", "zoom out"))
        self.img_shap.setText(_translate("MainWindow", "img_shape"))
        self.openfile.setText(_translate("MainWindow", "OpenFile"))
        self.img_processing.setText(_translate("MainWindow", "Img Processing"))
        self.label_img.setText(_translate("MainWindow", "label_img"))
        self.menuopenimg.setTitle(_translate("MainWindow", "canny"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

