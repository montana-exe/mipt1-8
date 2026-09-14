"""Калькулятор, реализованный по TDD, с журналированием операций."""

import logging

logger = logging.getLogger(__name__)
Number = int | float


class Calculator:
    """Четыре базовые арифметические операции."""

    def add(self, first: Number, second: Number) -> Number:
        result = first + second
        logger.info("Сложение: %s + %s = %s", first, second, result)
        return result

    def subtract(self, first: Number, second: Number) -> Number:
        result = first - second
        logger.info("Вычитание: %s - %s = %s", first, second, result)
        return result

    def multiply(self, first: Number, second: Number) -> Number:
        result = first * second
        logger.info("Умножение: %s * %s = %s", first, second, result)
        return result

    def divide(self, first: Number, second: Number) -> float:
        if second == 0:
            logger.error("Попытка деления числа %s на ноль", first)
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = first / second
        logger.info("Деление: %s / %s = %s", first, second, result)
        return result


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    calculator = Calculator()
    print("7 + 3 =", calculator.add(7, 3))
    print("7 - 3 =", calculator.subtract(7, 3))
    print("7 * 3 =", calculator.multiply(7, 3))
    print("7 / 2 =", calculator.divide(7, 2))


if __name__ == "__main__":
    main()
