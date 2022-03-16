import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Clock"
    property string currTime: "00:00:00"  // 定义一个字符串的属性：currTime，00:00:00 是默认值
    property QtObject backend  // QML支持的类型：bool, int, double, string, list, QtObject, var（var代表了任意python类型）

    // Connections 在我们后端 python 代码给 backend 属性等赋值时，会自动运行
    Connections {
        target: backend  // 定义了目标是 backend 这个属性，backend中携带了一个 updated 信号，下面的函数会自动处理这个信号
        // 函数名有特殊的规律： on+大写的首字母
        function onUpdated(msg) {
            currTime = msg;
        }
    }

    Rectangle {
        anchors.fill: parent

        Image {
            anchors.fill: parent
            source: "../images/background.png"
            fillMode: Image.PreserveAspectCrop  
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"  

            Text {
                
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12  
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime     // 文本设置成我们定义的属性
                font.pixelSize: 48
                color: "white"
            }
        }
    }
}