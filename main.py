from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QButtonGroup, QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt  

app = QApplication([])
window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Login")
window.show()


main_line = QVBoxLayout()
line1 = QHBoxLayout()
button1 = QPushButton("login")
username = QLineEdit()
password = QLineEdit()


usernameLabel = QLabel("Username")
passwordLabel = QLabel("Password")

main_line.addWidget(usernameLabel, alignment=Qt.AlignCenter)



window.setLayout(main_line)
main_line.addWidget(username, alignment=Qt.AlignCenter)

main_line.addWidget(passwordLabel, alignment=Qt.AlignCenter)

main_line.addWidget(password, alignment=Qt.AlignCenter)
main_line.addWidget(button1, alignment=Qt.AlignCenter)







app.exec_()
