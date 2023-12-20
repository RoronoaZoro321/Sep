import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_1 import Ui_Form

def say_hello():
    print("Hello World")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    From = QWidget()
    ui = Ui_Form()
    ui.setupUi(From)
    ui.hello_btn.clicked.connect(say_hello)
    From.show()
    sys.exit(app.exec())