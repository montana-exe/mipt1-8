"""Задание № 7: создать несколько связанных таблиц SQLite."""

import sqlite3
from pathlib import Path


def create_tables(database_name: str | Path) -> None:
    """Создать таблицы groups и students со связью по внешнему ключу."""
    # Открываем соединение с базой данных.
    connection = sqlite3.connect(database_name)
    try:
        # В SQLite поддержку внешних ключей нужно включить явно.
        connection.execute("PRAGMA foreign_keys = ON")
        # executescript позволяет выполнить несколько SQL-команд за один раз.
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                group_id INTEGER NOT NULL,
                FOREIGN KEY (group_id) REFERENCES groups(id)
            );
            """
        )
        # Сохраняем обе созданные таблицы.
        connection.commit()
    finally:
        # Закрываем файл базы данных.
        connection.close()


def get_table_names(database_name: str | Path) -> list[str]:
    """Вернуть названия пользовательских таблиц базы данных."""
    # Открываем соединение для чтения системной таблицы.
    connection = sqlite3.connect(database_name)
    try:
        # sqlite_master хранит описание таблиц SQLite.
        rows = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
        # Из каждой строки берём первый столбец — название таблицы.
        return [row[0] for row in rows]
    finally:
        connection.close()


def main() -> None:
    # Создаём отдельный файл базы для задания № 7.
    database_name = "lab07_task07.db"
    # Создаём обе таблицы.
    create_tables(database_name)
    # Выводим их названия для проверки.
    print(f"Созданы таблицы: {get_table_names(database_name)}")


if __name__ == "__main__":
    main()
