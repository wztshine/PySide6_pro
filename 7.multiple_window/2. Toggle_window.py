"""
我们可以调用代码关闭窗口
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys


class AnotherWindow(QWidget):
    """
    这个 'window' 是一个 widget， 如果它没有父级组件，它就会以一个自由漂浮的独立窗口而存在。
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w:
            # 调用 .close() 方法关闭窗口
            self.w.close()
            self.w = None
        else:
            self.w = AnotherWindow()
            self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()