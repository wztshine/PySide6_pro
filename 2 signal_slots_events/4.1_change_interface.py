"""
通过信号，我们可以知道发生了什么事情，然后通过 slot 接收信号，可以在 slot 中改变界面的显示
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        # 连上 slot
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        # 改变按钮的显示文本
        self.button.setText("You already clicked me.")

        # 让按钮置灰，变得不可用
        self.button.setEnabled(False)

        # 改变窗口标题
        self.setWindowTitle("My Oneshot App")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

"""
小结：
通过 slot 接收信号，我们可以进行相应的处理，达到自己想要的效果
"""