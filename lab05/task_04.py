import tkinter as tk

window = tk.Tk()
window.title("Задание № 4")
window.geometry("400x250")

items = ["Python", "Git", "SQLite", "FastAPI"]
listbox = tk.Listbox(window)

for item in items:
    listbox.insert(tk.END, item)

listbox.pack(pady=20)
result = tk.Label(window, text="Выберите элемент")
result.pack()


def show_selection(event):
    selected_index = listbox.curselection()
    if selected_index:
        result.config(text=f"Выбрано: {listbox.get(selected_index[0])}")


listbox.bind("<<ListboxSelect>>", show_selection)
window.mainloop()
