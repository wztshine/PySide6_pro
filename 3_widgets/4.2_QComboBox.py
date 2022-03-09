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

        # 将下拉选项设置成可以编辑的状态，这样用户动态插入选项！
        widget.setEditable(True)
        # 设置选项动态插入后的排序：以字母顺序排列
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        # 设置最多有几个选项
        widget.setMaxCount(10)

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


"""
动态插入的排序方式：

Flag	Behavior
QComboBox.NoInsert	    不插入
QComboBox.InsertAtTop	在第一个元素位置插入
QComboBox.InsertAtCurrent	取代当前的选项
QComboBox.InsertAtBottom	最后插入
QComboBox.InsertAfterCurrent	Insert after current item
QComboBox.InsertBeforeCurrent	Insert before current item
QComboBox.InsertAlphabetically	Insert in alphabetical order
"""