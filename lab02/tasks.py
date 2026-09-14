"""Задания 2, 4 и 7 среднего уровня для варианта 2."""

VOWELS = frozenset("аеёиоуыэюяaeiou")


def sum_odd_numbers(n: int) -> int:
    """Вернуть сумму положительных нечётных чисел от 1 до ``n`` включительно."""
    if n < 1:
        return 0
    return sum(number for number in range(1, n + 1, 2))


def gcd(first: int, second: int) -> int:
    """Вычислить неотрицательный НОД двух целых чисел алгоритмом Евклида."""
    first, second = abs(first), abs(second)
    while second:
        first, second = second, first % second
    return first


def count_vowels(text: str) -> int:
    """Подсчитать русские и английские гласные без учёта регистра."""
    return sum(character in VOWELS for character in text.casefold())


def main() -> None:
    """Запросить данные и продемонстрировать три решения."""
    n = int(input("Введите N: "))
    print(f"Сумма нечётных чисел до {n}: {sum_odd_numbers(n)}")

    first = int(input("Введите первое число для НОД: "))
    second = int(input("Введите второе число для НОД: "))
    print(f"НОД: {gcd(first, second)}")

    text = input("Введите строку: ")
    print(f"Количество гласных: {count_vowels(text)}")


if __name__ == "__main__":
    main()
