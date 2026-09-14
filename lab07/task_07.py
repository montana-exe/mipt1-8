import sqlite3

connection = sqlite3.connect("university.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS groups (id INTEGER PRIMARY KEY, name TEXT)"
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    )
    """
)

connection.commit()
connection.close()

print("Таблицы groups и students созданы")
