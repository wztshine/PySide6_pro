"""
QLabel 可以显示图片
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        # 设置窗口大小的上下限
        self.setMinimumSize(300, 200)
        self.setMaximumSize(800, 500)

        label = QLabel()

        # 给 label 可以设置一个 QPixmap 对象，就可以显示图片了
        label.setPixmap(QPixmap('../resource/butterfly.jpg'))

        # 可以自适应拉伸图片
        label.setScaledContents(True)

        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
