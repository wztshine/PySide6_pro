"""
如果你的程序要读一个大文件，或者联网之类的事情，你会发现你的程序在这期间是不可使用的状态。这是因为你的程序一次只能做一件事情。
譬如下面的例子，当你运行程序后，会有一个计时器计时，当你点击 'stuck 5 second' 按钮后，程序会卡顿5秒
"""

from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer

import sys
import time

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("stuck 5 second!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        # 一个时间组件
        self.timer = QTimer()
        # 设置时间间隔 1 秒
        self.timer.setInterval(1000)
        # 设置时间间隔超时后，连接到 slot （每隔一秒，触发一次 slot）
        self.timer.timeout.connect(self.recurring_timer)
        # 开始计时模块
        self.timer.start()

    def oh_no(self):
        """sleep 5 seconds"""
        time.sleep(5)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
