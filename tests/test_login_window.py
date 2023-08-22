
import unittest
from PyQt5.QtWidgets import QApplication
import LoginWindow

class TestLoginWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Inicializar una aplicación PyQt5 para las pruebas
        self.login_window = LoginWindow()

    def test_valid_login(self):
        self.login_window.username_input.setText("admin")
        self.login_window.password_input.setText("asiNO")
        self.login_window.login()
        self.assertTrue(self.login_window.isVisible())  # Verificar que la ventana sigue abierta

    def test_invalid_login(self):
        self.login_window.username_input.setText("user")
        self.login_window.password_input.setText("pass")
        self.login_window.login()
        self.assertFalse(self.login_window.isVisible())  # Verificar que la ventana se cerró

    def tearDown(self):
        self.login_window.close()  
        self.app.quit()  # Terminar la aplicación PyQt5 después de cada prueba

if __name__ == '__main__':
    unittest.main()
