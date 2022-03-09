import random
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.vlayout = QVBoxLayout()
        self.layout = QStackedLayout()

        # 尽管添加了很多组件，但是一次只能显示一个，其他的都会被遮住
        self.layout.addWidget(Color("red"))
        self.layout.addWidget(Color("green"))
        self.layout.addWidget(Color("blue"))
        self.layout.addWidget(Color("yellow"))

        # 可以让某个索引的组件，显示出来
        self.layout.setCurrentIndex(0)

        # *创建一个按钮，每次点击按钮，触发信号
        button = QPushButton('choose color')
        button.clicked.connect(self.choose_color)

        # 将按钮和堆叠布局，都放到垂直布局中
        self.vlayout.addWidget(button)
        self.vlayout.addLayout(self.layout)

        widget = QWidget()
        widget.setLayout(self.vlayout)
        self.setCentralWidget(widget)
        
    def choose_color(self):
        # 收到信号后，随机获取一个索引
        num = random.randint(0, 3)
        # 在堆叠布局中，将这个索引对应的组件显示出来
        self.layout.setCurrentIndex(num)


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