"""Запуск консольных демонстраций лабораторных работ."""

from lab01.feature import project_status
from lab01.main import greeting
from lab02.tasks import count_vowels, gcd, sum_odd_numbers
from lab03.models import Circle, Rectangle, Student, Vector2D
from lab04.functional import factorial, filter_even, logged
from lab07.database import add_student, connect, initialize_database, list_students
from lab08.calculator import Calculator


def main() -> None:
    """Вывести результаты всех консольных заданий."""
    print("Лабораторная № 1:", greeting("студент"), project_status())
    print("Лабораторная № 2:", sum_odd_numbers(10), gcd(54, 24), count_vowels("Привет"))

    student = Student("Иван", 20, "ПИ-21")
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    print("Лабораторная № 3:", student.info())
    print("Фигуры:", rectangle.area(), rectangle.perimeter(), round(circle.area(), 2))
    print("Сложение векторов:", Vector2D(1, 2) + Vector2D(3, 4))

    @logged
    def double(value: int) -> int:
        return value * 2

    print("Лабораторная № 4:", filter_even(range(1, 11)), factorial(5), double(4))

    with connect(":memory:") as connection:
        initialize_database(connection)
        student_id = add_student(connection, "Анна", "ПИ-21")
        print("Лабораторная № 7:", student_id, list_students(connection))

    calculator = Calculator()
    print("Лабораторная № 8:", calculator.add(2, 3), calculator.divide(10, 2))
    print("Лабораторные № 5 и № 6 запускаются отдельно (см. их README).")


if __name__ == "__main__":
    main()
