# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 721)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 95 12pt \"MS Shell Dlg 2\";")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(230, 0, 1051, 721))
        self.widget_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.517, y1:0.0113636, x2:0.482, y2:1, stop:0 rgba(219, 227, 255, 255), stop:1 rgba(168, 168, 168, 255));")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(520, 40, 481, 291))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 50px;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 231, 721))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/image/wallet_855279 2.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: #8995A0;\n"
"	margin: 20px;\n"
"	border: none;\n"
"	opacity: 0.3;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #2576EC;\n"
"	opacity: 1;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/image/home 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: #8995A0;\n"
"	margin: 20px;\n"
"	border: none;\n"
"	opacity: 0.3;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #2576EC;\n"
"	opacity: 1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/image/profit 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: #8995A0;\n"
"	margin: 20px;\n"
"	border: none;\n"
"	opacity: 0.3;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #2576EC;\n"
"	opacity: 1;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/image/profiles 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: #8995A0;\n"
"	margin: 20px;\n"
"	border: none;\n"
"	opacity: 0.3;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #2576EC;\n"
"	opacity: 1;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"ui/image/setting 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Portfolio", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Investment", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Event Tracking", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

