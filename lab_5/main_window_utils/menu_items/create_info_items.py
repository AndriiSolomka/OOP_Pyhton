from lab_5.main_window_utils.menu_items.base_menu_items.base_menu_items import BaseMenuItems


class CreateInfoItems(BaseMenuItems):
    def create_items(self):
        self._menu.add_command(label="More info")
