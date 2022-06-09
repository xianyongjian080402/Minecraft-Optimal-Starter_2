
import sys,os, requests, json, datetime
from os import path

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.\site-packages\PyQt5\Qt5\plugins'  #### 这一行是新增的。用的是相对路径。

from PyQt6.QtCore import *

from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS_catalogue_picture_ico_png = os.path.join("picture","ico.png")
        MOS_catalogue_picture_home_png = os.path.join("picture","home.png")
        MOS_catalogue_picture_online_png = os.path.join("picture","online.png")
        MOS_catalogue_picture_download_png = os.path.join("picture","download.png")
        MOS_catalogue_picture_music_png = os.path.join("picture","music.png")
        MOS_catalogue_picture_settings_png = os.path.join("picture","settings.png")
        MOS_catalogue_picture_about_png = os.path.join("picture","about.png")
        MOS_catalogue_picture_david_png = os.path.join("picture","david.jpg")
        MOS_catalogue_picture_heimnad_png = os.path.join("picture","heimnad.png")


        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QtCore.QSize(1000, 533))
        MOS.setStyleSheet("QMainwindow{\n"
"    border-radius:15px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_mos_left = QtWidgets.QWidget(self.centralwidget)
        self.widget_mos_left.setAutoFillBackground(False)
        self.widget_mos_left.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setObjectName("widget_mos_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_mos_left)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_mos_left_top = QtWidgets.QWidget(self.widget_mos_left)
        self.widget_mos_left_top.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-style:none;\n"
"    border-radius:15px;\n"
"}\n"
"QWidget::hover\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QWidget::pressed\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"")
        self.widget_mos_left_top.setObjectName("widget_mos_left_top")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_mos_left_top)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_mos_left_top_user = QtWidgets.QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_user.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_mos_left_top_user.setObjectName("label_mos_left_top_user")
        self.gridLayout_4.addWidget(self.label_mos_left_top_user, 0, 1, 1, 1)
        self.pushButton_mos_left_top = QtWidgets.QPushButton(self.widget_mos_left_top)
        self.pushButton_mos_left_top.setStyleSheet("width:50px;height:50px;border-radius: 23px;background-color: rgba(255, 255, 255, 0);")
        self.pushButton_mos_left_top.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_ico_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_mos_left_top.setIcon(icon)
        self.pushButton_mos_left_top.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_mos_left_top.setObjectName("pushButton_mos_left_top")
        self.gridLayout_4.addWidget(self.pushButton_mos_left_top, 0, 0, 2, 1)
        self.label_mos_left_top_add = QtWidgets.QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_add.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_mos_left_top_add.setObjectName("label_mos_left_top_add")
        self.gridLayout_4.addWidget(self.label_mos_left_top_add, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_mos_left_top)
        self.line_2 = QtWidgets.QFrame(self.widget_mos_left)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.pushButton_home = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_home.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_home.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_home_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_2.addWidget(self.pushButton_home)
        self.pushButton_lianji = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_lianji.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_online_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_lianji.setIcon(icon2)
        self.pushButton_lianji.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.verticalLayout_2.addWidget(self.pushButton_lianji)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_xiazai.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_download_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_xiazai.setIcon(icon3)
        self.pushButton_xiazai.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.verticalLayout_2.addWidget(self.pushButton_xiazai)
        self.pushButton_music = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_music.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_music_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_music.setIcon(icon4)
        self.pushButton_music.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_music.setObjectName("pushButton_music")
        self.verticalLayout_2.addWidget(self.pushButton_music)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_shezhi.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_settings_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_shezhi.setIcon(icon5)
        self.pushButton_shezhi.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.verticalLayout_2.addWidget(self.pushButton_shezhi)
        self.pushButton_about = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_about.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_about_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_about.setIcon(icon6)
        self.pushButton_about.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_2.addWidget(self.pushButton_about)
        spacerItem = QtWidgets.QSpacerItem(20, 184, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_mosll = QtWidgets.QLabel(self.widget_mos_left)
        self.label_mosll.setStyleSheet("color: rgb(0, 150, 255);font-size: 17px;font: 75 17pt \"Yuanti SC\";background-color: rgba(240, 239, 238,0);")
        self.label_mosll.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mosll.setObjectName("label_mosll")
        self.verticalLayout_2.addWidget(self.label_mosll)
        self.gridLayout_13.addWidget(self.widget_mos_left, 0, 0, 1, 1)
        self.stackedWidget_mos_right = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_mos_right.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.stackedWidget_mos_right.setObjectName("stackedWidget_mos_right")
        self.page_gonggao = QtWidgets.QWidget()
        self.page_gonggao.setObjectName("page_gonggao")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_gonggao)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_page_gonggao = QtWidgets.QScrollArea(self.page_gonggao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_page_gonggao.sizePolicy().hasHeightForWidth())
        self.scrollArea_page_gonggao.setSizePolicy(sizePolicy)
        self.scrollArea_page_gonggao.setMinimumSize(QtCore.QSize(790, 0))
        self.scrollArea_page_gonggao.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 128);")
        self.scrollArea_page_gonggao.setWidgetResizable(True)
        self.scrollArea_page_gonggao.setObjectName("scrollArea_page_gonggao")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 811, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.widget_scrollArea_page_gonggao_left = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_left.setStyleSheet("border:2px solid rgb(0, 150, 255);border-radius:15px;")
        self.widget_scrollArea_page_gonggao_left.setObjectName("widget_scrollArea_page_gonggao_left")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_left)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser_gonggao_left_txt = QtWidgets.QTextBrowser(self.widget_scrollArea_page_gonggao_left)
        self.textBrowser_gonggao_left_txt.setStyleSheet("border-style:none;")
        self.textBrowser_gonggao_left_txt.setObjectName("textBrowser_gonggao_left_txt")
        self.gridLayout_5.addWidget(self.textBrowser_gonggao_left_txt, 1, 0, 1, 1)
        self.label_gonggao_left_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_left)
        self.label_gonggao_left_txt.setStyleSheet("border-style:none;")
        self.label_gonggao_left_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gonggao_left_txt.setObjectName("label_gonggao_left_txt")
        self.gridLayout_5.addWidget(self.label_gonggao_left_txt, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_left, 0, 0, 1, 1)
        self.widget_scrollArea_page_gonggao_right = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_right.setStyleSheet("QWidget  {\n"
"    border:2px solid rgb(0, 150, 255);border-radius:15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 77);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.widget_scrollArea_page_gonggao_right.setObjectName("widget_scrollArea_page_gonggao_right")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_right)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_scrollArea_page_gonggao_statring = QtWidgets.QWidget(self.widget_scrollArea_page_gonggao_right)
        self.widget_scrollArea_page_gonggao_statring.setStyleSheet("border-style:none;")
        self.widget_scrollArea_page_gonggao_statring.setObjectName("widget_scrollArea_page_gonggao_statring")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_statring)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_3.setStyleSheet("border-style:none;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)
        self.label_7 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 4, 2, 1)
        self.progressBar = QtWidgets.QProgressBar(self.widget_scrollArea_page_gonggao_statring)
        self.progressBar.setStyleSheet("border-style:none;")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)
        self.gridLayout_6.addWidget(self.widget_scrollArea_page_gonggao_statring, 1, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 3, 1, 1, 1)
        self.pushButton__gonggao_start = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right)
        self.pushButton__gonggao_start.setObjectName("pushButton__gonggao_start")
        self.gridLayout_6.addWidget(self.pushButton__gonggao_start, 2, 1, 1, 1)
        self.comboBox_gonggao_right = QtWidgets.QComboBox(self.widget_scrollArea_page_gonggao_right)
        self.comboBox_gonggao_right.setObjectName("comboBox_gonggao_right")
        self.gridLayout_6.addWidget(self.comboBox_gonggao_right, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 3, 0, 1, 1)
        self.label__gonggao_right_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_right)
        self.label__gonggao_right_txt.setStyleSheet("border-style:none;")
        self.label__gonggao_right_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__gonggao_right_txt.setObjectName("label__gonggao_right_txt")
        self.gridLayout_6.addWidget(self.label__gonggao_right_txt, 0, 0, 1, 2)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_right, 0, 1, 1, 1)
        self.scrollArea_page_gonggao.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_page_gonggao)
        self.stackedWidget_mos_right.addWidget(self.page_gonggao)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(49, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_9.setIndent(10)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setStyleSheet("color:rgb(214, 214, 214)")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 2, 0, 1, 2)
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setStyleSheet("border-radius:10px;border:2px solid rgb(0, 150, 255);")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_8.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setStyleSheet("border-style:none;color:rgb(0, 150, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_5, 3, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 4, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 77);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_3.setObjectName("page_3")
        self.gridLayout = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 2, 1)
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 2)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setStyleSheet("QAbstractItemView::item {\n"
"    min-height: 110px;\n"
"    min-width: 40px; \n"
"}")
        self.page_9.setObjectName("page_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_9)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_9.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 50, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(self.page_10)
        self.label_11.setGeometry(QtCore.QRect(200, 70, 171, 16))
        self.label_11.setObjectName("label_11")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_3.setGeometry(QtCore.QRect(410, 50, 91, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_4.setGeometry(QtCore.QRect(450, 180, 91, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_19 = QtWidgets.QLabel(self.page_10)
        self.label_19.setGeometry(QtCore.QRect(240, 200, 171, 16))
        self.label_19.setObjectName("label_19")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 180, 113, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_5.setGeometry(QtCore.QRect(440, 280, 91, 32))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_20 = QtWidgets.QLabel(self.page_10)
        self.label_20.setGeometry(QtCore.QRect(230, 300, 171, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 280, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_6 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_6.setGeometry(QtCore.QRect(460, 360, 91, 32))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_21 = QtWidgets.QLabel(self.page_10)
        self.label_21.setGeometry(QtCore.QRect(250, 380, 171, 16))
        self.label_21.setObjectName("label_21")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 360, 113, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget_2.addWidget(self.page_10)
        self.gridLayout.addWidget(self.stackedWidget_2, 4, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_10.setIndent(10)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 2, 1)
        self.stackedWidget_mos_right.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_12.setIndent(10)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.page_4)
        self.line_4.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 2, 0, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.page_4)
        self.widget_8.setStyleSheet("border-radius:10px;\n"
"border:2px solid rgb(0, 150, 255);")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_10.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_13 = QtWidgets.QLabel(self.widget_8)
        self.label_13.setStyleSheet("border-style:none;color:rgb(0, 150, 255);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_8, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(832, 393, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 4, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.line_5 = QtWidgets.QFrame(self.page_5)
        self.line_5.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout_15.addWidget(self.line_5, 2, 0, 2, 2)
        spacerItem10 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_15.addItem(spacerItem10, 0, 0, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(796, 368, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_15.addItem(spacerItem11, 5, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_15.setIndent(10)
        self.label_15.setObjectName("label_15")
        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 2)
        self.widget_9 = QtWidgets.QWidget(self.page_5)
        self.widget_9.setStyleSheet("border-radius:10px;\n"
"border:2px solid rgb(0, 150, 255);")
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_11.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_14 = QtWidgets.QLabel(self.widget_9)
        self.label_14.setStyleSheet("border-style:none;color:rgb(0, 150, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 1, 0, 1, 1)
        self.gridLayout_15.addWidget(self.widget_9, 4, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem12 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_14.addItem(spacerItem12, 0, 0, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.page_6)
        self.label_17.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_17.setIndent(10)
        self.label_17.setObjectName("label_17")
        self.gridLayout_14.addWidget(self.label_17, 1, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.page_6)
        self.line_6.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout_14.addWidget(self.line_6, 2, 0, 1, 2)
        self.widget_10 = QtWidgets.QWidget(self.page_6)
        self.widget_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setStyleSheet("border-radius:15px;border:2px solid rgba(0, 150, 255, 128);")
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_13)
        self.label.setStyleSheet("border-style:none;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.widget_11 = QtWidgets.QWidget(self.widget_13)
        self.widget_11.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_11)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton = QtWidgets.QPushButton(self.widget_11)
        self.pushButton.setStyleSheet("border-style:none;")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_12.addItem(spacerItem13, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_11)
        self.label_16.setStyleSheet("border-style:none;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_13)
        self.widget_12.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_18 = QtWidgets.QLabel(self.widget_12)
        self.label_18.setStyleSheet("border-style:none;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_17.addWidget(self.label_18, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_4.setStyleSheet("border-style:none;")
        self.pushButton_4.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_david_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_17.addWidget(self.pushButton_4, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_17.addItem(spacerItem14, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_14)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_22 = QtWidgets.QLabel(self.widget_14)
        self.label_22.setStyleSheet("border-style:none;")
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_9.setStyleSheet("border-style:none;")
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_heimnad_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_18.addWidget(self.pushButton_9, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_18.addItem(spacerItem15, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.gridLayout_19.addWidget(self.widget_13, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(796, 368, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_19.addItem(spacerItem16, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.widget_10, 3, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_6)
        self.gridLayout_13.addWidget(self.stackedWidget_mos_right, 0, 1, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MOS)

    #=================================分割线===================================#

    def click_pushButton_home(self):
        self.stackedWidget_mos_right.setCurrentIndex(0)
        pushButton_home_true = ("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setStyleSheet(pushButton_home_true)

    def click_pushButton_lianji(self):
        self.stackedWidget_mos_right.setCurrentIndex(1)
        pushButton_lianji_true = ("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setStyleSheet(pushButton_lianji_true)

    def click_pushButton_xiazai(self):
        self.stackedWidget_mos_right.setCurrentIndex(2)
        pushButton_xiazai_true = ("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setStyleSheet(pushButton_xiazai_true)

    def click_pushButton_music(self):
        self.stackedWidget_mos_right.setCurrentIndex(3)
        pushButton_music_true = ("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setStyleSheet(pushButton_music_true)

    def click_pushButton_shezhi(self):
        self.stackedWidget_mos_right.setCurrentIndex(4)
        pushButton_shezhi_true = ("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setStyleSheet(pushButton_shezhi_true)

    def click_pushButton_about(self):
        self.stackedWidget_mos_right.setCurrentIndex(5)
        pushButton_about_true = ("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    padding-left:3px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setStyleSheet(pushButton_about_true)

    #=================================分割线===================================#


    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))
        self.label_mos_left_top_user.setText(_translate("MOS", "无用户"))
        self.label_mos_left_top_add.setText(_translate("MOS", "点击添加"))
        self.pushButton_home.setText(_translate("MOS", "Home"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_shezhi.setText(_translate("MOS", "设置"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.label_mosll.setText(_translate("MOS", "MOS II"))
        self.label_gonggao_left_txt.setText(_translate("MOS", "公告"))
        self.label_3.setText(_translate("MOS", "启动的图片"))
        self.label_7.setText(_translate("MOS", "TextLabel"))
        self.pushButton__gonggao_start.setText(_translate("MOS", "PushButton"))
        self.label__gonggao_right_txt.setText(_translate("MOS", "选择要启动的游戏"))
        self.label_9.setText(_translate("MOS", "联机模块"))
        self.label_8.setText(_translate("MOS", "联机模块正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.comboBox_2.setItemText(0, _translate("MOS", "游戏下载"))
        self.comboBox_2.setItemText(1, _translate("MOS", "Mod下载"))
        self.comboBox_2.setItemText(2, _translate("MOS", "整合包下载"))
        self.comboBox_2.setItemText(3, _translate("MOS", "世界下载"))
        self.comboBox_2.setItemText(4, _translate("MOS", "下载/安装/已完成"))
        self.treeWidget.headerItem().setText(0, _translate("MOS", "版本列表"))
        self.treeWidget.headerItem().setText(1, _translate("MOS", "种类"))
        self.pushButton_5.setText(_translate("MOS", "（图片）"))
        self.label_11.setText(_translate("MOS", "模组加载器（forge"))
        self.label_19.setText(_translate("MOS", "模组加载器（fabric"))
        self.pushButton_6.setText(_translate("MOS", "（图片）"))
        self.label_20.setText(_translate("MOS", "高清修复optifine"))
        self.pushButton_7.setText(_translate("MOS", "（图片）"))
        self.label_21.setText(_translate("MOS", "模组加载器（quilt"))
        self.pushButton_8.setText(_translate("MOS", "（图片）"))
        self.label_10.setText(_translate("MOS", "下载"))
        self.label_12.setText(_translate("MOS", "音乐"))
        self.label_13.setText(_translate("MOS", "音乐 正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.label_15.setText(_translate("MOS", "设置"))
        self.label_14.setText(_translate("MOS", "设置 正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.label_17.setText(_translate("MOS", "关于"))
        self.label.setText(_translate("MOS", "关于："))
        self.label_16.setText(_translate("MOS", "MOS启动器\n"
"版本V2.0.2-alpha-内部版本\n"
"请勿泄漏！"))
        self.label_18.setText(_translate("MOS", "MOS唯一开发者：David"))
        self.label_22.setText(_translate("MOS", "MOS网站支持、测试小组负责人：QHQQI"))
        
        #=================================分割线===================================#
        
        self.pushButton_home.clicked.connect(self.click_pushButton_home)
        self.pushButton_lianji.clicked.connect(self.click_pushButton_lianji)
        self.pushButton_xiazai.clicked.connect(self.click_pushButton_xiazai)
        self.pushButton_music.clicked.connect(self.click_pushButton_music)
        self.pushButton_shezhi.clicked.connect(self.click_pushButton_shezhi)
        self.pushButton_about.clicked.connect(self.click_pushButton_about)





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
