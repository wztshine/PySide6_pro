"""
创建第一个窗口
"""

from PySide6.QtWidgets import QApplication, QWidget

import sys

# 每个应用只需要一个 QApplication 实例， sys.argv 可以从命令行获取参数，QApplication([]) 也能执行。
app = QApplication(sys.argv)

# 获取一个窗口组件(在QT中，所有顶级 widget 都是‘窗口’-- 意味着它不需要父级组件或布局，任何 widget 都可以直接创建一个 window)
window = QWidget()

# 显示窗口，因为窗口默认是隐藏的！
window.show()
# window.hide()  同样，你也可以主动隐藏窗口

# 开启事件循环，一直阻塞，直到用户关闭窗口
app.exec_()


"""
总结：
1. 一个应用只需要一个 QApplication
2. 每个 widget（组件）都可以直接创建一个窗口
3. 窗口默认是隐藏的，需要调用 .show() 来显示它
4. app.exec() 会启动事件循环，直到用户关闭窗口
"""