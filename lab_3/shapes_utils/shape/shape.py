from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, canvas, x1, y1, x2=None, y2=None):
        self.canvas = canvas
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    @abstractmethod
    def show(self):
        pass
