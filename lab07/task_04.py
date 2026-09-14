import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, group_name TEXT)"
)
cursor.execute(
    "INSERT OR IGNORE INTO students (id, name, group_name) VALUES (1, 'Анна', 'ПИ-21')"
)

new_name = input("Введите новое имя: ")
cursor.execute("UPDATE students SET name = ? WHERE id = 1", (new_name,))

connection.commit()
connection.close()

print("Запись обновлена")
