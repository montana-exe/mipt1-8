"""Задание № 2: отфильтровать чётные числа из списка."""


def filter_even(numbers: list[int]) -> list[int]:
    """Вернуть только чётные числа с помощью filter."""
    # lambda возвращает True только для чисел, которые делятся на 2 без остатка.
    even_numbers = filter(lambda number: number % 2 == 0, numbers)
    # filter создаёт специальный объект, поэтому превращаем его в обычный список.
    return list(even_numbers)


def main() -> None:
    # Создаём исходный список чисел.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Передаём список в функцию фильтрации.
    result = filter_even(numbers)
    # Печатаем исходный список и результат.
    print(f"Исходный список: {numbers}")
    print(f"Чётные числа: {result}")


if __name__ == "__main__":
    main()
