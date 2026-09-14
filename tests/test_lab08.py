from lab08.task_04 import Calculator


def test_requests_dependency(run_script) -> None:
    result = run_script("lab08/task_02.py")
    assert "Библиотека requests установлена" in result.stdout


def test_calculator() -> None:
    calculator = Calculator()
    assert calculator.add(7, 3) == 10
    assert calculator.subtract(7, 3) == 4
    assert calculator.multiply(7, 3) == 21
    assert calculator.divide(7, 2) == 3.5


def test_logging(run_script) -> None:
    result = run_script("lab08/task_07.py")
    assert "Количество цен: 3" in result.stderr
    assert "Общая стоимость: 250.0" in result.stderr
