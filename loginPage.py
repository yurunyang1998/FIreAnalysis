# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import  PyQt5 as Qt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Login_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 579)
        Form.setMinimumSize(QtCore.QSize(774, 579))
        Form.setMaximumSize(QtCore.QSize(774, 579))
        Form.setStyleSheet("background-image: url(./background.png);")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(320, 270, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-image: url(./white.jpg);\n"
        "font: 28pt \"Agency FB\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 330, 211, 51))
        self.lineEdit_2.setStyleSheet("background-image: url(./white.jpg);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 400, 91, 31))
        self.pushButton.setStyleSheet("background-image: url(./white.jpg);\n"
        "font: 16pt \"Arial Narrow\";\n"
        "background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "登录"))
# import resource



class LoginPage(Login_UI, QDialog):
    def __init__(self):
        super(LoginPage,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_enter_clicked)

    def on_pushButton_enter_clicked(self):
        # 账号判断
        try:
            if self.lineEdit.text() == "tfri" and self.lineEdit_2.text() == "tfri509":
                return  self.accept()
            else:
                self.showDialog()
        except Exception as e:
            print(e)

    def showDialog(self):
        dialog = QDialog()
        btn = QPushButton('账号或密码错误', dialog)
        btn.clicked.connect(dialog.close)
        btn.move(50, 50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)  # 当对话框显示时，主窗口的所有控件都不可用
        dialog.exec()  # 显示对话框
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dialog = MainPage()
#     dialog.exec_()
