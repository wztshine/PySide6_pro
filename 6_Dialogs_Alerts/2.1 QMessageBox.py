"""
一个消息对话框
"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        # 创建消息对话框，绑定在当前窗口(self)上
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        # 设置消息对话框的消息内容
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()