import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, group_name TEXT)"
)

name = input("Введите имя студента: ")
group_name = input("Введите группу: ")

cursor.execute(
    "INSERT INTO students (name, group_name) VALUES (?, ?)",
    (name, group_name),
)

connection.commit()
connection.close()

print("Студент добавлен")
