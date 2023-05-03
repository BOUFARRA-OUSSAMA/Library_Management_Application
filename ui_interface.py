# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceaMqJzA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from myWidgets.Widgets import QCustomSlideMenu
from myWidgets.Widgets import QCustomStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1198, 666)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget,#mainBodyContent,#HomeBtn,#titleBar{\n"
"	background-color: #121212;\n"
"}\n"
"#header,#mainbody,#footer{\n"
"	background-color:#292929;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	padding:3px 10px;\n"
"}\n"
"#HomeBtn{\n"
"	border-left: 3px solid #fff\n"
"}\n"
"QLineEdit,QDateEdit,QComboBox{\n"
"	background-color:#121212;\n"
"	padding:5px 10px;\n"
"}\n"
"#bookAdd,#bookEdit,#searchBookBtn{\n"
"	background-color:#3700b3;\n"
"	text-align:center;\n"
"	padding:8px 5px;\n"
"	border-radius:7px\n"
"}\n"
"#deleteBookBtn,#clearBookBtn{\n"
"	text-align:center;\n"
"	background-color:#cf6679;\n"
"	padding:8px 5px;\n"
"	border-radius:7px\n"
"}\n"
"#deleteRef,#label_8{\n"
"	margin-bottom:25px;\n"
"}\n"
"\n"
"#bookupload{\n"
"	padding:8px 5px;\n"
"	background-color:#121212;\n"
"	text-align:center;\n"
"}\n"
"#titleBar{\n"
"	padding:0;\n"
"}\n"
"\n"
"#clos"
                        "eBtn::hover{\n"
"	background-color:#cf6679;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleBar = QWidget(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 42))
        self.horizontalLayout_7 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.titleBar)
        self.widget_18.setObjectName(u"widget_18")

        self.horizontalLayout_7.addWidget(self.widget_18)

        self.frame_5 = QFrame(self.titleBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.minBtn = QPushButton(self.frame_5)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setMinimumSize(QSize(30, 30))
        self.minBtn.setMaximumSize(QSize(16777215, 16777215))
        self.minBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon1)
        self.minBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_8.addWidget(self.minBtn)

        self.restoreBtn = QPushButton(self.frame_5)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setMinimumSize(QSize(30, 30))
        self.restoreBtn.setMaximumSize(QSize(16777215, 16777215))
        self.restoreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon2)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_5)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QSize(30, 30))
        self.closeBtn.setMaximumSize(QSize(30, 30))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.titleBar)

        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainbody.sizePolicy().hasHeightForWidth())
        self.mainbody.setSizePolicy(sizePolicy1)
        self.mainbody.setMinimumSize(QSize(800, 410))
        self.mainbody.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.mainbody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainbody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_4 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 10)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.HomeBtn = QPushButton(self.frame_3)
        self.HomeBtn.setObjectName(u"HomeBtn")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.HomeBtn.setFont(font1)
        self.HomeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon5)
        self.HomeBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.HomeBtn)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.membersBtn = QPushButton(self.frame_3)
        self.membersBtn.setObjectName(u"membersBtn")
        self.membersBtn.setFont(font2)
        self.membersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.membersBtn.setIcon(icon7)
        self.membersBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.membersBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.pushButton_8 = QPushButton(self.frame_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/tool.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.pushButton_6)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainbody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_3 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QCustomStackedWidget(self.mainBodyContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_11 = QVBoxLayout(self.Home)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_2 = QWidget(self.Home)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/folder-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/folder-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon11)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_17 = QPushButton(self.widget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon12)

        self.horizontalLayout_5.addWidget(self.pushButton_17)


        self.verticalLayout_11.addWidget(self.widget_2)

        self.tableWidget = QTableWidget(self.Home)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_11.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.Home)
        self.Books = QWidget()
        self.Books.setObjectName(u"Books")
        self.verticalLayout_12 = QVBoxLayout(self.Books)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_3 = QWidget(self.Books)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_9 = QPushButton(self.widget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/plus-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon13)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/edit-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon14)
        self.pushButton_10.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/trash-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon15)
        self.pushButton_11.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.widget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setIcon(icon12)
        self.pushButton_12.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_12)


        self.verticalLayout_12.addWidget(self.widget_3)

        self.tableWidget_2 = QTableWidget(self.Books)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_2.setLineWidth(5)
        self.tableWidget_2.setMidLineWidth(5)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setIconSize(QSize(128, 128))
        self.tableWidget_2.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_12.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.Books)
        self.Member = QWidget()
        self.Member.setObjectName(u"Member")
        self.verticalLayout_22 = QVBoxLayout(self.Member)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_8 = QWidget(self.Member)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_13 = QPushButton(self.widget_8)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/user-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon16)
        self.pushButton_13.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_8)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/Icons/user-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon17)
        self.pushButton_14.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.widget_8)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/Icons/user-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon18)
        self.pushButton_15.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_8)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/Icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon19)
        self.pushButton_16.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_16)


        self.verticalLayout_22.addWidget(self.widget_8)

        self.tableWidget_3 = QTableWidget(self.Member)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_22.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.Member)
        self.Historique = QWidget()
        self.Historique.setObjectName(u"Historique")
        self.verticalLayout_37 = QVBoxLayout(self.Historique)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_16 = QWidget(self.Historique)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_18 = QPushButton(self.widget_16)
        self.pushButton_18.setObjectName(u"pushButton_18")
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_18.setFont(font3)
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setIcon(icon12)
        self.pushButton_18.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton_18, 0, Qt.AlignLeft)


        self.verticalLayout_37.addWidget(self.widget_16)

        self.tableWidget_4 = QTableWidget(self.Historique)
        if (self.tableWidget_4.columnCount() < 7):
            self.tableWidget_4.setColumnCount(7)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_37.addWidget(self.tableWidget_4)

        self.stackedWidget.addWidget(self.Historique)
        self.Librarian = QWidget()
        self.Librarian.setObjectName(u"Librarian")
        self.verticalLayout_49 = QVBoxLayout(self.Librarian)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.widget_23 = QWidget(self.Librarian)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_20 = QPushButton(self.widget_23)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setIcon(icon16)
        self.pushButton_20.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.widget_23)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setIcon(icon14)
        self.pushButton_21.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_23)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFont(font2)
        self.pushButton_22.setIcon(icon15)
        self.pushButton_22.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.widget_23)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setFont(font2)
        self.pushButton_23.setIcon(icon12)
        self.pushButton_23.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_23)


        self.verticalLayout_49.addWidget(self.widget_23)

        self.tableWidget_5 = QTableWidget(self.Librarian)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.verticalLayout_49.addWidget(self.tableWidget_5)

        self.stackedWidget.addWidget(self.Librarian)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainbody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(234, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.rightMenu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/icons/Icons/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon20)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.subMenuStackedWidget = QCustomStackedWidget(self.rightMenu)
        self.subMenuStackedWidget.setObjectName(u"subMenuStackedWidget")
        self.emprunts = QWidget()
        self.emprunts.setObjectName(u"emprunts")
        self.verticalLayout_30 = QVBoxLayout(self.emprunts)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.stackedWidgetEmprunts = QCustomStackedWidget(self.emprunts)
        self.stackedWidgetEmprunts.setObjectName(u"stackedWidgetEmprunts")
        self.ajouterEmprunt = QWidget()
        self.ajouterEmprunt.setObjectName(u"ajouterEmprunt")
        self.verticalLayout_31 = QVBoxLayout(self.ajouterEmprunt)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_13 = QLabel(self.ajouterEmprunt)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.verticalLayout_31.addWidget(self.label_13, 0, Qt.AlignTop)

        self.widget_13 = QWidget(self.ajouterEmprunt)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.verticalLayout_32 = QVBoxLayout(self.widget_13)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.ajouterEmpruntRef = QLineEdit(self.widget_13)
        self.ajouterEmpruntRef.setObjectName(u"ajouterEmpruntRef")
        self.ajouterEmpruntRef.setFont(font3)

        self.verticalLayout_32.addWidget(self.ajouterEmpruntRef)

        self.ajouterEmpruntId = QLineEdit(self.widget_13)
        self.ajouterEmpruntId.setObjectName(u"ajouterEmpruntId")
        self.ajouterEmpruntId.setFont(font3)

        self.verticalLayout_32.addWidget(self.ajouterEmpruntId)

        self.ajouterEmpruntBtn = QPushButton(self.widget_13)
        self.ajouterEmpruntBtn.setObjectName(u"ajouterEmpruntBtn")
        self.ajouterEmpruntBtn.setFont(font3)
        self.ajouterEmpruntBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/icons/Icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ajouterEmpruntBtn.setIcon(icon21)
        self.ajouterEmpruntBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_32.addWidget(self.ajouterEmpruntBtn)


        self.verticalLayout_31.addWidget(self.widget_13)

        self.stackedWidgetEmprunts.addWidget(self.ajouterEmprunt)
        self.retrunEmprunt = QWidget()
        self.retrunEmprunt.setObjectName(u"retrunEmprunt")
        self.verticalLayout_33 = QVBoxLayout(self.retrunEmprunt)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_14 = QLabel(self.retrunEmprunt)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_14, 0, Qt.AlignTop)

        self.widget_14 = QWidget(self.retrunEmprunt)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy1.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy1)
        self.verticalLayout_34 = QVBoxLayout(self.widget_14)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.returnEmpruntRef = QLineEdit(self.widget_14)
        self.returnEmpruntRef.setObjectName(u"returnEmpruntRef")
        self.returnEmpruntRef.setFont(font3)

        self.verticalLayout_34.addWidget(self.returnEmpruntRef)

        self.empruntDate = QDateEdit(self.widget_14)
        self.empruntDate.setObjectName(u"empruntDate")

        self.verticalLayout_34.addWidget(self.empruntDate)

        self.returnEmprutnId = QLineEdit(self.widget_14)
        self.returnEmprutnId.setObjectName(u"returnEmprutnId")
        self.returnEmprutnId.setFont(font3)

        self.verticalLayout_34.addWidget(self.returnEmprutnId)

        self.returnEmpruntBtn = QPushButton(self.widget_14)
        self.returnEmpruntBtn.setObjectName(u"returnEmpruntBtn")
        self.returnEmpruntBtn.setFont(font3)
        self.returnEmpruntBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon22 = QIcon()
        icon22.addFile(u":/icons/Icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.returnEmpruntBtn.setIcon(icon22)
        self.returnEmpruntBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_34.addWidget(self.returnEmpruntBtn)


        self.verticalLayout_33.addWidget(self.widget_14)

        self.stackedWidgetEmprunts.addWidget(self.retrunEmprunt)
        self.searchEmprunt = QWidget()
        self.searchEmprunt.setObjectName(u"searchEmprunt")
        self.verticalLayout_35 = QVBoxLayout(self.searchEmprunt)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_15 = QLabel(self.searchEmprunt)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.verticalLayout_35.addWidget(self.label_15, 0, Qt.AlignTop)

        self.widget_15 = QWidget(self.searchEmprunt)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.verticalLayout_36 = QVBoxLayout(self.widget_15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.searchEmpruntId = QLineEdit(self.widget_15)
        self.searchEmpruntId.setObjectName(u"searchEmpruntId")
        self.searchEmpruntId.setFont(font3)

        self.verticalLayout_36.addWidget(self.searchEmpruntId)

        self.searchEmpruntNom = QLineEdit(self.widget_15)
        self.searchEmpruntNom.setObjectName(u"searchEmpruntNom")
        self.searchEmpruntNom.setFont(font3)

        self.verticalLayout_36.addWidget(self.searchEmpruntNom)

        self.searchEmpruntPrenom = QLineEdit(self.widget_15)
        self.searchEmpruntPrenom.setObjectName(u"searchEmpruntPrenom")
        self.searchEmpruntPrenom.setFont(font3)

        self.verticalLayout_36.addWidget(self.searchEmpruntPrenom)

        self.searchEmpruntRef = QLineEdit(self.widget_15)
        self.searchEmpruntRef.setObjectName(u"searchEmpruntRef")
        self.searchEmpruntRef.setFont(font3)

        self.verticalLayout_36.addWidget(self.searchEmpruntRef)

        self.searchEmpruntTitle = QLineEdit(self.widget_15)
        self.searchEmpruntTitle.setObjectName(u"searchEmpruntTitle")
        self.searchEmpruntTitle.setFont(font3)

        self.verticalLayout_36.addWidget(self.searchEmpruntTitle)

        self.searchEmpruntDate = QDateEdit(self.widget_15)
        self.searchEmpruntDate.setObjectName(u"searchEmpruntDate")
        self.searchEmpruntDate.setFont(font3)

        self.verticalLayout_36.addWidget(self.searchEmpruntDate)

        self.searchApplyBtn = QPushButton(self.widget_15)
        self.searchApplyBtn.setObjectName(u"searchApplyBtn")
        self.searchApplyBtn.setFont(font3)
        self.searchApplyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchApplyBtn.setIcon(icon12)
        self.searchApplyBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.searchApplyBtn)

        self.searchClearBtn = QPushButton(self.widget_15)
        self.searchClearBtn.setObjectName(u"searchClearBtn")
        self.searchClearBtn.setFont(font3)
        self.searchClearBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchClearBtn.setIcon(icon20)
        self.searchClearBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.searchClearBtn)


        self.verticalLayout_35.addWidget(self.widget_15)

        self.stackedWidgetEmprunts.addWidget(self.searchEmprunt)

        self.verticalLayout_30.addWidget(self.stackedWidgetEmprunts)

        self.subMenuStackedWidget.addWidget(self.emprunts)
        self.members = QWidget()
        self.members.setObjectName(u"members")
        self.verticalLayout_10 = QVBoxLayout(self.members)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetPerson = QCustomStackedWidget(self.members)
        self.stackedWidgetPerson.setObjectName(u"stackedWidgetPerson")
        self.addmember = QWidget()
        self.addmember.setObjectName(u"addmember")
        self.verticalLayout_23 = QVBoxLayout(self.addmember)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_10 = QLabel(self.addmember)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_10, 0, Qt.AlignTop)

        self.widget_9 = QWidget(self.addmember)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.verticalLayout_24 = QVBoxLayout(self.widget_9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.addMemberNom = QLineEdit(self.widget_9)
        self.addMemberNom.setObjectName(u"addMemberNom")
        self.addMemberNom.setFont(font3)

        self.verticalLayout_24.addWidget(self.addMemberNom)

        self.addMemberPrenom = QLineEdit(self.widget_9)
        self.addMemberPrenom.setObjectName(u"addMemberPrenom")
        self.addMemberPrenom.setFont(font3)

        self.verticalLayout_24.addWidget(self.addMemberPrenom)

        self.addMemberAdresse = QLineEdit(self.widget_9)
        self.addMemberAdresse.setObjectName(u"addMemberAdresse")
        self.addMemberAdresse.setFont(font3)

        self.verticalLayout_24.addWidget(self.addMemberAdresse)

        self.addMemberTel = QLineEdit(self.widget_9)
        self.addMemberTel.setObjectName(u"addMemberTel")
        self.addMemberTel.setFont(font3)

        self.verticalLayout_24.addWidget(self.addMemberTel)

        self.addMemberBtn = QPushButton(self.widget_9)
        self.addMemberBtn.setObjectName(u"addMemberBtn")
        self.addMemberBtn.setFont(font3)
        self.addMemberBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addMemberBtn.setIcon(icon21)
        self.addMemberBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_24.addWidget(self.addMemberBtn)


        self.verticalLayout_23.addWidget(self.widget_9)

        self.stackedWidgetPerson.addWidget(self.addmember)
        self.editmember = QWidget()
        self.editmember.setObjectName(u"editmember")
        self.verticalLayout_9 = QVBoxLayout(self.editmember)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.editmember)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_11, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.editmember)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.widget_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_25 = QVBoxLayout(self.widget_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.editMemberid = QLineEdit(self.widget_10)
        self.editMemberid.setObjectName(u"editMemberid")
        self.editMemberid.setFont(font3)

        self.verticalLayout_25.addWidget(self.editMemberid)

        self.editMemberNom = QLineEdit(self.widget_10)
        self.editMemberNom.setObjectName(u"editMemberNom")
        self.editMemberNom.setFont(font3)

        self.verticalLayout_25.addWidget(self.editMemberNom)

        self.editMemberPrenom = QLineEdit(self.widget_10)
        self.editMemberPrenom.setObjectName(u"editMemberPrenom")
        self.editMemberPrenom.setFont(font3)

        self.verticalLayout_25.addWidget(self.editMemberPrenom)

        self.editMemberAdresse = QLineEdit(self.widget_10)
        self.editMemberAdresse.setObjectName(u"editMemberAdresse")
        self.editMemberAdresse.setFont(font3)

        self.verticalLayout_25.addWidget(self.editMemberAdresse)

        self.editMemberTel = QLineEdit(self.widget_10)
        self.editMemberTel.setObjectName(u"editMemberTel")
        self.editMemberTel.setFont(font3)

        self.verticalLayout_25.addWidget(self.editMemberTel)

        self.editMemberBtn = QPushButton(self.widget_10)
        self.editMemberBtn.setObjectName(u"editMemberBtn")
        self.editMemberBtn.setFont(font3)
        self.editMemberBtn.setIcon(icon22)
        self.editMemberBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_25.addWidget(self.editMemberBtn)


        self.verticalLayout_9.addWidget(self.widget_10)

        self.stackedWidgetPerson.addWidget(self.editmember)
        self.deletemember = QWidget()
        self.deletemember.setObjectName(u"deletemember")
        self.verticalLayout_26 = QVBoxLayout(self.deletemember)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_9 = QLabel(self.deletemember)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_26.addWidget(self.label_9, 0, Qt.AlignTop)

        self.widget_11 = QWidget(self.deletemember)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.verticalLayout_27 = QVBoxLayout(self.widget_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.deleteMemberid = QLineEdit(self.widget_11)
        self.deleteMemberid.setObjectName(u"deleteMemberid")
        self.deleteMemberid.setFont(font3)

        self.verticalLayout_27.addWidget(self.deleteMemberid)

        self.deleteMemberBtn = QPushButton(self.widget_11)
        self.deleteMemberBtn.setObjectName(u"deleteMemberBtn")
        self.deleteMemberBtn.setFont(font3)
        self.deleteMemberBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteMemberBtn.setIcon(icon15)
        self.deleteMemberBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_27.addWidget(self.deleteMemberBtn)


        self.verticalLayout_26.addWidget(self.widget_11)

        self.stackedWidgetPerson.addWidget(self.deletemember)
        self.searchmember = QWidget()
        self.searchmember.setObjectName(u"searchmember")
        self.verticalLayout_28 = QVBoxLayout(self.searchmember)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_12 = QLabel(self.searchmember)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_28.addWidget(self.label_12, 0, Qt.AlignTop)

        self.widget_12 = QWidget(self.searchmember)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.widget_12.setAutoFillBackground(False)
        self.verticalLayout_29 = QVBoxLayout(self.widget_12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.searchMemberid = QLineEdit(self.widget_12)
        self.searchMemberid.setObjectName(u"searchMemberid")
        self.searchMemberid.setFont(font3)

        self.verticalLayout_29.addWidget(self.searchMemberid)

        self.searchMemberNom = QLineEdit(self.widget_12)
        self.searchMemberNom.setObjectName(u"searchMemberNom")
        self.searchMemberNom.setFont(font3)

        self.verticalLayout_29.addWidget(self.searchMemberNom)

        self.searchMemberPrenom = QLineEdit(self.widget_12)
        self.searchMemberPrenom.setObjectName(u"searchMemberPrenom")
        self.searchMemberPrenom.setFont(font3)

        self.verticalLayout_29.addWidget(self.searchMemberPrenom)

        self.searchMemberAdresse = QLineEdit(self.widget_12)
        self.searchMemberAdresse.setObjectName(u"searchMemberAdresse")
        self.searchMemberAdresse.setFont(font3)

        self.verticalLayout_29.addWidget(self.searchMemberAdresse)

        self.searchMemberTel = QLineEdit(self.widget_12)
        self.searchMemberTel.setObjectName(u"searchMemberTel")
        self.searchMemberTel.setFont(font3)

        self.verticalLayout_29.addWidget(self.searchMemberTel)

        self.MemberApplyFilter = QPushButton(self.widget_12)
        self.MemberApplyFilter.setObjectName(u"MemberApplyFilter")
        self.MemberApplyFilter.setFont(font3)
        self.MemberApplyFilter.setCursor(QCursor(Qt.PointingHandCursor))
        icon23 = QIcon()
        icon23.addFile(u":/icons/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MemberApplyFilter.setIcon(icon23)
        self.MemberApplyFilter.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.MemberApplyFilter)

        self.MemberClearFilter = QPushButton(self.widget_12)
        self.MemberClearFilter.setObjectName(u"MemberClearFilter")
        self.MemberClearFilter.setFont(font3)
        self.MemberClearFilter.setCursor(QCursor(Qt.PointingHandCursor))
        icon24 = QIcon()
        icon24.addFile(u":/icons/Icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MemberClearFilter.setIcon(icon24)
        self.MemberClearFilter.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.MemberClearFilter)


        self.verticalLayout_28.addWidget(self.widget_12)

        self.stackedWidgetPerson.addWidget(self.searchmember)

        self.verticalLayout_10.addWidget(self.stackedWidgetPerson)

        self.subMenuStackedWidget.addWidget(self.members)
        self.books = QWidget()
        self.books.setObjectName(u"books")
        self.verticalLayout_8 = QVBoxLayout(self.books)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetBook = QCustomStackedWidget(self.books)
        self.stackedWidgetBook.setObjectName(u"stackedWidgetBook")
        self.addBook = QWidget()
        self.addBook.setObjectName(u"addBook")
        self.verticalLayout_13 = QVBoxLayout(self.addBook)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_2 = QLabel(self.addBook)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_4 = QWidget(self.addBook)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.bookTitle = QLineEdit(self.widget_4)
        self.bookTitle.setObjectName(u"bookTitle")
        self.bookTitle.setFont(font3)

        self.verticalLayout_14.addWidget(self.bookTitle)

        self.bookAuthor = QLineEdit(self.widget_4)
        self.bookAuthor.setObjectName(u"bookAuthor")
        self.bookAuthor.setFont(font3)

        self.verticalLayout_14.addWidget(self.bookAuthor)

        self.bookYear = QDateEdit(self.widget_4)
        self.bookYear.setObjectName(u"bookYear")
        self.bookYear.setFont(font3)
        self.bookYear.setAlignment(Qt.AlignCenter)
        self.bookYear.setDisplayFormat(u"yyyy-MM-dd")

        self.verticalLayout_14.addWidget(self.bookYear)

        self.Edition = QLineEdit(self.widget_4)
        self.Edition.setObjectName(u"Edition")
        self.Edition.setFont(font3)

        self.verticalLayout_14.addWidget(self.Edition)

        self.bookqte = QLineEdit(self.widget_4)
        self.bookqte.setObjectName(u"bookqte")
        self.bookqte.setFont(font3)

        self.verticalLayout_14.addWidget(self.bookqte)

        self.bookupload = QPushButton(self.widget_4)
        self.bookupload.setObjectName(u"bookupload")
        self.bookupload.setFont(font3)
        icon25 = QIcon()
        icon25.addFile(u":/icons/Icons/upload-cloud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bookupload.setIcon(icon25)
        self.bookupload.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.bookupload)

        self.bookAdd = QPushButton(self.widget_4)
        self.bookAdd.setObjectName(u"bookAdd")
        self.bookAdd.setMinimumSize(QSize(120, 0))
        self.bookAdd.setFont(font3)
        self.bookAdd.setCursor(QCursor(Qt.PointingHandCursor))
        icon26 = QIcon()
        icon26.addFile(u":/icons/Icons/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bookAdd.setIcon(icon26)
        self.bookAdd.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.bookAdd, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.widget_4)

        self.stackedWidgetBook.addWidget(self.addBook)
        self.editBook = QWidget()
        self.editBook.setObjectName(u"editBook")
        self.verticalLayout_15 = QVBoxLayout(self.editBook)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_3 = QLabel(self.editBook)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_3, 0, Qt.AlignTop)

        self.widget_5 = QWidget(self.editBook)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.editRef = QLineEdit(self.widget_5)
        self.editRef.setObjectName(u"editRef")
        self.editRef.setFont(font3)

        self.verticalLayout_16.addWidget(self.editRef)

        self.editTitle = QLineEdit(self.widget_5)
        self.editTitle.setObjectName(u"editTitle")
        self.editTitle.setFont(font3)

        self.verticalLayout_16.addWidget(self.editTitle)

        self.editAuthor = QLineEdit(self.widget_5)
        self.editAuthor.setObjectName(u"editAuthor")
        self.editAuthor.setFont(font3)

        self.verticalLayout_16.addWidget(self.editAuthor)

        self.editYear = QDateEdit(self.widget_5)
        self.editYear.setObjectName(u"editYear")
        self.editYear.setFont(font3)
        self.editYear.setAlignment(Qt.AlignCenter)
        self.editYear.setDisplayFormat(u"yyyy-MM-dd")

        self.verticalLayout_16.addWidget(self.editYear)

        self.editEdition = QLineEdit(self.widget_5)
        self.editEdition.setObjectName(u"editEdition")
        self.editEdition.setFont(font3)

        self.verticalLayout_16.addWidget(self.editEdition)

        self.editQte = QLineEdit(self.widget_5)
        self.editQte.setObjectName(u"editQte")
        self.editQte.setFont(font3)

        self.verticalLayout_16.addWidget(self.editQte)

        self.bookEdit = QPushButton(self.widget_5)
        self.bookEdit.setObjectName(u"bookEdit")
        self.bookEdit.setMinimumSize(QSize(120, 0))
        self.bookEdit.setFont(font3)
        self.bookEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.bookEdit.setIcon(icon22)
        self.bookEdit.setIconSize(QSize(24, 24))

        self.verticalLayout_16.addWidget(self.bookEdit)


        self.verticalLayout_15.addWidget(self.widget_5)

        self.stackedWidgetBook.addWidget(self.editBook)
        self.deleteBook = QWidget()
        self.deleteBook.setObjectName(u"deleteBook")
        self.verticalLayout_17 = QVBoxLayout(self.deleteBook)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_6 = QLabel(self.deleteBook)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_6, 0, Qt.AlignTop)

        self.widget_6 = QWidget(self.deleteBook)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 0, 10, 0)
        self.deleteRef = QLineEdit(self.widget_6)
        self.deleteRef.setObjectName(u"deleteRef")
        self.deleteRef.setFont(font3)

        self.verticalLayout_18.addWidget(self.deleteRef)

        self.deleteBookBtn = QPushButton(self.widget_6)
        self.deleteBookBtn.setObjectName(u"deleteBookBtn")
        self.deleteBookBtn.setFont(font3)
        self.deleteBookBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteBookBtn.setIcon(icon15)
        self.deleteBookBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_18.addWidget(self.deleteBookBtn)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.stackedWidgetBook.addWidget(self.deleteBook)
        self.filerBooks = QWidget()
        self.filerBooks.setObjectName(u"filerBooks")
        self.verticalLayout_19 = QVBoxLayout(self.filerBooks)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_7 = QLabel(self.filerBooks)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_7, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.filerBooks)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_20 = QVBoxLayout(self.widget_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.searchRef = QLineEdit(self.widget_7)
        self.searchRef.setObjectName(u"searchRef")
        self.searchRef.setFont(font3)

        self.verticalLayout_20.addWidget(self.searchRef)

        self.searchTitle = QLineEdit(self.widget_7)
        self.searchTitle.setObjectName(u"searchTitle")
        self.searchTitle.setFont(font3)

        self.verticalLayout_20.addWidget(self.searchTitle)

        self.searchAuthor = QLineEdit(self.widget_7)
        self.searchAuthor.setObjectName(u"searchAuthor")
        self.searchAuthor.setFont(font3)

        self.verticalLayout_20.addWidget(self.searchAuthor)

        self.searchYear = QDateEdit(self.widget_7)
        self.searchYear.setObjectName(u"searchYear")
        self.searchYear.setFont(font3)
        self.searchYear.setAlignment(Qt.AlignCenter)
        self.searchYear.setDisplayFormat(u"yyyy-MM-dd")

        self.verticalLayout_20.addWidget(self.searchYear)

        self.searchEdition = QLineEdit(self.widget_7)
        self.searchEdition.setObjectName(u"searchEdition")
        self.searchEdition.setFont(font3)

        self.verticalLayout_20.addWidget(self.searchEdition)

        self.searchBookBtn = QPushButton(self.widget_7)
        self.searchBookBtn.setObjectName(u"searchBookBtn")
        self.searchBookBtn.setFont(font2)
        self.searchBookBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBookBtn.setIcon(icon12)
        self.searchBookBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_20.addWidget(self.searchBookBtn)

        self.clearBookBtn = QPushButton(self.widget_7)
        self.clearBookBtn.setObjectName(u"clearBookBtn")
        self.clearBookBtn.setFont(font2)
        self.clearBookBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon27 = QIcon()
        icon27.addFile(u":/icons/Icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBookBtn.setIcon(icon27)
        self.clearBookBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_20.addWidget(self.clearBookBtn)


        self.verticalLayout_19.addWidget(self.widget_7)

        self.stackedWidgetBook.addWidget(self.filerBooks)

        self.verticalLayout_8.addWidget(self.stackedWidgetBook)

        self.subMenuStackedWidget.addWidget(self.books)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_39 = QVBoxLayout(self.history)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.widget_17 = QWidget(self.history)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy1.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy1)
        self.verticalLayout_38 = QVBoxLayout(self.widget_17)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.searchHistoryId = QLineEdit(self.widget_17)
        self.searchHistoryId.setObjectName(u"searchHistoryId")
        self.searchHistoryId.setFont(font3)

        self.verticalLayout_38.addWidget(self.searchHistoryId)

        self.searchHistoryNom = QLineEdit(self.widget_17)
        self.searchHistoryNom.setObjectName(u"searchHistoryNom")
        self.searchHistoryNom.setFont(font3)

        self.verticalLayout_38.addWidget(self.searchHistoryNom)

        self.searchHistoryPrenom = QLineEdit(self.widget_17)
        self.searchHistoryPrenom.setObjectName(u"searchHistoryPrenom")
        self.searchHistoryPrenom.setFont(font3)

        self.verticalLayout_38.addWidget(self.searchHistoryPrenom)

        self.searchHistoryRef = QLineEdit(self.widget_17)
        self.searchHistoryRef.setObjectName(u"searchHistoryRef")
        self.searchHistoryRef.setFont(font3)

        self.verticalLayout_38.addWidget(self.searchHistoryRef)

        self.searchHistoryTitle = QLineEdit(self.widget_17)
        self.searchHistoryTitle.setObjectName(u"searchHistoryTitle")
        self.searchHistoryTitle.setFont(font3)

        self.verticalLayout_38.addWidget(self.searchHistoryTitle)

        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(11)
        self.label_4.setFont(font4)

        self.verticalLayout_38.addWidget(self.label_4)

        self.searchHistoryEmp = QDateEdit(self.widget_17)
        self.searchHistoryEmp.setObjectName(u"searchHistoryEmp")
        self.searchHistoryEmp.setFont(font3)

        self.verticalLayout_38.addWidget(self.searchHistoryEmp)

        self.label_16 = QLabel(self.widget_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 35))
        self.label_16.setFont(font4)

        self.verticalLayout_38.addWidget(self.label_16)

        self.searchHistoryRetour = QDateEdit(self.widget_17)
        self.searchHistoryRetour.setObjectName(u"searchHistoryRetour")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.searchHistoryRetour.setFont(font5)

        self.verticalLayout_38.addWidget(self.searchHistoryRetour)

        self.searchHistoryApplyBtn = QPushButton(self.widget_17)
        self.searchHistoryApplyBtn.setObjectName(u"searchHistoryApplyBtn")
        self.searchHistoryApplyBtn.setFont(font3)
        self.searchHistoryApplyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchHistoryApplyBtn.setIcon(icon12)
        self.searchHistoryApplyBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_38.addWidget(self.searchHistoryApplyBtn)

        self.searchHistoryClearBtn = QPushButton(self.widget_17)
        self.searchHistoryClearBtn.setObjectName(u"searchHistoryClearBtn")
        self.searchHistoryClearBtn.setFont(font3)
        self.searchHistoryClearBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchHistoryClearBtn.setIcon(icon20)
        self.searchHistoryClearBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_38.addWidget(self.searchHistoryClearBtn)


        self.verticalLayout_39.addWidget(self.widget_17)

        self.subMenuStackedWidget.addWidget(self.history)
        self.librarian = QWidget()
        self.librarian.setObjectName(u"librarian")
        self.verticalLayout_40 = QVBoxLayout(self.librarian)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.stackedWidgetLibrarian = QCustomStackedWidget(self.librarian)
        self.stackedWidgetLibrarian.setObjectName(u"stackedWidgetLibrarian")
        self.addLibrarian = QWidget()
        self.addLibrarian.setObjectName(u"addLibrarian")
        self.verticalLayout_41 = QVBoxLayout(self.addLibrarian)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_8 = QLabel(self.addLibrarian)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_41.addWidget(self.label_8, 0, Qt.AlignTop)

        self.widget_19 = QWidget(self.addLibrarian)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy1.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy1)
        self.verticalLayout_42 = QVBoxLayout(self.widget_19)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.addLibrarianNom = QLineEdit(self.widget_19)
        self.addLibrarianNom.setObjectName(u"addLibrarianNom")
        self.addLibrarianNom.setFont(font3)

        self.verticalLayout_42.addWidget(self.addLibrarianNom)

        self.addLibrarianPrenom = QLineEdit(self.widget_19)
        self.addLibrarianPrenom.setObjectName(u"addLibrarianPrenom")
        self.addLibrarianPrenom.setFont(font3)

        self.verticalLayout_42.addWidget(self.addLibrarianPrenom)

        self.addLibrarianLogin = QLineEdit(self.widget_19)
        self.addLibrarianLogin.setObjectName(u"addLibrarianLogin")
        self.addLibrarianLogin.setFont(font3)

        self.verticalLayout_42.addWidget(self.addLibrarianLogin)

        self.addLibrarianPassword = QLineEdit(self.widget_19)
        self.addLibrarianPassword.setObjectName(u"addLibrarianPassword")
        self.addLibrarianPassword.setFont(font3)
        self.addLibrarianPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_42.addWidget(self.addLibrarianPassword)

        self.addLibrarianConf = QLineEdit(self.widget_19)
        self.addLibrarianConf.setObjectName(u"addLibrarianConf")
        self.addLibrarianConf.setFont(font3)
        self.addLibrarianConf.setEchoMode(QLineEdit.Password)

        self.verticalLayout_42.addWidget(self.addLibrarianConf)

        self.addAdmin = QComboBox(self.widget_19)
        self.addAdmin.addItem("")
        self.addAdmin.addItem("")
        self.addAdmin.addItem("")
        self.addAdmin.setObjectName(u"addAdmin")
        self.addAdmin.setFont(font3)

        self.verticalLayout_42.addWidget(self.addAdmin)

        self.addLibrarianBtn = QPushButton(self.widget_19)
        self.addLibrarianBtn.setObjectName(u"addLibrarianBtn")
        self.addLibrarianBtn.setFont(font3)
        self.addLibrarianBtn.setIcon(icon21)
        self.addLibrarianBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_42.addWidget(self.addLibrarianBtn)


        self.verticalLayout_41.addWidget(self.widget_19)

        self.stackedWidgetLibrarian.addWidget(self.addLibrarian)
        self.editLibrarian = QWidget()
        self.editLibrarian.setObjectName(u"editLibrarian")
        self.verticalLayout_44 = QVBoxLayout(self.editLibrarian)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_17 = QLabel(self.editLibrarian)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.verticalLayout_44.addWidget(self.label_17)

        self.widget_20 = QWidget(self.editLibrarian)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy1.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy1)
        self.verticalLayout_43 = QVBoxLayout(self.widget_20)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.editLibrarianId = QLineEdit(self.widget_20)
        self.editLibrarianId.setObjectName(u"editLibrarianId")
        self.editLibrarianId.setFont(font3)

        self.verticalLayout_43.addWidget(self.editLibrarianId)

        self.editLibrarianNom = QLineEdit(self.widget_20)
        self.editLibrarianNom.setObjectName(u"editLibrarianNom")
        self.editLibrarianNom.setFont(font3)

        self.verticalLayout_43.addWidget(self.editLibrarianNom)

        self.editLibrarianPrenom = QLineEdit(self.widget_20)
        self.editLibrarianPrenom.setObjectName(u"editLibrarianPrenom")
        self.editLibrarianPrenom.setFont(font3)

        self.verticalLayout_43.addWidget(self.editLibrarianPrenom)

        self.editLibrarianLogin = QLineEdit(self.widget_20)
        self.editLibrarianLogin.setObjectName(u"editLibrarianLogin")
        self.editLibrarianLogin.setFont(font3)

        self.verticalLayout_43.addWidget(self.editLibrarianLogin)

        self.editLibrarianPassword = QLineEdit(self.widget_20)
        self.editLibrarianPassword.setObjectName(u"editLibrarianPassword")
        self.editLibrarianPassword.setFont(font3)
        self.editLibrarianPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_43.addWidget(self.editLibrarianPassword)

        self.editLibrarianConf = QLineEdit(self.widget_20)
        self.editLibrarianConf.setObjectName(u"editLibrarianConf")
        self.editLibrarianConf.setFont(font3)
        self.editLibrarianConf.setEchoMode(QLineEdit.Password)

        self.verticalLayout_43.addWidget(self.editLibrarianConf)

        self.editAdmin = QComboBox(self.widget_20)
        self.editAdmin.addItem("")
        self.editAdmin.addItem("")
        self.editAdmin.addItem("")
        self.editAdmin.setObjectName(u"editAdmin")
        self.editAdmin.setFont(font3)

        self.verticalLayout_43.addWidget(self.editAdmin)

        self.editLibrarianBtn = QPushButton(self.widget_20)
        self.editLibrarianBtn.setObjectName(u"editLibrarianBtn")
        self.editLibrarianBtn.setFont(font3)
        self.editLibrarianBtn.setIcon(icon22)
        self.editLibrarianBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_43.addWidget(self.editLibrarianBtn)


        self.verticalLayout_44.addWidget(self.widget_20)

        self.stackedWidgetLibrarian.addWidget(self.editLibrarian)
        self.deleteLibrarian = QWidget()
        self.deleteLibrarian.setObjectName(u"deleteLibrarian")
        self.verticalLayout_45 = QVBoxLayout(self.deleteLibrarian)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_18 = QLabel(self.deleteLibrarian)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.verticalLayout_45.addWidget(self.label_18, 0, Qt.AlignTop)

        self.widget_21 = QWidget(self.deleteLibrarian)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy1.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy1)
        self.verticalLayout_46 = QVBoxLayout(self.widget_21)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.deleteLibrarianId = QLineEdit(self.widget_21)
        self.deleteLibrarianId.setObjectName(u"deleteLibrarianId")
        self.deleteLibrarianId.setFont(font3)

        self.verticalLayout_46.addWidget(self.deleteLibrarianId)

        self.deleteLibrarianBtn = QPushButton(self.widget_21)
        self.deleteLibrarianBtn.setObjectName(u"deleteLibrarianBtn")
        self.deleteLibrarianBtn.setFont(font3)
        self.deleteLibrarianBtn.setIcon(icon15)
        self.deleteLibrarianBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_46.addWidget(self.deleteLibrarianBtn)


        self.verticalLayout_45.addWidget(self.widget_21)

        self.stackedWidgetLibrarian.addWidget(self.deleteLibrarian)
        self.searchLibrarian = QWidget()
        self.searchLibrarian.setObjectName(u"searchLibrarian")
        self.verticalLayout_48 = QVBoxLayout(self.searchLibrarian)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_19 = QLabel(self.searchLibrarian)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.verticalLayout_48.addWidget(self.label_19)

        self.widget_22 = QWidget(self.searchLibrarian)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy1.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy1)
        self.verticalLayout_47 = QVBoxLayout(self.widget_22)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.searchLibrarianId = QLineEdit(self.widget_22)
        self.searchLibrarianId.setObjectName(u"searchLibrarianId")
        self.searchLibrarianId.setFont(font3)

        self.verticalLayout_47.addWidget(self.searchLibrarianId)

        self.searchLibrarianNom = QLineEdit(self.widget_22)
        self.searchLibrarianNom.setObjectName(u"searchLibrarianNom")
        self.searchLibrarianNom.setFont(font3)

        self.verticalLayout_47.addWidget(self.searchLibrarianNom)

        self.searchLibrarianPrenom = QLineEdit(self.widget_22)
        self.searchLibrarianPrenom.setObjectName(u"searchLibrarianPrenom")
        self.searchLibrarianPrenom.setFont(font3)

        self.verticalLayout_47.addWidget(self.searchLibrarianPrenom)

        self.searchAdmin = QComboBox(self.widget_22)
        self.searchAdmin.addItem("")
        self.searchAdmin.addItem("")
        self.searchAdmin.addItem("")
        self.searchAdmin.setObjectName(u"searchAdmin")
        self.searchAdmin.setFont(font3)

        self.verticalLayout_47.addWidget(self.searchAdmin)

        self.searchLibrarianBtn = QPushButton(self.widget_22)
        self.searchLibrarianBtn.setObjectName(u"searchLibrarianBtn")
        self.searchLibrarianBtn.setFont(font3)
        self.searchLibrarianBtn.setIcon(icon12)
        self.searchLibrarianBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_47.addWidget(self.searchLibrarianBtn)

        self.LibrarianClearBtn = QPushButton(self.widget_22)
        self.LibrarianClearBtn.setObjectName(u"LibrarianClearBtn")
        self.LibrarianClearBtn.setFont(font3)
        self.LibrarianClearBtn.setIcon(icon15)
        self.LibrarianClearBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_47.addWidget(self.LibrarianClearBtn)


        self.verticalLayout_48.addWidget(self.widget_22)

        self.stackedWidgetLibrarian.addWidget(self.searchLibrarian)

        self.verticalLayout_40.addWidget(self.stackedWidgetLibrarian)

        self.subMenuStackedWidget.addWidget(self.librarian)

        self.verticalLayout_7.addWidget(self.subMenuStackedWidget)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainbody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 25))
        self.horizontalLayout_12 = QHBoxLayout(self.footer)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.icon = QWidget(self.footer)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(0, 20))
        self.icon.setMaximumSize(QSize(16777215, 20))
        self.verticalLayout_21 = QVBoxLayout(self.icon)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.resizeBtn = QPushButton(self.icon)
        self.resizeBtn.setObjectName(u"resizeBtn")
        self.resizeBtn.setMaximumSize(QSize(25, 16777215))
        self.resizeBtn.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.resizeBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_21.addWidget(self.resizeBtn)


        self.horizontalLayout_12.addWidget(self.icon, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.subMenuStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"gestion biblioth\u00e8que", None))
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Emprunts", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Livres", None))
        self.membersBtn.setText(QCoreApplication.translate("MainWindow", u"Adherents", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Historique", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Biblioth\u00e9caire", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"ajouter emprunt", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"retourner livre", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"rechercher emprunt", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id Adherent", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Prenom", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ref Livre", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Titre", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date emprunt", None));
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Ajouter Livre", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Modifier Livre", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Supprimer Livre", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Rechercher Livre", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"image du livre", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ref", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"titre", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ecrivain", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"date parution", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"edition", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"quantite", None));
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Ajouter Adherent", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Modifier Adherent", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Supprimer Adherent", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Rechercher Adherent", None))
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"nom", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"prenom", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"adresse", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"telephone", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"date d'inscription", None));
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"id Adherent", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"nom", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"prenom", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ref", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"titre", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"date emprunt", None));
        ___qtablewidgetitem25 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"date retour", None));
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Ajouter Biblioth\u00e9caire", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Modifier Biblioth\u00e9caire", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Supprimer Biblioth\u00e9caire", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"rechercher Biblioth\u00e9caire", None))
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Prenom", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"isAdmin", None));
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Date ajout", None));
        self.pushButton_3.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ajouter emprunt", None))
        self.ajouterEmpruntRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ref du livre", None))
        self.ajouterEmpruntId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id adherent", None))
        self.ajouterEmpruntBtn.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Retourner Livre", None))
        self.returnEmpruntRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ref", None))
        self.empruntDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.returnEmprutnId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id adherent", None))
        self.returnEmpruntBtn.setText(QCoreApplication.translate("MainWindow", u"enregistrer", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"rechercher emprunt", None))
        self.searchEmpruntId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.searchEmpruntNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.searchEmpruntPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.searchEmpruntRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ref", None))
        self.searchEmpruntTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.searchEmpruntDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.searchApplyBtn.setText(QCoreApplication.translate("MainWindow", u"appliquer", None))
        self.searchClearBtn.setText(QCoreApplication.translate("MainWindow", u"effacer", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ajouter adherent", None))
        self.addMemberNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.addMemberPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.addMemberAdresse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.addMemberTel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel", None))
        self.addMemberBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Modifier adherent", None))
        self.editMemberid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.editMemberNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.editMemberPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.editMemberAdresse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.editMemberTel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel", None))
        self.editMemberBtn.setText(QCoreApplication.translate("MainWindow", u"enregistrer", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"supprimer adherent", None))
        self.deleteMemberid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.deleteMemberBtn.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"rechercher adherent", None))
        self.searchMemberid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.searchMemberNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.searchMemberPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.searchMemberAdresse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.searchMemberTel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel", None))
        self.MemberApplyFilter.setText(QCoreApplication.translate("MainWindow", u"Appliquer", None))
        self.MemberClearFilter.setText(QCoreApplication.translate("MainWindow", u"Vider", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ajouter Livre", None))
        self.bookTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.bookAuthor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ecrivain", None))
        self.Edition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Edition", None))
        self.bookqte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantite", None))
        self.bookupload.setText(QCoreApplication.translate("MainWindow", u"Upload image", None))
        self.bookAdd.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Modifier Livre", None))
        self.editRef.setText("")
        self.editRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.editTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.editAuthor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ecrivain", None))
        self.editEdition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Edition", None))
        self.editQte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantite", None))
        self.bookEdit.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Supprimer Livre", None))
        self.deleteRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.deleteBookBtn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"rechercher Livre", None))
        self.searchRef.setText("")
        self.searchRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.searchTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.searchAuthor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ecrivain", None))
        self.searchEdition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Edition", None))
        self.searchBookBtn.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.clearBookBtn.setText(QCoreApplication.translate("MainWindow", u"Vider", None))
        self.searchHistoryId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.searchHistoryNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.searchHistoryPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.searchHistoryRef.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ref", None))
        self.searchHistoryTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"date emprunt :", None))
        self.searchHistoryEmp.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"date retour :", None))
        self.searchHistoryRetour.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.searchHistoryApplyBtn.setText(QCoreApplication.translate("MainWindow", u"Appliquer", None))
        self.searchHistoryClearBtn.setText(QCoreApplication.translate("MainWindow", u"Vider", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ajouter Biblioth\u00e9caire", None))
        self.addLibrarianNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.addLibrarianPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.addLibrarianLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.addLibrarianPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot De Passe", None))
        self.addLibrarianConf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmer mdp", None))
        self.addAdmin.setItemText(0, QCoreApplication.translate("MainWindow", u"is Admin", None))
        self.addAdmin.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))
        self.addAdmin.setItemText(2, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.addLibrarianBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Modifer Biblioth\u00e9caire", None))
        self.editLibrarianId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.editLibrarianNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.editLibrarianPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.editLibrarianLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.editLibrarianPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.editLibrarianConf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.editAdmin.setItemText(0, QCoreApplication.translate("MainWindow", u"is Admin", None))
        self.editAdmin.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))
        self.editAdmin.setItemText(2, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.editLibrarianBtn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Supprimer Biblioth\u00e9caire", None))
        self.deleteLibrarianId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.deleteLibrarianBtn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Rechercher Biblioth\u00e9caire", None))
        self.searchLibrarianId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.searchLibrarianNom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.searchLibrarianPrenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.searchAdmin.setItemText(0, QCoreApplication.translate("MainWindow", u"is Admin", None))
        self.searchAdmin.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))
        self.searchAdmin.setItemText(2, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.searchLibrarianBtn.setText(QCoreApplication.translate("MainWindow", u"Appliquer", None))
        self.LibrarianClearBtn.setText(QCoreApplication.translate("MainWindow", u"Vider", None))
        self.resizeBtn.setText("")
    # retranslateUi

