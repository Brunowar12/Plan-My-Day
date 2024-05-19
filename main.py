import json
import os
import sys

from PyQt6.QtCore import QTimer, Qt, QSize, QFile, QTextStream, QIODevice, pyqtSignal, QEvent, QDateTime
from PyQt6.QtGui import QColor, QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QMessageBox, QLineEdit, QPushButton, QWidget
from PyQt6 import uic
from ui_splash_screen import Ui_SplashScreen
from auth_ui import Ui_MainWindow as Ui_AuthWindow
from sidebar_ui import Ui_MainWindow as Ui_SidebarWindow

## ==> GLOBALS
counter = 0

class TaskItem(QWidget):
    closeClicked = pyqtSignal(int)
    favoriteToggled = pyqtSignal(int, bool)

    checked_style = "text-decoration: line-through;"
    unchecked_style = "text-decoration: none;"

    def __init__(self, text, state, position, created_date, is_favorite, *args, **kwargs):
        super().__init__()
        self.position = position

        self.ui = uic.loadUi("./task.ui", self)
        with open("./static/style_task.qss", "r") as f:
            style_str = f.read()
            self.setStyleSheet(style_str)

        self.task = self.ui.checkBox_3
        self.task.setText(text)
        self.task.setChecked(state)
        if state:
            self.task.setStyleSheet(self.checked_style)

        self.favorite_checkbox = self.ui.check_favorite
        self.favorite_checkbox.setChecked(is_favorite)
        self.favorite_checkbox.stateChanged.connect(self.update_favorite)

        self.task.stateChanged.connect(self.update_style)

        self.close_btn = self.ui.pushButton_4
        self.close_btn.setText("")
        self.close_btn.setIcon(QIcon("./static/icons/close_off.png"))
        self.close_btn.installEventFilter(self)

        self.close_btn.clicked.connect(self.emitCloseSignal)

        self.ui.label_day.setText(created_date)

    def eventFilter(self, obj, event):
        if obj == self.close_btn and event.type() == QEvent.Type.Enter:
            self.close_btn.setIcon(QIcon("./static/icons/close_on.png"))
        elif obj == self.close_btn and event.type() == QEvent.Type.Leave:
            self.close_btn.setIcon(QIcon("./static/icons/close_off.png"))
        return super().eventFilter(obj, event)

    def update_style(self, state):
        self.task.setStyleSheet(self.checked_style if state else self.unchecked_style)

    def update_favorite(self, state):
        self.favoriteToggled.emit(self.position, bool(state))

    def get_checkbox_state(self):
        return self.task.isChecked()

    def get_checkbox_text(self):
        return self.task.text()

    def get_favorite_state(self):
        return self.favorite_checkbox.isChecked()

    def emitCloseSignal(self):
        self.closeClicked.emit(self.position)

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

        # Connect signals to slots
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

        # Connect the Only Today button signal to the slot
        self.ui.btn_only_today.clicked.connect(self.on_only_today_btn_clicked)

        # Assign UI elements to variables for easier access
        self.list_view = self.ui.listView_2
        self.list_view_fav = self.ui.list_view_fav
        self.list_view_history = self.ui.list_view_history  # listView for history
        self.add_btn = self.ui.add_btn_task
        self.task_input = self.ui.add_task

        self.list_model = QStandardItemModel()  # Model for the task list
        self.fav_model = QStandardItemModel()  # Model for the favorite task list
        self.history_model = QStandardItemModel()  # Model for the history task list
        self.init_ui()  # Initialize UI components

        self.task_file_path = os.path.join(os.getcwd(), "static/tasks.json")  # Task storage file
        self.history_file_path = os.path.join(os.getcwd(), "static/history.json")  # History storage file

        self.task_list = self.get_tasks()  # Load tasks from storage
        self.history_list = self.get_history()  # Load history from storage

        self.show_tasks(self.task_list)  # Display tasks in the UI
        self.show_history(self.history_list)  # Display history in the UI

    def init_ui(self):
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)
        self.list_view_fav.setModel(self.fav_model)
        self.list_view_fav.setSpacing(5)
        self.list_view_history.setModel(self.history_model)
        self.list_view_history.setSpacing(5)

        self.add_btn.clicked.connect(self.add_new_task)

    def remove_item(self, position):
        removed_task = self.task_list.pop(position)
        self.add_to_history(removed_task)
        self.list_model.removeRow(position)
        self.get_all_tasks()  # Refresh the task list from the UI
        self.show_tasks(self.task_list)

    def get_tasks(self):
        if not os.path.exists(self.task_file_path):
            with open(self.task_file_path, "w") as f:
                f.write(json.dumps({"tasks": []}))
        with open(self.task_file_path, "r") as f:
            tasks = json.load(f)
            return tasks["tasks"]

    def get_history(self):
        if not os.path.exists(self.history_file_path):
            with open(self.history_file_path, "w") as f:
                f.write(json.dumps({"tasks": []}))
        with open(self.history_file_path, "r") as f:
            history = json.load(f)
            return history["tasks"]

    def add_to_history(self, task):
        self.history_list.append(task)
        with open(self.history_file_path, "w") as f:
            f.write(json.dumps({"tasks": self.history_list}))
        self.show_history(self.history_list)

    def show_history(self, history_list):
        self.history_model.clear()
        for i, task in enumerate(history_list):
            item = QStandardItem()
            self.history_model.appendRow(item)
            widget = TaskItem(task[0], task[1], i, task[2], task[3])
            item.setSizeHint(widget.sizeHint())
            self.list_view_history.setIndexWidget(self.history_model.indexFromItem(item), widget)

    def show_tasks(self, task_list):
        self.list_model.clear()
        self.fav_model.clear()
        for i, task in enumerate(task_list):
            item = QStandardItem()
            self.list_model.appendRow(item)
            widget = TaskItem(task[0], task[1], i, task[2], task[3])
            widget.closeClicked.connect(self.remove_item)
            widget.favoriteToggled.connect(self.update_favorites)
            item.setSizeHint(widget.sizeHint())
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)
            if task[3]:
                fav_item = QStandardItem()
                self.fav_model.appendRow(fav_item)
                fav_widget = TaskItem(task[0], task[1], i, task[2], task[3])
                fav_widget.closeClicked.connect(self.remove_item)
                fav_widget.favoriteToggled.connect(self.update_favorites)
                fav_item.setSizeHint(fav_widget.sizeHint())
                self.list_view_fav.setIndexWidget(self.fav_model.indexFromItem(fav_item), fav_widget)

    def update_favorites(self, position, is_favorite):
        self.task_list[position][3] = is_favorite
        self.show_tasks(self.task_list)

    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task:
            import datetime
            today = datetime.date.today()
            created_date = today.strftime("%d %B")

            self.task_list.append([new_task, False, created_date, False])
            self.show_tasks(self.task_list)
            self.task_input.clear()

    def get_all_tasks(self):
        self.task_list = []
        for row in range(self.list_model.rowCount()):
            item = self.list_model.item(row, 0)
            widget = self.list_view.indexWidget(item.index())
            if isinstance(widget, TaskItem):
                self.task_list.append(
                    [widget.get_checkbox_text(), widget.get_checkbox_state(), widget.ui.label_day.text(), widget.get_favorite_state()])

    def closeEvent(self, event):
        self.get_all_tasks()
        with open(self.task_file_path, "w") as f:
            f.write(json.dumps({"tasks": self.task_list}))

    def on_search_btn_clicked(self):
        # Handle the search button click event
        pass

    def on_user_btn_clicked(self):
        # Handle the user button click event
        pass

    def on_stackedWidget_currentChanged(self, index):
        # Handle the stacked widget current changed event
        pass

    def on_home_btn_1_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.home_btn_2.setChecked(True)

    def on_home_btn_2_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.home_btn_1.setChecked(True)

    def on_favorites_btn_1_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.favorites_btn_2.setChecked(True)

    def on_favorites_btn_2_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.favorites_btn_1.setChecked(True)

    def on_calendar_btn_1_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.calendar_btn_2.setChecked(True)

    def on_calendar_btn_2_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.calendar_btn_1.setChecked(True)

    def on_history_btn_1_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.history_btn_2.setChecked(True)

    def on_history_btn_2_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.history_btn_1.setChecked(True)

    def on_options_btn_1_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.options_btn_2.setChecked(True)

    def on_options_btn_2_toggled(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.options_btn_1.setChecked(True)

    def on_only_today_btn_clicked(self):
        # Handle the "Only Today" button click event
        pass

    def update_current_date(self):
        current_date = QDateTime.currentDateTime().toString("dddd, MMMM d, yyyy")
        self.ui.label_current_date.setText(current_date)

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

        ## SHOW ==> MAIN WINDOW
        self.auth = AuthWindow()

        ## INITIAL TEXT
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        ## CHANGE DESCRIPTION TEXT
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        ## SHOW ==> MAIN WINDOW
        QTimer.singleShot(4500, self.show_main_window)

    def show_main_window(self):
        self.auth.show()
        self.close()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        counter += 1
        if counter > 100:
            self.timer.stop()

if __name__ == "__main__":
    import new_icon.resources
    app = QApplication(sys.argv)
    with open("./static/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
