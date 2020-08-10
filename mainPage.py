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
        self.pushButton_6.clicked.connect(self.CalculateRate)
        self.pushButton_7.clicked.connect(self.addThresholdValue)

        ## 内部用属性
        self.rateInX = 1
        self.rateInY = 1

        self.X1inPixel = 0
        self.X2inPixel = 0
        self.Y1inPixel = 0
        self.Y2inPixel = 0

        self.minThresholdValue=0
        self.maxThresholdValue=0

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

            self.X1inPixel = int(s.x())
            self.Y1inPixel = int(s.y())

            self.lastPoint = (int(s.x()),int(s.y()))


    def mouseReleaseEvent(self, event):
        if(self.moveMouse):
            print("mouse release")
            s = event.windowPos()
            # self.setMouseTracking(True)
            self.label_5.setText(str(s.x()))
            self.label_12.setText(str(s.y()))

            self.X2inPixel = int(s.x())
            self.Y1inPixel = int(s.y())

            self.moveMouse = False
            self.endPoint = (int(s.x()),int(s.y()))

            self.th.DrawRect(self.lastPoint, self.endPoint)



    def setImage(self, image):
        try:
            self.label_6.setPixmap(QPixmap.fromImage(image))
        except Exception as e:
            print(e)


    def CalculateRate(self):

        try:
            if(self.lineEdit.text() == "" or self.lineEdit_2.text()==""):
                alert(self, "请输入距离")
                return
            Xdistance,Ydistance = self.lineEdit.text(), self.lineEdit_2.text()

            XdisInPix = abs(self.X1inPixel-self.X2inPixel)
            YdisInPix = abs(self.Y1inPixel-self.Y2inPixel)

            self.rateInX = XdisInPix/int(Xdistance)
            self.rateInY = YdisInPix/int(Ydistance)
            self.label_7.setText("1:"+str(self.rateIn6756tX))
            self.label_13.setText("1:"+str(self.rateInY))
            #alert(self, "添加成功，正在计算比例")

        except Exception as e:
            print(e)

    def addThresholdValue(self):
        if(self.lineEdit_3.text()==""or self.lineEdit_4.text()==""):
            alert(self,"请输入阈值")
            return

        self.minThresholdValue = int(self.lineEdit_3.text())
        self.maxThresholdValue = int(self.lineEdit_4.text())

        if(self.minThresholdValue > self.maxThresholdValue):
            alert(self,"左边的阈值应小于右边的")
            return


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

                        self.processImage(self.rgbImage)

                        self.width,self.height = self.rgbImage.shape[1],self.rgbImage.shape[0]
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

    def processImage(self,img):
        pass




    def CloseVideo(self):


        self.closeSignal = True
        self.cap.release()
        self.closeSignal = False
        return


