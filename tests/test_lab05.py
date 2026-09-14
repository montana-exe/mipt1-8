from pathlib import Path


def source(name: str) -> str:
    return (Path(__file__).parents[1] / "lab05" / name).read_text(encoding="utf-8")


def test_text_field_and_button() -> None:
    code = source("task_02.py")
    assert "tk.Entry" in code
    assert "tk.Button" in code
    assert "entry.get()" in code


def test_listbox() -> None:
    code = source("task_04.py")
    assert "tk.Listbox" in code
    assert "<<ListboxSelect>>" in code


def test_file_exit_menu() -> None:
    code = source("task_07.py")
    assert 'label="Exit"' in code
    assert "window.destroy" in code
