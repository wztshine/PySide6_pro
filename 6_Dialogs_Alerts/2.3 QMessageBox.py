"""
消息对话框的简洁写法：
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)

或者自定义按键：
QMessageBox.warning(parent, title, message, buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard)

"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        # 这样写：QMessageBox.question(parent, title, message)
        button = QMessageBox.question(self, "Question dialog", "The longer message")
        # 还可以自定义按键和默认选中的按键
        button2 = QMessageBox.question(self, "Question 2", 'Question22222', buttons=QMessageBox.Ok|QMessageBox.Discard, defaultButton=QMessageBox.Discard)

        # 注意：我们上面这种写法不用 .exec() 来执行弹窗，上面写法的返回值，就是我们按下的按键
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


"""
消息对话框可以设置的按键有：
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Discard
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.RestoreDefaults
QMessageBox.Help
QMessageBox.SaveAll
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
QMessageBox.NoButton


消息对话框左侧的图标样式有：
Icon state	Description
QMessageBox.NoIcon	    没有图标
QMessageBox.Question	问号图标：一个？
QMessageBox.Information	提示图标：一个i
QMessageBox.Warning	    警告图标
QMessageBox.Critical	致命警告

"""