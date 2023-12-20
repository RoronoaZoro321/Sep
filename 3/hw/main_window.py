# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'try.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 577)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(59, -1, 521, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout.addWidget(self.label_1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_1 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.horizontalLayout.addWidget(self.lineEdit_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBox_1 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        font = QFont()
        font.setPointSize(10)
        self.checkBox_1.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_3)

        self.result = QLabel(self.verticalLayoutWidget)
        self.result.setObjectName(u"result")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.result.setFont(font1)

        self.verticalLayout.addWidget(self.result)

        self.pushButton_1 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(False)
        self.pushButton_1.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700; color:#aa5500;\">Password Manager</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">Generate Password</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#00007f;\">Password Length :</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"Include Numbers", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Include Symbols", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Include Uppercase", None))
        self.result.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#aa55ff;\">Generate</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Save Your password for : ", None))
        self.lineEdit_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"View list of saved password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#55557f;\">Add Password</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"For :", None))
        self.lineEdit_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.lineEdit_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Done", None))
    # retranslateUi

