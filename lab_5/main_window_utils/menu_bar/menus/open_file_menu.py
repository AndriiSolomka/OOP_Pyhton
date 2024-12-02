from lab_5.main_window_utils.menu_bar.base_menus.base_item_menu import BaseItemMenu
from lab_5.main_window_utils.menu_items.menu_items import MenuBarItems


class CreateOpenFileMenu(BaseItemMenu):
    def create_menu(self):
        self.open_file = MenuBarItems(self._menu, self._main_window)
        self.open_file.create_single_menu("Open File", self.handle_action)

    def handle_action(self):
        self._main_window._read_csv()
