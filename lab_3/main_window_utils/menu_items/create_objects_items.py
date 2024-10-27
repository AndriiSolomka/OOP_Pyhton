from lab_3.main_window_utils.menu_items.base_menu_items.base_menu_items import BaseMenuItems


class CreateObjectsItems(BaseMenuItems):
    def create_items(self):
        self._menu.add_command(
            label="Point", command=lambda: self.main_window.select_figure("Point")
        )

        self._menu.add_command(
            label="Line",
            command=lambda: self.main_window.select_figure("Line"),
        )

        self._menu.add_command(
            label="Square",
            command=lambda: self.main_window.select_figure("Square"),
        )

        self._menu.add_command(
            label="Ellipse",
            command=lambda: self.main_window.select_figure("Ellipse"),
        )
