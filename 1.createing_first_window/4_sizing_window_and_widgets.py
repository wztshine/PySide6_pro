"""
定义窗口和组件大小
"""

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 必须调用父类方法生成对象


        self.setWindowTitle("My App")

        button = QPushButton("Press Me")
        """
        setFixedSize() 可以设置固定大小      
        self.setMinimumSize()  设置窗口最小能有多小
        self.setMaximumSize()  设置窗口最大能有多大
        任何组件都可以使用这三个方法！
        """
        self.setFixedSize(QSize(400, 300))  # QSize 接受宽和高，来定义组件大小
        self.setMaximumSize(QSize(800, 700))

        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()