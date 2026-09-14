"""Задание № 4: калькулятор, реализованный по методике TDD."""


class Calculator:
    """Простой калькулятор с четырьмя операциями."""

    def add(self, first: float, second: float) -> float:
        """Сложить два числа."""
        # Оператор + возвращает сумму аргументов.
        return first + second

    def subtract(self, first: float, second: float) -> float:
        """Вычесть второе число из первого."""
        return first - second

    def multiply(self, first: float, second: float) -> float:
        """Умножить два числа."""
        return first * second

    def divide(self, first: float, second: float) -> float:
        """Разделить первое число на второе."""
        # До деления отдельно проверяем недопустимый нулевой делитель.
        if second == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        # Оператор / выполняет обычное деление.
        return first / second


def main() -> None:
    # Создаём один объект калькулятора.
    calculator = Calculator()
    # Вызываем каждую операцию с демонстрационными числами.
    print(f"7 + 3 = {calculator.add(7, 3)}")
    print(f"7 - 3 = {calculator.subtract(7, 3)}")
    print(f"7 * 3 = {calculator.multiply(7, 3)}")
    print(f"7 / 2 = {calculator.divide(7, 2)}")


if __name__ == "__main__":
    main()
