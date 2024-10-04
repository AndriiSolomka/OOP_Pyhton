class MenuBarItems:
    def __init__(self, tabs_menu, main_window):
        self.tabs_menu = tabs_menu
        self.main_window = main_window

    def create_items(self):
        self.tabs_menu.add_command(
            label="Point", command=lambda: self.main_window.select_figure("Point")
        )

        self.tabs_menu.add_command(
            label="Line",
            command=lambda: self.main_window.select_figure("Line"),
        )

        self.tabs_menu.add_command(
            label="Square",
            command=lambda: self.main_window.select_figure("Square"),
        )

        self.tabs_menu.add_command(
            label="Ellipse",
            command=lambda: self.main_window.select_figure("Ellipse"),
        )
