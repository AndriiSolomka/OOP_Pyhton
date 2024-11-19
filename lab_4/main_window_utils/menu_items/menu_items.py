import tkinter as tk


class MenuBarItems:
    def __init__(self, menu, main_window):
        self._menu = menu
        self.main_window = main_window

    def create_menu(self, label, items_creator):
        new_menu = tk.Menu(self._menu, tearoff=0)
        self._menu.add_cascade(label=label, menu=new_menu)
        items_creator(new_menu)
        return new_menu

    def create_single_menu(self, label, command):
        self._menu.add_command(label=label, command=command)
