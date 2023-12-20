# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2_2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(447, 388)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 280, 131, 81))
        font = QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.num_label = QLabel(self.widget)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(50, 90, 151, 161))
        font1 = QFont()
        font1.setPointSize(72)
        self.num_label.setFont(font1)
        self.num_label.setLayoutDirection(Qt.LeftToRight)
        self.num_label.setAlignment(Qt.AlignCenter)
        self.dec_button = QPushButton(self.widget)
        self.dec_button.setObjectName(u"dec_button")
        self.dec_button.setGeometry(QRect(230, 140, 131, 121))
        font2 = QFont()
        font2.setPointSize(36)
        self.dec_button.setFont(font2)
        self.inc_button = QPushButton(self.widget)
        self.inc_button.setObjectName(u"inc_button")
        self.inc_button.setGeometry(QRect(230, 10, 131, 121))
        self.inc_button.setMinimumSize(QSize(0, 24))
        self.inc_button.setFont(font2)
        self.pushButton.raise_()
        self.dec_button.raise_()
        self.inc_button.raise_()
        self.num_label.raise_()

        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.num_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.dec_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

