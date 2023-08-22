import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 150)
        self.setStyleSheet("background-color:#0F7D25;")

        self.username_label = QLabel("Username:", self)
        self.username_label.move(20, 20)
        self.username_input = QLineEdit(self)
        self.username_input.move(100, 20)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(20, 50)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(100, 50)

        self.login_button = QPushButton("Login", self)
        self.login_button.move(100, 90)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "asiNO":
            QMessageBox.information(self, "Login", "Login exitoso")
            self.close()
            self.openMainAppWindow()
        else:
            QMessageBox.warning(self, "Login", "Credenciales inválidas")

    def openMainAppWindow(self):
        main_window = QMainWindow()
        main_window.setWindowTitle("Aplicación principal")
        main_window.setGeometry(100, 100, 400, 300)

        label = QLabel("Selecciona un elemento:", main_window)
        label.move(20, 20)

        button1 = QPushButton("Elemento 1", main_window)
        button1.move(20, 50)

        button2 = QPushButton("Elemento 2", main_window)
        button2.move(20, 80)

        button3 = QPushButton("Elemento 3", main_window)
        button3.move(20, 110)

        main_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
