import  mainPage
from  PyQt5.QtWidgets import QApplication, QDialog
import sys
import  PyQt5 as Qt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  loginPage import LoginPage

################################################
#######对话框
################################################
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # app = QApplication(sys.argv)
    # dialog = LoginPage()
    # if dialog.exec_() == QDialog.Accepted:
        app = QApplication(sys.argv)
        ex = mainPage.MainPage()
        ex.show()
        sys.exit(app.exec_())


# import matplotlib.pyplot as plt
#
#
# # f2 = plt.figure()
# # plt.title("figure2")
# #
# # f3 = plt.figure(5)
# # plt.title("figure5")
# #
# f6 = plt.figure(6, (4, 4), 100)
# # plt.title("figure6")
#
# f7 = plt.figure(7, None, None, '#FFD700', '#FF0000')
# plt.title("figure7")
# # f1 = plt.figure()
#
#
#
# plt.show()
