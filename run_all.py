"""Краткая проверка консольных частей лабораторных работ."""

from pathlib import Path
from tempfile import TemporaryDirectory

from lab01.feature import project_status
from lab01.main import greeting
from lab02.task_02 import sum_odd_numbers
from lab02.task_04 import gcd
from lab02.task_07 import count_vowels
from lab03.task_02 import Student
from lab03.task_04 import Shape
from lab03.task_07 import Vector
from lab04.task_02 import filter_even
from lab04.task_04 import factorial
from lab04.task_07 import add
from lab07.task_02 import insert_student
from lab07.task_04 import get_student_name, prepare_database, update_student
from lab07.task_07 import create_tables, get_table_names
from lab08.task_02 import requests_version
from lab08.task_04 import Calculator
from lab08.task_07 import calculate_total


def main() -> None:
    """Запустить примеры, которым не требуется окно или веб-сервер."""
    print("Лабораторная № 1:", greeting("студент"), project_status())
    print("Лабораторная № 2:", sum_odd_numbers(10), gcd(54, 24), count_vowels("Привет"))

    student = Student("Иван", 20, "ПИ-21")
    shape = Shape(4, 5)
    vector = Vector(1, 2) + Vector(3, 4)
    print("Лабораторная № 3:", student.get_info(), shape.area(), shape.perimeter(), vector)
    print("Лабораторная № 4:", filter_even(list(range(1, 11))), factorial(5))
    add(2, 3)

    with TemporaryDirectory() as directory:
        task02_database = Path(directory) / "task02.db"
        task04_database = Path(directory) / "task04.db"
        task07_database = Path(directory) / "task07.db"
        student_id = insert_student(task02_database, "Анна", "ПИ-21")
        prepare_database(task04_database)
        update_student(task04_database, 1, "Анна Соколова")
        create_tables(task07_database)
        print(
            "Лабораторная № 7:",
            student_id,
            get_student_name(task04_database, 1),
            get_table_names(task07_database),
        )

    calculator = Calculator()
    print("Лабораторная № 8:", requests_version(), calculator.add(2, 3), calculate_total([1, 2]))
    print("Лабораторные № 5 и № 6 запускаются отдельными файлами (см. README).")


if __name__ == "__main__":
    main()
