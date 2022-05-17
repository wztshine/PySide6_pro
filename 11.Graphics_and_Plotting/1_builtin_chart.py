"""
一个根据表格数据，绘制饼图的小程序
"""
import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QPainter
from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.items = 0

        # 示例数据
        self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
                      "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
                      "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}

        # 左边的表格
        self.table = QTableWidget()
        self.table.setColumnCount(2)  # 表格几列
        self.table.setHorizontalHeaderLabels(["Description", "Price"])  # 表头
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动拉伸表格宽度

        # 图表部分：创建图表的视图
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)  # 图表渲染时，消除锯齿

        # 右边的添加，清除，绘制等按钮
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.plot = QPushButton("Plot")

        # 禁用添加按钮
        self.add.setEnabled(False)

        # 设置布局，将各组件添加到布局中
        self.right = QVBoxLayout()
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # 水平布局
        self.layout = QHBoxLayout()

        # 添加到布局
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        # 布局应用到当前窗口
        self.setLayout(self.layout)

        # 给各按钮绑定 slot
        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)

        # 填充图表
        self.fill_table()

    @Slot()
    def add_element(self):
        """给表格添加元素

        :return:
        """
        # 获取用户输入的描述和价格的文本
        des = self.description.text()
        price = self.price.text()

        try:
            # 创建表格子项（类似于单元格）
            price_item = QTableWidgetItem(f"{float(price):.2f}")
            description_item = QTableWidgetItem(des)

            # 设置文本对齐方式（靠右对齐）
            price_item.setTextAlignment(Qt.AlignRight)

            # 插入一行
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, description_item)  # 给坐标为某行某列的单元格设置内容
            self.table.setItem(self.items, 1, price_item)

            # 清空输入框的内容
            self.description.setText("")
            self.price.setText("")

            self.items += 1
        except ValueError:
            print("Wrong price", price)

    @Slot()
    def check_disable(self, s):
        """如果输入框没有文字内容，就将 add 按钮禁用

        :param s:
        :return:
        """
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def plot_data(self):
        """绘制数据饼图

        :return:
        """
        # 创建一个饼图的数据序列
        series = QPieSeries()
        for i in range(self.table.rowCount()):  # 遍历行
            text = self.table.item(i, 0).text()  # 遍历每一行中的单元格，获取内容
            number = float(self.table.item(i, 1).text())
            series.append(text, number)  # 添加数据（标签，值）

        # 创建图表，添加序列，设置图例
        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)  # 图例的对齐方式
        # 给视图设置图表
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):  # 退出应用
        QApplication.quit()

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            # QTableWidgetItem 是表格的子项，即单元格
            description_item = QTableWidgetItem(desc)
            price_item = QTableWidgetItem(f"{price:.2f}")
            price_item.setTextAlignment(Qt.AlignRight)
            # 插入一行
            self.table.insertRow(self.items)
            # 设置单元格
            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)
            self.items += 1

    @Slot()
    def clear_table(self):  # 清除图表，将行数设置为0
        self.table.setRowCount(0)
        self.items = 0


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    # 应用程序
    app = QApplication(sys.argv)
    # 实例化自定义的组件
    widget = Widget()
    # MainWindow 作为主窗口，把 widget 作为窗口中的内容
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # 执行应用
    sys.exit(app.exec())