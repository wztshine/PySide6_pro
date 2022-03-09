"""
通过编写 QDialog 子类，我们可以自定义对话框的内容和格式
"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel


# 对话框子类
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")
        # 使用 '|' 组合 OK 和 Cancel 键； QBtn 现在是一个整数，代表了这两个按键
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        # 我们需要将 buttons 传递给 QDialogButtonBox 来生成对话框中的按键
        self.buttonBox = QDialogButtonBox(QBtn)
        # 也可以用这种方式添加按键
        self.buttonBox.addButton(QDialogButtonBox.Close)

        # 想要按键生效，必须要将它们连接到对话框的 slot 上。我们这里将 accepted,rejected 信号连到了 self.accept, self.reject 上，
        # 这两个方法都是 QDialog 类内置的方法。
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # 想要 QDialogButtonBox 显示在对话框中，必须把它放到对话框的 layout 上
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        # 按钮连接到 slot 上， slot 中会创建一个对话框
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        # 创建对话框对象，如果给它绑定一个父级组件，则对话框会基于父级组件的窗口位置的中央弹出，否则就基于屏幕中央弹出
        dlg = CustomDialog(self)
        # dlg = CustomDialog()

        if dlg.exec():
            print('OK')
        else:
            print("Cancel!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

"""
可用的按键选项：
QDialogButtonBox.Ok
QDialogButtonBox.Open
QDialogButtonBox.Save
QDialogButtonBox.Cancel
QDialogButtonBox.Close
QDialogButtonBox.Discard
QDialogButtonBox.Apply
QDialogButtonBox.Reset
QDialogButtonBox.RestoreDefaults
QDialogButtonBox.Help
QDialogButtonBox.SaveAll
QDialogButtonBox.Yes
QDialogButtonBox.YesToAll
QDialogButtonBox.No
QDialogButtonBox.Abort
QDialogButtonBox.Retry
QDialogButtonBox.Ignore
QDialogButtonBox.NoButton
"""