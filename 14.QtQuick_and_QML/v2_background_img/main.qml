import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {  // 主应用，设置窗口的可见性，大小，标题
    visible: true
    width: 600
    height: 500
    title: "Clock"

    // 定义一个四方形
    Rectangle {
        anchors.fill: parent  // 这个四方形，填充满父级对象

        Image {
            anchors.fill: parent  // 定义图片，填充父级对象
            source: "../images/background.png"
            fillMode: Image.PreserveAspectCrop  // 设置填充模式：保持图片比例，超出部分裁剪
        }

    // 也可以使用如下方式：
    //  Image {
    //      sourceSize.width: parent.width     // 设置宽高
    //      sourceSize.height: parent.height/2   // 可使用除法
    //      source: "../images/background.png"
    //      fillMode: Image.PreserveAspectCrop
    //  }

        // 这个方形堆叠在上面定义的 image 上面的（如果了解PhotoShop的话，可以理解为不同图层）。默认它的背景色是白色
        Rectangle {
            anchors.fill: parent
            color: "transparent"  // 设置颜色为透明

            Text {
                // 设置文字的锚点，也就是文字的位置（左下角，距离边缘 12 像素）
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12  // margin,有点像 web css 的margin
                    left: parent.left
                    leftMargin: 12
                }
                text: "16:38:33"
                font.pixelSize: 48
                color: "white"
            }
        }
    }
}