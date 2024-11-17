from lab_4.shapes_utils.shape.shape import Shape


class LineShape(Shape):
    def show(self, color):
        if not isinstance(self, LineShape):
            raise TypeError("This method can only be called in classes that inherit LineShape.")
        self.canvas.create_line(self._x1, self._y1, self._x2, self._y2, fill=color)
