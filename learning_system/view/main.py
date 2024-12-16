import tkinter as tk
from tkinter import messagebox


from models.course import Course
from models.student import Student
from models.teacher import Teacher


from models.services.course_service import Course_service
from models.services.student_service import Student_service
from models.services.teacher_service import Teacher_service


from course_register_window import RegisterToCourseWindow
from create_course_window import CreateCourseWindow
from learning_materials_window import LearningMaterialsWindow
from login_window import LoginWindow
from main_window_student import StudentDashboard
from main_window_teacher import TeacherDashboard
from register_window import RegisterWindow
from student_progress_window import StudentProgressWindow
from teacher_assignments_window import ViewTasksWindow
from teacher_progress_window import TeacherProgressWindow


class DistanceLearningSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Дистанционная образовательная платформа")
        self.current_user = None

        self.role_selection_menu()

    def role_selection_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Выберите роль", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Войти как студент", command=lambda: self.login_window("студент"), width=30, height=2).pack(pady=10)
        tk.Button(self.root, text="Войти как преподаватель", command=lambda: self.login_window("преподаватель"), width=30, height=2).pack(pady=10)

    def login_window(self, role):
        self.clear_window()

        login_window = LoginWindow(self.root)
        login_window.login_entry.insert(0, "user")
        login_window.password_entry.insert(0, "password")

        def login():
            login = login_window.login_entry.get()
            password = login_window.password_entry.get()

            
            if role == "студент":
                user = next((s for s in Student_service.find_all() if s.get_email() == login and s.get_password() == password), None)
            else:
                user = next((t for t in Teacher_service.find_all() if t.get_email() == login and t.get_password() == password), None)

            if user:
                self.current_user = user
                messagebox.showinfo("Успех", "Вы успешно вошли!")
                self.dashboard()
            else:
                messagebox.showerror("Ошибка", "Неверный логин или пароль")

        login_window.login_button.config(command=login)
        login_window.register_button.config(command=lambda: self.register_window(role))

    def register_window(self, role):
        self.clear_window()

        register_window = RegisterWindow(self.root)

        def register():
            login = register_window.email_entry.get()
            password = register_window.password_entry.get()
            name = register_window.first_name_entry.get()
            surname = register_window.last_name_entry.get()
            middlename = register_window.middle_name_entry.get()

            
            if role == "студент":
                existing_user = next((s for s in Student_service.find_all() if s.get_email() == login), None)
            else:
                existing_user = next((t for t in Teacher_service.find_all() if t.get_email() == login), None)

            if existing_user:
                messagebox.showerror("Ошибка", "Логин уже используется")
                return

            
            if role == "студент":
                new_user = Student(id=len(Student_service.find_all()) + 1, name=name, email=login, password=password)
                Student_service.save(new_user)
            else:
                new_user = Teacher(id=len(Teacher_service.find_all()) + 1, name=name, email=login, password=password)
                Teacher_service.save(new_user)

            messagebox.showinfo("Успех", "Регистрация прошла успешно!")
            self.role_selection_menu()

        register_window.create_account_button.config(command=register)
        register_window.go_back_button.config(command=self.role_selection_menu)

    def dashboard(self):
        self.clear_window()

        if isinstance(self.current_user, Student):
            student_dashboard = StudentDashboard(self.root)
            student_dashboard.register_course_button.config(command=self.register_course)
            student_dashboard.open_course_button.config(command=self.open_course)
            student_dashboard.view_assignments_button.config(command=self.view_assignments)
            student_dashboard.view_performance_button.config(command=self.view_performance)
            student_dashboard.logout_button.config(command=self.logout)
        else:
            teacher_dashboard = TeacherDashboard(self.root)
            teacher_dashboard.create_course_button.config(command=self.create_course)
            teacher_dashboard.open_course_button.config(command=self.open_course)
            teacher_dashboard.view_assignments_button.config(command=self.view_assignments)
            teacher_dashboard.view_student_performance_button.config(command=self.view_student_performance)
            teacher_dashboard.logout_button.config(command=self.logout)

    def register_course(self):
        register_course_window = RegisterToCourseWindow(tk.Toplevel(self.root))

    def open_course(self):
        learning_materials_window = LearningMaterialsWindow(tk.Toplevel(self.root))

    def view_assignments(self):
        view_tasks_window = ViewTasksWindow(tk.Toplevel(self.root))

    def view_performance(self):
        student_progress_window = StudentProgressWindow(tk.Toplevel(self.root))

    def view_student_performance(self):
        teacher_progress_window = TeacherProgressWindow(tk.Toplevel(self.root))

    def create_course(self):
        create_course_window = CreateCourseWindow(tk.Toplevel(self.root))

        
        def create_course_logic(name, start_date, end_date):
            new_course = Course(name=name, start=start_date, end=end_date)
            Course_service.save(new_course)
            messagebox.showinfo("Успех", f"Курс '{name}' создан успешно!")

        create_course_window.create_course_button.config(command=lambda: create_course_logic(
            create_course_window.course_name_entry.get(),
            create_course_window.start_date_entry.get_date(),
            create_course_window.end_date_entry.get_date()
        ))

    def logout(self):
        self.current_user = None
        self.role_selection_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = DistanceLearningSystem(root)
    root.mainloop()