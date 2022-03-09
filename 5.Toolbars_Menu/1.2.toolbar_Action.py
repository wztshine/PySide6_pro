"""
一个 QAction，就相当于一个命令。它的好处是：一个Action可以同时添加到菜单中和工具栏中。

譬如复制命令：你可以使用快捷键 Ctrl+C, 可以从工具栏复制按钮，可以从菜单中选择复制命令。
    如果你使用Button 来做，你需要分别给菜单，工具栏各自写一个 Button，然后绑定
    如果用Action做，你只需要写一个Action就行了。
"""

import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # 1. 生成工具栏
        toolbar = QToolBar("My main toolbar")

        # 2. 将工具栏添加到主窗口
        self.addToolBar(toolbar)

        # 3. 创建 QAction(Action名字， 父级组件） self 代表了主窗口这个组件，QAction 的这个参数必须是 QObject 对象。
        button_action = QAction("Your button", self)

        # 设置一个状态栏：QStatusBar 实例化时，要传递给一个父级组件对象
        self.setStatusBar(QStatusBar(self))
        # 设置Action的状态栏提示
        button_action.setStatusTip("This is your button")

        # 4. 给 Action 添加触发时的 slot
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        # 5. 将 Action 添加到工具栏对象上
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


"""
添加工具栏的几个步骤：
1. 创建一个工具栏对象：QToolBar
2. 将工具栏对象添加到当前窗口上：self.addToolBar()
3. 创建Action 对象
4. 给 Action 对象添加触发时的 slot 
5. 将 Action 对象添加到工具栏对象上：toolbar.addAction()

主窗口 -> 工具栏对象 -> Action 对象 -> 绑定 slot 
"""