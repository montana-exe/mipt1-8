from lab05.task_02 import text_for_output
from lab05.task_04 import selected_message


def test_selected_message() -> None:
    assert selected_message(None) == "Элемент не выбран"
    assert selected_message("Git") == "Выбрано: Git"


def test_text_for_output() -> None:
    assert text_for_output("  Привет  ") == "Привет"
    assert text_for_output("   ") == "Текст не введён"
