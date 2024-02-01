import math
import random
import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import *


class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 800, 500)
		self.setWindowTitle("Gift")
		self.showMaximized()  # 自动最大化窗口

		layout = QHBoxLayout()

		# 设置人数的取值范围：最小值和最大值
		label = QLabel("人数")
		self.people_number = 1
		self.input_box = QSpinBox()
		self.input_box.setMinimum(1)
		self.input_box.setMaximum(300)
		self.input_box.setToolTip("1 ~ 300")
		self.input_box.valueChanged.connect(self.input_box_changed)

		layout.addWidget(label)
		layout.addWidget(self.input_box)

		button = QPushButton("匹配")
		button.clicked.connect(self.shuffle_and_fill)
		layout.addWidget(button)

		# 表格行列数
		self.table = QTableWidget()
		self.row = 25
		self.col = 9  # 这个数一定要是 3 的倍数，否则可能会有问题。这是因为我们后续会让每 3 列作为一组来填充列。如果数据不是 3 的倍数会有问题。
		self.table.setRowCount(self.row)
		self.table.setColumnCount(self.col)

		# 设置单元格的宽高
		# self.row_height = 30
		# self.col_width = 100
		# self.set_column_width(self.col_width)
		# self.set_row_height(self.row_height)

		# 隐藏行列表头(或者叫表格的行列号，譬如 excel 中的顶部的 A,B,C... 列名）
		# self.table.verticalHeader().setVisible(False)
		# self.table.horizontalHeader().setVisible(False)

		# 行列填满屏幕
		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 根据空间自动拉伸
		self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
		"""
		QHeaderView.ResizeMode.ResizeToContents  # 根据单元格内容自适应宽度或高度
		QHeaderView.ResizeMode.Stretch           # 根据表格空间自动拉伸每个单元格的宽度或高度
		QHeaderView.ResizeMode.Interactive       # 用户交互式。即用户可以在程序中使用鼠标修改宽度或高度（默认值）
		QHeaderView.ResizeMode.Fixed             # 固定值。用户不可更改宽度或高度。
		
		当表格设置了 ResizeToContents 或者 Stretch 时， setColumnWidth(index, value) 不会生效。
		"""
		layout.addWidget(self.table)
		self.setLayout(layout)

	def input_box_changed(self, n):
		self.people_number = n

	def set_table_size(self, length):
		"""动态设置表格的列数，来扩大表格。

		:param length:
		:return:
		"""
		col = math.ceil(length / self.row)
		# 保证是 3 的倍数
		if col > self.col:
			self.col = col
			val = self.col % 3
			if val == 1:
				self.col += 2
			elif val == 2:
				self.col += 1
			self.table.setColumnCount(self.col)

	def shuffle_and_fill(self):
		"""根据人数构造列表[1,2,3,...]，并打乱列表。然后将列表填充表格。

		:return:
		"""
		# 先清空表格
		self.table.clear()

		people_nums = list(range(1, self.people_number + 1))
		random.shuffle(people_nums)

		people_nums = self.construct_data(people_nums)
		self.set_table_size(len(people_nums))
		people_nums = iter(people_nums)

		# 优先横向填充
		# for r in range(self.row):
		# 	for c in range(self.col):
		# 		try:
		# 			val = next(people_nums)
		# 		except StopIteration:
		#           return
		# 		else:
		# 			cell = QTableWidgetItem(f"{val}")
		# 			if val == "":
		# 				cell.setBackground(self.get_rgb_from_hex("#FFFFFF"))
		# 			else:
		# 				cell.setBackground(self.get_rgb_from_hex("#FFFF88"))
		# 			self.table.setItem(r, c, cell)

		# 优先竖向填充
		col = 0  # 填充起始列
		while 1:
			for r in range(self.row):
				for c in range(3):  # 每次填充 3 列
					c += col
					try:
						val = next(people_nums)
					except StopIteration:
						return
					else:
						cell = QTableWidgetItem(f"{val}")
						if val == "":
							cell.setBackground(self.get_rgb_from_hex("#FFFFFF"))
						else:
							cell.setBackground(self.get_rgb_from_hex("#FFFF88"))
						self.table.setItem(r, c, cell)
			col += 3  # 起始列右移 3 列
			if col >= self.col:
				break

	def get_rgb_from_hex(self, code):
		"""16进制颜色字符串转换成颜色

		:param code:
		:return:
		"""
		code_hex = code.replace("#", "")
		rgb = tuple(int(code_hex[i:i + 2], 16) for i in (0, 2, 4))
		return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

	def construct_data(self, data: list):
		"""

		:param data:
		:return:
		"""
		# 每隔两个数，插入一个空值，这是为了模拟中间空了一列，留出间隔。
		new_data = []
		for i, d in enumerate(data, start=1):
			new_data.append(d)
			if i % 2 == 0:
				new_data.append("")
		try:
			# 当倒数第二个值是 "", 说明最后还剩一个数值，没有成对出现。这里把这个数值前移到原本应该留空的列
			if new_data[-2] == "":
				del new_data[-2]
		except IndexError:
			pass
		return new_data

	def set_column_width(self, val: int):
		"""批量设置每列的宽度

		:param val: 每列的宽度
		:return:
		"""
		for i in range(self.col):
			self.table.setColumnWidth(i, val)

	def set_row_height(self, val: int):
		"""批量设置每行的高度

		:param val: 每行的高度
		:return:
		"""
		for i in range(self.row):
			self.table.setRowHeight(i, val)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = Table()
	form.show()
	sys.exit(app.exec())
