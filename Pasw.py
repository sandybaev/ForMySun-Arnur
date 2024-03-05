import tkinter as tk
from tkinter import messagebox

def try_login():
    # Получаем значения из полей ввода
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Проверяем учетные данные
    if entered_username == "rauan" and entered_password == "5522":
        messagebox.showinfo("Успешно", "Вы успешно вошли!")
    else:
        messagebox.showerror("Ошибка", "Неверные учетные данные. Попробуйте снова.")

# Создание главного окна
root = tk.Tk()
root.title("Авторизация")

# Увеличение размеров окна
root.geometry("200x200")  # Ширина x Высота

# Создание полей ввода
username_label = tk.Label(root, text="Имя пользователя:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Пароль:")
password_entry = tk.Entry(root, show="*")

# Создание кнопки для авторизации
login_button = tk.Button(root, text="Войти", command=try_login)

# Размещение виджетов на форме
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()

# Запуск главного цикла
root.mainloop()
