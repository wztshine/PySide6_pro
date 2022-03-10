"""
一个使用 PyQt5 实现的，MVC架构（模型层，视图层，控制层）的待办事项处理程序。
需要安装 PyQt5: pip install PyQt5
"""
import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

# 一个 Qt Designer 导出的 .ui 文件，加载它
qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

tick = QtGui.QImage('tick.png')


# 模型层视图，用来存储：待办事项
class TodoModel(QtCore.QAbstractListModel):
    """继承自 QAbstractListModel，一个列表显然有 row, column 两个属性"""
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []  # todos: [(bool, str), ...]; bool 代表事项是否完成，str 是事项的名称
        
    def data(self, index, role):
        """
        这个方法定义了模型层和视图层交互时，如何处理和显示数据
        :param index: 代表了数据所在的 row, column，所以它有这两个方法： index.row(), index.column()
        :param role: 数据代表的角色
        :return:
        """
        print(f"index is: {index}, row is: {index.row()}, role is: {role}")
        # displayRole 代表要显示的内容
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        # DecorationRole 代表要要渲染的内容，如图标，颜色
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        """
        这个方法定义了我们的视图层，显示多少行数据，我们需要返回一个数
        :param index:
        :return:
        """
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # 运行并加载 Ui_MainWindow 中的界面
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.model = TodoModel()
        # 加载数据库中的数据
        self.load_db()
        # 这些都是从 .ui 加载出来的 widget 中继承来的
        # todoView 是一个 QListView 对象，代表一系列代办事项
        # addButton 就是添加按钮，可以添加一个代办事项
        # deleteButton 删除事项
        # completeButton 将事项标记成完成状态
        self.todoView.setModel(self.model)  # QListView 对象的 setModel 方法，将模型和视图绑定
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        添加一个事项到代办列表中
        """
        text = self.todoEdit.text()
        if text:
            # 获取事项列表，追加进去
            self.model.todos.append((False, text))
            # layoutChanged 信号说明数据模型的大小发生变化了（多了数据)，所以需要刷新布局
            self.model.layoutChanged.emit()
            # 清空用户输入的事项
            self.todoEdit.setText("")
            # 保存到数据库
            self.save()
        
    def delete(self):
        # 获取用户选中的那些行
        indexes = self.todoView.selectedIndexes()  # 返回的一个列表
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
            
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged 是数据发生变化时，我们触发的操作，让视图仅仅刷新当前位置，也就是左上角和右下角，都是同一行数据：index。
            # takes top-left and bottom right, which are equal
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    
    def load_db(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

"""
各种角色代表的值和描述
角色          	    值	描述
Qt.DisplayRole	    0	The key data to be rendered in the form of text. (QString)
Qt.DecorationRole	1	The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap)
Qt.EditRole	        2	The data in a form suitable for editing in an editor. (QString)
Qt.ToolTipRole	    3	The data displayed in the item's tooltip. (QString)
Qt.StatusTipRole	4	The data displayed in the status bar. (QString)
Qt.WhatsThisRole	5	The data displayed for the item in "What's This?" mode. (QString)
Qt.SizeHintRole	    13	The size hint for the item that will be supplied to views. (QSize)

更多角色: https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum
"""
