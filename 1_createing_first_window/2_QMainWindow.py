"""
QMainWindow 简单介绍
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)

# 之前说过，任何单独一个 widget 都可以是一个窗口，但是如果一个窗口只包含一个小组件，显然太单一了，没什么太大用处，因此我们还是需要对组件进行布局
# 将组件放到一个大窗口里面，QMainWindow 提供了一个标准的窗口，包含了：工具栏，菜单栏，状态栏...
window = QMainWindow()

window.show()
app.exec_()