import pytest

from lab04.task_02 import filter_even
from lab04.task_04 import factorial
from lab04.task_07 import add


def test_filter_even() -> None:
    assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


@pytest.mark.parametrize(("number", "expected"), [(0, 1), (1, 1), (5, 120)])
def test_factorial(number: int, expected: int) -> None:
    assert factorial(number) == expected


def test_factorial_rejects_negative_number() -> None:
    with pytest.raises(ValueError):
        factorial(-1)


def test_logging_decorator(capsys: pytest.CaptureFixture[str]) -> None:
    assert add(2, 3) == 5
    output = capsys.readouterr().out
    assert "Вызов функции: add" in output
    assert "Результат: 5" in output
