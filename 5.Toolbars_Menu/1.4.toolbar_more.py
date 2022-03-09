"""
介绍让工具栏的按钮变成 Checkable 状态（普通按钮只能 Clickable）
另外介绍了工具栏不仅可以添加 Action，还可以添加普通 widget
"""

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("../resource/address-book--arrow.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # 设置按钮 checkable
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        # 在工具栏下一个组件之间，添加一个分割线
        toolbar.addSeparator()

        # 工具栏添加普通 widget
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

"""
1. 一个 Action 可以设置 checkable：
    button_action.setCheckable(True)
2. 工具栏可以添加普通的 widget
3. 工具栏的组件之间，可以添加分隔符：
    toolbar.addSeparator()
"""