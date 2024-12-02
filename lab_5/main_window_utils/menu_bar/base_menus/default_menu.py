import tkinter as tk


class DefaultMenu:
    def __init__(self, root, main_window):
        self.menu_index = None
        self._root = root
        self._main_window = main_window
        self._menu = tk.Menu(self._root)
        root.config(menu=self._menu)
