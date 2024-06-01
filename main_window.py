from imports import *
from assets.UI.sidebar_ui import Ui_MainWindow as Ui_SidebarWindow
from task_item import TaskItem


# POPUP WINDOW CLASS
class DateTimePopup(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./assets/UI/date_time_popup.ui', self)
        self.setStyleSheet(open("./static/style.qss").read())

        # Set today's date and time as default
        current_date_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_date_time)

        self.okButton.clicked.connect(self.accept)
        self.dateTimeEdit.dateTimeChanged.connect(self.update_selected_date_time)

    def update_selected_date_time(self):
        selected_date_time = self.dateTimeEdit.dateTime()
        self.labelSelectedDateTime.setText(f"Selected date and time: {selected_date_time.toString('dd.MM.yyyy HH:mm')}")

    def get_selected_date_time(self):
        return self.dateTimeEdit.dateTime()


# MAIN APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SidebarWindow()
        self.ui.setupUi(self)

        self.settings = QSettings("YourCompanyName", "YourAppName")

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

        self.task_file_path = os.path.join(os.getcwd(), "static/tasks.yaml")  # Task storage file
        self.history_file_path = os.path.join(os.getcwd(), "static/history.yaml")  # History storage file

        self.task_list = self.get_tasks()  # Load tasks from storage
        self.history_list = self.get_history()  # Load history from storage

        self.show_tasks(self.task_list)  # Display tasks in the UI
        self.show_history(self.history_list)  # Display history in the UI
        self.update_current_date()

        # Connect the popup button signal to the slot
        self.add_btn_time.clicked.connect(self.show_date_time_popup)

        self.selected_end_date_time = None  # Store the selected end date and time

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
                print("Не удалось открыть файл темы.")
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

    def remove_item(self, position):
        removed_task = self.task_list.pop(position)
        self.add_to_history(removed_task)
        self.show_tasks(self.task_list)

    def get_tasks(self):
        if not os.path.exists(self.task_file_path):
            with open(self.task_file_path, "w") as f:
                yaml.dump({"tasks": []}, f)
        with open(self.task_file_path, "r") as f:
            tasks = yaml.safe_load(f)
            if tasks is None or "tasks" not in tasks:
                return []
            return tasks["tasks"]

    def get_history(self):
        if not os.path.exists(self.history_file_path):
            with open(self.history_file_path, "w") as f:
                yaml.dump({"tasks": []}, f)
        with open(self.history_file_path, "r") as f:
            history = yaml.safe_load(f)
            if history is None or "tasks" not in history:
                return []
            return history["tasks"]

    def add_to_history(self, task):
        self.history_list.append(task)
        with open(self.history_file_path, "w") as f:
            f.write(yaml.dump({"tasks": self.history_list}))
        self.show_history(self.history_list)

    def show_history(self, history_list):
        self.history_model.clear()
        for i, task in enumerate(history_list):
            item = QStandardItem()
            self.history_model.appendRow(item)
            widget = TaskItem(task[0], task[1], i, task[2], task[3], task[4])
            item.setSizeHint(widget.sizeHint())
            self.list_view_history.setIndexWidget(self.history_model.indexFromItem(item), widget)

    def show_tasks(self, task_list):
        self.list_model.clear()
        self.fav_model.clear()
        for i, task in enumerate(task_list):
            item = QStandardItem()
            self.list_model.appendRow(item)
            widget = TaskItem(task[0], task[1], i, task[2], task[3], task[4])
            widget.closeClicked.connect(self.remove_item)
            widget.favoriteToggled.connect(self.update_favorites)
            widget.checkboxToggled.connect(self.update_task_status)  # Correctly connect the checkboxToggled signal
            item.setSizeHint(widget.sizeHint())
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)
            if task[3]:
                fav_item = QStandardItem()
                self.fav_model.appendRow(fav_item)
                fav_widget = TaskItem(task[0], task[1], i, task[2], task[3], task[4])
                fav_widget.closeClicked.connect(self.remove_item)
                fav_widget.favoriteToggled.connect(self.update_favorites)
                fav_widget.checkboxToggled.connect(
                    self.update_task_status)  # Correctly connect the checkboxToggled signal
                fav_item.setSizeHint(fav_widget.sizeHint())
                self.list_view_fav.setIndexWidget(self.fav_model.indexFromItem(fav_item), fav_widget)

    def update_favorites(self, position, is_favorite):
        self.task_list[position][3] = is_favorite
        self.show_tasks(self.task_list)

    def update_task_status(self, position, is_checked):
        self.task_list[position][1] = is_checked
        self.show_tasks(self.task_list)

    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task and self.selected_end_date_time:
            today = datetime.date.today()
            created_date = today.strftime("%d %B")
            end_date_time_str = self.selected_end_date_time.toString('dd.MM.yyyy HH:mm')

            self.task_list.append([new_task, False, created_date, False, end_date_time_str])
            self.show_tasks(self.task_list)
            self.task_input.clear()
            self.selected_end_date_time = None  # Clear the selected end date and time

    def get_all_tasks(self):
        self.task_list = []
        for row in range(self.list_model.rowCount()):
            item = self.list_model.item(row, 0)
            widget = self.list_view.indexWidget(item.index())
            if isinstance(widget, TaskItem):
                self.task_list.append(
                    [widget.get_checkbox_text(), widget.get_checkbox_state(), widget.ui.label_day.text(), widget.get_favorite_state(), widget.get_end_date_time()])

    def closeEvent(self, event):
        self.get_all_tasks()
        task_data = []
        for task in self.task_list:
            task_data.append([task[0], task[1], task[2], task[3], task[4].toString('dd.MM.yyyy HH:mm')])

        with open(self.task_file_path, "w") as f:
            yaml.dump({"tasks": task_data}, f)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

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
            print(f"Selected date and time: {self.selected_end_date_time.toString('dd.MM.yyyy HH:mm')}")

    def update_current_date(self):
        today = datetime.date.today()
        self.ui.label_current_day.setText(today.strftime("%d %B, %A"))
        self.ui.label_current_day_2.setText(today.strftime("%d %B, %A"))
        self.ui.label_current_day_3.setText(today.strftime("%d %B, %A"))

    def on_only_today_btn_clicked(self):
        self.sort_tasks_by_date()

    def sort_tasks_by_date(self):
        today = datetime.date.today().strftime("%d %B")
        today_tasks = [task for task in self.task_list if task[2] == today]
        other_tasks = [task for task in self.task_list if task[2] != today]
        self.task_list = today_tasks + other_tasks
        self.show_tasks(self.task_list)

    def on_btn_more_clicked(self):
        self.sort_tasks_by_date_left()

    def sort_tasks_by_date_left(self):
        sorted_tasks = sorted(self.task_list, key=lambda task: datetime.datetime.strptime(task[2], "%d %B"))
        self.show_tasks(sorted_tasks)


# Entry point for the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
