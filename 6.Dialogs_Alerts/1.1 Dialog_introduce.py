"""
一个最普通的对话框
"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        # 按钮连接到 slot 上， slot 中会创建一个对话框
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        # 创建对话框: QDialog(父级组件)，对话框一旦弹出，就会阻塞用户和父级组件的交互，直到对话框被关闭
        dlg = QDialog(self)
        # 设置对话框标题
        dlg.setWindowTitle("HELLO!")
        # 执行对话框，让它弹出（这会给对话框创建一个事件循环）
        dlg.exec_()


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()