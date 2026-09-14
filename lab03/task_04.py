"""Задание № 4: класс «Фигура» с вычислением площади и периметра."""


class Shape:
    """Прямоугольная фигура с заданными шириной и высотой."""

    def __init__(self, width: float, height: float) -> None:
        # Нельзя построить фигуру с неположительной стороной.
        if width <= 0 or height <= 0:
            raise ValueError("Стороны фигуры должны быть положительными")

        # Сохраняем ширину фигуры.
        self.width = width
        # Сохраняем высоту фигуры.
        self.height = height

    def area(self) -> float:
        """Вернуть площадь прямоугольной фигуры."""
        # Площадь прямоугольника равна ширине, умноженной на высоту.
        return self.width * self.height

    def perimeter(self) -> float:
        """Вернуть периметр прямоугольной фигуры."""
        # Периметр равен удвоенной сумме двух сторон.
        return 2 * (self.width + self.height)


def main() -> None:
    # Создаём фигуру со сторонами 4 и 5.
    shape = Shape(4, 5)
    # Вызываем два метода объекта и выводим результаты.
    print(f"Площадь: {shape.area()}")
    print(f"Периметр: {shape.perimeter()}")


if __name__ == "__main__":
    main()
