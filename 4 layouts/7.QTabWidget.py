"""
一个带有 Tab 的布局，点击相应的标签按钮，可以显示相应的控件
"""
import sys

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()

        # 设置文档模式，看上去更简洁一些？
        # tabs.setDocumentMode(True)

        # 设置 tab 键的位置，West，North，South，East, 上北下南, 左西右东
        tabs.setTabPosition(QTabWidget.North)

        # 可以鼠标拖拽排列 Tab 的位置
        tabs.setMovable(True)

        for color in ["red", "green", "blue", "yellow"]:
            # 添加tab: (组件，tab名称)
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


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