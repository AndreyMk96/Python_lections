import sqlite3
#подключение к бд
conn = sqlite3.connect("base.db")

#считывание бд
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_base")
    rows = cur.fetchall()
    for i in rows:
        print(i)

#удаление определенных записей из бд
sql = "DELETE FROM users_base WHERE surname = 'Markov'"

cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
