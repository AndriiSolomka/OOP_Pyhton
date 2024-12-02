from lab_5.main_window_utils.menu_bar.base_menus.base_item_menu import BaseItemMenu
from lab_5.main_window_utils.menu_items.create_objects_items import CreateObjectsItems
from lab_5.main_window_utils.menu_items.menu_items import MenuBarItems


class CreateShapesMenu(BaseItemMenu):

    def create_menu(self):
        shapes_menu = MenuBarItems(self._menu, self._main_window)
        shapes_menu.create_menu("Object", self.create_shapes_menu_items)

    def create_shapes_menu_items(self, menu):
        menu_items = CreateObjectsItems(menu, self._main_window)
        menu_items.create_items()
