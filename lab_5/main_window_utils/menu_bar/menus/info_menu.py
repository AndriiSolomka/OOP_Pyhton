from lab_5.main_window_utils.menu_bar.base_menus.base_item_menu import BaseItemMenu
from lab_5.main_window_utils.menu_items.create_info_items import CreateInfoItems
from lab_5.main_window_utils.menu_items.menu_items import MenuBarItems


class CreateInfoMenu(BaseItemMenu):
    def create_menu(self):
        info_menu = MenuBarItems(self._menu, self._main_window)
        info_menu.create_menu("Info", self.create_info_menu_items)

    def create_info_menu_items(self, menu):
        menu_items = CreateInfoItems(menu, self._main_window)
        menu_items.create_items()
