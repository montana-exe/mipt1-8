import sqlite3


def test_insert_student(run_script, tmp_path) -> None:
    result = run_script("lab07/task_02.py", "Анна\nПИ-21\n", tmp_path)
    with sqlite3.connect(tmp_path / "students.db") as connection:
        row = connection.execute("SELECT name, group_name FROM students").fetchone()
    assert row == ("Анна", "ПИ-21")
    assert "Студент добавлен" in result.stdout


def test_update_student(run_script, tmp_path) -> None:
    run_script("lab07/task_04.py", "Мария\n", tmp_path)
    with sqlite3.connect(tmp_path / "students.db") as connection:
        name = connection.execute("SELECT name FROM students WHERE id = 1").fetchone()[0]
    assert name == "Мария"


def test_create_multiple_tables(run_script, tmp_path) -> None:
    run_script("lab07/task_07.py", cwd=tmp_path)
    with sqlite3.connect(tmp_path / "university.db") as connection:
        tables = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    assert {"groups", "students"} <= {row[0] for row in tables}
