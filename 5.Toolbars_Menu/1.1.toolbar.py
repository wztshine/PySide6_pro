import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # 创建一个 工具栏，并添加到当前窗口（运行后，在工具栏处右键才能看到）
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()