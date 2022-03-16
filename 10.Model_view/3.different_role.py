from datetime import datetime
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        # 展示内容
        if role == Qt.DisplayRole:
            # 获取某行某列的原始数据
            value = self._data[index.row()][index.column()]
            # 判断数据类型，返回不同的数据格式，而不影响原始数据类型
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value
            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value
            # Default (anything not captured above: e.g. int)
            return value

        # 文本对齐方式
        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                # 垂直居中，水平右对齐
                return Qt.AlignVCenter + Qt.AlignRight

        # 添加前景色
        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if ((isinstance(value, int) or isinstance(value, float)) and value < 0):
                return QtGui.QColor('red')

        # 16进制颜色
        if role == Qt.BackgroundRole:
            COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d',
                      '#b2182b', '#67001f']
            value = self._data[index.row()][index.column()]
            if (isinstance(value, int) or isinstance(value, float)):
                value = int(value)  # Convert to integer for indexing.

                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10

                return QtGui.QColor(COLORS[value])

        # 给日期单元格的数据前面，添加一个 图标（每个单元格的前面都有一个装饰区，可以显示颜色，图标，图片等）
        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QtGui.QIcon('../resource/address-book--arrow.png')

            if (isinstance(value, int) or isinstance(value, float)):
                value = int(value)
                return QtGui.QColor('green')

    def rowCount(self, index):

        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口大小
        self.resize(350, 200)
        self.table = QtWidgets.QTableView()

        data = [
            [4, 9, 2],
            [1, -1, 'hello'],
            [3.023, 5, -5],
            [3, 3, datetime(2017, 10, 1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()

"""
Role	            Type
Qt.BackgroundRole	QBrush (also QColor)
Qt.CheckStateRole	Qt.CheckState
Qt.DecorationRole	QIcon, QPixmap, QColor
Qt.DisplayRole	    QString (also int, float, bool)
Qt.FontRole	        QFont
Qt.SizeHintRole	    QSize
Qt.TextAlignmentRole	Qt.Alignment
Qt.ForegroundRole	QBrush (also QColor)
"""