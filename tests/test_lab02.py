import pytest

from lab02.tasks import count_vowels, gcd, sum_odd_numbers


@pytest.mark.parametrize(("n", "expected"), [(10, 25), (1, 1), (0, 0), (-5, 0)])
def test_sum_odd_numbers(n: int, expected: int) -> None:
    assert sum_odd_numbers(n) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [(54, 24, 6), (-54, 24, 6), (0, 7, 7), (0, 0, 0)],
)
def test_gcd(first: int, second: int, expected: int) -> None:
    assert gcd(first, second) == expected


def test_count_vowels_for_russian_and_english() -> None:
    assert count_vowels("Привет, Python!") == 3
