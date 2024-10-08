import tkinter as tk

from lab_2.main_window_utils.menu_items.menu_items import MenuBarItems


class MenuBar:
    def __init__(self, root, main_window):
        self.menu_index = None
        self.__root = root
        self._main_window = main_window
        self._menu = tk.Menu(root)

        self._file_menu = self.create_menu("File", self.create_file_menu_items)
        self._shapes_menu = self.create_menu("Object", self.create_shapes_menu_items)
        self._info_menu = self.create_menu("Info", self.create_info_menu_items)

        root.config(menu=self._menu)

    def create_menu(self, label, items_creator):
        new_menu = tk.Menu(self._menu, tearoff=0)
        self._menu.add_cascade(label=label, menu=new_menu)
        items_creator(new_menu)
        return new_menu

    def create_file_menu_items(self, menu):
        menu_items = MenuBarItems(menu, self._main_window)
        menu_items.create_file_items()

    def create_shapes_menu_items(self, menu):
        self.menu_index = self._menu.index("end")
        menu_items = MenuBarItems(menu, self._main_window)
        menu_items.create_shapes_items()

    def create_info_menu_items(self, menu):
        menu_items = MenuBarItems(menu, self._main_window)
        menu_items.create_info_items()

    def select_name(self, figure):
        label = figure if figure else "Object"
        self._menu.entryconfig(self.menu_index, label=label)
