from datetime import datetime
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
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

        # 给第三列数据添加背景色
        if role == Qt.BackgroundRole and index.column() == 2:
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