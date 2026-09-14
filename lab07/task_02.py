"""Задание № 2: вставить данные в таблицу SQLite."""

# sqlite3 входит в стандартную библиотеку и работает с базами SQLite.
import sqlite3
from pathlib import Path


def insert_student(database_name: str | Path, name: str, group_name: str) -> int:
    """Создать таблицу, добавить студента и вернуть его id."""
    # connect открывает существующую базу или создаёт новый файл.
    connection = sqlite3.connect(database_name)
    try:
        # cursor позволяет выполнять SQL-команды.
        cursor = connection.cursor()
        # IF NOT EXISTS не вызывает ошибку при повторном запуске программы.
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                group_name TEXT NOT NULL
            )
            """
        )
        # Знаки ? безопасно передают значения в SQL-запрос.
        cursor.execute(
            "INSERT INTO students (name, group_name) VALUES (?, ?)",
            (name, group_name),
        )
        # commit сохраняет изменения в файле базы данных.
        connection.commit()
        # lastrowid содержит id только что добавленной записи.
        return int(cursor.lastrowid)
    finally:
        # Соединение нужно закрыть даже при возникновении ошибки.
        connection.close()


def main() -> None:
    # Добавляем одну демонстрационную запись.
    student_id = insert_student("lab07_task02.db", "Анна", "ПИ-21")
    # Показываем идентификатор новой записи.
    print(f"Студент добавлен, id = {student_id}")


if __name__ == "__main__":
    main()
