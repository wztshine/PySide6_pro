"""
QPropertyAnimation()：
    不仅可以接收 widget 作为参数，还可以接收 effect(特效）作为参数，然后控制特效效果，所有应用了这个特效的组件，都会被影响
动画的组合：
    QSequentialAnimationGroup：可以添加多个动画，执行完一个动画后后，再执行下一个
    QParallelAnimationGroup：添加多个动画，这些动画同时执行
"""

from PySide6.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSequentialAnimationGroup, QParallelAnimationGroup


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        # 创建一个透明度的特效，作用于 self.child 上（这个特效单独是不起作用的）
        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)

        self.anim2 = QPropertyAnimation(self.child, b'size')
        self.anim2.setEndValue(QPoint(400, 400))
        self.anim.setDuration(2500)

        # 这个动画启用了透明度的特效，它并没有直接作用于 self.child, 而是直接传递了 effect 给它
        self.anim3 = QPropertyAnimation(effect, b'opacity')  # 第一个参数是 effect
        self.anim3.setStartValue(0)  # 设置透明度为0：全透明
        self.anim3.setEndValue(1)
        self.anim3.setDuration(2500)

        # 创建一个串行的群组，会让里面的动画一个接一个的进行
        # self.group = QSequentialAnimationGroup()
        # self.group.addAnimation(self.anim)
        # self.group.addAnimation(self.anim2)
        # self.group.start()

        # 创建一个并行的群组，可以让动画同时进行
        self.grou2 = QParallelAnimationGroup()
        self.grou2.addAnimation(self.anim3)
        self.grou2.addAnimation(self.anim)
        self.grou2.start()

app = QApplication([])
window = Window()
window.show()
app.exec()
