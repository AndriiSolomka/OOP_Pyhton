from lab_5.shapes_utils.shape.shape import Shape


class EllipseShape(Shape):
    def show(self, color):
        self.canvas.create_oval(
            self._x1, self._y1, self._x2, self._y2, outline=color, fill="yellow"
        )
