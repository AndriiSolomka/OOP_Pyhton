from lab_4.shapes_utils.shape.shape import Shape


class TempPoint(Shape):

    def show(self):
        return self.canvas.create_oval(self._x1, self._y1, self._x2, self._y2)
