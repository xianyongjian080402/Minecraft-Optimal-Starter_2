
import sys,os, requests, json, datetime
from os import path



from PyQt6.QtCore import *

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QtCore.QSize(1000, 533))
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
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(790, 0))
        self.scrollArea.setStyleSheet("border-style:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 790, 485))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setStyleSheet("border:2px double rgb(0, 150, 255);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setStyleSheet("border-style:none;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setStyleSheet("border-style:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setStyleSheet("border:2px double rgb(0, 150, 255);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_2.setStyleSheet("border-style:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_6.addWidget(self.textBrowser_2, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setStyleSheet("border-style:none;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 2)
        self.gridLayout_7.addWidget(self.widget_4, 0, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setStyleSheet("border:2px double rgb(0, 150, 255);")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setStyleSheet("border-style:none;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.widget_5)
        self.comboBox.setStyleSheet("border-style:none;")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget_5)
        self.pushButton.setStyleSheet("border-style:none;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_7.addWidget(self.widget_5, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
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
        self.pushButton_lianji.setStyleSheet("height:23px;\n"
"color: rgb(0, 150, 255);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;\n"
"border-radius: 10px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/online.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_lianji.setIcon(icon)
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.gridLayout_3.addWidget(self.pushButton_lianji, 2, 0, 1, 2)
        self.pushButton_music = QtWidgets.QPushButton(self.widget)
        self.pushButton_music.setStyleSheet("height:23px;\n"
"color: rgb(0, 150, 255);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;\n"
"border-radius: 10px;")
        self.pushButton_music.setObjectName("pushButton_music")
        self.gridLayout_3.addWidget(self.pushButton_music, 6, 0, 1, 2)
        self.pushButton_about = QtWidgets.QPushButton(self.widget)
        self.pushButton_about.setStyleSheet("height:23px;\n"
"color: rgb(0, 150, 255);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;\n"
"border-radius: 10px;")
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout_3.addWidget(self.pushButton_about, 9, 0, 1, 2)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget)
        self.pushButton_xiazai.setStyleSheet("height:23px;\n"
"color: rgb(0, 150, 255);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;\n"
"border-radius: 10px;")
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.gridLayout_3.addWidget(self.pushButton_xiazai, 4, 0, 1, 2)
        self.pushButton_home = QtWidgets.QPushButton(self.widget)
        self.pushButton_home.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_home.setStyleSheet("height:23px;\n"
"color: rgb(0, 150, 255);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;\n"
"border-radius: 10px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(20, 20))
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
"border-radius: 10px;")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/ico.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 2)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget)
        self.pushButton_shezhi.setStyleSheet("height:23px;\n"
"color: rgb(0, 150, 255);\n"
"background-origin: content;\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"text-align: left;\n"
"padding-right:10px;\n"
"font-size: 15px;\n"
"border-radius: 10px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_shezhi.setIcon(icon3)
        self.pushButton_shezhi.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.gridLayout_3.addWidget(self.pushButton_shezhi, 8, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 10, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MOS)

    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))
        self.label_4.setText(_translate("MOS", "公告"))
        self.label_5.setText(_translate("MOS", "杂谈"))
        self.label_3.setText(_translate("MOS", "选择要启动的游戏"))
        self.pushButton.setText(_translate("MOS", "PushButton"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_home.setText(_translate("MOS", "Home"))
        self.label.setText(_translate("MOS", "无用户"))
        self.label_2.setText(_translate("MOS", "点击添加"))
        self.pushButton_shezhi.setText(_translate("MOS", "设置"))





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
