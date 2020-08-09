from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import *
from PyQt5 import QtGui
class VideoLabel(QLabel):
      # 创建双击信号
    doubleClicked = pyqtSignal()
    singleClicked = pyqtSignal()
    def __init__(self,parent=None):
        super(VideoLabel,self).__init__(parent)

    def mouseDoubleClickEvent(self,QMouseEvent):     #双击事件
        self.doubleClicked.emit()
       # print("emit")

