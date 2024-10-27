from abc import ABC, abstractmethod


class BaseFrame(ABC):
    def __init__(self, frame, main_window, name):
        self._frame = frame
        self._main_window = main_window
        self._name = name

    @abstractmethod
    def create_btn(self):
        pass
