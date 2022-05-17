"""
widget 可以设置类似于 CSS 样式，更多样式：https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea
QSS其实就像是CSS文件，我们可以单独将样式提取出来，放到文件中，然后从文件读取内容，给窗口设置样式。
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, \
    QHBoxLayout


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.resize(500, 500)

        menu_widget = QListWidget()
        for i in range(9):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        text_widget = QLabel("This is the lable content")
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication()
    window = Widget()

    with open('StyleSheet.qss', 'r', encoding='utf8') as f:
        style = f.read()
        window.setStyleSheet(style)

    window.show()
    sys.exit(app.exec())
