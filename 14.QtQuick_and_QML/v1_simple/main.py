"""
QML(Qt Modeling Language), 可以用来定义用户界面，它不使用 QtWidget 类，因为它使用自身来创建窗口UI，
但是它可以使用其他如 QtCore, QtGui等。

"""

import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# 创建一个应用
app = QGuiApplication(sys.argv)

# 创建引擎，引擎绑定了应用的 quit 方法
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")  # 加载同级目录下的 qml 文件

sys.exit(app.exec())