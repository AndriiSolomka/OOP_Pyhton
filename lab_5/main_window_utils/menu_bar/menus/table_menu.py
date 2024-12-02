from lab_5.main_window_utils.menu_bar.base_menus.base_item_menu import BaseItemMenu
from lab_5.main_window_utils.menu_items.menu_items import MenuBarItems


class CreateTableMenu(BaseItemMenu):
    def create_menu(self):
        self.table = MenuBarItems(self._menu, self._main_window)
        self.table.create_single_menu("Table", self.handle_action)

    def handle_action(self):
        self._main_window._create_table()
