"""
event，事件
每一个用户的操作，都是一个事件。事件有很多类型，每种类型都代表了用户不同的交互操作。
Qt 用事件对象来代表事件，每一个事件对象都封装了用户交互的信息，当事件发生时，每个事件都会传递给组件相应的事件处理器来处理。
我们也可以自定义事件处理器来处理事件，事件处理器和普通函数是一样的，只不过它拥有自己特殊的名字。

譬如：QMouseEvent，它代表了鼠标的移动和点击操作，它拥有下面的事件处理器
    处理器	     代表事件
mouseMoveEvent	   鼠标移动
mousePressEvent	   鼠标点击
mouseReleaseEvent  鼠标释放
mouseDoubleClickEvent 鼠标双击
"""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    # 通过重写鼠标的事件处理器，可以自定义事件处理
    def mouseMoveEvent(self, e):
        """鼠标按下的同时，移动鼠标"""
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        # super(MainWindow, self).mousePressEvent()  # 通过继承父类的方法，可以让鼠标依然正常运行，同时还能执行自己下方自定义的其他操作
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

"""
小结：
通过重写事件处理器，我们可以自定义一些事件的处理方式。
上面的代码中，我们只能按下鼠标的同时移动鼠标，才会触发鼠标移动事件，想要只移动鼠标就能触发这个事件，需要在 __init__()方法中，添加如下代码：
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
上面的代码会对窗口和窗口中的label组件设置鼠标跟踪。
"""