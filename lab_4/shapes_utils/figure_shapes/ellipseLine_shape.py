from lab_4.shapes_utils.figure_shapes.ellipse_shape import EllipseShape
from lab_4.shapes_utils.figure_shapes.line_shape import LineShape


class EllipseLineShape(LineShape, EllipseShape):
    def show(self, color):
        LineShape.show(self, color)

        radius = 5
        self.draw_circle(self._x1, self._y1, radius, color)
        self.draw_circle(self._x2, self._y2, radius, color)

    def draw_circle(self, x, y, radius, color):
        original_coords = (self._x1, self._y1, self._x2, self._y2)

        self._x1, self._y1 = x - radius, y - radius
        self._x2, self._y2 = x + radius, y + radius

        EllipseShape.show(self, color)

        self._x1, self._y1, self._x2, self._y2 = original_coords


print(EllipseLineShape.__mro__)
