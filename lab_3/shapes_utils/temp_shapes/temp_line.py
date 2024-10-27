from lab_3.shapes_utils.shape.shape import Shape


class TempLine(Shape):

    def show(self):
        return self.canvas.create_line(
            self._x1, self._y1, self._x2, self._y2, fill="grey", dash=(4, 2)
        )
