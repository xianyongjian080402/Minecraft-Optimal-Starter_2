
import sys,os, requests, json, datetime
from os import path

import MOS_rc

from PyQt6.QtCore import *

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 530)
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(231, 230, 228);")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_lianji = QtWidgets.QPushButton(self.widget)
        self.pushButton_lianji.setStyleSheet("background-image: url(:/img/picture/home.png);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;")
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.gridLayout_3.addWidget(self.pushButton_lianji, 2, 0, 1, 2)
        self.pushButton_music = QtWidgets.QPushButton(self.widget)
        self.pushButton_music.setStyleSheet("background-image: url(:/img/picture/home.png);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;")
        self.pushButton_music.setObjectName("pushButton_music")
        self.gridLayout_3.addWidget(self.pushButton_music, 6, 0, 1, 2)
        self.pushButton_about = QtWidgets.QPushButton(self.widget)
        self.pushButton_about.setStyleSheet("background-image: url(:/img/picture/home.png);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;")
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout_3.addWidget(self.pushButton_about, 9, 0, 1, 2)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget)
        self.pushButton_xiazai.setStyleSheet("background-image: url(:/img/picture/home.png);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;")
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.gridLayout_3.addWidget(self.pushButton_xiazai, 4, 0, 1, 2)
        self.pushButton_home = QtWidgets.QPushButton(self.widget)
        self.pushButton_home.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_home.setStyleSheet("background-image: url(:/img/picture/home.png);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;")
        self.pushButton_home.setObjectName("pushButton_home")
        self.gridLayout_3.addWidget(self.pushButton_home, 1, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("width:50px;\n"
"height:50px;\n"
"border-image: url(:/img/picture/ico.png);")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/ico.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(53, 53))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 2)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget)
        self.pushButton_shezhi.setStyleSheet("height:40px;\n"
"background-image: url(:/img/picture/shape.png);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;")
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.gridLayout_3.addWidget(self.pushButton_shezhi, 8, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 10, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        QtCore.QMetaObject.connectSlotsByName(MOS)

    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))
        self.pushButton.setText(_translate("MOS", "PushButton"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_home.setText(_translate("MOS", "    Home"))
        self.label.setText(_translate("MOS", "无用户"))
        self.label_2.setText(_translate("MOS", "点击添加"))
        self.pushButton_shezhi.setText(_translate("MOS", "        设置"))




if __name__ == '__main__':
    print ("程序已开始运行！")
    app = QtWidgets.QApplication(sys.argv)
    print ("请稍等...")
    MainWindow = QtWidgets.QMainWindow()
    print ("创建窗口对象成功！")
    ui = Ui_MOS()
    print ("创建PyQt窗口对象成功！")
    ui.setupUi(MainWindow)
    print ("初始化设置成功！")
    MainWindow.show()
    print ("已成功显示窗体")
    sys.exit(app.exec())
