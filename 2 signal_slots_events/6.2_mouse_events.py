"""
所有的鼠标事件都是一个 QMouseEvent 对象，它包含了以下方法：
Method	          Returns
.button()	    Specific button that triggered this event
.buttons()	    State of all mouse buttons (OR'ed flags)
.globalPos()	Application-global position as a QPoint
.globalX()	    Application-global horizontal X position
.globalY()	    Application-global vertical Y position
.pos()	        Widget-relative position as a QPoint integer
.posF()	        Widget-relative position as a QPointF float
"""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e: QMouseEvent):
        """

        :param e: e 是一个 QMouseEvent 对象。所有的鼠标处理器处理的都是这个对象
        :return:
        """
        print(e)
        if e.button() == Qt.LeftButton:
            # 鼠标左键按下时，触发下面的操作
            self.label.setText("mousePressEvent LEFT")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
