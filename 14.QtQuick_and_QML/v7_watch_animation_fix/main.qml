import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 300
    height: 300
    x: screen.desktopAvailableWidth - width
    y: screen.desktopAvailableHeight - height
    title: "Clock"
    color: "transparent"  // 设置主窗口透明
    flags: Qt.FramelessWindowHint | Qt.Window

    property var hms: {'hours': 0, 'minutes': 0, 'seconds': 0 }
    property QtObject backend

    
    Connections {
        target: backend  

        function onHms(hours, minutes, seconds){
            hms = {"hours": hours, "minutes": minutes, "seconds": seconds}
        }
    }

    Image {
        id: clockface
        sourceSize.width: parent.width
        fillMode: Image.PreserveAspectFit
        source: "../images/clockface.png"

        Image {
            x: clockface.width/2 - width/2
            y: (clockface.height/2) - height/2
            scale: clockface.width/465
            source: "../images/hour.png"
            antialiasing: true

            transform: Rotation {
                origin.x: 12.5; origin.y: 166;
                angle: (hms.hours * 30) + (hms.minutes * 0.5) // 让时针根据分针进行偏移
            }
        }

        Image {
            x: clockface.width/2 - width/2
            y: clockface.height/2 - height/2
            source: "../images/minute.png"
            scale: clockface.width/465
            antialiasing: true
            transform: Rotation {
                origin.x: 5.5; origin.y: 201;
                angle: hms.minutes * 6
               // 定义了 angle 的动画效果
                Behavior on angle {
                    // 弹簧动画，类似于摆锤一样，来回摆动几下
                    SpringAnimation {
                        spring: 1;     // 效果的大小
                        damping: 0.2;  // 衰退率
                        modulus: 360   // 最大程度不超过 360 度
                    }
                }
            }
        }

        Image {
            x: clockface.width/2 - width/2
            y: clockface.height/2 - height/2
            source: "../images/second.png"
            scale: clockface.width/465
            antialiasing: true
            transform: Rotation {
                origin.x: 2;
                origin.y: 202;
                angle: hms.seconds * 6
                Behavior on angle {
                    SpringAnimation { spring: 3; damping: 0.2; modulus: 360 }
                }
            }
        }

        Image {
            x: clockface.width/2 - width/2
            y: clockface.height/2 - height/2
            source: "../images/cap.png"
            scale: clockface.width/465
        }
    }
}