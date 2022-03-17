"""
树型结构的组件
"""

import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem


data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}

app = QApplication()

# 定义树形组件
tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

items = []
for key, values in data.items():
    item = QTreeWidgetItem([key])  # item 使用 key 来定义， 是一个大类别
    for value in values:
        ext = value.split(".")[-1].upper()  # 获取后缀
        child = QTreeWidgetItem([value, ext])  # child 就是一个小类别，拥有两列，所以添加了长度为 2 的列表
        item.addChild(child)
    items.append(item)

# 插入所有的项目到顶层
tree.insertTopLevelItems(0, items)

tree.show()
sys.exit(app.exec())
