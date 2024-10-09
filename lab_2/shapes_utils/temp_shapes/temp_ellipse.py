from lab_2.shapes_utils.shape.shape import Shape


class TempEllipse(Shape):

    def show(self):
        return self.canvas.create_oval(
            self._x1,
            self._y1,
            self._x2,
            self._y2,
            outline="black",
            dash=(4, 2),
        )
