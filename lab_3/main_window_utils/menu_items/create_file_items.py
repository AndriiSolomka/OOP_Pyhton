from lab_3.main_window_utils.menu_items.base_menu_items.base_menu_items import BaseMenuItems


class CreateFileItems(BaseMenuItems):
    def create_items(self):
        self._menu.add_command(label="Save")
        self._menu.add_command(label="Delete")
