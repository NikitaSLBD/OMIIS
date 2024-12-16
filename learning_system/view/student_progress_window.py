import tkinter as tk

class StudentProgressWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Успеваемость студента")

        tk.Label(self.root, text="Список курсов:").grid(row=0, column=0, padx=10, pady=5)
        self.courses_listbox = tk.Listbox(self.root, height=10, width=50)
        self.courses_listbox.grid(row=1, column=0, padx=10, pady=5)
        self.courses_listbox.bind("<Double-1>", self.show_course_progress)

        self.progress_data = {
            "Курс 1": {
                "average": 8.5,
                "modules": {
                    "Модуль 1": 9.0,
                    "Модуль 2": 8.0,
                },
                "details": {
                    "Модуль 1": [("Задание 1", 9.5), ("Задание 2", 8.5)],
                    "Модуль 2": [("Задание A", 7.5), ("Задание B", 8.5)],
                },
            },
            "Курс 2": {
                "average": 7.5,
                "modules": {
                    "Модуль A": 7.0,
                    "Модуль B": 8.0,
                },
                "details": {
                    "Модуль A": [("Задание X", 6.5), ("Задание Y", 7.5)],
                    "Модуль B": [("Задание M", 8.5), ("Задание N", 7.5)],
                },
            },
        }

        self.load_courses()

    def load_courses(self):
        for course_name, data in self.progress_data.items():
            self.courses_listbox.insert(tk.END, f"{course_name} - Средняя оценка: {data['average']}")

    def show_course_progress(self, event):
        selected_index = self.courses_listbox.curselection()
        if not selected_index:
            return

        selected_course = list(self.progress_data.keys())[selected_index[0]]
        course_data = self.progress_data[selected_course]

        CourseProgressWindow(tk.Toplevel(self.root), selected_course, course_data)


class CourseProgressWindow:
    def __init__(self, root, course_name, course_data):
        self.root = root
        self.root.title(f"Успеваемость по курсу: {course_name}")

        tk.Label(self.root, text=f"Курс: {course_name}").grid(row=0, column=0, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Модули:").grid(row=1, column=0, padx=10, pady=5)
        self.modules_listbox = tk.Listbox(self.root, height=10, width=50)
        self.modules_listbox.grid(row=2, column=0, padx=10, pady=5)
        self.modules_listbox.bind("<Double-1>", self.show_module_progress)

        self.modules_data = course_data["modules"]
        self.details = course_data["details"]

        for module_name, average in self.modules_data.items():
            self.modules_listbox.insert(tk.END, f"{module_name} - Средняя оценка: {average}")

    def show_module_progress(self, event):
        selected_index = self.modules_listbox.curselection()
        if not selected_index:
            return

        selected_module = list(self.modules_data.keys())[selected_index[0]]
        module_details = self.details[selected_module]

        ModuleProgressWindow(tk.Toplevel(self.root), selected_module, module_details)


class ModuleProgressWindow:
    def __init__(self, root, module_name, module_details):
        self.root = root
        self.root.title(f"Успеваемость по модулю: {module_name}")

        tk.Label(self.root, text=f"Модуль: {module_name}").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Задания:").grid(row=1, column=0, padx=10, pady=5)

        self.tasks_listbox = tk.Listbox(self.root, height=10, width=50)
        self.tasks_listbox.grid(row=2, column=0, padx=10, pady=5)

        for task_name, grade in module_details:
            self.tasks_listbox.insert(tk.END, f"{task_name} - Оценка: {grade}")