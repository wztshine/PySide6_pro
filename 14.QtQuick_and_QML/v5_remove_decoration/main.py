"""
移除装饰：移除标题，最大化、最小化、关闭窗口按钮（可以通过任务栏关闭）
"""

import sys
import time

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer, QObject, Signal

# 创建一个应用
app = QGuiApplication(sys.argv)

# 创建引擎，引擎绑定了应用的 quit 方法，并且加载 qml 文件
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")


class Backend(QObject):
    updated = Signal(str)

    def __init__(self):
        super().__init__()

        # Define timer.
        self.timer = QTimer()
        self.timer.setInterval(100)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        # Pass the current time to QML.
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        self.updated.emit(curr_time)


backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)

backend.update_time()
sys.exit(app.exec())
