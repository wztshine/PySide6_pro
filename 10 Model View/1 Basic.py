"""
MVC 就是 Model-View-Controller 架构。也就是模型层-视图层-控制层。模型层存储数据，视图层用来界面展示，控制层用来连接视图和模型层，
根据用户在界面上的操作，从而控制模型层，譬如改写某些数据。

模型层，需要继承抽象的模型类，它有几个基础的方法：data(), rowCount(), columnCount()
data(index, role):
    这个方法是控制视图层和模型层交互展示的。它接收两个参数 index, role.
    index：代表了视图层所请求的数据的位置，它有两个方法：index.row(), index.column()，分别代表了数据所在的行和列。
    role: 代表了需要返回数据的类型（视图层携带着role参数来请求某个位置的数据）：是仅用来展示的数据，还是可以被编辑的数据，又或者是图标，颜色等装饰性的数据。分为不同的类型。
        用户只要判断 role，然后返回不同的数据类型就行，不用关心怎么传递 role 参数
rowCount(index):
    这个方法代表了当前图表需要展示多少行数据，需要返回一个数字代表要展示多少行
columnCount(index):
    同上，代表要展示多少列数据，要返回一个数字。

视图层：
创建模型层后，需要将模型层和视图层绑定：xxx.setModel(self.model)，这样两者才会同步。

个人理解，可能有很大错误！！！仅供理解：
程序运行后，视图层会主动去数据层拿数据，来进行界面展示。在去视图层获取数据的过程中，视图层会携带 role 参数去 模型层的 data(index, role) 拿数据
针对每一个数据，视图层都会尝试用不同的 role 参数去获取结果，这样的话，针对每一个数据，可能会返回多个不同 role 的结果：
    譬如针对 DisplayRole -> 得到一个字符串
    针对 DecorationRole -> 得到一个图标
    针对 BackgroundRole -> 得到一个背景色
这样的话，每一个数据都可能返回多个不同的结果，视图层将这些结果互相叠加，显示出一个带有背景色的带图标的字符串
"""

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


# 模型类，存放一个类似于表格的数据
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        # 用来存储数据
        self._data = data

    def data(self, index, role):
        # DisplayRole 就是仅仅用来显示的数据
        if role == Qt.DisplayRole:
            # 获取数据所在的行列，然后返回某行某列的数据
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # 获取数据的行数
        return len(self._data)

    def columnCount(self, index):
        """展示多少列"""
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口大小
        self.resize(350, 200)
        self.table = QtWidgets.QTableView()

        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]
        # 实例化模型层
        self.model = TableModel(data)
        # 给视图设置模型
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()

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