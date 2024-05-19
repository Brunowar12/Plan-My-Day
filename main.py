import json
import os
import sys


from PyQt6.QtCore import QTimer, Qt, QSize, QFile, QTextStream, QIODevice,pyqtSignal, QEvent, QDateTime
from PyQt6.QtGui import QColor,QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QMessageBox, QLineEdit, QPushButton, QWidget
from PyQt6 import uic
from ui_splash_screen import Ui_SplashScreen
from auth_ui import Ui_MainWindow as Ui_AuthWindow
from sidebar_ui import Ui_MainWindow as Ui_SidebarWindow

## ==> GLOBALS
counter = 0

class TaskItem(QWidget):
    # Signal to indicate when the task's close button is clicked
    closeClicked = pyqtSignal(int)

    # CSS styles for checked and unchecked tasks
    checked_style = "text-decoration: line-through;"
    unchecked_style = "text-decoration: none;"

    def __init__(self, text, state, position, created_date, *args, **kwargs):
        super().__init__()
        self.position = position  # Position of the task in the list, used for deletion

        # Load the task item UI and apply task-specific styles
        self.ui = uic.loadUi("./task.ui", self)
        with open("./static/style_task.qss", "r") as f:
            style_str = f.read()
            self.setStyleSheet(style_str)

        # Initialize the task checkbox with provided text and completion state
        self.task = self.ui.checkBox_3
        self.task.setText(text)
        self.task.setChecked(state)
        if state:
            self.task.setStyleSheet(self.checked_style)

        # Connect the checkbox state change to the style update method
        self.task.stateChanged.connect(self.update_style)

        # Initialize and configure the close button
        self.close_btn = self.ui.pushButton_4
        self.close_btn.setText("")  # Removing default text
        self.close_btn.setIcon(QIcon("./static/icons/close_off.png"))

        # Connect the close button hover event to JavaScript function
        self.close_btn.installEventFilter(self)

        self.close_btn.clicked.connect(self.emitCloseSignal)

        # Set the created date label text
        self.ui.label_day.setText(created_date)

    def eventFilter(self, obj, event):
        if obj == self.close_btn and event.type() == QEvent.Type.Enter:
            # При наведении курсора на кнопку меняем иконку
            self.close_btn.setIcon(QIcon("./static/icons/close_on.png"))
        elif obj == self.close_btn and event.type() == QEvent.Type.Leave:
            # При уходе курсора с кнопки возвращаем исходную иконку
            self.close_btn.setIcon(QIcon("./static/icons/close_off.png"))
        return super().eventFilter(obj, event)

    # Update the task's visual style based on its completion state
    def update_style(self, state):
        self.task.setStyleSheet(self.checked_style if state else self.unchecked_style)

    # Retrieve the current state and text of the task
    def get_checkbox_state(self):
        return self.task.isChecked()

    def get_checkbox_text(self):
        return self.task.text()

    # Emit a signal indicating the task should be closed, passing its position
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
        self.add_btn = self.ui.add_btn_task
        self.task_input = self.ui.add_task

        self.list_model = QStandardItemModel()  # Model for the task list
        self.init_ui()  # Initialize UI components

        self.task_file_path = os.path.join(os.getcwd(), "static/tasks.json")  # Task storage file
        self.task_list = self.get_tasks()  # Load tasks from storage
        self.show_tasks(self.task_list)  # Display tasks in the UI

        # Update the current date label
        self.update_current_date()

    # Initialize UI components and connect signals
    def init_ui(self):
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)


        self.add_btn.clicked.connect(self.add_new_task)

    # Remove a task item from the list
    def remove_item(self, position):
        self.list_model.removeRow(position)
        self.task_list.pop(position)
        self.get_all_tasks()  # Refresh the task list from the UI
        self.show_tasks(self.task_list)

    # Load tasks from the JSON storage file
    def get_tasks(self):
        with open(self.task_file_path, "r") as f:
            tasks = json.load(f)
            return tasks["tasks"]

    # Display tasks in the list view using custom widgets
    def show_tasks(self, task_list):
        self.list_model.clear()
        for i, task in enumerate(task_list):
            item = QStandardItem()
            self.list_model.appendRow(item)
            widget = TaskItem(task[0], task[1], i, task[2])
            widget.closeClicked.connect(self.remove_item)
            item.setSizeHint(widget.sizeHint())
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)

    # Add a new task based on user input
    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task:
            # Get the current date and format it as required
            import datetime
            today = datetime.date.today()
            created_date = today.strftime("%d %B")

            self.task_list.append([new_task, False, created_date])
            self.show_tasks(self.task_list)
            self.task_input.clear()

    # Update the task list based on the current UI state
    def get_all_tasks(self):
        self.task_list = []
        for row in range(self.list_model.rowCount()):
            item = self.list_model.item(row, 0)
            widget = self.list_view.indexWidget(item.index())
            if isinstance(widget, TaskItem):
                self.task_list.append(
                    [widget.get_checkbox_text(), widget.get_checkbox_state(), widget.ui.label_day.text()])

    # Save the current tasks to a JSON file when the application is closed.
    def closeEvent(self, event):
        self.get_all_tasks()
        with open(self.task_file_path, "w") as f:
            f.write(json.dumps({"tasks": self.task_list}))

    ## Search function
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function to change page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change the status of QPushButton Checkable when the stackedWidget index changes
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    ## functions to change the menu page
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

    ## Function to display only today's tasks
    def on_only_today_btn_clicked(self):
        today_tasks = [task for task in self.task_list if task[2] == QDateTime.currentDateTime().toString("dd MMMM")]
        self.show_tasks(today_tasks)

    ## Function to update the current date
    def update_current_date(self):
        current_date_time = QDateTime.currentDateTime()
        formatted_date_time = current_date_time.toString("dddd, MMMM d")
        self.ui.label_current_day.setText(formatted_date_time)
        self.ui.label_current_day_2.setText(formatted_date_time)
        self.ui.label_current_day_3.setText(formatted_date_time)

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

    style_file = QFile("./static/style.qss")
    if style_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
        style_stream = QTextStream(style_file)
        app.setStyleSheet(style_stream.readAll())
    else:
        print("Could not open style.qss")

    splash = SplashScreen()
    sys.exit(app.exec())
