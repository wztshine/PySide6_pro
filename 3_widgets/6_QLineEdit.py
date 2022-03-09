"""
QLineEdit 是一个单行文本编辑区域
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QListWidget,
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

        widget = QLineEdit()
        # 限制输入文本的长度：10个字符
        widget.setMaxLength(10)
        # 设置默认提示文字
        widget.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True)  # 只读状态，不允许编辑

        # 输入框文本变化时，触发信号
        widget.textChanged.connect(self.text_changed)
        # 输入框文本被用户编辑时，触发信号（只有用户编辑，才会触发）
        widget.textEdited.connect(self.text_edited)
        # 输入框内敲击回车键，触发信号
        widget.returnPressed.connect(self.return_pressed)
        # 输入框内文字被选中，触发信号
        widget.selectionChanged.connect(self.selection_changed)

        self.setCentralWidget(widget)


    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


"""
除了限制输入长度，还可以限制输入的格式或内容：譬如下面的代码，可以限制输入ip地址类似的内容：
widget.setInputMask('000.000.000.000;_')

"""
