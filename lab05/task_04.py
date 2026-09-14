"""Задание № 4: список Listbox и выбор элемента."""

import tkinter as tk

# Эти значения будут показаны пользователю в списке.
ITEMS = ("Python", "Git", "SQLite", "FastAPI")


def selected_message(item: str | None) -> str:
    """Вернуть сообщение для выбранного или отсутствующего элемента."""
    # Если элемент не передан, сообщаем, что выбор ещё не сделан.
    if item is None:
        return "Элемент не выбран"
    # Иначе добавляем название выбранного элемента в ответ.
    return f"Выбрано: {item}"


def main() -> None:
    # Создаём и настраиваем главное окно.
    window = tk.Tk()
    window.title("Лабораторная № 5 — задание № 4")
    window.geometry("420x250")

    # Создаём список высотой в количество элементов.
    listbox = tk.Listbox(window, height=len(ITEMS))
    # Добавляем каждый элемент в конец списка.
    for item in ITEMS:
        listbox.insert(tk.END, item)
    listbox.pack(fill=tk.X, padx=30, pady=20)

    # Переменная хранит текст под списком.
    result_text = tk.StringVar(value=selected_message(None))

    def show_selection(_event: tk.Event) -> None:
        # curselection возвращает номера выбранных строк.
        selected_indexes = listbox.curselection()
        # Если выбор есть, получаем текст первой выбранной строки.
        selected_item = listbox.get(selected_indexes[0]) if selected_indexes else None
        # Показываем результат в надписи.
        result_text.set(selected_message(selected_item))

    # Событие срабатывает каждый раз при изменении выбора.
    listbox.bind("<<ListboxSelect>>", show_selection)
    tk.Label(window, textvariable=result_text).pack()

    window.mainloop()


if __name__ == "__main__":
    main()
