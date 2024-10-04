import tkinter as tk

from main_window_utils.menu_items.menu_items import MenuBarItems


class MenuBar:
    def __init__(self, root, main_window):
        self.menu = self.create_menu(root, main_window)
        root.config(menu=self.menu)

    def create_menu(self, root, main_window):
        menu = tk.Menu(root)
        tabs_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Objects", menu=tabs_menu)

        menu_items = MenuBarItems(tabs_menu, main_window)
        menu_items.create_items()

        return menu
