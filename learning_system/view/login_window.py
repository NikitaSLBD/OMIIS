import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Вход в систему")

        tk.Label(self.root, text="Вход в систему", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Логин:").pack()
        self.login_entry = tk.Entry(self.root, width=30)
        self.login_entry.pack(pady=5)

        tk.Label(self.root, text="Пароль:").pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Войти", width=20, command=self.login)
        self.login_button.pack(pady=10)
        self.register_button = tk.Button(self.root, text="Зарегистрироваться", width=20, command=self.register)
        self.register_button.pack(pady=5)

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Введите логин и пароль.")
            return

        
        messagebox.showinfo("Успех", "Вы успешно вошли в систему.")

    def register(self):
        messagebox.showinfo("Регистрация", "Окно регистрации пользователя.")