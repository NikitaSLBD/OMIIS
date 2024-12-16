import tkinter as tk
from tkinter import messagebox

class StudentDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Студент: Главная панель")

        tk.Label(self.root, text="Добро пожаловать, студент!", font=("Arial", 16)).pack(pady=20)
        
        self.register_course_button = tk.Button(self.root, text="Регистрация на курс", width=30, height=2, command=self.register_course)
        self.register_course_button.pack(pady=10)
        self.open_course_button = tk.Button(self.root, text="Открыть курс", width=30, height=2, command=self.open_course)
        self.open_course_button.pack(pady=10)
        self.view_assignments_button = tk.Button(self.root, text="Просмотреть доступные задания", width=30, height=2, command=self.view_assignments_student)
        self.view_assignments_button.pack(pady=10)
        self.view_performance_button = tk.Button(self.root, text="Просмотреть успеваемость", width=30, height=2, command=self.view_performance)
        self.view_performance_button.pack(pady=10)
        self.logout_button = tk.Button(self.root, text="Выйти из аккаунта", width=30, height=2, command=self.logout)
        self.logout_button.pack(pady=10)

    def register_course(self):
        messagebox.showinfo("Регистрация на курс", "Функция регистрации на курс.")

    def open_course(self):
        messagebox.showinfo("Открыть курс", "Функция открытия курса.")

    def view_assignments_student(self):
        messagebox.showinfo("Просмотреть задания", "Функция просмотра доступных заданий.")

    def view_performance(self):
        messagebox.showinfo("Просмотреть успеваемость", "Функция просмотра успеваемости.")

    def logout(self):
        messagebox.showinfo("Выход", "Выход из аккаунта.")
        self.root.destroy()