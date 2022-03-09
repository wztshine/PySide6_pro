"""
QRC就是资源管理。当我们将 Qt 项目打包（譬如制作成 .exe 文件）时，我们的资源（图片，图标等）不会跟着打包，这会
导致你打包后的软件，根本找不到相应的图片或图标，所以出现了 QRC 这个东西，它可以将静态资源一起打包进代码中。

QRC 文件的样例：
<!DOCTYPE RCC>
<RCC version="1.0">
    <qresource prefix="icons">
        <file alias="penguin.png">animal-penguin.png</file>
        <file alias="monkey.png">animal-monkey.png</file>
    </qresource>
</RCC>

注意上面的代码：
<qresource> 这个标签 有个 prefix 属性，它代表了一个虚拟文件夹，意味着文件夹是： icons/
<file> 标签的内容是文件的路径：animal-penguin.png （这是图片的路径）; alias 属性代表的是这个路径的别名：penguin.png，以后在
    python 代码中，如果你想要使用这个路径的图片，可以直接写 penguin.png，也就是这个别名

"""


