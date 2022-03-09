"""
SpinBox 是一个带有数字的区域，可以使用小箭头增加和减少数字
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
        super().__init__()

        self.setWindowTitle("My App")

        # QSpinBox 是整数类型的，QDoubleSpinBox() 是浮点数类型的
        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        # 设置数字的取值范围：最小值和最大值
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        # 设置数字显示的前缀和后缀
        widget.setPrefix("$")
        widget.setSuffix("c")

        # 设置数字的步长：即每次增加或减少 3
        widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox

        # ValueChanged 信号只会携带数字， textChanged 会携带前缀和后缀作为字符串
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i, type(i))

    def value_changed_str(self, s):
        print(s, type(s))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
