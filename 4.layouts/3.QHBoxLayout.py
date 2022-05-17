import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QHBoxLayout()

        # 设置拉伸宽度，即每个组件占据的宽度
        layout.addWidget(Color('red'), 1)
        layout.addWidget(Color('green'), 2)
        layout.addWidget(Color('blue'), 3)

        # 可以不设置拉伸宽度，会默认均分布局大小
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))

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

app.exec_()