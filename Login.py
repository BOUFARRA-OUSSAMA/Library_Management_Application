# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginjzHMNk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from main import MainWindow
import mysql.connector
import bcrypt
import res_rc
from Librarian import Librarian


class Ui_login(object):
    def openWindow(self):
        login = self.lineEdit.text().rstrip()
        password = self.lineEdit_2.text().rstrip()
        if not login or not password :
                return False
        self.cursor.execute("SELECT salt,password FROM librarian WHERE login=%s",(login,))
        res = self.cursor.fetchone()
        if res:
                salt,pwd = res
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
                print("hashed pwd : ",hashed_password,"actuel pwd : ",pwd)
                if pwd == hashed_password.decode('utf-8'):
                        self.cursor.execute("SELECT isAdmin FROM librarian WHERE login=%s",(login,))
                        isAdmin = self.cursor.fetchone()[0]
                        window.hide()
                        self.window2=MainWindow(isAdmin)
                        self.window2.show()
                else:
                        dialog = QMessageBox(self.centralwidget)
                        dialog.setText("mot de passe incorrect")
                        dialog.setWindowTitle("Error !!")
                        dialog.setIcon(QMessageBox.Critical)
                        dialog.exec_()

        else:
                dialog1 = QMessageBox(self.centralwidget)
                dialog1.setText("user n'existe pas")
                dialog1.setWindowTitle("Error !!")
                dialog1.setIcon(QMessageBox.Critical)
                dialog1.exec_()


    def setupUi(self, MainWindow):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library"
        )
        self.cursor = self.conn.cursor()
        lib = Librarian()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(413, 600)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 380, 580))
        self.widget.setStyleSheet(u"QPushButton#pushButton{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(105, 118, 132, 219), stop:1 rgba(29,67,80, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(29,67,80, 226), stop:1 rgba(105, 118, 132, 219));\n"
"}\n"
"QPushButton#pushButton:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 350, 550))
        self.label.setStyleSheet(u"border-image: url(:/images/new.png);\n"
"border-radius:20px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 350, 550))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 350, 550))
        self.label_3.setStyleSheet(u"background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(155, 155, 90, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 225, 200, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 290, 200, 40))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 380, 200, 40))
        self.pushButton.clicked.connect(self.openWindow)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  User Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"L o g  I n", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    login_ui = Ui_login()
    login_ui.setupUi(window)
    window.show()
    app.exec_()
