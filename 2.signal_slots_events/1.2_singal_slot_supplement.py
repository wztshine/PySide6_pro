"""
演示了如何指定类型，来将不同类型的信号连接到 slot，还能指定发送某个类型的信号
"""
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, Signal, Slot


class Communicate(QObject):
    # 创建一个可选类型的信号：可以是 int，也可是 str
    speak = Signal((int,), (str,))

    def __init__(self, parent=None):
        super(Communicate, self).__init__(parent)

        # speak[int] 可以指定将 int 类型的信号，连接到某个 slot 上（这里将两个信号都连接到同一个 slot）
        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)

    # 声明一个 slot，可以接收 int，str两种类型（其实将下面的装饰器注释掉也没关系，这里只是演示一下它可以接收参数）
    @Slot(int)
    @Slot(str)
    def say_something(self, arg):
        if isinstance(arg, int):
            print("This is a number:", arg)
        elif isinstance(arg, str):
            print("This is a string:", arg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Communicate()

    someone.speak.emit(10)
    # 同样，可以指定发送某个类型的信号
    someone.speak[str].emit("Hello everybody!")
    # app.exec()