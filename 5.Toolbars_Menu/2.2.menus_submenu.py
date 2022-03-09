"""
子菜单：一个菜单项下面不再仅仅是一个Action（命令），还可以添加子菜单，然后子菜单中添加Action (菜单的某些功能，在 macOS 上可能不支持）
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
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("../resource/address-book--arrow.png"), "Your &button2", self)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # 创建菜单栏
        menu = self.menuBar()

        # 创建 &File 菜单项，并在菜单项中添加 Action
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

        # 添加一个分隔符
        file_menu.addSeparator()

        # 创建一个 子菜单项
        file_submenu = file_menu.addMenu("Submenu")
        # 子菜单项中添加一个 Action
        file_submenu.addAction(button_action2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


"""
菜单项中不仅可以 .addAction() 添加Action，还可以 .addMenu() 添加子菜单项，然后在子菜单项中添加 Action。
"""