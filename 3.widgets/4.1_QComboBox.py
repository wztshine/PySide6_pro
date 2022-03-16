"""
QComboBox 是下拉选项，我们可以通过 .addItem() 来添加选项。
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        # 批量添加选项
        widget.addItems(["One", "Two", "Three"])

        # 从 currentIndexChanged 默认发出去的信号是 选项的索引
        widget.currentIndexChanged.connect(self.index_changed)

        # currentTextChanged，可以发送选项的文本内容
        widget.currentTextChanged.connect(self.content_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i, type(i))

    def content_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()