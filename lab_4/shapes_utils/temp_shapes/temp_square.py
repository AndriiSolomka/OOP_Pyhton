from lab_4.shapes_utils.shape.shape import Shape


class TempSquare(Shape):

    def show(self):
        return self.canvas.create_rectangle(
            self._x1, self._y1, self._x2, self._y2, outline="grey", dash=(4, 2)
        )
