"""Задание № 7: окно с меню File → Exit."""

import tkinter as tk


def main() -> None:
    # Создаём главное окно.
    window = tk.Tk()
    window.title("Лабораторная № 5 — задание № 7")
    window.geometry("420x180")

    # Создаём общую строку меню окна.
    menu_bar = tk.Menu(window)
    # Создаём выпадающее меню без пунктирного разделителя tearoff.
    file_menu = tk.Menu(menu_bar, tearoff=False)
    # Команда destroy полностью закрывает главное окно.
    file_menu.add_command(label="Exit", command=window.destroy)
    # Добавляем выпадающее меню с названием File в строку меню.
    menu_bar.add_cascade(label="File", menu=file_menu)
    # Подключаем готовую строку меню к окну.
    window.config(menu=menu_bar)

    # Добавляем в окно краткую инструкцию.
    tk.Label(window, text="Для выхода выберите File → Exit", font=("Arial", 12)).pack(pady=55)

    # Запускаем цикл обработки событий интерфейса.
    window.mainloop()


if __name__ == "__main__":
    main()
