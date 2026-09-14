from math import pi

import pytest

from lab03.models import Circle, Rectangle, Student, Vector2D


def test_student_information() -> None:
    student = Student("Анна", 20, "ПИ-21")
    assert student.info() == "Студент: Анна; возраст: 20; группа: ПИ-21"


def test_shapes() -> None:
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    assert rectangle.area() == 20
    assert rectangle.perimeter() == 18
    assert circle.area() == pytest.approx(9 * pi)
    assert circle.perimeter() == pytest.approx(6 * pi)


def test_vector_addition() -> None:
    assert Vector2D(1, 2) + Vector2D(3, 4) == Vector2D(4, 6)


def test_shape_dimensions_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Circle(0)
