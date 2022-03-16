import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    x: screen.desktopAvailableWidth - width - 0  // 窗口左上角距离屏幕左侧水平方向的位置
    y: screen.desktopAvailableHeight - height - 20  // 窗口左上角距离屏幕上方垂直方向的位置
    title: "Clock"
    flags: Qt.FramelessWindowHint | Qt.Window  // 设置成无边框的窗口类型 | Qt.Window 可以让窗口依然存在于任务栏

    property string currTime: "00:00:00"  
    property QtObject backend

    
    Connections {
        target: backend  
        
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
                text: currTime     
                font.pixelSize: 48
                color: "white"
            }
        }
    }
}