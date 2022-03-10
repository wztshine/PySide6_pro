"""
每一个 widget 都是作为一个 位图（bitmap) 画在一个'画布'上，所以我们要先理解如何画图（QPainter)
"""

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # QLable 可以用来显示图片，所以我们用它来显示后面定义的 QPixmap 对象
        self.label = QtWidgets.QLabel()
        # 创建一个 QPixmap 对象
        canvas = QtGui.QPixmap(400, 300)
        # 填充白色（到这里，canvas 就是一张空白的图片）
        canvas.fill(Qt.white)

        # 将 QPixmap 这个图片对象，放到label上显示
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        # 重新获取 label 上的这个空白图片
        canvas = self.label.pixmap()
        # 给图片创建画笔
        painter = QtGui.QPainter(canvas)
        # 画笔开始划线
        painter.drawLine(10, 10, 300, 200)
        # 画笔停下
        painter.end()
        # 画完的图片，重新放到 label 上显示
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()