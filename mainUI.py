# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QtWidgetsApplication1Class(object):
    def setupUi(self, QtWidgetsApplication1Class):
        QtWidgetsApplication1Class.setObjectName("QtWidgetsApplication1Class")
        QtWidgetsApplication1Class.setEnabled(True)
        QtWidgetsApplication1Class.resize(1133, 949)
        self.centralWidget = QtWidgets.QWidget(QtWidgetsApplication1Class)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = VideoLabel(self.centralWidget)
        self.label_6.setMinimumSize(QtCore.QSize(700, 550))
        self.label_6.setMaximumSize(QtCore.QSize(800, 16777215))
        self.label_6.setAutoFillBackground(True)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(800, 16999))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setGeometry(QtCore.QRect(9, 9, 1091, 257))
        self.widget_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(182, 9, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(396, 35, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(217, 35, 71, 21))
        self.label_12.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(54, 9, 71, 20))
        self.label_8.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(9, 35, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(182, 35, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(54, 35, 71, 20))
        self.label_11.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(310, 9, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(9, 9, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 0, 0)")
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(310, 35, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(396, 9, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(217, 9, 71, 21))
        self.label_5.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(9, 61, 101, 31))
        self.pushButton.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(396, 61, 81, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(500, 10, 51, 21))
        self.label_7.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(500, 36, 51, 20))
        self.label_13.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.lineEdit_3.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 110, 131, 31))
        self.lineEdit_4.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(148, 137, 16, 16))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 110, 81, 31))
        self.pushButton_7.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 170, 131, 31))
        self.lineEdit_5.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 170, 133, 31))
        self.lineEdit_6.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 170, 81, 31))
        self.pushButton_8.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 170, 104, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setGeometry(QtCore.QRect(10, 146, 131, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(220, 145, 101, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(480, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setGeometry(QtCore.QRect(490, 170, 61, 31))
        self.label_19.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(770, 0, 311, 241))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.tab_4)
        self.widget_4.setMinimumSize(QtCore.QSize(200, 150))
        self.widget_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.widget_4.setObjectName("widget_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 20, 251, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 60, 251, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 60, 251, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 100, 251, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 251, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.widget_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.tab_5)
        self.widget_5.setMinimumSize(QtCore.QSize(200, 150))
        self.widget_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 60, 251, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 100, 251, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_12.setGeometry(QtCore.QRect(300, 100, 251, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_11.setGeometry(QtCore.QRect(300, 60, 251, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_10.setGeometry(QtCore.QRect(300, 20, 251, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_13.setGeometry(QtCore.QRect(70, 20, 191, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)
        QtWidgetsApplication1Class.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(QtWidgetsApplication1Class)
        self.statusBar.setObjectName("statusBar")
        QtWidgetsApplication1Class.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(QtWidgetsApplication1Class)
        self.toolBar.setObjectName("toolBar")
        QtWidgetsApplication1Class.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(QtWidgetsApplication1Class)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1133, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        QtWidgetsApplication1Class.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(QtWidgetsApplication1Class)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(QtWidgetsApplication1Class)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QtWidgetsApplication1Class)

    def retranslateUi(self, QtWidgetsApplication1Class):
        _translate = QtCore.QCoreApplication.translate
        QtWidgetsApplication1Class.setWindowTitle(_translate("QtWidgetsApplication1Class", "QtWidgetsApplication1"))
        self.label_3.setText(_translate("QtWidgetsApplication1Class", "X2"))
        self.label_2.setText(_translate("QtWidgetsApplication1Class", "Y1"))
        self.label_4.setText(_translate("QtWidgetsApplication1Class", "Y2"))
        self.label_9.setText(_translate("QtWidgetsApplication1Class", "距离(m)"))
        self.label.setText(_translate("QtWidgetsApplication1Class", "X1"))
        self.label_10.setText(_translate("QtWidgetsApplication1Class", "距离(m)"))
        self.pushButton.setText(_translate("QtWidgetsApplication1Class", "截取辅助标记物"))
        self.pushButton_6.setText(_translate("QtWidgetsApplication1Class", "添加距离"))
        self.lineEdit_3.setText(_translate("QtWidgetsApplication1Class", "187,255,232"))
        self.lineEdit_4.setText(_translate("QtWidgetsApplication1Class", "255,255,255"))
        self.pushButton_7.setText(_translate("QtWidgetsApplication1Class", "添加阈值"))
        self.lineEdit_5.setText(_translate("QtWidgetsApplication1Class", "添加火焰高度"))
        self.lineEdit_6.setText(_translate("QtWidgetsApplication1Class", "添加火焰直径"))
        self.pushButton_8.setText(_translate("QtWidgetsApplication1Class", "添加"))
        self.pushButton_9.setText(_translate("QtWidgetsApplication1Class", "自动分析火焰数据"))
        self.label_16.setText(_translate("QtWidgetsApplication1Class", "火焰高度(m)"))
        self.label_17.setText(_translate("QtWidgetsApplication1Class", "火焰直径(m)"))
        self.label_18.setText(_translate("QtWidgetsApplication1Class", "火焰倾斜角"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QtWidgetsApplication1Class", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QtWidgetsApplication1Class", "高度"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QtWidgetsApplication1Class", "直径"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("QtWidgetsApplication1Class", "火焰形态处理"))
        self.pushButton_3.setText(_translate("QtWidgetsApplication1Class", "沿火焰倾斜方向的热流密度沿X轴分布"))
        self.pushButton_2.setText(_translate("QtWidgetsApplication1Class", "垂直火焰倾斜方向的热流密度沿Y轴分布"))
        self.pushButton_16.setText(_translate("QtWidgetsApplication1Class", "垂直圆柱体火焰垂直方向的热流密度分布"))
        self.pushButton_15.setText(_translate("QtWidgetsApplication1Class", "垂直圆柱体火焰热流密度分布俯视图"))
        self.pushButton_5.setText(_translate("QtWidgetsApplication1Class", "垂直圆柱体火焰在水平方向热流密度分布"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("QtWidgetsApplication1Class", "辐射热流计算"))
        self.pushButton_14.setText(_translate("QtWidgetsApplication1Class", "垂直圆柱体火焰伤害半径示意图"))
        self.pushButton_4.setText(_translate("QtWidgetsApplication1Class", "以火焰中心为中心的伤害范围示意图"))
        self.pushButton_12.setText(_translate("QtWidgetsApplication1Class", "假设人在c点不同辐射热流值的伤害范围"))
        self.pushButton_11.setText(_translate("QtWidgetsApplication1Class", "假设人在b点不同辐射热流值的伤害范围"))
        self.pushButton_10.setText(_translate("QtWidgetsApplication1Class", "假设人在a点不同辐射热流值的伤害范围"))
        self.pushButton_13.setText(_translate("QtWidgetsApplication1Class", "添加热流值参数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("QtWidgetsApplication1Class", "伤害范围"))
        self.toolBar.setWindowTitle(_translate("QtWidgetsApplication1Class", "toolBar"))
        self.menu.setTitle(_translate("QtWidgetsApplication1Class", "菜单"))
        self.action.setText(_translate("QtWidgetsApplication1Class", "读取视频"))

from videolabel import VideoLabel
