"""Объектно-ориентированные задания варианта 2."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi


@dataclass(slots=True)
class Student:
    """Студент с краткой информацией для вывода."""

    name: str
    age: int
    group: str

    def info(self) -> str:
        """Вернуть форматированную информацию о студенте."""
        return f"Студент: {self.name}; возраст: {self.age}; группа: {self.group}"

    def display_info(self) -> None:
        """Вывести информацию о студенте в консоль."""
        print(self.info())


class Shape(ABC):
    """Интерфейс геометрической фигуры."""

    @abstractmethod
    def area(self) -> float:
        """Вернуть площадь."""

    @abstractmethod
    def perimeter(self) -> float:
        """Вернуть периметр."""


@dataclass(frozen=True, slots=True)
class Rectangle(Shape):
    width: float
    height: float

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительными")

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


@dataclass(frozen=True, slots=True)
class Circle(Shape):
    radius: float

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError("Радиус должен быть положительным")

    def area(self) -> float:
        return pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


@dataclass(frozen=True, slots=True)
class Vector2D:
    x: float
    y: float

    def __add__(self, other: object) -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)


def main() -> None:
    student = Student("Анна", 20, "ПИ-21")
    student.display_info()
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    print(f"Прямоугольник: S={rectangle.area()}, P={rectangle.perimeter()}")
    print(f"Круг: S={circle.area():.2f}, P={circle.perimeter():.2f}")
    print("Сумма векторов:", Vector2D(1, 2) + Vector2D(3, 4))


if __name__ == "__main__":
    main()
