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

        # self.minThresholdValueR=0
        # self.maxThresholdValueR=0
        # self.minThresholdValueG=0
        # self.maxThresholdValueG=0
        # self.minThresholdValueB=0
        # self.maxThresholdValueB=0

        self.minBar = 0
        self.maxBar = 0


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
            self.th.changeSegmentPic.connect(self.setSegmentedPic)
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

            # self.th.DrawRect(self.lastPoint, self.endPoint)



    def setImage(self, image):
        try:
            self.label_6.setPixmap(QPixmap.fromImage(image))
        except Exception as e:
            print(e)

    def setSegmentedPic(self, image):
        try:
            self.label_15.setPixmap(QPixmap.fromImage(image))
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
            self.label_7.setText("1:"+str(self.rateInX))
            self.label_13.setText("1:"+str(self.rateInY))


            #alert(self, "添加成功，正在计算比例")

        except Exception as e:
            print(e)

    def addThresholdValue_Grey(self):
        if(self.lineEdit_3.text()==""or self.lineEdit_4.text()==""):
            alert(self,"请输入阈值")
            return


        self.minBar = int(self.lineEdit_3.text())
        self.maxBar = int(self.lineEdit_4.text())



        self.th.setThresholdValue(self.minBar, self.maxBar)

          #print(self.minThresholdValueR,self.maxThresholdValueB)

        return


    def addThresholdValue_Color(self):
        if(self.lineEdit_3.text()==""or self.lineEdit_4.text()==""):
            alert(self,"请输入阈值")
            return


        self.minBar = int(self.lineEdit_3.text())
        self.maxBar = int(self.lineEdit_4.text())



        self.th.setThresholdValue(self.minBar, self.maxBar)

          #print(self.minThresholdValueR,self.maxThresholdValueB)

        return



class Thread(QThread):

    changePixmap = pyqtSignal(QtGui.QImage)
    changeSegmentPic = pyqtSignal(QtGui.QImage)


    paused = False
    closeSignal = False
    rgbImage = True
    width = 0
    height = 0
    minbar = []
    maxbar = []
    segmented = False

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

                        if(self.segmented):
                            segImg = self.processImage(self.rgbImage)
                            self.changeSegmentPic.emit(segImg)
                            # cv2.waitKey(1)
                        self.width,self.height = self.rgbImage.shape[1],self.rgbImage.shape[0]
                        convertToQtFormat = QtGui.QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                        currentCaputre = convertToQtFormat.scaled(self.width/2, self.height/2, QtCore.Qt.KeepAspectRatio)
                        self.changePixmap.emit(currentCaputre)


                        time.sleep(0.1) #控制视频播放的速度

                    else:
                        return
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


    def processImage(self,img):
        try:
            if(self.segmented):
                # print("haha")
                img = self.color_seperate(img, self.minbar, self.maxbar)

                # img =  self.threshold_demo(img, self.minbar, self.maxbar)
                convertToQtFormat = QtGui.QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
                currentCaputre = convertToQtFormat.scaled(self.width/2, self.height/2, QtCore.Qt.KeepAspectRatio)
                # self.changeSegmentPic.emit(currentCaputre)
        except Exception as e:
            print(e)
        return currentCaputre

    def CloseVideo(self):


        self.closeSignal = True
        self.cap.release()
        self.closeSignal = False
        return

    def color_seperate(self, image, minBar, maxBar):
        try:
            #print(type(minBar),type(maxBar))
            lower_bgr = np.array(minBar)  # 设定bgr下限
            upper_bgr = np.array(maxBar)  # 设定bgr上 限
            print(lower_bgr,upper_bgr)
            mask = cv2.inRange(image, lowerb=lower_bgr, upperb=upper_bgr)  # 依据设定的上下限对目标图像进行二值化转换
            # cv2.imshow("0", mask)
            kernel1 = np.uint8(np.zeros((6, 6)))
            for x in range(5):
                kernel1[x, 2] = 1
                kernel1[2, x] = 1

            kernel = np.uint8(np.zeros((3, 3)))
            for x in range(3):
                kernel[x, 1] = 1;
                kernel[1, x] = 1;
            # 膨胀图像
            dilated = cv2.dilate(mask, kernel1)
            # 腐蚀图像
            eroded = cv2.erode(dilated, kernel);

            mask = eroded
            dst = cv2.bitwise_and(image, image, mask=mask)  # 将二值化图像与原图进行“与”操作；实际是提取前两个frame 的“与”结果，然后输出mask 为1的部分

        except Exception as e:
            print(e)
        return dst

    def threshold_demo(self,image,lowBar, highBar):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
        # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
        ret, binary = cv2.threshold(gray, lowBar, highBar, cv2.THRESH_BINARY)


        print("阈值：", ret)
        # cv2.imshow("binary", binary)
        return binary

    def setThresholdValue(self,minBar_, maxBar_):
        self.minbar = minBar_
        self.maxbar = maxBar_
        self.segmented = True

