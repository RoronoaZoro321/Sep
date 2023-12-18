import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from try_1 import Ui_MainWindow
import time
import random

class PasswordGenerator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_1.clicked.connect(self.generate)
        self.ui.pushButton_2.clicked.connect(self.save)
        self.ui.pushButton_3.clicked.connect(self.viewSavedList)  
        self.saved_passwords = {}
    
    def generate(self):
        self.ui.result.setText("Generating...")
        length = self.ui.lineEdit_1.text()
        number_checked = self.ui.checkBox_1.isChecked()
        symbol_checked = self.ui.checkBox_2.isChecked()
        uppercase_checked = self.ui.checkBox_3.isChecked()
        
        password = ""
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

        if number_checked:
            alphabets.extend(numbers)
            random_from_numbers = random.choice(numbers)
            password += random_from_numbers
        if symbol_checked:
            alphabets.extend(symbols)
            random_from_symbols = random.choice(symbols)
            password += random_from_symbols
        if uppercase_checked:
            alphabets.extend([i.upper() for i in alphabets])
            random_from_uppercase = random.choice([i.upper() for i in alphabets])
            password += random_from_uppercase
        for i in range(int(length) - len(password)):
            random_from_alphabets = random.choice(alphabets)
            password += random_from_alphabets
        
        self.ui.result.setText(password)

    def save(self):
        self.saved_passwords[self.ui.lineEdit_2.text()] = self.ui.result.text()
        self.ui.lineEdit_2.setText("")
        self.ui.result.setText("Saved!")
        self.ui.result.setText("")

    def viewSavedList(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Saved Passwords:")
        layout.addWidget(label)
        for key, value in self.saved_passwords.items():
            label = QLabel(self)
            label.setText(key + ": " + value)
            layout.addWidget(label)
        close_btn = QPushButton("close", self)
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
