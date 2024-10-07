class MenuBarItems:
    def __init__(self, menu, main_window):
        self.menu = menu
        self.main_window = main_window

    def create_shapes_items(self):
        self.menu.add_command(
            label="Point", command=lambda: self.main_window._select_figure("Point")
        )

        self.menu.add_command(
            label="Line",
            command=lambda: self.main_window._select_figure("Line"),
        )

        self.menu.add_command(
            label="Square",
            command=lambda: self.main_window._select_figure("Square"),
        )

        self.menu.add_command(
            label="Ellipse",
            command=lambda: self.main_window._select_figure("Ellipse"),
        )

    def create_file_items(self):
        self.menu.add_command(label="Save")
        self.menu.add_command(label="Delete")

    def create_info_items(self):
        self.menu.add_command(label="More info")
