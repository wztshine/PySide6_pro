"""
一个简单的系统托盘，可以设置图标，还有托盘菜单
"""
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# 创建一个 QIcon 对象
icon = QIcon("../resource/address-book--arrow.png")

# 创建任务栏托盘，设置图标等
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# 创建系统任务栏托盘菜单
menu = QMenu()

# 创建几个Action
action = QAction("A menu item")
quit = QAction("Quit")
quit.triggered.connect(app.quit)  # 给Aciton绑定上推出应用的 slot

# 将 Action 添加到菜单
menu.addAction(action)
menu.addAction(quit)

# 托盘添加上下文菜单
tray.setContextMenu(menu)

app.exec()