"""Функциональные задания варианта 2."""

import logging
from collections.abc import Callable, Iterable
from functools import reduce, wraps
from operator import mul
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger(__name__)


def filter_even(numbers: Iterable[int]) -> list[int]:
    """Вернуть чётные элементы с использованием ``filter``."""
    return list(filter(lambda number: number % 2 == 0, numbers))


def factorial(number: int) -> int:
    """Вычислить факториал неотрицательного целого числа через ``reduce``."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Факториал определён только для целых чисел")
    if number < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    return reduce(mul, range(1, number + 1), 1)


def logged(function: Callable[P, R]) -> Callable[P, R]:
    """Записать в журнал имя, аргументы и результат вызова функции."""

    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        logger.info("Вызов %s: args=%r, kwargs=%r", function.__name__, args, kwargs)
        result = function(*args, **kwargs)
        logger.info("Результат %s: %r", function.__name__, result)
        return result

    return wrapper


@logged
def add(first: int, second: int) -> int:
    return first + second


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    print("Чётные:", filter_even(range(1, 11)))
    print("5! =", factorial(5))
    print("2 + 3 =", add(2, 3))


if __name__ == "__main__":
    main()
