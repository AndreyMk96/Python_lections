"""Урок 3 Разлиные запросы"""
import sqlite3
# Подключение к бд
conn = sqlite3.connect("base.db")
cursor = conn.cursor()

# Запрос поиска
cursor.execute("SELECT * FROM users_base WHERE name='Denis'")
print(cursor.fetchall()) # or use fetchone()
cursor.execute("SELECT * FROM users_base WHERE age>'24'")
print(cursor.fetchall()) # or use fetchone()
cursor.execute("SELECT * FROM users_base WHERE age>'19' AND age < '26'")
print(cursor.fetchall()) # or use fetchone()


