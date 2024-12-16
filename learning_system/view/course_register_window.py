import tkinter as tk
from tkinter import messagebox

class RegisterToCourseWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация на курс")

        tk.Label(self.root, text="Доступные курсы:").grid(row=0, column=0, padx=10, pady=5)
        self.courses_listbox = tk.Listbox(self.root, height=10, width=50)
        self.courses_listbox.grid(row=1, column=0, padx=10, pady=5)

        self.load_courses(["Курс 1", "Курс 2", "Курс 3", "Курс 4"])

        self.register_to_course_button = tk.Button(self.root, text="Зарегистрироваться на курс", command=self.register_to_course)
        self.register_to_course_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        
    def load_courses(self, courses):
        for course in courses:
            self.courses_listbox.insert(tk.END, course)

    def register_to_course(self):
        selected_course = self.courses_listbox.get(tk.ACTIVE)
        if not selected_course:
            messagebox.showerror("Ошибка", "Выберите курс для регистрации")
            return
        
        messagebox.showinfo("Успех", f"Вы успешно зарегистрировались на курс '{selected_course}'!")