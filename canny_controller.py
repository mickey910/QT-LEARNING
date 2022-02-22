# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:49:28 2022

@author: WINS
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy

from canny import Ui_MainWindow
from canny_img_controller import img_controller

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):        
        self.file_path = ''
        self.img_controller = img_controller(img_path=self.file_path,
                                             label_img=self.ui.label_img,
                                             label_file_path=self.ui.filename,                                            
                                             label_img_shape=self.ui.img_shap)
        #功能鈕 設定
        self.ui.openfile.clicked.connect(self.open_file)
        self.ui.zoom_in.clicked.connect(self.img_controller.set_zoom_in) 
        self.ui.zoom_out.clicked.connect(self.img_controller.set_zoom_out)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.label_img.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # self.ui.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # 將圖片置中
        self.ui.img_processing.clicked.connect(self.img_controller.canny)
    
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./") # start path        
        self.init_new_picture(filename)

    def init_new_picture(self, filename):       
        self.img_controller.set_path(filename) 