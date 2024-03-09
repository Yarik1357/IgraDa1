from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


app = QApplication([])

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Login")
window.show()



app.exec_()

