"""
widget 可以设置类似于 CSS 样式，更多样式：https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placeholder text")
    w.resize(300,100)
    w.setAlignment(Qt.AlignCenter)
    w.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        """)
    w.show()
    sys.exit(app.exec())