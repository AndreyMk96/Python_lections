"""Тема 1 Создание БД и добавление в нее данных"""
import sqlite3

# Создание базы
"""Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection. 
Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе:"""
conn = sqlite3.connect("base.db")
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()
#cursor.execute("""CREATE TABLE users_base
#                      (Surname,  Name, Phone, Age)
#                   """)

# Добавление данных в базу
cursor.execute("""INSERT INTO users_base
                  VALUES ('Markov', 'Andrey',
                  '79047721122', 23)"""
               )
# Сохраняем изменения
conn.commit()

# Добавление набора данных
surnames = ["Ivanov", "Petrov", "Sergeeva", "Petrov", "Georgiev", "Malykh", "Markov"]
names = ["Denis", "Roman", "Nastya", "Sergey", "Roman", "Yakov", "Semyon"]
phones = ["123", "345","678", "121", "122", "545", "989"]
ages = [20,25,27, 22, 23, 29, 21]
for i in range(len(surnames)):
    cursor.execute("""INSERT INTO users_base
                         VALUES ('%s','%s','%s','%d')
                         """ % (surnames[i], names[i], phones[i],ages[i]))
conn.commit()
"""Задание создать базу данных из трех столбцов User, Login, Password
- Поле User состоит из двух строк, имени и фамилии пользователя. Имя и фамилия начинаются с заглавной буквы и могут
быть любой длины от 4 до 10 символов
- Поля Login и Password состоят из строк от 8 до 12 символов, любого регистра
Сгенерировать и заполнить базу 1000 записями пользователей, их логинов и паролей"""
