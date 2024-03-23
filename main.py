from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt 
from baza import *


app = QApplication([])

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Authorize 0.1")

window1 = QWidget()
window1.resize(600, 500)
window1.setWindowTitle("Authorize 0.1")

login_btn = QPushButton("Login")
login_lb = QLabel("Enter your login")
passw_lb = QLabel("Enter password")

login_line = QLineEdit()
passw_line = QLineEdit()

main_line1 = QVBoxLayout()
main_line1.addStretch(1)
main_line1.addWidget(login_lb, alignment=Qt.AlignCenter)
main_line1.addWidget(login_line, alignment=Qt.AlignCenter)
main_line1.addWidget(passw_lb, alignment=Qt.AlignCenter)
main_line1.addWidget(passw_line,alignment=Qt.AlignCenter)
main_line1.addWidget(login_btn, alignment=Qt.AlignCenter)
main_line1.addStretch(1)
window.setLayout(main_line1)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)

window1.setLayout(main_line2)

window.show()

def login():
    login_input = login_line.text()
    passw_input = passw_line.text()
    data = get_data(login_input)
    if data:
        if passw_input == data[0][1]:
            print(data)

            window.hide()
            window1.show()
        else:
            print("Wrong password")
    else:
        print("No such login found")
login_btn.clicked.connect(login)

app.exec()