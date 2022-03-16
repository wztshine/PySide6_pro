"""
添加一个可以自动更新的时间
"""

import sys
import time

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer

# 创建一个应用
app = QGuiApplication(sys.argv)

# 创建引擎，引擎绑定了应用的 quit 方法，并且加载 qml 文件
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")

def update_time():
    # 生成当前时间的字符串
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    # 将时间赋值给 rootObjects()，rootObjects() 返回的是 qml 文件中的根对象：ApplicationWindow，所以我们给第一个 ApplicationWindow 设置属性
    engine.rootObjects()[0].setProperty("currTime", curr_time)  # currTime 是 qml 中定义的属性名

# 一个计时器对象
timer = QTimer()
timer.setInterval(100)  # 设置时间间隔 100ms
timer.timeout.connect(update_time)  # 计时器超时(100ms后)，就触发 update_time
timer.start()  # 开启计时

update_time()  # 初始化时间字符串，否则可能会显示 qml 定义的默认值 00:00:00
sys.exit(app.exec())