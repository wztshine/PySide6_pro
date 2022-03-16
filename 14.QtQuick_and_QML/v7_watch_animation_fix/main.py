"""
实现钟表指针走动的效果,完善展示效果
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
        self.hms.emit(time_.tm_hour, time_.tm_min, time_.tm_sec)  # 发送信号


backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)

backend.update_time()
sys.exit(app.exec())
