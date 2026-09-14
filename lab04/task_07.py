"""Задание № 7: декоратор для логирования вызова функции."""

# wraps сохраняет имя и описание декорируемой функции.
from functools import wraps
# Callable используется в подсказках типов для функций.
from collections.abc import Callable
from typing import Any


def log_call(function: Callable[..., Any]) -> Callable[..., Any]:
    """Добавить вывод имени и результата к вызову функции."""

    # wraps сообщает Python, что wrapper заменяет исходную функцию.
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Печатаем имя функции перед её запуском.
        print(f"Вызов функции: {function.__name__}")
        # Запускаем исходную функцию с полученными аргументами.
        result = function(*args, **kwargs)
        # Печатаем значение, которое вернула функция.
        print(f"Результат: {result}")
        # Возвращаем результат вызывающему коду.
        return result

    # Декоратор должен вернуть новую функцию-обёртку.
    return wrapper


# Применяем созданный декоратор к функции сложения.
@log_call
def add(first: int, second: int) -> int:
    """Сложить два числа."""
    return first + second


def main() -> None:
    # При вызове add сначала выполняется функция wrapper.
    add(2, 3)


if __name__ == "__main__":
    main()
