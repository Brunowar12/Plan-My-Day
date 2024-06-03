from imports import *
from task_item import TaskItem

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
        created_date TEXT NOT NULL,
        favorite BOOLEAN NOT NULL CHECK (favorite IN (0, 1)),
        end_date_time TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
        created_date TEXT NOT NULL,
        favorite BOOLEAN NOT NULL CHECK (favorite IN (0, 1)),
        end_date_time TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

class Database:
    def get_tasks(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, task, completed, created_date, favorite, end_date_time FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    def get_history(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, task, completed, created_date, favorite, end_date_time FROM history')
        history = cursor.fetchall()
        conn.close()
        return history

    def add_task(self, task_text, end_date_time_str):
        created_date = datetime.date.today().strftime("%d %B")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (task, completed, created_date, favorite, end_date_time) VALUES (?, ?, ?, ?, ?)",
            (task_text, False, created_date, False, end_date_time_str),
        )
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.show_tasks(self.task_list)

    def remove_item(self, position):
        task_id = self.task_list[position][0]
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.add_to_history(self.task_list[position])
        self.show_tasks(self.task_list)

    def add_to_history(self, task):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO history (task, completed, created_date, favorite, end_date_time)
        VALUES (?, ?, ?, ?, ?)
        ''', (task[1], task[2], task[3], task[4], task[5]))
        conn.commit()
        conn.close()
        self.history_list = self.get_history()
        self.show_history(self.history_list)

    def show_tasks(self, task_list):
        self.list_model.clear()
        self.fav_model.clear()
        for i, task in enumerate(task_list):
            if len(task) < 6:
                print(f"Invalid task format at index {i}: {task}")
                continue

            item = QStandardItem()
            self.list_model.appendRow(item)
            widget = TaskItem(task[1], task[2], i, task[3], task[4], task[5])
            widget.closeClicked.connect(self.remove_item)
            widget.favoriteToggled.connect(self.update_favorites)
            widget.checkboxToggled.connect(self.update_task_status)

            # Update task status and set styles accordingly
            end_date_time = QDateTime.fromString(task[5], 'dd.MM.yyyy HH:mm')
            if widget.ui.checkBox_3.isChecked():
                widget.ui.label_task_status.setText("Task Completed")
                widget.ui.label_task_status.setStyleSheet("color: green;")
            elif end_date_time < QDateTime.currentDateTime():
                widget.ui.label_task_status.setText("Task Expired")
                widget.ui.label_task_status.setStyleSheet("color: red;")
            else:
                widget.ui.label_task_status.setText("Task In Progress")
                widget.ui.label_task_status.setStyleSheet("color: yellow;")

            item.setSizeHint(widget.sizeHint())
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)
            if task[4]:
                fav_item = QStandardItem()
                self.fav_model.appendRow(fav_item)
                fav_widget = TaskItem(task[1], task[2], i, task[3], task[4], task[5])
                fav_widget.closeClicked.connect(self.remove_item)
                fav_widget.favoriteToggled.connect(self.update_favorites)
                fav_widget.checkboxToggled.connect(self.update_task_status)

                # Update task status and set styles accordingly
                end_date_time = QDateTime.fromString(task[5], 'dd.MM.yyyy HH:mm')
                if fav_widget.ui.checkBox_3.isChecked():
                    fav_widget.ui.label_task_status.setText("Task Completed")
                    fav_widget.ui.label_task_status.setStyleSheet("color: green;")
                elif end_date_time < QDateTime.currentDateTime():
                    fav_widget.ui.label_task_status.setText("Task Expired")
                    fav_widget.ui.label_task_status.setStyleSheet("color: red;")
                else:
                    fav_widget.ui.label_task_status.setText("Task In Progress")
                    fav_widget.ui.label_task_status.setStyleSheet("color: yellow;")

                fav_item.setSizeHint(fav_widget.sizeHint())
                self.list_view_fav.setIndexWidget(self.fav_model.indexFromItem(fav_item), fav_widget)

    def show_history(self, history_list):
        self.history_model.clear()
        for i, task in enumerate(history_list):
            item = QStandardItem()
            self.history_model.appendRow(item)
            widget = TaskItem(task[1], task[2], i, task[3], task[4], task[5])
            item.setSizeHint(widget.sizeHint())
            self.list_view_history.setIndexWidget(self.history_model.indexFromItem(item), widget)

    def update_favorites(self, position, is_favorite):
        task_id = self.task_list[position][0]
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET favorite = ? WHERE id = ?', (is_favorite, task_id))
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.show_tasks(self.task_list)

    def update_task_status(self, position, is_checked):
        task_id = self.task_list[position][0]
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (is_checked, task_id))
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.show_tasks(self.task_list)

    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task and self.selected_end_date_time:
            end_date_time_str = self.selected_end_date_time.toString('dd.MM.yyyy HH:mm')
            self.add_task(new_task, end_date_time_str)
            self.task_input.clear()
            self.selected_end_date_time = None  # Clear the selected end date and time

    def get_all_tasks(self):
        self.task_list = []
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        for task in tasks:
            self.task_list.append([
                task[1],  # Task text
                bool(task[2]),  # Completed
                task[3],  # Created date
                bool(task[4]),  # Favorite
                QDateTime.fromString(task[5], 'dd.MM.yyyy HH:mm')  # End date time
            ])

    def closeEvent(self, event):
        self.get_all_tasks()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for task in self.task_list:
            cursor.execute('UPDATE tasks SET task = ?, completed = ?, created_date = ?, favorite = ?, end_date_time = ? WHERE id = ?',
                           (task[0], task[1], task[2], task[3], task[4].toString('dd.MM.yyyy HH:mm'), task[0]))
        conn.commit()
        conn.close()
