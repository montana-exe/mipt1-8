from lab03.task_02 import Student
from lab03.task_04 import Shape
from lab03.task_07 import Vector


def test_student(capsys) -> None:
    Student("Анна", 20, "ПИ-21").show_info()
    output = capsys.readouterr().out
    assert "Студент: Анна" in output
    assert "Возраст: 20" in output
    assert "Группа: ПИ-21" in output


def test_shape() -> None:
    shape = Shape(4, 5)
    assert shape.area() == 20
    assert shape.perimeter() == 18


def test_vector_addition() -> None:
    result = Vector(1, 2) + Vector(3, 4)
    assert result.x == 4
    assert result.y == 6
