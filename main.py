import  mainPage
from  PyQt5.QtWidgets import QApplication
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainPage.MainPage()
    ex.show()
    sys.exit(app.exec_())




# from PyQt5.QtWidgets import QApplication
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import pyqtSignal
#
#
# class Emit(QtWidgets.QWidget):
#     closeEmitApp = pyqtSignal()
#
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self)
#
#         self.setWindowTitle('escape')
#         self.resize(350, 300)
#         self.closeEmitApp.connect(self.close)
#
#     def mousePressEvent(self, event):
#         self.closeEmitApp.emit()
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#     qb = Emit()
#     qb.show()
#     app.exec()