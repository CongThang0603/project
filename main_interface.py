# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import*
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import sys


class Ui_Main_interface(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 650)
        MainWindow.setMinimumSize(QtCore.QSize(950, 650))
        MainWindow.setMaximumSize(QtCore.QSize(950, 650))
        MainWindow.setStyleSheet("border-left-color: rgb(41, 186, 191);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 281, 621))
        self.groupBox.setStyleSheet("background-color: rgb(41, 186, 191);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(90, 60, 101, 101))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/avarta.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 540, 50, 50))
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/dx.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 290, 50, 50))
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/hs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 350, 50, 50))
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_8.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 410, 50, 50))
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/avarta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 191, 50))
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(80, 350, 191, 50))
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(80, 410, 191, 50))
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(70, 540, 191, 50))
        self.label_7.setMinimumSize(QtCore.QSize(0, 50))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 230, 50, 50))
        self.pushButton_10.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_10.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/kbyt.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 290, 191, 50))
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(280, 0, 671, 621))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_16.setGeometry(QtCore.QRect(200, 130, 181, 101))
        self.pushButton_16.setObjectName("pushButton_16")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 111, 111))
        self.pushButton.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/glucosemeter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(111, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 390, 111, 111))
        self.pushButton_2.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_2.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/blood-group.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 30, 111, 111))
        self.pushButton_3.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_3.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/heartbeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 200, 111, 111))
        self.pushButton_4.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_4.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_4.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/weight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 30, 111, 111))
        self.pushButton_6.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_6.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_6.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/blood-pressure.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_11 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_11.setGeometry(QtCore.QRect(180, 200, 111, 111))
        self.pushButton_11.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_11.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_11.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/height.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon10)
        self.pushButton_11.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_12 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_12.setGeometry(QtCore.QRect(530, 200, 111, 111))
        self.pushButton_12.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_12.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_12.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/BMI.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon11)
        self.pushButton_12.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 200, 111, 111))
        self.pushButton_13.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_13.setMaximumSize(QtCore.QSize(111, 111))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/temperature.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon12)
        self.pushButton_13.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_14 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 390, 111, 111))
        self.pushButton_14.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_14.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_14.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/blood-ABO.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon13)
        self.pushButton_14.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.pushButton_15 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_15.setGeometry(QtCore.QRect(180, 30, 111, 111))
        self.pushButton_15.setMinimumSize(QtCore.QSize(111, 111))
        self.pushButton_15.setMaximumSize(QtCore.QSize(111, 111))
        self.pushButton_15.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("image/SPO2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon14)
        self.pushButton_15.setIconSize(QtCore.QSize(111, 111))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 50px;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: white;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }        
        ''')
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet('''color: #29BABF;''')
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(210, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet('''color: #29BABF;''')
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(370, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet('''color: #29BABF;''')
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(540, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet('''color: #29BABF;''')
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(30, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet('''color: #29BABF;''')
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(190, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet('''color: #29BABF;''')
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(370, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet('''color: #29BABF;''')
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(530, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet('''color: #29BABF;''')
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(10, 510, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet('''color: #29BABF;''')
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(240, 510, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_17.setStyleSheet('''color: #29BABF;''')
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 671, 621))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("icon/bảo trì.jpg"))
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_10.clicked.connect(self.showpage_1)
        self.pushButton_7.clicked.connect(self.showpage_2)
        self.pushButton_8.clicked.connect(self.showpage_3)
        self.pushButton_9.clicked.connect(self.showpage_4)
        self.pushButton.clicked.connect(self.show_popup)
        self.pushButton_15.clicked.connect(self.show_popup)
        self.pushButton_6.clicked.connect(self.show_popup)
        self.pushButton_3.clicked.connect(self.show_popup)
        self.pushButton_13.clicked.connect(self.show_popup)
        self.pushButton_11.clicked.connect(self.show_popup)
        self.pushButton_4.clicked.connect(self.show_popup)
        self.pushButton_12.clicked.connect(self.show_popup)
        self.pushButton_14.clicked.connect(self.show_popup)
        self.pushButton_2.clicked.connect(self.show_popup)

    def showpage_1(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def showpage_2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

    def showpage_3(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def showpage_4(self):
        self.stackedWidget.setCurrentWidget(self.page_4)

    def show_popup(self):
        msg = QMessageBox()
        msg.setMinimumWidth(300)
        msg.setWindowTitle("notification")
        msg.setText("Rất xin lỗi vì sự bất tiện này, hiện chúng tôi đang cập nhật thêm các tính năng <3")
        msg.setStyleSheet('QMessageBox {background-color: #29BABF; border-radius: 20px;}'
                          'QMessageBox QLabel {color: #ffffff; font-weight: bold; border: 2px solid #29BABF}')

        anim = QPropertyAnimation(msg, b"geometry")
        anim.setDuration(500)
        anim.setStartValue(QRect(800, 180, 200, 100))
        anim.setEndValue(QRect(800, 200, 200, 100))
        anim.start()

        QTimer.singleShot(2000, msg.close)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Xin chào, full name"))
        self.label_3.setText(_translate("MainWindow", "Khai báo y tế"))
        self.label_5.setText(_translate("MainWindow", "Tư vấn từ xa"))
        self.label_6.setText(_translate("MainWindow", "Cá nhân"))
        self.label_7.setText(_translate("MainWindow", "Đăng xuất"))
        self.label_4.setText(_translate("MainWindow", "Hồ sơ sức khỏe"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.label_8.setText(_translate("MainWindow", "Đường huyết"))
        self.label_9.setText(_translate("MainWindow", "SPO2"))
        self.label_10.setText(_translate("MainWindow", "Huyết áp"))
        self.label_11.setText(_translate("MainWindow", "Nhịp tim"))
        self.label_12.setText(_translate("MainWindow", "Nhiệt độ"))
        self.label_13.setText(_translate("MainWindow", "Chiều cao"))
        self.label_14.setText(_translate("MainWindow", "Cân nặng"))
        self.label_15.setText(_translate("MainWindow", "Chỉ số BMI"))
        self.label_16.setText(_translate("MainWindow", "Nhóm máu ABO"))
        self.label_17.setText(_translate("MainWindow", "Nhóm máu RH"))
import source