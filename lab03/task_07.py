"""Задание № 7: перегрузить оператор сложения +."""


class Vector:
    """Двумерный вектор с координатами x и y."""

    def __init__(self, x: float, y: float) -> None:
        # Сохраняем координату по горизонтальной оси.
        self.x = x
        # Сохраняем координату по вертикальной оси.
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        """Определить работу оператора + для двух векторов."""
        # Координаты двух векторов складываются отдельно.
        new_x = self.x + other.x
        new_y = self.y + other.y
        # Возвращаем новый вектор, не изменяя исходные объекты.
        return Vector(new_x, new_y)

    def __eq__(self, other: object) -> bool:
        """Сравнить два вектора по координатам."""
        # Сравнение возможно только с другим объектом Vector.
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        """Вернуть понятное текстовое представление вектора."""
        return f"Vector({self.x}, {self.y})"


def main() -> None:
    # Создаём два исходных вектора.
    first = Vector(1, 2)
    second = Vector(3, 4)
    # Оператор + вызывает метод __add__.
    result = first + second
    # Вывод вызывает метод __str__ у результата.
    print(f"{first} + {second} = {result}")


if __name__ == "__main__":
    main()
