from random import randint, choice
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)

        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # -------------------------- drawPoint -------------------
    # 画点
    def draw_point(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawPoint(100, 150)  # 点的中心，（到左边距离，上边距离）
        painter.end()
        self.label.setPixmap(canvas)

    # 画带大小，颜色的点
    def draw_point2(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        # 一个画笔对象
        pen = QtGui.QPen()
        # 设置画笔大小，颜色
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        # 应用画笔
        painter.setPen(pen)
        painter.drawPoint(20, 200)
        painter.end()
        self.label.setPixmap(canvas)

    # 给画笔换颜色
    def draw_point_change_pen(self):
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            # pen = painter.pen() 可以获取当前使用的笔
            # 给画笔换颜色
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + randint(-100, 100),  # x
                150 + randint(-100, 100)  # y
            )
        painter.end()
        self.label.setPixmap(canvas)

    # 画线
    def draw_line(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(15)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawLine(
            QtCore.QPoint(100, 100),  # 起始坐标点
            QtCore.QPoint(300, 200)   # 结束坐标点
        )
        painter.end()
        self.label.setPixmap(canvas)

    # 画四方形
    def draw_rect(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)
        painter.drawRect(50, 50, 100, 100)  # x1: int, y1: int, w: int, h: int
        painter.drawRect(60, 60, 150, 100)
        painter.drawRect(70, 70, 100, 150)
        painter.drawRect(80, 80, 150, 100)
        painter.drawRect(90, 90, 100, 150)

        """
        上面连续画多个四方形，可以这样：
        painter.drawRects(
            QtCore.QRect(50, 50, 100, 100),
            QtCore.QRect(60, 60, 150, 100),
            QtCore.QRect(70, 70, 100, 150),
            QtCore.QRect(80, 80, 150, 100),
            QtCore.QRect(90, 90, 100, 150),
        )
        """
        painter.end()
        self.label.setPixmap(canvas)

    # 笔刷，笔刷相当于一个刷子，它可以给区域填充颜色
    def draw_rect_with_brush(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FFD141"))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRects([
            QtCore.QRect(50, 50, 100, 100),
            QtCore.QRect(60, 60, 150, 100),
            QtCore.QRect(70, 70, 100, 150),
            QtCore.QRect(80, 80, 150, 100),
            QtCore.QRect(90, 90, 100, 150),
        ])
        painter.end()
        self.label.setPixmap(canvas)

    # 圆角方形
    def draw_RoundRect(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)
        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)  # 多了两个参数，x，y方向的半径
        painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        painter.drawRoundedRect(160, 160, 100, 100, 50, 50)
        painter.end()
        self.label.setPixmap(canvas)

    # 椭圆
    def draw_Ellipse(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204, 0, 0))  # r, g, b
        painter.setPen(pen)

        painter.drawEllipse(10, 10, 100, 100)  # 中心点，x半径，y半径
        painter.drawEllipse(10, 10, 150, 200)
        painter.drawEllipse(10, 10, 200, 300)
        # 也可以写成如下形式：
        painter.drawEllipse(QtCore.QPoint(100, 100), 10, 10)

        painter.end()
        self.label.setPixmap(canvas)

    # 画文字
    def draw_text(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)  # 画笔宽度对文字无效
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(10, 200, 'Hello, world!')  # 左间距，上间距

        # 多了2个数字，代表宽和高。超出宽和高的部分会被隐藏掉，在这个区域内，文字以居中对齐
        painter.drawText(100, 100, 200, 100, Qt.AlignHCenter, 'Hello, world!')

        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()