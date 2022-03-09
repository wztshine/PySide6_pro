from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0
        self.setWindowTitle("My App")
        self.setFixedSize(300, 200)

        self.button = QPushButton("Press Me!")
        # 1. 给按钮的 clicked 信号 连接 slot 函数，这个 slot 函数会改变窗口标题文字
        self.button.clicked.connect(self.the_button_was_clicked)

        # 2. 窗口组件的 windowTitleChanged 信号，连上 slot 函数，以后一旦窗口标题改动，会触发 the_window_title_changed 这个 slot 函数
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        # 3. 改变了窗口标题，会触发窗口的信号
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        # 4. 当窗口标题改变，会触发了这个 slot 函数
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()


"""
小结：
这个例子主要讲了：按钮按下的信号引发了按钮的slot函数，slot 函数中改变了窗口的标题，而这个改变窗口标题的动作，又触发了窗口的信号，
从而又触发了窗口标题改变的 slot 函数。也就是说，我们可以写一系列连锁反应。

注意：
windowTitleChanged 信号不一定每次都会触发，只有当你当前的标题和上一次标题不同时才会触发，如果两次标题相同，则不会触发！
"""