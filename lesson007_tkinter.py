import os
import tkinter as tk
from tkinter import messagebox, Text
from cryptography.fernet import Fernet
import xml.etree.ElementTree as ET

# Генерация ключа для шифрования и сохранение его в файл
if not os.path.exists('keys.key'):
    key = Fernet.generate_key()
    with open('keys.key', 'wb') as key_file:
        key_file.write(key)
else:
    with open('keys.key', 'rb') as key_file:
        key = key_file.read()
cipher_suite = Fernet(key)


def create_xml_file():
    root = ET.Element("root")
    tree = ET.ElementTree(root)
    tree.write("data.xml")


def write_to_xml(data):
    tree = ET.parse('data.xml')
    root = tree.getroot()
    encrypted_data = cipher_suite.encrypt(data.encode())
    ET.SubElement(root, "data", name="info").text = encrypted_data.decode()
    tree.write('data.xml')


def read_from_xml():
    if not os.path.exists('data.xml'):
        create_xml_file()
    tree = ET.parse('data.xml')
    root = tree.getroot()
    data_list = []
    for elem in root.findall('data'):
        encrypted_data = elem.text.encode()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        data_list.append(decrypted_data.decode())
    return data_list


def login():
    # Проверка логина и пароля
    if username.get() == 'admin' and password.get() == 'password':
        messagebox.showinfo('', 'Успешный вход')
        # Чтение и дешифрование данных из XML
        if not os.path.exists('data.xml'):
            create_xml_file()
        tree = ET.parse('data.xml')
        root = tree.getroot()
        for elem in root:
            for subelem in elem:
                decrypted_text = cipher_suite.decrypt(subelem.text)
                print(decrypted_text)
        # Отображение данных из XML в текстовом поле
        data = read_from_xml()
        text_field.delete(1.0, tk.END)
        if data is not None:
            for item in data:
                text_field.insert(tk.END, item + '\n')
    else:
        messagebox.showinfo('', 'Неверный логин или пароль')


def save_changes():
    # Получение данных из текстового поля
    data = text_field.get(1.0, tk.END)
    # Запись и шифрование данных в XML
    write_to_xml(data)
    messagebox.showinfo('', 'Изменения сохранены')


# Создание GUI
root = tk.Tk()
root.geometry('800x600')
username = tk.StringVar()
password = tk.StringVar()

tk.Label(root, text='Логин').pack()
tk.Entry(root, textvariable=username).pack()
tk.Label(root, text='Пароль').pack()
tk.Entry(root, textvariable=password, show='*').pack()
tk.Button(root, text='Войти', command=login).pack()

text_field = Text(root)
text_field.pack()
tk.Button(root, text='Сохранить изменения', command=save_changes).pack()


def quit_app():
    root.destroy()


tk.Button(root, text='Выйти', command=quit_app).pack()

root.mainloop()
