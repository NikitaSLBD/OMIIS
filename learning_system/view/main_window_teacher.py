import tkinter as tk
from tkinter import messagebox


class TeacherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Панель управления преподавателя")

        tk.Label(self.root, text="Добро пожаловать, Преподаватель", font=("Arial", 16)).pack(pady=20)

        self.create_course_button = tk.Button(self.root, text="Создать курс", command=self.create_course, width=30, height=2)
        self.create_course_button.pack(pady=10)
        self.open_course_button = tk.Button(self.root, text="Открыть курс", command=self.open_course, width=30, height=2)
        self.create_course_button.pack(pady=10)
        self.view_assignments_button = tk.Button(self.root, text="Просмотр заданий", command=self.view_assignments_teacher, width=30, height=2)
        self.view_assignments_button.pack(pady=10)
        self.view_student_performance_button = tk.Button(self.root, text="Успеваемость студентов", command=self.view_student_performance, width=30, height=2)
        self.view_student_performance_button.pack(pady=10)
        self.logout_button = tk.Button(self.root, text="Выйти из аккаунта", command=self.logout, width=30, height=2)
        self.logout_button.pack(pady=20).pack(pady=20)

    def create_course(self):
        messagebox.showinfo("Создание курса", "Открыто окно создания курса")
        

    def open_course(self):
        messagebox.showinfo("Открыть курс", "Открыто окно выбора курса")
        

    def view_assignments_teacher(self):
        messagebox.showinfo("Просмотр заданий", "Открыто окно просмотра заданий")
        

    def view_student_performance(self):
        messagebox.showinfo("Успеваемость студентов", "Открыто окно успеваемости студентов")
        

    def logout(self):
        answer = messagebox.askyesno("Выход", "Вы действительно хотите выйти из аккаунта?")
        if answer:
            self.root.destroy()  