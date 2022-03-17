"""
直接加载 Qt Designer 生成的 .ui 文件，不用将其转换成 python 文件。
"""
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader


app = QtWidgets.QApplication(sys.argv)
loader = QUiLoader()
# 第二个参数是你要创建的 widget 的父级组件对象，因为我们 sample.ui 是一个独立的窗口，所以我们没给它绑定父级组件
window = loader.load("../resource/sample.ui", None)
window.show()
app.exec()
