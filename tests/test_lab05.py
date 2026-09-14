import pytest

from lab05.app import selected_message


def test_selected_message() -> None:
    items = ("Python", "Git")
    assert selected_message(items, None) == "Элемент не выбран"
    assert selected_message(items, 1) == "Выбрано: Git"


def test_selected_message_rejects_invalid_index() -> None:
    with pytest.raises(IndexError):
        selected_message(("Python",), 2)
