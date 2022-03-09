"""
简单的演示各个常用组件的效果
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


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        # 一个垂直布局组件
        layout = QVBoxLayout()

        widgets = [
            QCheckBox,  # 单选框
            QComboBox,  # 下拉选项
            QDateEdit,  # 日期编辑
            QDateTimeEdit,  # 时间编辑
            QDial,          # 一个类似拨号的圆盘
            QDoubleSpinBox,  # 带小数的增减区域
            QFontComboBox,  # 字体选择下拉框
            QLCDNumber,     # 仿 LCD 显示器
            QLabel,         # 标签
            QLineEdit,      # 单行文本编辑
            QProgressBar,   # 进度条
            QPushButton,    # 按钮
            QRadioButton,
            QSlider,        # 滑动条
            QSpinBox,       # 带有小箭头，可以增加和减少整数的组件
            QTimeEdit,
        ]

        for w in widgets:
            # 将各组件加入到布局中
            layout.addWidget(w())

        widget = QWidget()
        # 给组件设置布局
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()