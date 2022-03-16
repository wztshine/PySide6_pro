"""
一个窗口可以有很多组件，那么这个窗口就是这些组件的父级组件，这就是它的层级关系。
当一个事件发生在某个组件上时，你可以让这个组件忽略这个事件，那么事件就会层层向上传递给父级组件，直到这个事件被处理。
"""

from PySide6.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def mousePressEvent(self, e):
        e.accept()  # 表示事件被处理了

class CustomButton(QPushButton):
    def event(self, e):
        e.ignore()  # 表示事件未处理，会向上传递