from lab_4.shapes_utils.shape.shape import Shape


class PointShape(Shape):
    def show(self):
        self.canvas.create_oval(
            self._x1 - 2, self._y1 - 2, self._x1 + 2, self._y1 + 2, fill="black"
        )
