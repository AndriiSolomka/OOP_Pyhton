import tkinter as tk

from constants import main_const as const
from modules import slider_input, text_input

root = tk.Tk()


root.title(const.TITLE)
root.geometry(const.GEOMETRY)
root.resizable(width=False, height=False)


menu = tk.Menu(root)
root.config(menu=menu)


info_output = tk.Label(root, width=const.INFO_WIDTH, font=const.FONT)
info_output.pack(pady=const.INFO_PADY)


def open_slider_menu():
    selected_number = slider_input.open_slider()

    if selected_number:
        info_output.config(text=selected_number)


def open_text_menu():
    selected_text = text_input.open_text()

    if selected_text:
        info_output.config(text=selected_text)


tabs_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label=const.MENU_1_NAME, menu=tabs_menu)

tabs_menu.add_command(label=const.MENU_1_LABEL, command=open_slider_menu)
tabs_menu.add_command(label=const.MENU_2_LABEL, command=open_text_menu)


root.mainloop()
