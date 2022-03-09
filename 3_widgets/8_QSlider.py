"""
QSlider 是一个滑块，它和 QDoubleSpinBox 很像，只不过它不以数字显示，而是用滑块显示。它通常用来设置不太精确的数值，譬如音量。
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

        # 指定一个水平方向的滑块，或竖直方向：Qt.Vertical（默认不写参数是竖直方向）
        widget = QSlider(Qt.Horizontal)

        # 设置滑块的范围
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        # 设置滑动的步长
        widget.setSingleStep(3)

        # 数值变化时发出信号
        widget.valueChanged.connect(self.value_changed)
        # 滑块移动时发出信号
        widget.sliderMoved.connect(self.slider_position)
        # 滑块按下时
        widget.sliderPressed.connect(self.slider_pressed)
        # 滑块释放时
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
