import os
from PyQt6 import uic
from PySide6 import QtUiTools
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        
        # Імпортуємо основний віджет з mainWindow.ui
        self.main_widget = self.import_ui("mainWindow.ui")
        if self.main_widget:
            layout.addWidget(self.main_widget)
        else:
            layout.addWidget(QPushButton("No main window found"))

        # Додаємо кнопку, яка відкликає відкриття вікна form[0-9].ui
        self.button = QPushButton("Open Widget", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.open_widget)

    def import_ui(self, ui_file):
        if os.path.exists(ui_file):
            return QUiLoader().load(ui_file)
        return None

    def open_widget(self):
        found = False
        widget = QWidget()
        widget.setWindowTitle("Widget")
        layout = QVBoxLayout(widget)
        for i in range(1, 11):  # Перевірка з form1.ui до form10.ui
            form_file = f"form{i}.ui"
            if os.path.exists(form_file):
                form_widget = self.import_ui(form_file)
                layout.addWidget(form_widget)
                found = True
        if not found:
            layout.addWidget(QPushButton("No forms found"))
        widget.show()


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()