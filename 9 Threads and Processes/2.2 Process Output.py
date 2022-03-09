"""
在进程中运行其他脚本，可以获取输出结果
"""
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PySide6.QtCore import QProcess
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        # 追加文字到编辑区
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:
            self.message("Executing process")
            self.p = QProcess()
            # 准备可以读取标准输出
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            # 准备可以读取标准错误
            self.p.readyReadStandardError.connect(self.handle_stderr)
            # 进程状态改变
            self.p.stateChanged.connect(self.handle_state)
            # 进程完成时
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            # 启动进程
            self.p.start("python", ['../resource/dummy_script.py'])

    def handle_stderr(self):
        data = self.p.readAllStandardError()  # 返回的都是字节类型
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None


app = QApplication(sys.argv)

w = MainWindow()
w.show()
app.exec()


"""
进程的三种状态：
常量                 值       描述
QProcess.NotRunning	 0	 The process is not running.
QProcess.Starting	 1	 The process is starting, but the program has not yet been invoked.
QProcess.Running	 2	 The process is running and is ready for reading and writing.
"""
