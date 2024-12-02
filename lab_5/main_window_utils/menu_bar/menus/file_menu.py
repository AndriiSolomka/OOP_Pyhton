from lab_5.main_window_utils.menu_bar.base_menus.base_item_menu import BaseItemMenu
from lab_5.main_window_utils.menu_items.create_file_items import CreateFileItems
from lab_5.main_window_utils.menu_items.menu_items import MenuBarItems


class CreateFileMenu(BaseItemMenu):
    def create_menu(self):
        file_menu = MenuBarItems(self._menu, self._main_window)
        file_menu.create_menu("File", self.create_file_menu_items)

    def create_file_menu_items(self, menu):
        menu_items = CreateFileItems(menu, self._main_window)
        menu_items.create_items()
