"""
各个布局之前还可以嵌套，一个布局可以放到另一个布局内部
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        # 你可以分别注释下面两行，看看效果
        layout1.setContentsMargins(0, 0, 0, 0)  # 设置布局中，各组件距离窗口 left, top, right, bottom 四个边的距离
        layout1.setSpacing(20)  # 设置布局中，各组件之间的间距

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


class Color(QWidget):
    """一个颜色组件，通过传递一个字符串类型的颜色，就可以生成一个带颜色的组件"""
    def __init__(self, color):
        super(Color, self).__init__()
        # 自动填充背景颜色
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()