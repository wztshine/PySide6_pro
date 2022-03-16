"""
后端（py代码）和前端（qml）之间发送和接收数据，并根据数据的传输，实现钟表指针走动的效果
"""

import sys
import time

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer, QObject, Signal


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")


class Backend(QObject):
    updated = Signal(str)
    # 声明一个信号，发送三个int值，arguments 代表了三个值的名字
    hms = Signal(int, int, int, arguments=['hours', 'minutes', 'seconds'])

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(100)  
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        time_ = time.localtime()
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        self.updated.emit(curr_time)
        self.hms.emit(time_.tm_hour, time_.tm_min, time_.tm_sec)  # 发送信号


backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)

backend.update_time()
sys.exit(app.exec())
