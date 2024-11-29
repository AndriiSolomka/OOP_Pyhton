from lab_5.shapes_utils.shape.shape import Shape


class TempLine(Shape):

    def show(self):
        if not isinstance(self, TempLine):
            raise TypeError("This method can only be called in classes that inherit TempLine.")
        return self.canvas.create_line(
            self._x1, self._y1, self._x2, self._y2, fill="grey", dash=(4, 2)
        )
