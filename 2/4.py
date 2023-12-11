import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Convert_money(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.num = 0.0
        vbox = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setText("Currency Converter")
        vbox.addWidget(self.label)

        self.number = QLineEdit(self)
        vbox.addWidget(self.number)
        btn_to_usd = QPushButton("To USD", self)
        btn_to_usd.clicked.connect(self.convert)
        btn_to_thb = QPushButton("To THB", self)
        btn_to_thb.clicked.connect(self.convert)
        vbox.addWidget(btn_to_usd)
        vbox.addWidget(btn_to_thb)
        self.setLayout(vbox)
        self.show()

    def convert(self):
        text = self.sender().text()
        if text == "To USD":
            self.num = int(self.number.text()) / 30
        else:
            self.num = int(self.number.text()) * 30
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Result = " + str(self.num))
        layout.addWidget(label)
        close_btn = QPushButton("close", self)
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Convert_money()
    sys.exit(app.exec())