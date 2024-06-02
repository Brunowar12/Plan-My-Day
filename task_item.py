from imports import *


class TaskItem(QWidget):
    closeClicked = pyqtSignal(int)
    favoriteToggled = pyqtSignal(int, bool)
    checkboxToggled = pyqtSignal(int, bool)  # Add this line to define the checkboxToggled signal

    checked_style = "text-decoration: line-through;"
    unchecked_style = "text-decoration: none;"
    expired_style = "color: red;"
    in_progress_style = "color: yellow;"
    completed_style = "color: green;"

    def __init__(self, text, state, position, created_date, is_favorite, end_date_time, *args, **kwargs):
        super().__init__()
        self.position = position
        self.end_date_time = QDateTime.fromString(end_date_time, 'dd.MM.yyyy HH:mm')  # Convert string to QDateTime

        self.ui = uic.loadUi("./assets/UI/task.ui", self)
        with open("./static/style_task.qss", "r") as f:
            style_str = f.read()
            self.setStyleSheet(style_str)

        self.task = self.ui.checkBox_3
        self.task.setText(text)
        self.task.setChecked(state)
        if state:
            self.task.setStyleSheet(self.checked_style)
        else:
            self.task.setStyleSheet(self.unchecked_style)

        self.favorite_checkbox = self.ui.check_favorite
        self.favorite_checkbox.setChecked(is_favorite)
        self.favorite_checkbox.stateChanged.connect(self.update_favorite)

        self.task.stateChanged.connect(self.update_style)
        self.task.stateChanged.connect(self.emitCheckboxToggled)  # Connect the stateChanged signal to emitCheckboxToggled

        self.close_btn = self.ui.pushButton_4
        self.close_btn.setText("")
        self.close_btn.setIcon(QIcon("./static/icons/close_off.png"))
        self.close_btn.installEventFilter(self)

        self.close_btn.clicked.connect(self.emitCloseSignal)

        self.ui.task_label_end.setText(created_date)
        self.ui.task_label_end.setText(f"End {self.end_date_time.toString('dd.MM.yyyy HH:mm')}")
        self.ui.label_day.setText(created_date)

        self.update_task_status()  # Update task status initially

    def eventFilter(self, obj, event):
        if obj == self.close_btn and event.type() == QEvent.Type.Enter:
            self.close_btn.setIcon(QIcon("./static/icons/close_on.png"))
        elif obj == self.close_btn and event.type() == QEvent.Type.Leave:
            self.close_btn.setIcon(QIcon("./static/icons/close_off.png"))
        return super().eventFilter(obj, event)

    def update_style(self, state):
        self.task.setStyleSheet(self.checked_style if state else self.unchecked_style)
        self.update_task_status()

    def update_favorite(self, state):
        self.favoriteToggled.emit(self.position, bool(state))

    def get_checkbox_state(self):
        return self.task.isChecked()

    def get_checkbox_text(self):
        return self.task.text()

    def get_favorite_state(self):
        return self.favorite_checkbox.isChecked()

    def get_end_date_time(self):
        return self.end_date_time  # Return the stored end date and time

    def emitCloseSignal(self):
        self.closeClicked.emit(self.position)

    def emitCheckboxToggled(self, state):
        self.checkboxToggled.emit(self.position, bool(state))

    def set_expired_style(self):
        self.ui.label_task_status.setStyleSheet(self.expired_style)

    def set_in_progress_style(self):
        self.ui.label_task_status.setStyleSheet(self.in_progress_style)

    def set_completed_style(self):
        self.ui.label_task_status.setStyleSheet(self.completed_style)

    def update_task_status(self):
        if self.task.isChecked():
            self.ui.label_task_status.setText("Task Completed")
            self.set_completed_style()
        elif self.end_date_time < QDateTime.currentDateTime():
            self.ui.label_task_status.setText("Task Expired")
            self.set_expired_style()
        else:
            self.ui.label_task_status.setText("Task In Progress")
            self.set_in_progress_style()
