"""
使用信号来更新时间，下面的代码有些绕，解释一下：
1. 创建了一个类：Backend, 它继承了 QObject（因为 Signal 只能用于 QObject对象）
2. Backend 类中创建了计时器，会定时发出信号
3. qml 文件中，预先定义好相关的属性（本例中 qml里面定义了一个 QObject 类型的 backend 属性用来接收上面的 Backend 类的实例）
4. qml 文件中，定义 Connections 对象，在这里面设置 target: backend 和 function（用来处理 backend 这个属性中的信号）
5. 将后端实例化的 backend 实例传递给 qml 属性
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


# 实例化 backend 对象，将其传递给 qml 模板中
backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)

backend.update_time()  # 初始化时间字符串，否则可能会显示 qml 定义的默认值 00:00:00
sys.exit(app.exec())
