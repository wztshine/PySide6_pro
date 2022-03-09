"""
使用线程池来创建线程
"""
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer
from PySide6.QtCore import QRunnable, Slot, QThreadPool

import sys
import time


# 一个线程类
class Worker(QRunnable):
    @Slot()  # QtCore.Slot
    def run(self):
        """
        这个方法里面放你想要在线程中执行的代码
        :return:
        """
        print("Thread start")
        time.sleep(5)
        print("Thread complete")


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.counter = 0
        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("thread 5 second!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        # 创建一个线程池
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # 一个时间组件
        self.timer = QTimer()
        # 设置时间间隔 1 秒
        self.timer.setInterval(1000)
        # 设置时间间隔超时后，连接到 slot （每隔一秒，触发一次 slot）
        self.timer.timeout.connect(self.recurring_timer)
        # 开始计时模块
        self.timer.start()

    def oh_no(self):
        # 实例化线程类
        worker = Worker()
        # 在线程池中启动线程
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()


"""
要点：
1. 将你想要在线程中执行的代码 worker，写到一个继承了 QRunnable 的类的 run() 方法中。你可以在这个类中编写其他任何方法，也可以接收任何参数，
    然后在 run() 中调用它们
2. 建立一个线程池，将线程类放到线程池中执行：threadpool.start(worker)
"""