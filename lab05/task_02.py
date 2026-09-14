import tkinter as tk

window = tk.Tk()
window.title("Задание № 2")
window.geometry("400x180")

entry = tk.Entry(window, width=40)
entry.pack(pady=20)

result = tk.Label(window, text="")
result.pack()


def show_text():
    result.config(text=entry.get())


button = tk.Button(window, text="Вывести", command=show_text)
button.pack(pady=10)

window.mainloop()
