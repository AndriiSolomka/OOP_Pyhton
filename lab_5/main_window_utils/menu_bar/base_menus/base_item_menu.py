class BaseItemMenu:
    def __init__(self, menu, main_window):
        self._menu = menu
        self._main_window = main_window
        self.menu_index = self._menu.index("end")
