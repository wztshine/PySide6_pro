import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        # 按钮通常还有一个 checked 或 toggled 的状态（类似于开关那种按钮）。正常按钮的 checked 或 toggled 状态总是 False
        # 所以我们可以 setCheckable() 来赋予它可以切换状态
        button.setCheckable(True)

        # 一个信号，可以连接到多个 slot 上。clicked 信号会给 slot 发送一个按钮状态的信息，slot 可以选择接收或者不接收这个信息
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        """
        这个 slot 函数没有接受参数，按钮 click 时会发送 signal，它携带了按钮的状态，我们这里忽略了这个信息
        :return:
        """
        print("点击了!")

    def the_button_was_toggled(self, checked):
        """
        一个按钮按下后，它的 clicked 信号总是会携带一个参数来说明这个按钮是按下还是松开的状态，这里用参数接受了这个状态
        :param checked:
        :return:
        """
        print("选中状态?", checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


"""
小结：
1. 信号可以携带数据
2. 一个信号可以连接多个 slot
3. slot 可以选择接收或者不接收信号携带的数据（通过 slot 函数中添加相应的参数来接收数据）
"""