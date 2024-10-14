from lab_3.shapes_utils.shape.shape import Shape


class LineShape(Shape):
    def show(self):
        self.canvas.create_line_btn(self._x1, self._y1, self._x2, self._y2, fill="black")
