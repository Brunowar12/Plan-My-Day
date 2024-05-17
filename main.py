import sys
from PyQt6.QtCore import QTimer, Qt, QSize, QFile, QTextStream, QIODevice
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QMessageBox, QLineEdit, QPushButton
from ui_splash_screen import Ui_SplashScreen
from auth_ui import Ui_MainWindow as Ui_AuthWindow
from sidebar_ui import Ui_MainWindow as Ui_SidebarWindow

## ==> GLOBALS
counter = 0

# AUTHENTICATION WINDOW
class AuthWindow(QMainWindow, Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.auth_login_button.clicked.connect(self.login)
        self.auth_change_button.clicked.connect(self.change_account)
        self.offline_button.clicked.connect(self.offline_mode)
        self.button_create.clicked.connect(self.create_account)

    def login(self):
        email = self.input_email.text()
        password = self.input_password.text()
        if email == "test@example.com" and password == "password":
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
            QMessageBox.information(self, "Create Account", "Account created successfully")
        else:
            QMessageBox.warning(self, "Create Account", "Passwords do not match")

# MAIN APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SidebarWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.stackedWidget.currentChanged.connect(self.on_stackedWidget_currentChanged)
        self.ui.home_btn_1.toggled.connect(self.on_home_btn_1_toggled)
        self.ui.home_btn_2.toggled.connect(self.on_home_btn_2_toggled)
        self.ui.favorites_btn_1.toggled.connect(self.on_favorites_btn_1_toggled)
        self.ui.favorites_btn_2.toggled.connect(self.on_favorites_btn_2_toggled)
        self.ui.calendar_btn_1.toggled.connect(self.on_calendar_btn_1_toggled)
        self.ui.calendar_btn_2.toggled.connect(self.on_calendar_btn_2_toggled)
        self.ui.history_btn_1.toggled.connect(self.on_history_btn_1_toggled)
        self.ui.history_btn_2.toggled.connect(self.on_history_btn_2_toggled)
        self.ui.options_btn_1.toggled.connect(self.on_options_btn_1_toggled)
        self.ui.options_btn_2.toggled.connect(self.on_options_btn_2_toggled)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_favorites_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_favorites_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_calendar_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_calendar_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_history_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_history_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_options_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_options_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.ui.label_description.setText("<strong>WELCOME</strong> TO PLAN MY DAY")
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.auth_window = AuthWindow()
            self.auth_window.show()
            self.close()

        counter += 1

if __name__ == "__main__":
    import new_icon.resources
    app = QApplication(sys.argv)

    style_file = QFile("style.qss")
    if style_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
        style_stream = QTextStream(style_file)
        app.setStyleSheet(style_stream.readAll())
    else:
        print("Не вдалося відкрити style.qss")

    splash = SplashScreen()
    sys.exit(app.exec())
