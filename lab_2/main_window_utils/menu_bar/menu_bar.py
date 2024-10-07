import tkinter as tk

from main_window_utils.menu_items.menu_items import MenuBarItems


class MenuBar:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.menu = tk.Menu(root)

        self.file_menu = self.create_menu("File", self.create_file_menu_items)
        self.shapes_menu = self.create_menu("Object", self.create_shapes_menu_items)
        self.info_menu = self.create_menu("Info", self.create_info_menu_items)

        root.config(menu=self.menu)

    def create_menu(self, label, items_creator):
        new_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=label, menu=new_menu)
        items_creator(new_menu)
        return new_menu

    def create_file_menu_items(self, menu):
        menu_items = MenuBarItems(menu, self.main_window)
        menu_items.create_file_items()

    def create_shapes_menu_items(self, menu):
        self.menu_index = self.menu.index("end")
        menu_items = MenuBarItems(menu, self.main_window)
        menu_items.create_shapes_items()

    def create_info_menu_items(self, menu):
        menu_items = MenuBarItems(menu, self.main_window)
        menu_items.create_info_items()

    def select_name(self, figure):
        label = figure if figure else "Object"
        self.menu.entryconfig(self.menu_index, label=label)
