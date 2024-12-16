import tkinter as tk
from tkinter import messagebox

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация пользователя")

        tk.Label(self.root, text="Регистрация", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Имя:").pack()
        self.first_name_entry = tk.Entry(self.root, width=30)
        self.first_name_entry.pack(pady=5)

        tk.Label(self.root, text="Фамилия:").pack()
        self.last_name_entry = tk.Entry(self.root, width=30)
        self.last_name_entry.pack(pady=5)

        tk.Label(self.root, text="Отчество:").pack()
        self.middle_name_entry = tk.Entry(self.root, width=30)
        self.middle_name_entry.pack(pady=5)

        tk.Label(self.root, text="Электронная почта:").pack()
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Пароль:").pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=5)

        self.create_account_button = tk.Button(self.root, text="Создать аккаунт", width=20, command=self.register)
        self.create_account_button.pack(pady=10)
        self.go_back_button = tk.Button(self.root, text="Назад", width=20, command=self.go_back)
        self.go_back_button.pack(pady=5)

    def register(self):
        name = self.first_name_entry.get()
        surname = self.last_name_entry.get()
        middlename = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not name or not surname or not email or not password:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля.")
            return

        messagebox.showinfo("Успех", "Аккаунт успешно создан.")
        self.go_back_to_login()

    def go_back(self):
        from view.login_window import LoginWindow

        self.root.destroy()
        root = tk.Tk()
        LoginWindow(root)
        root.mainloop()