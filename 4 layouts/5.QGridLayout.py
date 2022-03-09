"""
QGridLayout 是一个网格的布局。它类似于表格，可以多行多列，并且可以留空（就像表格一样，某些格子空着），也可以让某些组件横跨多行或者多列
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        # 网格布局
        layout = QGridLayout()

        # 后面的数字，分别代表当前组件位于：第几行，第几列，纵跨几行，横跨几列（基于当前列，向右方拓展）
        # 注意，这些数字都是行列的索引，从0开始
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        # 表格位于：索引为2的行，索引0列，纵跨1行（保持本行不变），横跨2列（向右扩展一列）
        layout.addWidget(Color('purple'), 2, 0, 1, 2)

        widget = QWidget()
        widget.setLayout(layout)
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