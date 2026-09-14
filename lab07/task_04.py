"""Задание № 4: обновить запись в таблице SQLite."""

import sqlite3
from pathlib import Path


def prepare_database(database_name: str | Path) -> None:
    """Создать таблицу и первую запись для примера."""
    # Открываем соединение с базой данных.
    connection = sqlite3.connect(database_name)
    try:
        # Создаём простую таблицу студентов.
        connection.execute(
            "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL)"
        )
        # INSERT OR IGNORE не добавляет запись повторно, если id уже существует.
        connection.execute("INSERT OR IGNORE INTO students VALUES (?, ?)", (1, "Анна"))
        # Сохраняем созданную таблицу и запись.
        connection.commit()
    finally:
        # Явно закрываем файл базы данных.
        connection.close()


def update_student(database_name: str | Path, student_id: int, new_name: str) -> bool:
    """Изменить имя студента и сообщить, была ли найдена запись."""
    # Открываем соединение с нужным файлом базы данных.
    connection = sqlite3.connect(database_name)
    try:
        # Выполняем параметризованный запрос UPDATE.
        cursor = connection.execute(
            "UPDATE students SET name = ? WHERE id = ?",
            (new_name, student_id),
        )
        # Сохраняем изменение.
        connection.commit()
        # rowcount равен количеству изменённых строк.
        return cursor.rowcount > 0
    finally:
        # Закрываем соединение независимо от результата запроса.
        connection.close()


def get_student_name(database_name: str | Path, student_id: int) -> str | None:
    """Получить имя студента для проверки результата."""
    # Открываем соединение для выполнения SELECT.
    connection = sqlite3.connect(database_name)
    try:
        # fetchone возвращает одну строку результата или None.
        row = connection.execute(
            "SELECT name FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()
        # Если строка найдена, возвращаем первый столбец с именем.
        return row[0] if row else None
    finally:
        connection.close()


def main() -> None:
    # Имя файла базы используется во всех действиях примера.
    database_name = "lab07_task04.db"
    # Подготавливаем исходную запись.
    prepare_database(database_name)
    # Меняем имя студента с id 1.
    updated = update_student(database_name, 1, "Анна Соколова")
    # Показываем результат обновления и новое имя.
    print(f"Запись обновлена: {updated}")
    print(f"Новое имя: {get_student_name(database_name, 1)}")


if __name__ == "__main__":
    main()
