def test_sum_odd_numbers(run_script) -> None:
    result = run_script("lab02/task_02.py", "10\n")
    assert "Сумма нечётных чисел до 10: 25" in result.stdout


def test_gcd(run_script) -> None:
    result = run_script("lab02/task_04.py", "54\n24\n")
    assert "НОД: 6" in result.stdout


def test_count_vowels(run_script) -> None:
    result = run_script("lab02/task_07.py", "Привет, Python!\n")
    assert "Количество гласных: 3" in result.stdout
