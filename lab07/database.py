"""Операции SQLite для заданий 2, 4 и 7."""

import sqlite3
from pathlib import Path

DatabasePath = str | Path


def connect(database: DatabasePath = "lab07.db") -> sqlite3.Connection:
    """Открыть соединение с включённой поддержкой внешних ключей."""
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database(connection: sqlite3.Connection) -> None:
    """Создать две связанные таблицы и начальные группы."""
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
    connection.executemany(
        "INSERT OR IGNORE INTO groups(name) VALUES (?)",
        (("ПИ-21",), ("ПИ-22",)),
    )
    connection.commit()


def _group_id(connection: sqlite3.Connection, group_name: str) -> int:
    row = connection.execute("SELECT id FROM groups WHERE name = ?", (group_name,)).fetchone()
    if row is None:
        raise ValueError(f"Группа {group_name!r} не найдена")
    return int(row["id"])


def add_student(connection: sqlite3.Connection, name: str, group_name: str) -> int:
    """Вставить студента и вернуть его идентификатор."""
    normalized_name = name.strip()
    if not normalized_name:
        raise ValueError("Имя студента не может быть пустым")
    cursor = connection.execute(
        "INSERT INTO students(name, group_id) VALUES (?, ?)",
        (normalized_name, _group_id(connection, group_name)),
    )
    connection.commit()
    return int(cursor.lastrowid)


def update_student(
    connection: sqlite3.Connection,
    student_id: int,
    *,
    name: str,
    group_name: str,
) -> bool:
    """Обновить имя и группу студента; вернуть признак найденной записи."""
    normalized_name = name.strip()
    if not normalized_name:
        raise ValueError("Имя студента не может быть пустым")
    cursor = connection.execute(
        "UPDATE students SET name = ?, group_id = ? WHERE id = ?",
        (normalized_name, _group_id(connection, group_name), student_id),
    )
    connection.commit()
    return cursor.rowcount > 0


def list_students(connection: sqlite3.Connection) -> list[dict[str, object]]:
    """Вернуть студентов вместе с названиями групп."""
    rows = connection.execute(
        """
        SELECT students.id, students.name, groups.name AS group_name
        FROM students
        JOIN groups ON groups.id = students.group_id
        ORDER BY students.id
        """
    ).fetchall()
    return [dict(row) for row in rows]


def main() -> None:
    with connect() as connection:
        initialize_database(connection)
        existing = connection.execute("SELECT id FROM students LIMIT 1").fetchone()
        if existing is None:
            student_id = add_student(connection, "Анна Петрова", "ПИ-21")
        else:
            student_id = int(existing["id"])
        update_student(connection, student_id, name="Анна Соколова", group_name="ПИ-22")
        print("Студенты:", list_students(connection))


if __name__ == "__main__":
    main()
