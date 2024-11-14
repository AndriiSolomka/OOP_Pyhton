import tkinter as tk

from lab_4.main_window_utils.menu_items.create_file_items import CreateFileItems
from lab_4.main_window_utils.menu_items.create_info_items import CreateInfoItems
from lab_4.main_window_utils.menu_items.create_objects_items import CreateObjectsItems
from lab_4.main_window_utils.menu_items.create_tables_items import CreateTablesItems
from lab_4.main_window_utils.menu_items.menu_items import MenuBarItems


class MenuBar:
    def __init__(self, root, main_window):
        self.menu_index = None
        self._root = root
        self._main_window = main_window
        self._menu = tk.Menu(self._root)

        # Make "File"
        self._file_menu = MenuBarItems(self._menu, self._main_window)
        self._file_menu.create_menu("File", self.create_file_menu_items)

        # Make "Object"
        self._shapes_menu = MenuBarItems(self._menu, self._main_window)
        self._shapes_menu.create_menu("Object", self.create_shapes_menu_items)

        # Make "Info"
        self._info_menu = MenuBarItems(self._menu, self._main_window)
        self._info_menu.create_menu("Info", self.create_info_menu_items)

        # Make "Table"
        self._table = MenuBarItems(self._menu, self._main_window)
        self._table.create_menu("Table", self.create_table_menu_items)

        root.config(menu=self._menu)

    def create_file_menu_items(self, menu):
        menu_items = CreateFileItems(menu, self._main_window)
        menu_items.create_items()

    def create_shapes_menu_items(self, menu):
        self.menu_index = self._menu.index("end")
        menu_items = CreateObjectsItems(menu, self._main_window)
        menu_items.create_items()

    def create_info_menu_items(self, menu):
        menu_items = CreateInfoItems(menu, self._main_window)
        menu_items.create_items()

    def create_table_menu_items(self, menu):
        menu_items = CreateTablesItems(menu, self._main_window)
        menu_items.create_items()

    def select_name(self, figure):
        label = figure if figure else "Object"
        self._menu.entryconfig(self.menu_index, label=label)
