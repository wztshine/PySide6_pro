you can look through this blog: https://blog.csdn.net/Enderman_xiaohei/article/details/109261980

Using custom widget in qt designer: https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/#:~:text=Right%20click%20on%20the%20widget%20and%20select%20Promote,choosing%20Demote%20to%20from%20the%20widget%27s%20context%20menu.

备忘：
想要让整个窗口中的元素，都可以随着窗口自适应，需要在**窗口**空白处右键(不要选中任何元素或者布局，因为我们需要针对窗口) - layout - 选择一种layout方式。
这样你的窗口最大化或者更改大小时，便可以自动拉伸里面的元素了

想要使用自定义的控件。可以先创建一个小控件，然后右键它 - promote to - promoted class name 处填写你的控件的 类名； Header file 处写你的模块名。
譬如你有个 `core` 包，里面有个 `ui` 模块文件，文件里有个 `Checkable` 类。你的 `promoted class name` 就写 `Checkable` ，Header file 写：`core.ui` 