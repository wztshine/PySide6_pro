"""
补充小结：自定义一个带有信号的组件
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt, Signal



class Button(QPushButton):  # 继承自 QPushButton，它的底层继承了 QObject（要记住，如果想用 Signal 必须使用 QObject 对象）
    click_ed = Signal(Qt.MouseButton)  # 自定义了一个信号，信号类型是 Qt.MouseButton

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        """重写鼠标事件，点击时，让 click_ed 这个发出信号"""
        self.click_ed.emit(event.button())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        button = Button("sss")

        # 将按钮的 click_ed 信号，连接到 the_button_was_clicked 槽（slot) 上
        # 这样每按下一次按钮，就会发送一个信号给 the_button_was_clicked ，然后自动执行这个函数
        button.click_ed.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    @Slot()
    def the_button_was_clicked(self, button):
        print(button.name)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

"""
小结：
只有 QObject 对象才能使用信号。
信号可以有很多类型。

============== 信号的定义方式 =================
signal1 = Signal(int)  # Python types
signal2 = Signal(QUrl)  # Qt Types
signal3 = Signal(int, str, int)  # more than one type
signal4 = Signal((float,), (QDate,))  # optional types


============== 信号的参数：name ====================
signal5 = Signal(int, name='rangeChanged')  # name 属性可以给信号重命名，不指定这个name的话，会默认用变量名来作为信号名
rangeChanged.emit(...)

============== 信号的参数2：arguments ==========
sumResult = Signal(int, arguments=['sum'])  # arguments参数是给 qml 系统用的（qml是一个前端页面模板语言系统）

qml中这样写：
Connections {
    target: ...
    function onSumResult(sum) {  // onSumResult 是信号 sumResult 的 slot 函数。sum就是它的参数名字
        // do something with 'sum'
    }
"""