"""
signal（信号)是当发生了某事时，由 widget（组件）发送出来的通知。比如：按下按钮，输入文本，窗口文本改变... 这些用户做出的行为，都可以触发信号
并且信号还可以提供一些关于发生了什么事情的，额外的上下文数据

slots（某些人翻译作：槽） 是信号（signal）的接收器。Python的任何函数或方法都可以用作 slot——只要连上 signal 就行了。
一些 widget 也有内置的 slot
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My APP")

        button = QPushButton("Press Me")

        # 将按钮的 clicked 信号，连接到 the_button_was_clicked 槽（slot) 上
        # 这样每按下一次按钮，就会发送一个信号给 the_button_was_clicked ，然后自动执行这个函数
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('Clicked!')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

"""
小结：
1. 当某些组件发生改变，或者用户触发了某些行为，都可以触发 signal， 如果我们想要捕获这种变化，就可以捕获信号，进行相应的处理，信号的接收器是 slot
2. 每个Python函数或方法都可以作为 slot 函数，只要和 signal 连接上就行了
"""