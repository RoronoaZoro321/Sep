import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_2 import Ui_Form

class TestUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.num = 0
        self.ui.inc_button.clicked.connect(self.inc)
        self.ui.dec_button.clicked.connect(self.dec)
        self.ui.pushButton.clicked.connect(self.reset)

    def inc(self):
        self.num += 1
        self.ui.num_label.setText(str(self.num))

    def dec(self):
        self.num -= 1
        self.ui.num_label.setText(str(self.num))

    def reset(self):
        self.num = 0
        self.ui.num_label.setText(str(self.num))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TestUI()
    w.show()
    sys.exit(app.exec())