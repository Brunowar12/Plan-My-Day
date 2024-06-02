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
        favorite BOOLEAN NOT NULL CHECK (favorite IN (0, 1))
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
        created_date TEXT NOT NULL,
        favorite BOOLEAN NOT NULL CHECK (favorite IN (0, 1))
    )
    ''')
    conn.commit()
    conn.close()
    
class Database:
    def get_tasks(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    def get_history(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM history")
        history = cursor.fetchall()
        conn.close()
        return history

    def add_task(self, task_text):
        today = datetime.date.today()
        created_date = today.strftime("%d %B")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (task, completed, created_date, favorite) VALUES (?, ?, ?, ?)",
            (task_text, False, created_date, False),
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
        cursor.execute(
            "INSERT INTO history (task, completed, created_date, favorite) VALUES (?, ?, ?, ?)",
            (task[1], task[2], task[3], task[4]),
        )
        conn.commit()
        conn.close()
        self.history_list = self.get_history()
        self.show_history(self.history_list)

    def show_tasks(self, task_list):
        self.list_model.clear()
        self.fav_model.clear()
        for i, task in enumerate(task_list):
            item = QStandardItem()
            self.list_model.appendRow(item)
            widget = TaskItem(task[1], task[2], i, task[3], task[4])
            widget.closeClicked.connect(self.remove_item)
            widget.favoriteToggled.connect(self.update_favorites)
            widget.checkboxToggled.connect(self.update_task_status)
            item.setSizeHint(widget.sizeHint())
            self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)
            if task[4]:
                fav_item = QStandardItem()
                self.fav_model.appendRow(fav_item)
                fav_widget = TaskItem(task[1], task[2], i, task[3], task[4])
                fav_widget.closeClicked.connect(self.remove_item)
                fav_widget.favoriteToggled.connect(self.update_favorites)
                fav_widget.checkboxToggled.connect(self.update_task_status)
                fav_item.setSizeHint(fav_widget.sizeHint())
                self.list_view_fav.setIndexWidget(
                    self.fav_model.indexFromItem(fav_item), fav_widget
                )

    def show_history(self, history_list):
        self.history_model.clear()
        for i, task in enumerate(history_list):
            item = QStandardItem()
            self.history_model.appendRow(item)
            widget = TaskItem(task[1], task[2], i, task[3], task[4])
            item.setSizeHint(widget.sizeHint())
            self.list_view_history.setIndexWidget(
                self.history_model.indexFromItem(item), widget
            )

    def update_favorites(self, position, is_favorite):
        task_id = self.task_list[position][0]
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET favorite = ? WHERE id = ?", (is_favorite, task_id)
        )
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.show_tasks(self.task_list)

    def update_task_status(self, position, is_checked):
        task_id = self.task_list[position][0]
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?", (is_checked, task_id)
        )
        conn.commit()
        conn.close()
        self.task_list = self.get_tasks()
        self.show_tasks(self.task_list)

    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task:
            self.add_task(new_task)
            self.task_input.clear()

    def closeEvent(self, event):
        # Here you might want to handle any other cleanup
        event.accept()