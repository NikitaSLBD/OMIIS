import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class CreateCourseWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Создание курса")

        tk.Label(self.root, text="Название курса:").grid(row=0, column=0, padx=10, pady=5)
        self.course_name_entry = tk.Entry(self.root)
        self.course_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Дата начала:").grid(row=1, column=0, padx=10, pady=5)
        self.start_date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.start_date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Дата конца:").grid(row=2, column=0, padx=10, pady=5)
        self.end_date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.end_date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Модули:").grid(row=3, column=0, padx=10, pady=5)
        self.modules_listbox = tk.Listbox(self.root, height=5, width=30)
        self.modules_listbox.grid(row=3, column=1, padx=10, pady=5)

        self.add_module_button = tk.Button(self.root, text="Добавить модуль", command=self.add_module)
        self.add_module_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.create_course_button = tk.Button(self.root, text="Создать курс", command=self.create_course)
        self.create_course_button.grid(row=5, column=1, padx=10, pady=5, sticky="e")

    def create_course(self):
        course_name = self.course_name_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        modules = list(self.modules_listbox.get(0, tk.END))

        if not course_name:
            messagebox.showerror("Ошибка", "Введите название курса")
            return

        if not modules:
            messagebox.showerror("Ошибка", "Добавьте хотя бы один модуль")
            return

        messagebox.showinfo("Успех", f"Курс '{course_name}' создан успешно!")
        self.root.destroy()

    def add_module(self):

        CreateModuleWindow(tk.Toplevel(self.root), self.modules_listbox)


class CreateModuleWindow:
    def __init__(self, root, modules_listbox):
        self.root = root
        self.root.title("Добавление модуля")
        self.modules_listbox = modules_listbox

        tk.Label(self.root, text="Заголовок модуля:").grid(row=0, column=0, padx=10, pady=5)
        self.module_title_entry = tk.Entry(self.root)
        self.module_title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Содержание:").grid(row=1, column=0, padx=10, pady=5)
        self.module_content_text = tk.Text(self.root, height=5, width=30)
        self.module_content_text.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Задания:").grid(row=2, column=0, padx=10, pady=5)
        self.tasks_listbox = tk.Listbox(self.root, height=5, width=30)
        self.tasks_listbox.grid(row=2, column=1, padx=10, pady=5)

        self.add_task_button = tk.Button(self.root, text="Добавить задание", command=self.add_module)
        self.add_task_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.save_module_button = tk.Button(self.root, text="Сохранить модуль", command=self.create_course)
        self.save_module_button.grid(row=5, column=1, padx=10, pady=5, sticky="e")

    def add_task(self): CreateTaskWindow(tk.Toplevel(self.root), self.tasks_listbox)

    def save_module(self):
        module_title = self.module_title_entry.get()
        module_content = self.module_content_text.get("1.0", tk.END).strip()
        tasks = list(self.tasks_listbox.get(0, tk.END))

        if not module_title:
            messagebox.showerror("Ошибка", "Введите заголовок модуля")
            return

        if not module_content:
            messagebox.showerror("Ошибка", "Введите содержание модуля")
            return

        module_info = f"{module_title} (Заданий: {len(tasks)})"
        self.modules_listbox.insert(tk.END, module_info)
        self.root.destroy()

class CreateTaskWindow:
    def __init__(self, root, tasks_listbox):
        self.root = root
        self.root.title("Добавление задания")
        self.tasks_listbox = tasks_listbox

        tk.Label(self.root, text="Заголовок задания:").grid(row=0, column=0, padx=10, pady=5)
        self.task_title_entry = tk.Entry(self.root)
        self.task_title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Описание задания:").grid(row=1, column=0, padx=10, pady=5)
        self.task_description_text = tk.Text(self.root, height=5, width=30)
        self.task_description_text.grid(row=1, column=1, padx=10, pady=5)

        self.save_task_button = tk.Button(self.root, text="Сохранить задание", command=self.save_task)
        self.save_task_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    def save_task(self):
        task_title = self.task_title_entry.get()
        task_description = self.task_description_text.get("1.0", tk.END).strip()

        if not task_title:
            messagebox.showerror("Ошибка", "Введите заголовок задания")
            return

        if not task_description:
            messagebox.showerror("Ошибка", "Введите описание задания")
            return

        task_info = f"{task_title}: {task_description[:30]}..."
        self.tasks_listbox.insert(tk.END, task_info)
        self.root.destroy()