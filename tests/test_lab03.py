import pytest

from lab03.task_02 import Student
from lab03.task_04 import Shape
from lab03.task_07 import Vector


def test_student_information() -> None:
    student = Student("Анна", 20, "ПИ-21")
    assert student.get_info() == "Студент: Анна; возраст: 20; группа: ПИ-21"


def test_shape() -> None:
    shape = Shape(4, 5)
    assert shape.area() == 20
    assert shape.perimeter() == 18


def test_vector_addition() -> None:
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)


def test_shape_dimensions_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Shape(0, 5)
