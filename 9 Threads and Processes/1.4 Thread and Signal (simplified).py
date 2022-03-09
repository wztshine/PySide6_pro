"""
简化版的自定义信号发送数据
"""
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool

import sys
import time


class WorkerSignals(QObject):
    # 定义了Signal，这个 signal 发送 int 类型的数据
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self):
        super(Worker, self).__init__()
        # 实例化信号类
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        """
        你要在线程中执行的代码，写在这个函数中
        """
        for i in range(100):
            time.sleep(1)
            # 每隔1秒，发送一次信号
            self.signals.progress.emit(i)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        # 每次点击这个按钮，就会启动一个线程！可以点击多次按钮，然后看控制台输出内容
        b = QPushButton("Click me!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()

        # 线程池
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def progress_fn(self, n):
        """这个 slot 函数将接收到的信号传输的数据，打印出来"""
        print(n)

    def oh_no(self):
        # 实例化线程类
        worker = Worker()
        # 将线程类中的信号，连接到 self.progress_fn 这个 slot 上
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()

"""
流程：
1. 定义信号类，设置信号和信号发送数据的类型
2. 将信号在 QRunnable 的线程类中实例化，在 run() 函数中根据需要 emit 数据
3. 在主线程中实例化 线程类，将线程类中的信号，连接到某个 slot 上来接收数据。
4. threadPool.start(线程类实例) 
"""