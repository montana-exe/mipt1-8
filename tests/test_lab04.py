from lab04.task_02 import even_numbers
from lab04.task_07 import add


def test_filter_even() -> None:
    assert even_numbers == [2, 4, 6, 8, 10]


def test_factorial(run_script) -> None:
    result = run_script("lab04/task_04.py", "5\n")
    assert "5! = 120" in result.stdout


def test_decorator(capsys) -> None:
    assert add(2, 3) == 5
    output = capsys.readouterr().out
    assert "Вызов функции add" in output
    assert "Результат: 5" in output
