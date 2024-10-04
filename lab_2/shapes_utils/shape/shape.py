from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, canvas, x1, y1, x2=None, y2=None):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @abstractmethod
    def show(self):
        pass
