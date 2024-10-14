from abc import ABC, abstractmethod


class BaseMenuItems(ABC):
    def __init__(self, menu, main_window):
        self._menu = menu
        self.main_window = main_window

    @abstractmethod
    def create_items(self):
        pass
