"""
QLabel
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        # 一个 label 组件，内容是：Hello
        label = QLabel("Hello")

        # 从 label 组件中，提取它的 font 对象，并给 font 设置字体大小
        font = label.font()
        font.setPointSize(30)
        
        # 重新将字体设置给 label 组件
        label.setFont(font)

        # 设置 label 的对齐方式：水平对齐|竖直对齐，| 的作用，见下面解析
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

"""
| 的作用：
    Qt.AlignLeft 的16进制值 0x0001,  Qt.AlignBottom 的16进制值 0x0040. 
    两者进行 | 运算，得到 0x0041 代表 'bottom left'. 


水平对齐方式：
Qt.AlignLeft	左对齐
Qt.AlignRight	右对齐
Qt.AlignHCenter	水平居中
Qt.AlignJustify	自动对齐

竖直对齐方式：
Qt.AlignTop	    顶部
Qt.AlignBottom	底部
Qt.AlignVCenter	居中

水平和竖直：
Qt.AlignCenter	水平和竖直方向都居中
"""