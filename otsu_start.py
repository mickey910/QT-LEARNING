# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 20:44:07 2022

@author: WINS
"""

#### 照片檔名跟路徑必須為英文 ####

from PyQt5 import QtWidgets


from otsu_controller import MainWindow_controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
    
    