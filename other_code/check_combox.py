import sys

from PySide6.QtWidgets import QComboBox, QLineEdit, QListWidgetItem, QListWidget, QCheckBox, QApplication, QVBoxLayout, \
	QWidget


class ComboCheckBox(QComboBox):
	def __init__(self, parent=None):
		"""initial function

		:param items: the items of the list
		"""
		super(ComboCheckBox, self).__init__()
		self.items = []
		self.text = QLineEdit()  # use to selected items

		self.list_widget = QListWidget()
		self.text.setReadOnly(True)
		self.setLineEdit(self.text)

		self.setModel(self.list_widget.model())
		self.setView(self.list_widget)

	def get_selected_text(self) -> list:
		"""get selected items text

		:return: The selected item text.
		"""
		ret = []
		for item in self.items:
			if item.isChecked():
				item.setStyleSheet("background-color: #87CEFA;")
				ret.append(item.text())
			else:
				item.setStyleSheet("background-color: #FFFFFF;")
		return ret

	def get_selected_index(self) -> list:
		"""Get selected item's index.

		:return: The indexes of the item.
		"""
		ret = []
		for i in range(len(self.items)):
			if self.items[i].isChecked():
				ret.append(i)
		return ret

	def show_selected(self):
		"""
		show selected items
		:return:
		"""
		ret = '; '.join(self.get_selected_text())
		self.text.setText(ret)

	def addItems(self, items):
		for txt in items:
			self.items.append(QCheckBox())
			self.items[-1].setText(txt)
			item = QListWidgetItem(self.list_widget)
			self.list_widget.setItemWidget(item, self.items[-1])
			self.items[-1].stateChanged.connect(self.show_selected)

	def getItems(self):
		return self.items

	def clear(self):
		self.items = []
		self.list_widget.clear()


class UiMainWindow(QWidget):
	def __init__(self):
		super(UiMainWindow, self).__init__()
		self.setWindowTitle('Test')
		self.resize(600, 400)
		self.combo = ComboCheckBox(self)
		self.combo.addItems(['a', 'b'])
		layout = QVBoxLayout()
		layout.addWidget(self.combo)
		self.setLayout(layout)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = UiMainWindow()
	ui.show()
	sys.exit(app.exec_())
