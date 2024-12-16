import tkinter as tk
from tkinter import messagebox

class StudentTasksWindow:
    def __init__(self, root):
        self.root = root
        self.assignments = [{"title": "Задание 1", "content": "Описание задания 1"},
                              {"title": "Задание 2", "content": "Описание задания 2"},
                              {"title": "Задание 3", "content": "Описание задания 3"},]
        
        self.selected_assignment = None

        self.create_assignment_list()

    def create_assignment_list(self):

        tk.Label(self.root, text="Список заданий", font=("Arial", 16)).pack(pady=10)
        
        self.assignment_listbox = tk.Listbox(self.root, width=50, height=15)
        for idx, assignment in enumerate(self.assignments):
            self.assignment_listbox.insert(idx, assignment['title'])
        self.assignment_listbox.pack(pady=10)

        self.answer_task_button = tk.Button(self.root, text="Ответить на задание", command=self.open_answer_window)
        self.answer_task_button.pack(pady=5)

    def open_answer_window(self):
        try:
            selection_index = self.assignment_listbox.curselection()[0]
            self.selected_assignment = self.assignments[selection_index]
            self.display_answer_window()
        except IndexError:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите задание из списка.")

    def display_answer_window(self):

        tk.Label(self.root, text=self.selected_assignment['title'], font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=self.selected_assignment['content'], wraplength=400).pack(pady=10)

        tk.Label(self.root, text="Ваш ответ:").pack(pady=5)
        self.answer_entry = tk.Text(self.root, height=10, width=50)
        self.answer_entry.pack(pady=10)

        self.submit_answer_button = tk.Button(self.root, text="Отправить ответ", command=self.submit_answer)
        self.submit_answer_button.pack(pady=5)

    def submit_answer(self):
        answer = self.answer_entry.get("1.0", tk.END).strip()
        if answer:
            # Here you would save the answer to the database or backend service.
            messagebox.showinfo("Успех", "Ваш ответ был отправлен.")
            self.create_assignment_list()
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите ответ перед отправкой.")
        