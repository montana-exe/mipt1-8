"""Задание № 4: вычислить факториал через reduce."""

# Импортируем функцию reduce из стандартного модуля functools.
from functools import reduce


def factorial(number: int) -> int:
    """Вернуть факториал неотрицательного целого числа."""
    # Факториал для отрицательных чисел не определён.
    if number < 0:
        raise ValueError("Факториал отрицательного числа не определён")

    # range создаёт числа от 1 до number включительно.
    numbers = range(1, number + 1)
    # reduce последовательно умножает элементы; 1 является начальным значением.
    return reduce(lambda result, item: result * item, numbers, 1)


def main() -> None:
    # Получаем целое число от пользователя.
    number = int(input("Введите неотрицательное число: "))
    # Вычисляем и выводим факториал.
    print(f"{number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
