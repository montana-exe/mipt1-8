import sqlite3
from pathlib import Path

from lab07.task_02 import insert_student
from lab07.task_04 import get_student_name, prepare_database, update_student
from lab07.task_07 import create_tables, get_table_names


def test_insert_student(tmp_path: Path) -> None:
    database = tmp_path / "insert.db"
    student_id = insert_student(database, "Анна", "ПИ-21")

    with sqlite3.connect(database) as connection:
        row = connection.execute(
            "SELECT name, group_name FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

    assert row == ("Анна", "ПИ-21")


def test_update_student(tmp_path: Path) -> None:
    database = tmp_path / "update.db"
    prepare_database(database)

    assert update_student(database, 1, "Анна Соколова")
    assert get_student_name(database, 1) == "Анна Соколова"
    assert not update_student(database, 999, "Неизвестный студент")


def test_multiple_tables_are_created(tmp_path: Path) -> None:
    database = tmp_path / "tables.db"
    create_tables(database)

    assert set(get_table_names(database)) == {"groups", "students"}
