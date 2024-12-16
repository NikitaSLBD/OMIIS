import tkinter as tk
from tkinter import messagebox

class TeacherTasksWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Просмотр заданий")

        tk.Label(self.root, text="Список заданий:").grid(row=0, column=0, padx=10, pady=5)
        self.tasks_listbox = tk.Listbox(self.root, height=10, width=50)
        self.tasks_listbox.grid(row=0, column=1, padx=10, pady=5)

        self.grade_task_button = tk.Button(self.root, text="Оценить задание", command=self.grade_task)
        self.grade_task_button.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    def grade_task(self):
        
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if not selected_task:
            messagebox.showerror("Ошибка", "Выберите задание для оценки")
            return

        EvaluateAssignmentsWindow(tk.Toplevel(self.root))


class EvaluateAssignmentsWindow:
    def __init__(self, root, assignment_name: str):
        self.root = root
        self.root.title(f"Оценка задания {assignment_name}")

        tk.Label(self.root, text="Оценка:").grid(row=1, column=0, padx=10, pady=5)
        self.grade_entry = tk.Entry(self.root)
        self.grade_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Комментарий:").grid(row=2, column=0, padx=10, pady=5)
        self.comment_text = tk.Text(self.root, height=5, width=30)
        self.comment_text.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Оценить", command=self.submit_grade).grid(row=3, column=1, padx=10, pady=5, sticky="e")