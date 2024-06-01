from imports import *
from init_database import *
from assets.UI.sidebar_ui import Ui_MainWindow as Ui_SidebarWindow

# MAIN APPLICATION WINDOW
class MainWindow(QMainWindow, Database):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SidebarWindow()
        self.db_path = os.path.join(os.getcwd(), "tasks.db")
        init_db(self.db_path)
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
                
        # self.task_file_path = os.path.join(os.getcwd(), "static/tasks.yaml")  # Task storage file;
        # self.history_file_path = os.path.join(os.getcwd(), "static/history.yaml")  # History storage file;

        self.task_list = self.get_tasks()  # Load tasks from storage
        self.history_list = self.get_history()  # Load history from storage

        self.show_tasks(self.task_list)  # Display tasks in the UI
        self.show_history(self.history_list)  # Display history in the UI
        self.update_current_date()

    def init_ui(self):
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)
        self.list_view_fav.setModel(self.fav_model)
        self.list_view_fav.setSpacing(5)
        self.list_view_history.setModel(self.history_model)
        self.list_view_history.setSpacing(5)

        self.add_btn.clicked.connect(self.add_new_task)

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
        print("Only today button clicked!")

    def update_current_date(self):
        today = datetime.date.today()
        formatted_date = today.strftime("%A, %B %d")
        self.ui.label_current_day.setText(formatted_date)
        self.ui.label_current_day_2.setText(formatted_date)
        self.ui.label_current_day_3.setText(formatted_date)

    def set_text_color_red(self):
        self.ui.label_current_date.setStyleSheet("color: red;")
