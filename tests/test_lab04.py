import logging

import pytest

from lab04.functional import factorial, filter_even, logged


def test_filter_even() -> None:
    assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


@pytest.mark.parametrize(("number", "expected"), [(0, 1), (1, 1), (5, 120)])
def test_factorial(number: int, expected: int) -> None:
    assert factorial(number) == expected


def test_factorial_rejects_negative_number() -> None:
    with pytest.raises(ValueError):
        factorial(-1)


def test_logged_decorator(caplog: pytest.LogCaptureFixture) -> None:
    @logged
    def square(number: int) -> int:
        return number**2

    with caplog.at_level(logging.INFO, logger="lab04.functional"):
        assert square(4) == 16
    assert "Вызов square" in caplog.text
    assert "Результат square: 16" in caplog.text
