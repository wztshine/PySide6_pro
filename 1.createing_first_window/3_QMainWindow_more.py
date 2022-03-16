"""
QMainWindow 子类自定义窗口
"""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# QMainWindow 的子类，用来自定义窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 必须调用父类方法生成对象

        # 设置窗口的命令
        self.setWindowTitle("My App")
        # 创建一个按钮
        button = QPushButton("Press Me")
        # 将按钮置于窗口中央
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()