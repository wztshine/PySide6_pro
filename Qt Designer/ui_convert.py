"""
开发者使用 Qt Designer 生成 ui 文件后，可以将其转换成 python 文件，这样可以直接导入和继承此文件。
"""
import pathlib
import sys
import subprocess

"""
转换其实很简单，命令行运行：
python安装路径/Scripts/pyside6-uic ui文件.ui -o 转换后的文件.py
"""


# pyside6-uic.exe 路径位于你 python 安装目录的 Scripts/ 下
pyside6_uic = str(pathlib.Path(sys.prefix) / "Scripts" / 'pyside6-uic')
ui_file = str(pathlib.Path('../resource/sample.ui').resolve())
subprocess.run(f'{pyside6_uic} {ui_file} -o sample.py')
# 上面的代码执行完成后，会在当前目录下生成一个 sample.py 文件，这就是ui文件转换后的python脚本


import sys
from PySide6 import QtWidgets

from sample import Ui_MainWindow  # sample 是上面转换后形成的 py 文件


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
