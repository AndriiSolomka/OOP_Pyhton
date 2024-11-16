from lab_4.main_window_utils.menu_bar.base_menus.default_menu import DefaultMenu
from lab_4.main_window_utils.menu_bar.menus.file_menu import CreateFileMenu
from lab_4.main_window_utils.menu_bar.menus.info_menu import CreateInfoMenu
from lab_4.main_window_utils.menu_bar.menus.shapes_menu import CreateShapesMenu
from lab_4.main_window_utils.menu_bar.menus.table_menu import CreateTableMenu


class MenuBar(DefaultMenu):
    def create_menu(self):
        # Make "File"
        file_menu = CreateFileMenu(self._menu, self._main_window)
        file_menu.create_menu()

        # Make "Shape"
        shapes_menu = CreateShapesMenu(self._menu, self._main_window)
        shapes_menu.create_menu()

        # Make "Info"
        info_menu = CreateInfoMenu(self._menu, self._main_window)
        info_menu.create_menu()

        # Make "Table"
        table_menu = CreateTableMenu(self._menu, self._main_window)
        table_menu.create_menu()

    def select_name(self, figure):
        if self.menu_index is not None:
            label = figure if figure else "Untitled"
            self._menu.entryconfig(self.menu_index, label=label)
