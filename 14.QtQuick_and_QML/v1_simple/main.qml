import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {  // 主应用，设置窗口的可见性，大小，标题
    visible: true
    width: 600
    height: 500
    title: "Clock"

    // 窗口内的文本设置
    Text {
        anchors.centerIn: parent  // 以父级组件为基准，居中
        text: "Hello World"
        font.pixelSize: 24
    }
}