"""
一个消息对话框，可以自定义按键和图标样式
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
        # 创建消息对话框，绑定在当前窗口(self)上
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")

        # 设置消息对话框的消息内容
        dlg.setText("This is a simple dialog")

        # 设置对话框上面有哪些按键
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # 设置对话框左侧的图标：问号样式
        dlg.setIcon(QMessageBox.Information)

        # 执行对话框，关闭时会返回用户按下的按键信息
        button = dlg.exec()
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No")


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