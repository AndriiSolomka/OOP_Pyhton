from lab_5.shapes_utils.shape.shape import Shape


class SquareShape(Shape):
    def show(self, color):
        self.canvas.create_rectangle(
            self._x1, self._y1, self._x2, self._y2, outline=color
        )
