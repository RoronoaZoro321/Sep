# include textbox, button, and label
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import time
import random

class PasswordGenerator(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Password Generator")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.label = QLabel(self)
        self.label.setText("Password Generator")
        self.layout.addWidget(self.label)

        self.label = QLabel(self)
        self.label.setText("Password Length:")
        self.layout.addWidget(self.label)

        self.length = QLineEdit(self)
        self.layout.addWidget(self.length)

        self.checkbox_number = QCheckBox("Include numbers", self)
        self.layout.addWidget(self.checkbox_number)

        self.checkbox_symbol = QCheckBox("Include symbols", self)
        self.layout.addWidget(self.checkbox_symbol)

        self.checkbox_uppercase = QCheckBox("Include uppercase", self)
        self.layout.addWidget(self.checkbox_uppercase)

        self.btn = QPushButton("Generate", self)
        self.btn.clicked.connect(self.generate)
        
        self.password = QLabel(self)
        self.password.setText("")
        self.layout.addWidget(self.password)

        self.layout.addWidget(self.btn)
        self.show()

    def generate(self):
        self.password.setText("Generating...")
        length = self.length.text()
        number_checked = self.checkbox_number.isChecked()
        symbol_checked = self.checkbox_symbol.isChecked()
        uppercase_checked = self.checkbox_uppercase.isChecked()
        
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
        
        self.password.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec())