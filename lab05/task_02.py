"""Задание № 2: окно с текстовым полем и кнопкой вывода текста."""

# tkinter входит в стандартную библиотеку Python и создаёт окна.
import tkinter as tk


def text_for_output(text: str) -> str:
    """Подготовить введённый текст для вывода в окне."""
    # strip удаляет пробелы в начале и конце строки.
    cleaned_text = text.strip()
    # Если строка пустая, возвращаем понятное сообщение.
    return cleaned_text if cleaned_text else "Текст не введён"


def main() -> None:
    # Создаём главное окно программы.
    window = tk.Tk()
    # Устанавливаем заголовок окна.
    window.title("Лабораторная № 5 — задание № 2")
    # Задаём начальный размер окна.
    window.geometry("420x190")

    # Добавляем поясняющую надпись.
    tk.Label(window, text="Введите текст:").pack(pady=(20, 5))
    # Создаём поле ввода.
    entry = tk.Entry(window, width=45)
    entry.pack()
    # StringVar хранит текст результирующей надписи.
    result_text = tk.StringVar(value="Здесь появится результат")

    def show_text() -> None:
        # entry.get читает строку из поля ввода.
        entered_text = entry.get()
        # set изменяет текст связанной надписи.
        result_text.set(text_for_output(entered_text))

    # Кнопка вызывает show_text после щелчка мышью.
    tk.Button(window, text="Вывести", command=show_text).pack(pady=10)
    # Надпись автоматически показывает значение result_text.
    tk.Label(window, textvariable=result_text).pack()

    # mainloop ожидает действия пользователя и не даёт окну закрыться сразу.
    window.mainloop()


if __name__ == "__main__":
    main()
