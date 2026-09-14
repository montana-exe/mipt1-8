import logging

import pytest

from lab08.task_04 import Calculator
from lab08.task_07 import calculate_total


def test_calculator_operations() -> None:
    calculator = Calculator()
    assert calculator.add(7, 3) == 10
    assert calculator.subtract(7, 3) == 4
    assert calculator.multiply(7, 3) == 21
    assert calculator.divide(7, 2) == 3.5


def test_division_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="ноль"):
        Calculator().divide(10, 0)


def test_calculator_writes_log(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO, logger="lab08.task_07"):
        result = calculate_total([2, 3])
    assert result == 5
    assert "Получено цен: 2" in caplog.text
    assert "Итоговая сумма: 5" in caplog.text
