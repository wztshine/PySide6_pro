"""
一个简单的系统托盘，可以设置图标，还有托盘菜单，双击托盘图标，看看效果
"""
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PySide6 import QtWidgets


class Window(QMainWindow):
    def __init__(self, app):
        super(Window, self).__init__()
        self.system_tray(app)

    def system_tray(self, app):
        # 创建一个 QIcon 对象
        self.icon = QIcon("../resource/address-book--arrow.png")

        # 创建任务栏托盘，设置图标等
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        # 创建系统任务栏托盘菜单
        self.menu = QMenu()

        # 创建 Action
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)  # 给Aciton绑定上退出应用的 slot

        # 将 Action 添加到菜单(可以添加多个Action哦）
        self.menu.addAction(self.quit)
        # 托盘添加上下文菜单
        self.tray.setContextMenu(self.menu)
        # 点击托盘图标时，触发 slot
        self.tray.activated.connect(self.tray_active)

    def tray_active(self, reason):
        # 如果用户双击托盘图标
        if reason == QSystemTrayIcon.DoubleClick:
            # 切换窗口的隐藏和显示
            if self.isVisible():
                self.hide()
            else:
                self.show()


app = QApplication([])
# 设置关闭窗口时，是否退出应用（不退出，就放到系统托盘）
app.setQuitOnLastWindowClosed(False)
window = Window(app)
window.show()
app.exec()
