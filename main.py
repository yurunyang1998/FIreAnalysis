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

if __name__ == '__main__':
    v_compare = QVersionNumber(5, 6, 0)
    v_current, _ = QVersionNumber.fromString(QT_VERSION_STR)  # 获取当前Qt版本
    if QVersionNumber.compare(v_current, v_compare) >= 0:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
        app = QApplication(sys.argv)  #
    else:
        app = QApplication(sys.argv)
        font = QFont("宋体")
        pointsize = font.pointSize()
        font.setPixelSize(pointsize * 90 / 72)
        app.setFont(font)
    # app = QApplication(sys.argv)
    dialog = LoginPage()
    if dialog.exec_() == QDialog.Accepted:
        ex = mainPage.MainPage()
        ex.show()
        sys.exit(app.exec_())

    # # app = QApplication(sys.argv)
    # ex = mainPage.MainPage()
    # ex.show()
    # sys.exit(app.exec_())