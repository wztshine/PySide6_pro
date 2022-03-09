import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 通过将属性绑定在当前实例上，实现数据的存储
        self.button_is_checked = True
        self.setWindowTitle("My App")

        # 同样，也可以将 button 绑定在实例上，来存放数据
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

"""
小结：
想要存放数据，可以将数据乃至其他组件，作为主窗口的属性，这样可以在主窗口的实例的任意函数中调用这个属性。
"""