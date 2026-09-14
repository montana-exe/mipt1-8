"""GUI на Tkinter для заданий 2, 4 и 7."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def selected_message(items: tuple[str, ...], index: int | None) -> str:
    """Сформировать сообщение о выбранном элементе списка."""
    if index is None:
        return "Элемент не выбран"
    if index < 0 or index >= len(items):
        raise IndexError("Индекс элемента находится вне списка")
    return f"Выбрано: {items[index]}"


class LabApplication(tk.Tk):
    """Главное окно, объединяющее три задания лабораторной работы."""

    ITEMS = ("Python", "Git", "SQLite", "FastAPI")

    def __init__(self) -> None:
        super().__init__()
        self.title("Лабораторная работа № 5 — вариант 2")
        self.geometry("520x390")
        self.minsize(440, 340)
        self._build_menu()
        self._build_content()

    def _build_menu(self) -> None:
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.configure(menu=menu_bar)

    def _build_content(self) -> None:
        container = ttk.Frame(self, padding=20)
        container.pack(fill=tk.BOTH, expand=True)

        ttk.Label(container, text="Задание № 2", font=("Segoe UI", 13, "bold")).pack(anchor=tk.W)
        self.text_entry = ttk.Entry(container)
        self.text_entry.pack(fill=tk.X, pady=(8, 6))
        self.output_text = tk.StringVar(value="Введите текст и нажмите кнопку")
        ttk.Button(container, text="Вывести", command=self._show_text).pack(anchor=tk.W)
        ttk.Label(container, textvariable=self.output_text).pack(anchor=tk.W, pady=(6, 20))

        ttk.Separator(container).pack(fill=tk.X, pady=(0, 16))
        ttk.Label(container, text="Задание № 4", font=("Segoe UI", 13, "bold")).pack(anchor=tk.W)
        self.listbox = tk.Listbox(container, height=len(self.ITEMS), exportselection=False)
        for item in self.ITEMS:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(fill=tk.X, pady=(8, 6))
        self.listbox.bind("<<ListboxSelect>>", self._show_selection)
        self.selection_text = tk.StringVar(value=selected_message(self.ITEMS, None))
        ttk.Label(container, textvariable=self.selection_text).pack(anchor=tk.W)

    def _show_text(self) -> None:
        value = self.text_entry.get().strip()
        self.output_text.set(value if value else "Текст не введён")

    def _show_selection(self, _event: tk.Event[tk.Misc]) -> None:
        selection = self.listbox.curselection()
        index = selection[0] if selection else None
        self.selection_text.set(selected_message(self.ITEMS, index))


def main() -> None:
    LabApplication().mainloop()


if __name__ == "__main__":
    main()
