import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    x: screen.desktopAvailableWidth - width - 0  
    y: screen.desktopAvailableHeight - height - 20  
    title: "Clock"

    property var hms: {'hours': 0, 'minutes': 0, 'seconds': 0 } // var 是一个通用类型，可以代表任意 python 类型
    property string currTime: "00:00:00"  
    property QtObject backend

    
    Connections {
        target: backend  
        
        function onUpdated(msg) {
            currTime = msg;
        }

        // 新声明一个函数，会自动处理 backend 属性中 携带的 hms 信号的内容（函数命名规则： on+信号首字母大写）
        function onHms(hours, minutes, seconds){
            // hms 不是一个字典，而是一个对象！可以通过 hms.key 来获取值: hms.hours, hms.minutes,...
            hms = {"hours": hours, "minutes": minutes, "seconds": seconds}
        }
    }

    Rectangle {
        anchors.fill: parent

        Image {
            anchors.fill: parent
            source: "../images/background.png"
            fillMode: Image.PreserveAspectCrop  
        }
        // 新创建一个 Image 对象，用来显示钟表上的数字
        Image {
            id: clockface  // 定义了id：clockface，以后可以使用 clockface 来代指当前对象
            sourceSize.width: parent.width  // 图片宽度：父级对象一样宽
            fillMode: Image.PreserveAspectFit  // 图片填充：保持比例自适应
            source: "../images/clockface.png"

            Image {
                x: clockface.width/2 - width/2
                y: (clockface.height/2) - height/2
                scale: clockface.width/465      // 图片放大几倍（465是当前 hour.png 的实际像素，这里是计算放大几倍）
                source: "../images/hour.png"
                antialiasing: true              // 消除图片锯齿

                // transform 定义了图片的转变效果
                transform: Rotation {           // Rotation 可以定义图片旋转
                    origin.x: 12.5; origin.y: 166;  // origin.x, origin.y 定义了图片旋转的心中点的位置（这个图片原始大小是：25*332，所以12.5，166是图片的中心）
                    angle: hms.hours * 30       // 旋转角度
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
                }
            }

            // 一个小红点，放置在钟表原点，代表了钟表指针转动的轴
            Image {
                x: clockface.width/2 - width/2
                y: clockface.height/2 - height/2
                source: "../images/cap.png"
                scale: clockface.width/465
            }
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