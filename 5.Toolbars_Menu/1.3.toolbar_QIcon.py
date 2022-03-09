"""
QIcon 就是一个图标对象，可以添加到其他组件上，让组件拥有图标
"""

import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # 1. 生成工具栏
        toolbar = QToolBar("My main toolbar")
        # 2. 事先设置工具栏中 Icon 的大小，16x16像素
        toolbar.setIconSize(QSize(16, 16))
        # 3. 添加工具栏到当前窗口
        self.addToolBar(toolbar)

        # 4. 创建 QAction(QIcon对象，Action名字， 父级组件）； 很多其他组件的第一个参数，也可以使用 QIcon 对象来填充图标
        button_action = QAction(QIcon('../resource/address-book--arrow.png'), "Your button", self)

        # 5. 给 Action 添加触发时的 slot
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        # 6. 将 Action 添加到工具栏对象上
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()