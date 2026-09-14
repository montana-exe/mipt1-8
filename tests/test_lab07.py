import sqlite3

import pytest

from lab07.database import add_student, connect, initialize_database, list_students, update_student


@pytest.fixture
def database() -> sqlite3.Connection:
    connection = connect(":memory:")
    initialize_database(connection)
    yield connection
    connection.close()


def test_multiple_tables_are_created(database: sqlite3.Connection) -> None:
    names = {
        row["name"]
        for row in database.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    }
    assert {"groups", "students"} <= names


def test_insert_and_update(database: sqlite3.Connection) -> None:
    student_id = add_student(database, "Анна", "ПИ-21")
    assert list_students(database) == [
        {"id": student_id, "name": "Анна", "group_name": "ПИ-21"}
    ]

    assert update_student(
        database,
        student_id,
        name="Анна Соколова",
        group_name="ПИ-22",
    )
    assert list_students(database) == [
        {"id": student_id, "name": "Анна Соколова", "group_name": "ПИ-22"}
    ]


def test_unknown_group_is_rejected(database: sqlite3.Connection) -> None:
    with pytest.raises(ValueError, match="не найдена"):
        add_student(database, "Анна", "НЕИЗВЕСТНАЯ")
