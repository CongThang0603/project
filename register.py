# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registration(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 650)
        MainWindow.setMinimumSize(QtCore.QSize(950, 650))
        MainWindow.setMaximumSize(QtCore.QSize(950, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 475, 650))
        self.label.setMinimumSize(QtCore.QSize(475, 650))
        self.label.setMaximumSize(QtCore.QSize(475, 650))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/login_background.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 150, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('''
            font-weight: bold;
            color: #29BABF;
        ''')
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 230, 361, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet('''
            font-weight: bold;
            color: #29BABF;
            border-radius: 20px;
        ''')
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 280, 361, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet('''
            font-weight: bold;
            color: #29BABF;
            border-radius: 20px;
        ''')
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(550, 330, 361, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet('''
            font-weight: bold;
            color: #29BABF;
            border-radius: 20px;
        ''')
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 380, 361, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet('''
            font-weight: bold;
            color: #29BABF;
            border-radius: 20px;
        ''')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 430, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                border-radius: 20px;
                background-color: #FFFFFF;
            }
            QPushButton:hover {
                background-color: #29BABF;
                color: #FFFFFF;
            }
            QPushButton:pressed {
                background-color: #29BABF;
                border-style: inset;
            }
        ''')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 540, 361, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                color: #29BABF;
                background-color: rgba(0, 0, 0, 0%);
            }
        ''')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Đăng ký"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Tên đăng nhập"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Mật khẩu"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Xác nhận mật khẩu"))
        self.pushButton.setText(_translate("MainWindow", "Đăng ký"))
        self.pushButton_2.setText(_translate("MainWindow", "Nếu bạn có tài khoản rồi, hãy bấm vào đây"))
import source
