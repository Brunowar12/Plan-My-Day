from imports import *
from init_database import *
from assets.UI.sidebar_ui import Ui_MainWindow as Ui_SidebarWindow

# POPUP WINDOW CLASS
class DateTimePopup(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./assets/UI/date_time_popup.ui", self)
        self.setStyleSheet(open("./static/style.qss").read())

        # Access and resize the internal calendar widget
        calendar = self.dateTimeEdit.calendarWidget()
        calendar.setMinimumSize(200, 150)
        calendar.setMaximumSize(600, 400)

        # Set today's date and time as default
        current_date_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_date_time)

        self.okButton.clicked.connect(self.accept)
        self.dateTimeEdit.dateTimeChanged.connect(self.update_selected_date_time)

    def update_selected_date_time(self):
        selected_date_time = self.dateTimeEdit.dateTime()
        self.labelSelectedDateTime.setText(
            f"Selected date and time: {selected_date_time.toString('dd.MM.yyyy HH:mm')}"
        )

    def get_selected_date_time(self):
        return self.dateTimeEdit.dateTime()

# MAIN APPLICATION WINDOW
class MainWindow(QMainWindow, Database):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SidebarWindow()
        self.db_path = os.path.join(os.getcwd(), "tasks.db")
        init_db(self.db_path)
        self.ui.setupUi(self)

        self.settings = QSettings("YourCompanyName", "YourAppName")

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        # Connect signals to slots
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.stackedWidget.currentChanged.connect(
            self.on_stackedWidget_currentChanged
        )
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

        # Dark Theme
        self.ui.checkBox_theme.stateChanged.connect(self.toggle_dark_mode)

        dark_mode_enabled = self.settings.value("darkModeEnabled", False, type=bool)
        self.ui.checkBox_theme.setChecked(dark_mode_enabled)
        self.apply_dark_mode(dark_mode_enabled)

        # Connect the Only Today button signal to the slot
        self.ui.btn_only_today.clicked.connect(self.on_only_today_btn_clicked)

        # Assign UI elements to variables for easier access
        self.list_view = self.ui.listView_2
        self.list_view_fav = self.ui.list_view_fav
        self.list_view_history = self.ui.list_view_history  # listView for history
        self.add_btn = self.ui.add_btn_task
        self.task_input = self.ui.add_task
        self.add_btn_time = self.ui.add_btn_time  # Button to open the popup

        self.list_model = QStandardItemModel()  # Model for the task list
        self.fav_model = QStandardItemModel()  # Model for the favorite task list
        self.history_model = QStandardItemModel()  # Model for the history task list
        self.init_ui()  # Initialize UI components

        # self.task_file_path = os.path.join(os.getcwd(), "static/tasks.yaml")  # Task storage file;
        # self.history_file_path = os.path.join(os.getcwd(), "static/history.yaml")  # History storage file;

        self.task_list = self.get_tasks()  # Load tasks from storage
        self.history_list = self.get_history()  # Load history from storage

        self.show_tasks(self.task_list)  # Display tasks in the UI
        self.show_history(self.history_list)  # Display history in the UI
        self.update_current_date()

        # Connect the popup button signal to the slot
        self.add_btn_time.clicked.connect(self.show_date_time_popup)

        self.selected_end_date_time = None  # Store the selected end date and time

        # Highlight tasks in calendar
        self.highlight_tasks_in_calendar()

    def toggle_dark_mode(self, state):
        self.settings.setValue("darkModeEnabled", bool(state))
        self.apply_dark_mode(bool(state))

    def apply_dark_mode(self, enable):
        if enable:
            dark_theme = QFile("./static/dark_theme.qss")
            if dark_theme.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
                stream = QTextStream(dark_theme)
                self.setStyleSheet(stream.readAll())
                dark_theme.close()
            else:
                print("Failed to open theme file.")
        else:
            self.setStyleSheet(open("./static/style.qss").read())

    def init_ui(self):
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)
        self.list_view_fav.setModel(self.fav_model)
        self.list_view_fav.setSpacing(5)
        self.list_view_history.setModel(self.history_model)
        self.list_view_history.setSpacing(5)

        self.add_btn.clicked.connect(self.add_new_task)

    def on_search_btn_clicked(self):
        # self.ui.stackedWidget.setCurrentIndex(5)
        self.get_tasks_by_title(self.search_input.text())

    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

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

    def show_date_time_popup(self):
        popup = DateTimePopup()
        if popup.exec():
            self.selected_end_date_time = popup.get_selected_date_time()
            print(
                f"Selected date and time: {self.selected_end_date_time.toString('dd.MM.yyyy HH:mm')}")

    def update_current_date(self):
        today = datetime.date.today()
        self.ui.label_current_day.setText(today.strftime("%d %B, %A"))
        self.ui.label_current_day_2.setText(today.strftime("%d %B, %A"))
        self.ui.label_current_day_3.setText(today.strftime("%d %B, %A"))

    def on_only_today_btn_clicked(self):
        print("Button clicked!")
        self.get_tasks_for_today()

    def on_btn_more_clicked(self):
        self.sort_tasks_by_deadline()

    def get_tasks_with_deadlines(self):
        """
        Получить задачи с датами окончания из базы данных.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT task, end_date_time FROM tasks WHERE end_date_time IS NOT NULL")
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    def highlight_tasks_in_calendar(self):
        tasks = self.get_tasks_with_deadlines()
        calendar = self.ui.calendarWidget

        for task in tasks:
            end_time_str = task[1]
            end_time = QDateTime.fromString(end_time_str, "dd.MM.yyyy HH:mm")
            if end_time.isValid():
                format = QTextCharFormat()
                format.setForeground(QtGui.QColor("orange"))
                calendar.setDateTextFormat(end_time.date(), format)

        calendar.update()
