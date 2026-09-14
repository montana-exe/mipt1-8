import tkinter as tk

window = tk.Tk()
window.title("Задание № 7")
window.geometry("400x180")

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="Exit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

label = tk.Label(window, text="Для выхода выберите File → Exit")
label.pack(pady=60)

window.mainloop()
