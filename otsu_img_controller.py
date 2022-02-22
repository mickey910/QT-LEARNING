# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 00:20:51 2022

@author: WINS
"""
from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap
import cv2

class img_controller(object):
    def __init__(self, img_path, label_img, label_file_path, label_img_shape):
        self.img_path = img_path
        self.label_img = label_img
        self.label_file_path = label_file_path        
        self.img_shap = label_img_shape
        self.ratio_value = 50
        self.read_file_and_init()
        self.__update_img()

    def read_file_and_init(self):
        try:
            self.img = cv2.imread(self.img_path)
            self.origin_height, self.origin_width, self.origin_channel = self.img.shape            
        except:
            self.img = cv2.imread('FB_IMG_1551688638181.jpg')
            self.origin_height, self.origin_width, self.origin_channel = self.img.shape    

        bytesPerline = 3 * self.origin_width  #3個channel
        self.qimg = QImage(self.img, self.origin_width, self.origin_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        #numpy.ndarray轉成Qimage
        print(type(self.qimg))
        self.origin_qpixmap = QPixmap.fromImage(self.qimg)
        #Qimage轉換成Qpixmap
        print(type(self.origin_qpixmap))
        self.ratio_value = 50
        self.__update_text_file_path()
        self.set_img_ratio()
       
    def set_path(self, img_path):
        self.img_path = img_path
        self.read_file_and_init()
        self.__update_img()        

    def __update_img(self):       
        self.label_img.setPixmap(self.qpixmap)
        self.label_img.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    def __update_text_file_path(self):
        self.label_file_path.setText(f"File path = {self.img_path}")

    def set_img_ratio(self):
        self.ratio_rate = pow(10, (self.ratio_value - 50)/50)
        qpixmap_height = self.origin_height * self.ratio_rate
        self.qpixmap = self.origin_qpixmap.scaledToHeight(qpixmap_height)
        #使照片依ratio rate比例縮放
        self.__update_img()
        self.__update_text_img_shape()


    def __update_text_img_shape(self):
        current_text = f"Current img shape = ({self.qpixmap.width()}, {self.qpixmap.height()})"
        origin_text = f"Origin img shape = ({self.origin_width}, {self.origin_height})"
        self.img_shap.setText(current_text+"\t"+origin_text)

    def set_zoom_in(self):
        self.ratio_value = max(0, self.ratio_value - 1)
        self.set_img_ratio()

    def set_zoom_out(self):
        self.ratio_value = min(100, self.ratio_value + 1)
        self.set_img_ratio()
        
    def otsu(self):
        self.img1 = cv2.imread(self.img_path,0)
        self.ret,self.th = cv2.threshold(self.img1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #otau轉換後type為 numpy.ndarray
        print(type(self.th))
        height, width = self.th.shape
        bytesPerLine =  self.origin_width  #grayscale只有1個channel
        self.th1 = QImage(self.th, width, height, bytesPerLine, QImage.Format_Grayscale8).rgbSwapped()
        #numpy.ndarray轉成Qimage
        self.origin_qpixmap = QPixmap.fromImage(self.th1)
        #Qimage轉換成Qpixmap
        print(type(self.th1))
        self.set_img_ratio()
        
    
   