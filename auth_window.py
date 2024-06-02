from imports import *

from assets.UI.auth_ui import Ui_MainWindow as Ui_AuthWindow
from main_window import MainWindow

class AuthWindow(QMainWindow, Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.yaml_file_path = os.path.join(os.getcwd(), "accounts.yaml")

    def initUI(self):
        self.auth_login_button.clicked.connect(self.login)
        self.auth_change_button.clicked.connect(self.change_account)
        self.offline_button.clicked.connect(self.offline_mode)
        self.button_create.clicked.connect(self.create_account)

    def login(self):
        email = self.input_email.text()
        password = self.input_password.text()
        
        accounts = read_from_yaml(self.yaml_file_path)
        
        if email in accounts and accounts[email]['password'] == password:
            QMessageBox.information(self, "Login", "Login successful")
        else:
            QMessageBox.warning(self, "Login", "Invalid email or password")

    def change_account(self):
        self.auth_login.hide()
        self.auth_login_button.hide()
        self.auth_change_button.hide()

        self.input_email = QLineEdit(self.auth)
        self.input_email.setMinimumSize(QSize(0, 40))
        self.input_email.setStyleSheet(
            """
            QLineEdit {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.505682, stop:0 rgba(80, 36, 100, 255), stop:1 rgba(80, 36, 98, 255));
                border: none;
                color: white;
                font-size: 16px;
                padding-left: 5px;
                border-radius: 10px;
            }
            """
        )
        self.input_email.setPlaceholderText("Enter your email")
        self.verticalLayout_7.addWidget(self.input_email)

        self.input_password = QLineEdit(self.auth)
        self.input_password.setMinimumSize(QSize(0, 40))
        self.input_password.setStyleSheet(
            """
            QLineEdit {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.505682, stop:0 rgba(80, 36, 100, 255), stop:1 rgba(80, 36, 98, 255));
                border: none;
                color: white;
                font-size: 16px;
                padding-left: 5px;
                border-radius: 10px;
            }
            """
        )
        self.input_password.setPlaceholderText("Enter your password")
        self.verticalLayout_7.addWidget(self.input_password)

        self.login_button = QPushButton(self.auth)
        self.login_button.setMinimumSize(QSize(0, 40))
        self.login_button.setStyleSheet(
            """
            QPushButton {
                color: white;
                background-color: rgb(115, 44, 133);
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }
            """
        )
        self.login_button.setText("LOGIN")
        self.login_button.clicked.connect(self.login)
        self.verticalLayout_7.addWidget(self.login_button)

        self.button_create.show()

    def offline_mode(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def create_account(self):
        email = self.input_email.text()
        password = self.input_password.text()
        conf_password = self.confpassword_input.text()
        
        if password == conf_password:
            accounts = read_from_yaml(self.yaml_file_path)
            if email in accounts:
                QMessageBox.warning(self, "Create Account", "Account already exists")
            else:
                accounts[email] = {'password': password}
                write_to_yaml(self.yaml_file_path, accounts)
                QMessageBox.information(self, "Create Account", "Account created successfully")
                self.offline_mode()
        else:
            QMessageBox.warning(self, "Create Account", "Passwords do not match")

            
def write_to_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def read_from_yaml(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as file:
        return yaml.safe_load(file) or {}

