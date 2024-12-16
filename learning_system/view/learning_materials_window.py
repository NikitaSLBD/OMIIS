import tkinter as tk
from tkinter import messagebox


class LearningMaterialsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Учебные материалы")

        tk.Label(self.root, text="Список курсов:").grid(row=0, column=0, padx=10, pady=5)
        self.courses_listbox = tk.Listbox(self.root, height=10, width=50)
        self.courses_listbox.grid(row=1, column=0, padx=10, pady=5)
        self.courses_listbox.bind("<Double-1>", self.show_course_info)

        self.courses_data = {
            "Курс 1": {
                "start_date": "01.01.2024",
                "end_date": "01.06.2024",
                "modules": {
                    "Модуль 1": "Содержание модуля 1",
                    "Модуль 2": "Содержание модуля 2",
                },
            },
            "Курс 2": {
                "start_date": "15.02.2024",
                "end_date": "15.07.2024",
                "modules": {
                    "Модуль A": "Содержание модуля A",
                    "Модуль B": "Содержание модуля B",
                },
            },
        }

        self.load_courses()

    def load_courses(self):
        for course_name in self.courses_data.keys():
            self.courses_listbox.insert(tk.END, course_name)

    def show_course_info(self, event):
        selected_course = self.courses_listbox.get(tk.ACTIVE)
        if not selected_course:
            return

        course_info = self.courses_data.get(selected_course)
        if not course_info:
            messagebox.showerror("Ошибка", "Информация о курсе не найдена")
            return

        CourseInfoWindow(tk.Toplevel(self.root), selected_course, course_info)

class CourseInfoWindow:
    def __init__(self, root, course_name, course_info):
        self.root = root
        self.root.title(f"Информация о курсе: {course_name}")

        tk.Label(self.root, text=f"Название курса: {course_name}").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text=f"Дата начала: {course_info['start_date']}").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text=f"Дата окончания: {course_info['end_date']}").grid(row=2, column=0, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Модули:").grid(row=3, column=0, padx=10, pady=5)
        self.modules_listbox = tk.Listbox(self.root, height=10, width=50)
        self.modules_listbox.grid(row=4, column=0, padx=10, pady=5)
        self.modules_listbox.bind("<Double-1>", self.show_module_info)

        for module_name in course_info['modules'].keys():
            self.modules_listbox.insert(tk.END, module_name)

        self.course_modules = course_info['modules']

    def show_module_info(self, event):
        selected_module = self.modules_listbox.get(tk.ACTIVE)
        if not selected_module:
            return

        module_content = self.course_modules.get(selected_module)
        if not module_content:
            messagebox.showerror("Ошибка", "Содержание модуля не найдено")
            return

        ModuleInfoWindow(tk.Toplevel(self.root), selected_module, module_content)

class ModuleInfoWindow:
    def __init__(self, root, module_name, module_content):
        self.root = root
        self.root.title(f"Информация о модуле: {module_name}")

        tk.Label(self.root, text=f"Название модуля: {module_name}").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Содержание:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.content_text = tk.Text(self.root, height=10, width=50, wrap="word")
        self.content_text.grid(row=2, column=0, padx=10, pady=5)
        self.content_text.insert(tk.END, module_content)
        self.content_text.config(state="disabled")