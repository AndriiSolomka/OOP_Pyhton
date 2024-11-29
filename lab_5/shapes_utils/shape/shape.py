from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, figure, canvas, x1, y1, x2=None, y2=None):
        self.canvas = canvas
        self.figure = figure
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_coordinates(self):
        return (self.figure, self._x1, self._y1, self._x2, self._y2)

    @abstractmethod
    def show(self, color):
        pass
