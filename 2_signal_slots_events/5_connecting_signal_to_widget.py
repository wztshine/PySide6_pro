"""
某个信号被发出去后，可以直接连上某个widget的方法（将这个widget的方法当作 slot 函数）
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # 生成一个标签
        self.label = QLabel()

        # 一个单行输入框组件
        self.input = QLineEdit()

        # 输入框组件的 textChanged 信号连上 label.setText，将它当作 slot 接收者
        # 要注意的是，textChanged 信号会携带输入的文字，self.label.setText 也有一个参数，可以接收文本，将其设置成 label 上显示的文字
        self.input.textChanged.connect(self.label.setText)

        # 暂时忽略下方内容，下面创建一个竖直方向的布局，将组件放到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()