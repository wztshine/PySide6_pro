"""
QRC就是资源管理。当我们将 Qt 项目打包（譬如制作成 .exe 文件）时，我们的资源（图片，图标等）不会跟着打包，这会
导致你打包后的软件，根本找不到相应的图片或图标，所以出现了 QRC 这个东西，它可以将静态资源一起打包进代码中。
使用QRC，你需要制作 .qrc 文件，其实就是一个类似于 xml 的文件，QRC 文件的样例：
<!DOCTYPE RCC>
<RCC version="1.0">
    <qresource prefix="icons">
        <file alias="arrow.png">../resource/address-book--arrow.png</file>
    </qresource>
</RCC>
注意上面的代码：
<qresource> 这个标签 有个 prefix 属性，它代表了一个命名空间，可以简单理解为一个虚拟文件夹： icons/
<file> 标签的内容是文件的路径：../resource/address-book--arrow.png ; alias 属性代表的是这个路径的别名：arrow.png，以后在
    python 代码中，如果你想要使用这个路径的图片，可以写 icons/arrow.png，也就是这个别名

编写完 .qrc 文件后，需要将其转换一下： 将 xxx.qrc -> yyy.py
python安装路径/Scripts/pyside6-rcc xxx.qrc -o yyy.py
"""
import pathlib
import sys
import subprocess

# 转换当前路径下的 QRC_sample.qrc -> resource.py
pyside6_rcc = str(pathlib.Path(sys.prefix) / "Scripts" / 'pyside6-rcc')
qrc_file = str(pathlib.Path('QRC_sample.qrc').resolve())
subprocess.run(f'{pyside6_rcc} "{qrc_file}" -o resource.py')



from PySide6 import QtGui, QtWidgets

import resource  # 我们 qrc 转换成的 py 文件，导入进来


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.button = QtWidgets.QPushButton("My button")

        # :/ 这个前缀，代表了使用 QRC 资源内容； icons/ 是命名空间， arrow.png 是命名空间下的资源的 alias
        icon = QtGui.QIcon(":/icons/arrow.png")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.change_icon)

        self.setCentralWidget(self.button)

        self.show()

    def change_icon(self):
        icon = QtGui.QIcon(":/icons/butterfly")
        self.button.setIcon(icon)



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()


"""
1. 编写 .qrc 文件：
    <qresource> 标签的 prefix 属性值代表命名空间的名字，可以简单理解成虚拟文件夹
    <file> 标签的内容代表资源的路径，alias 属性代表使用时的别名
2. 转换 .qrc -> .py
    命令行运行： python安装路径/Scripts/pyside6-rcc xxx.qrc -o yyy.py
3. 导入转换后的 .py 文件
4. 想要使用资源，写成:":/虚拟文件夹/alias" 形式，其中 ":/" 代表引用的资源来自 QRC 系统
"""


