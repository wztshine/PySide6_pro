"""
菜单，一个窗口中经常使用的功能。一个 Action 被添加到菜单和工具栏后，两者是互通的，点击两者中的任意一个，另一个都会跟着联动。
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
        button_action.setCheckable(True)

        button_action2 = QAction(QIcon("../resource/address-book--arrow.png"), "&Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.setCheckable(True)

        toolbar.addAction(button_action)
        toolbar.addAction(button_action2)

        # 创建菜单栏
        menu = self.menuBar()
        # 菜单栏添加一个菜单项：File
        file_menu = menu.addMenu("File")
        # 菜单项添加一个 Action （因为这个Action和工具栏上添加的是同一个，所以菜单和工具栏可以联动，两者是同步的哦）
        file_menu.addAction(button_action)
        # 菜单中添加一个分隔符
        file_menu.addSeparator()
        # 再次添加一个 Action
        file_menu.addAction(button_action2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
