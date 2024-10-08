from lab_2.shapes_utils.shape.shape import Shape


class LineShape(Shape):
    def show(self):
        self.canvas.create_line(self._x1, self._y1, self._x2, self._y2, fill="black")
