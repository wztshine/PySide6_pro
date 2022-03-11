"""
之前的例子中，动画的运动速率是恒定的，这显得不太真实
"""
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSequentialAnimationGroup


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")

        # 三种不同的效果，每一种都取消注释尝试一下
        # self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        # self.anim.setEasingCurve(QEasingCurve.OutInCubic)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)

        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
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