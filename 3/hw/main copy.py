import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
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
        self.ui.pushButton.clicked.connect(self.addToList)
        self.saved_passwords = {}
    
    def generate(self):
        self.ui.result.setText("Generating...")
        length = self.ui.lineEdit_1.text()
        if length == "":
            self.ui.result.setText("Please enter password length")
            return
        if length.isdigit() == False:
            self.ui.result.setText("Please enter number only")
            return
        length = int(length)
        if length < 3 and length > 50:
            self.ui.result.setText("Please enter number more than 3 and less than 50")
            return
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
        for i in range(length - len(password)):
            random_from_alphabets = random.choice(alphabets)
            password += random_from_alphabets
        
        self.ui.result.setText(password)

    def save(self):
        self.saved_passwords[self.ui.lineEdit_2.text()] = self.ui.result.text()
        self.ui.lineEdit_2.setText("")
        self.ui.result.setText("Saved!")
        self.ui.result.setText("")

    def viewSavedList(self):
        from dialog import Ui_Dialog
        dialog = QDialog(self)
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        

        for key, value in self.saved_passwords.items():
            label_key = QLabel(self)
            label_key.setText(key)
            label_key.setStyleSheet("font-weight: bold; color:  brown;")

            label_value = QLabel(self)
            label_value.setText(value)
            label_value.setStyleSheet("font-weight: bold; color:  grey;")

            box = QGroupBox(self)   
            box.setStyleSheet("border: 2px solid black; border-radius: 5px;")   
            box_layout = QHBoxLayout()
            box.setLayout(box_layout)
            box_layout.addWidget(label_key)
            box_layout.addWidget(label_value)

            # spacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
            # box_layout.addItem(spacer)

            # button = QPushButton(self)
            # button.setText("Copy")
            # button.setStyleSheet("background-color: blue; color: white; border-radius: 5px;")
            # add the style to the button when clicked
            # button.clicked.connect(lambda: button.setStyleSheet("background-color: green; color: white; border-radius: 5px;"))
            # button.clicked.connect(lambda: QApplication.clipboard().setText(value))
            # button.setMaximumWidth(50)
            # button.setMaximumHeight(25)
            # ui.setAlignment(button, Qt.AlignRight)
            # ui.verticalLayout_2.addWidget(button)            
            
            ui.verticalLayout_2.addWidget(box)
            
        dialog.show()
        dialog.exec()

    def addToList(self):
        self.saved_passwords[self.ui.lineEdit_3.text()] = self.ui.lineEdit_4.text()
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
