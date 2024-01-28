import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from gui_2 import Ui_MainWindow

class TestUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.result = ""
        # self.ui.pushButton_0.clicked.connect(self.clicked)
        # self.ui.pushButton_1.clicked.connect(self.clicked)
        # self.ui.pushButton_2.clicked.connect(self.clicked)
        # self.ui.pushButton_3.clicked.connect(self.clicked)
        # self.ui.pushButton_4.clicked.connect(self.clicked)
        # self.ui.pushButton_5.clicked.connect(self.clicked)
        # self.ui.pushButton_6.clicked.connect(self.clicked)
        # self.ui.pushButton_7.clicked.connect(self.clicked)
        # self.ui.pushButton_8.clicked.connect(self.clicked)
        # self.ui.pushButton_9.clicked.connect(self.clicked)
        # self.ui.pushButton_mul.clicked.connect(self.clicked)
        # self.ui.pushButton_hashtag.clicked.connect(self.clicked)
        # self.ui.pushButton_delete.clicked.connect(self.clicked)
        # self.ui.pushButton_talk.clicked.connect(self.clicked)

    # def clicked(self):
    #     sender = self.sender()
    #     if sender.text() == "Talk":
    #         dialog = QDialog(self)
    #         layout = QVBoxLayout()
    #         label = QLabel(self)
    #         label.setText("Daillaing" + self.result)
    #         layout.addWidget(label)
    #         close_btn = QPushButton("close", self)
    #         close_btn.clicked.connect(dialog.close)
    #         layout.addWidget(close_btn)
    #         dialog.setLayout(layout)
    #         dialog.show()
    #     elif sender.text() == "<":
    #         self.result = self.result[:-1]
    #         self.ui.output.setText(self.result)
    #     else:
    #         self.result += sender.text()
    #         self.ui.output.setText(self.result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TestUI()
    w.show()
    sys.exit(app.exec())