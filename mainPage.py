import time

from PyQt5.QtWidgets import QFileDialog,QMainWindow,QApplication,QMessageBox,QErrorMessage
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QPainter, QPixmap, QPen, QImage
from PyQt5.QtCore import QPoint, QThread, pyqtSignal
import cv2
import numpy as np
from qtpy import QtGui, QtCore

from mainUI import  Ui_QtWidgetsApplication1Class

def alert(Qwidget, message):
    reply = QMessageBox.information(Qwidget, '提示', message, QMessageBox.Ok | QMessageBox.Close,
                                    QMessageBox.Close)


videoName = ""

class MainPage(Ui_QtWidgetsApplication1Class, QMainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        self.setupUi(self)

        ## connect 函数
        self.action.triggered.connect(self.OpenVideo)
        self.pushButton.clicked.connect(self.MarkSize)
        self.label_6.doubleClicked.connect(self.DoubleClick)



        ## 内部用属性


        self.paused = False
        self.moveMouse = False

        self.th = Thread(self)
    def OpenVideo(self):

        try:

            global videoName
            videoName = QFileDialog.getOpenFileName(self,"选择视频文件")[0]
            #TODO: 判断视频文件后缀

            if(self.th.isRunning()):
                #TODO: 实现在视频播放时切换视频的功能
                self.th.CloseVideo()
                #self.th.closeSignal = False
            self.th.changePixmap.connect(self.setImage)
            self.th.start()

        except Exception as e :
            alert(self,"请选择视频文件")
            print(e)



    def DoubleClick(self):   #双击事件，视频暂停
        print("double Click")
        self.th.PauseVideo()


    def MarkSize(self):
        self.th.PauseVideo()
        self.moveMouse = True



    def mousePressEvent(self, event):
        if(self.moveMouse):
            print("mouse press")
            s = event.windowPos()
            #self.setMouseTracking(True)
            self.label_8.setText(str(s.x()))
            self.label_11.setText(str(s.y()))
            self.lastPoint = (int(s.x()),int(s.y()))


    def mouseReleaseEvent(self, event):
        if(self.moveMouse):
            print("mouse release")
            s = event.windowPos()
            # self.setMouseTracking(True)
            self.label_5.setText(str(s.x()))
            self.label_12.setText(str(s.y()))
            self.moveMouse = False
            self.endPoint = (int(s.x()),int(s.y()))

            self.th.DrawRect(self.lastPoint, self.endPoint)



    def setImage(self, image):
        try:
            self.label_6.setPixmap(QPixmap.fromImage(image))
        except Exception as e:
            print(e)






class Thread(QThread):

    changePixmap = pyqtSignal(QtGui.QImage)
    paused = False
    closeSignal = False
    rgbImage = True
    width = 0
    height = 0

    def run(self):
        try:
            self.cap = cv2.VideoCapture(videoName)
            print(videoName)
            while (self.cap.isOpened()==True):
                if(self.closeSignal == True):
                    return
                if(not self.paused):
                    ret, frame = self.cap.read()
                    if ret:
                        self.rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #在这里可以对每帧图像进行处理，
                        self.width,self.height = self.rgbImage.shape[1],self.rgbImage.shape[0]
                        #print(self.width, self.height)
                        convertToQtFormat = QtGui.QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                        currentCaputre = convertToQtFormat.scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio)
                        self.changePixmap.emit(currentCaputre)
                        #print("play")
                        time.sleep(0.02) #控制视频播放的速度

                    else:
                        break
                else:
                    continue
            #self.cap.release()
        except Exception as e:
            print(e)

    def PauseVideo(self):
        try:
            if(self.paused == True):
                self.paused = False
            else:
                self.paused = True
        except Exception as e:
            print(e)

    def DrawRect(self,Qpoint1, Qpoint2):
        try:

            # self.rgbImage =  self.QImageToCvMat(self.currentCaputre)

            self.rgbImage = cv2.resize(self.rgbImage,(self.width,self.height),3)

            cv2.rectangle(self.rgbImage,Qpoint1,Qpoint2,(0,255,0))
            convertToQtFormat = QtGui.QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0],
                                             QImage.Format_RGB888)  # 在这里可以对每帧图像进行处理，
            #self.currentCaputre = convertToQtFormat.scaled(800, 1000, QtCore.Qt.KeepAspectRatio)
            self.changePixmap.emit(convertToQtFormat)
        except Exception as e:
            print(e)


    def CloseVideo(self):


        self.closeSignal = True
        self.cap.release()
        self.closeSignal = False
        return
