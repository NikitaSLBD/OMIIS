import tkinter as tk

class TeacherProgressWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Успеваемость студентов")

        tk.Label(self.root, text="Список студентов:").grid(row=0, column=0, padx=10, pady=5)
        self.students_listbox = tk.Listbox(self.root, height=10, width=50)
        self.students_listbox.grid(row=1, column=0, padx=10, pady=5)


        self.progress_data = {
            "Иван Иванов": {
                "Курс 1": 8.5,
                "Курс 2": 7.0,
            },
            "Мария Петрова": {
                "Курс 1": 9.0,
                "Курс 3": 8.0,
            },
        }

        self.load_students()

    def load_students(self):
        for student_name, courses in self.progress_data.items():
            average_grade = self.calculate_average(courses)
            self.students_listbox.insert(tk.END, f"{student_name} - Средняя оценка: {average_grade}")