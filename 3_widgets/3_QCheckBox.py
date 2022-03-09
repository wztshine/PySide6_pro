"""
单选框
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox()
        # 设置成已选中的状态
        widget.setCheckState(Qt.Checked)  # 这个方法要手动传递一个状态参数
        # widget.setChecked(True)  # 和上面等同，都是设置选中，传递bool类型

        # 单选框默认只有两种状态，如果想有三种状态，可以运行下面的代码
        # widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)

        # 给 stateChanged 信号绑定 slot 函数
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        """
        slot 函数可以接收一个参数：代表了勾选框的状态
        :param s:
        :return:
        """
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


"""
勾选框的三种状态：
Qt.Unchecked	未选中
Qt.PartiallyChecked	部分选中（通常有很多项目时，只选中一部分内容）
Qt.Checked	    选中
"""