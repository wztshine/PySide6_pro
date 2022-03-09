"""
context menu，上下文菜单，当你在一个程序上右键时，显示出来的菜单。

下面的例子中用到了 QAction，QAction可以视为命令。我们可以将命令附加到菜单上或者工具栏上，这样我们点击工具栏或者菜单栏，就可以激发某些操作
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    # 重写 contextMenuEvent 这个事件处理器，所有的上下文相关的事件，都由它处理
    def contextMenuEvent(self, e):
        """
        e 参数，是一个 ContextMenu 事件对象。
        :param e:
        :return:
        """
        print(e)
        context = QMenu(self)
        # QAction('action name', parent_widget)  我们需要给 QAction 一个名字，还要绑定它的父级组件
        # 然后把 QAction 添加到 menu 中。
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())  # 退出时，要传递一个相对父级组件的位置给 exec()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()