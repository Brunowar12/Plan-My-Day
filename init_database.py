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
    def execute_query(self, query, params=()):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results

    def get_tasks(self):
        query = 'SELECT id, task, completed, created_date, favorite, end_date_time FROM tasks'
        return self.execute_query(query)

    def get_tasks_for_today(self):
        today = datetime.date.today().strftime("%d.%m.%Y")
        query = f"SELECT * FROM tasks WHERE end_date_time >= ?"
        tasks = self.execute_query(query, (today,))
        self.show_tasks(tasks)

    def sort_tasks_by_deadline(self):
        order = "ASC"
        query = f"SELECT id, task, completed, created_date, favorite, end_date_time FROM tasks ORDER BY end_date_time {order}"
        tasks = self.execute_query(query)
        self.show_tasks(tasks)

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
        task = self.task_list[position]  # Зберігаємо завдання для історії
        task_id = task[0]
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        
        self.add_to_history(task)  # Додаємо збережене завдання до історії
        
        self.task_list = self.get_tasks()  # Оновлюємо список завдань
        self.show_tasks(self.task_list)  # Показуємо оновлений список завдань

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

    def update_task_view(self, model, task):
        item = QStandardItem()
        model.appendRow(item)
        widget = TaskItem(task[1], task[2], model.rowCount() - 1, task[3], task[4], task[5])
        widget.closeClicked.connect(self.remove_item)
        widget.favoriteToggled.connect(self.update_favorites)
        widget.checkboxToggled.connect(self.update_task_status)

        end_date_time = QDateTime.fromString(task[5], 'dd.MM.yyyy HH:mm')
        if widget.ui.checkBox_3.isChecked():
            status_text = "Task Completed"
            status_color = "green"
        elif end_date_time < QDateTime.currentDateTime():
            status_text = "Task Expired"
            status_color = "red"
        else:
            status_text = "Task In Progress"
            status_color = "yellow"

        widget.ui.label_task_status.setText(status_text)
        widget.ui.label_task_status.setStyleSheet(f"color: {status_color};")

        item.setSizeHint(widget.sizeHint())
        return item, widget

    def show_tasks(self, task_list):
        self.list_model.clear()
        self.fav_model.clear()

        for task in task_list:
            if len(task) < 6:
                print(f"Invalid task format: {task}")
                continue

            item, widget = self.update_task_view(self.list_model, task)
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)

            if task[4]:
                fav_item, fav_widget = self.update_task_view(self.fav_model, task)
                self.list_view_fav.setIndexWidget(self.fav_model.indexFromItem(fav_item), fav_widget)

    def show_history(self, history_list):
        self.history_model.clear()
        for i, task in enumerate(history_list):
            item = QStandardItem()
            self.history_model.appendRow(item)
            widget = TaskItem(task[1], task[2], i, task[3], task[4], task[5])
            item.setSizeHint(widget.sizeHint())
            self.list_view_history.setIndexWidget(self.history_model.indexFromItem(item), widget)

    def update_database(self, task_id, column, value):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'UPDATE tasks SET {column} = ? WHERE id = ?', (value, task_id))
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.show_tasks(self.task_list)

    def update_favorites(self, position, is_favorite):
        task_id = self.task_list[position][0]
        self.update_database(task_id, 'favorite', is_favorite)

    def update_task_status(self, position, is_checked):
        task_id = self.task_list[position][0]
        self.update_database(task_id, 'completed', is_checked)

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
            
    def get_tasks_by_title(self, title):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE title = ?', (title,))
        found_tasks = cursor.fetchall()
        
        # Переносимо знайдені завдання в самий верх списку
        self.task_list = [task for task in found_tasks] + [task for task in self.task_list if task not in found_tasks]
        
        conn.close()

    def closeEvent(self, event):
        self.get_all_tasks()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for task in self.task_list:
            cursor.execute('UPDATE tasks SET task = ?, completed = ?, created_date = ?, favorite = ?, end_date_time = ? WHERE id = ?',
                           (task[0], task[1], task[2], task[3], task[4].toString('dd.MM.yyyy HH:mm'), task[0]))
        conn.commit()
        conn.close()
