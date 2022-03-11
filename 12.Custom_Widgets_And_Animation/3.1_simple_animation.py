from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 当前组件的大小
        self.resize(600, 600)

        # 创建一个子组件
        self.child = QWidget(self)
        # 设置组件的样式和大小
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        # 一个动画效果：(要实现动画的组件，一个bytes类型的属性名称） pos 代表了组件的位置positoin
        # 代表了要对 self.child 的 位置属性进行动画的效果
        self.anim = QPropertyAnimation(self.child, b"pos")
        # 设置动画的终点（起点可以忽略）
        self.anim.setEndValue(QPoint(400, 400))
        # 设置动画的持续时间（默认250ms）
        self.anim.setDuration(1500)
        # 开始动画效果
        self.anim.start()

app = QApplication([])
window = Window()
window.show()
app.exec()


"""
1. 告诉 QPropertyAnimation 我们想要作用的组件(上面例子是 self.child) 以及 bytes 类型的属性名（b"pos")
2. [Optional] 动画的起始值
3. 动画的终点值
4. [Optional] 动画持续时间 [ms], 默认 250 ms.
"""