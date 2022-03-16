"""
相对于 v1,添加了背景图片等内容
"""

import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# 创建一个应用
app = QGuiApplication(sys.argv)

# 创建引擎，引擎绑定了应用的 quit 方法，并且加载 qml 文件
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")

sys.exit(app.exec())