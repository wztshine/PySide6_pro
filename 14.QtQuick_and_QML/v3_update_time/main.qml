import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Clock"
    property string currTime: "00:00:00"  // 定义一个字符串的属性：currTime，00:00:00 是默认值

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