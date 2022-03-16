"""
这一个例子，讲述了在循环过程中出现的问题。
运行下面的代码，无论你点击窗口中的哪个数字，下面 label 中的文字都会显示 9
"""
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QWidget, QLabel, QVBoxLayout, QHBoxLayout
)

import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        v = QVBoxLayout()
        h = QHBoxLayout()

        # 这里 a 其实是全局变量。在 for 循环完成后，依然可以访问这个变量
        for a in range(10):
            button = QPushButton(str(a))
            button.pressed.connect(
                # 尽管每次我们都传递了变量 a，但是创建这个按键时 a 的值没有传递进来，只有当发送信号时，才会发送a的值给 slot
                # 而当我们发送信号时，for循环早就遍历完成了，那时a的值是9
                # 想要解决这个问题，可以取消注释掉的那行，再试试
                lambda: self.button_pressed(a)
                # lambda x=a: self.button_pressed(x)
            )
            h.addWidget(button)

        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)
        self.setLayout(v)

    def button_pressed(self, n):
        self.label.setText(str(n))


app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()