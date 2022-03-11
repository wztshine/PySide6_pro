"""
如何使用 property 触发信号。因为后续的动画部分，原理就是这样：修改 QPropertyAnimation 的属性，会触发它的自动刷新功能，实现动画的效果。
"""
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
from PySide6.QtCore import Property, Signal


class CustomWindow(QMainWindow):
    # 设置一个会发送 int 类型的信号
    valueChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._value = 0

        # 设置两个组件
        self.label = QLabel("null")
        self.button = QPushButton('click')

        # 添加组件到当前窗口
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        w = QWidget(self)
        w.setLayout(layout)
        self.setCentralWidget(w)

        # 按钮触发增加 value 的 slot 函数
        self.button.clicked.connect(self.add_value)
        # 信号连接到 slot 函数
        self.valueChanged.connect(self.value_changed)

    # 将 value 设置成一个属性（int类型）
    @Property(int)
    def value(self):
        return self._value

    # 添加设置 value 的功能（python基础知识，属性的 setter 方法）
    @value.setter
    def value(self, value):
        if value != self._value:
            self._value = value
            self.valueChanged.emit(value)  # 当属性值变动时，发出信号

    def add_value(self):
        # 给 value 增加值，会触发 value.setter
        self.value += 1

    def value_changed(self, value):
        self.label.setText(str(value))


app = QApplication([])
window = CustomWindow()
window.show()
app.exec()