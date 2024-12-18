from lab_5.main_window_utils.menu_items.base_menu_items.base_menu_items import BaseMenuItems


class CreateObjectsItems(BaseMenuItems):
    def create_items(self):
        shapes = ['Point', 'Line', 'Square', 'Ellipse', 'EllipseLine', "Cube"]

        for shape in shapes:
            self._menu.add_command(label=shape, command=lambda s=shape: self.main_window._select_figure(s))
