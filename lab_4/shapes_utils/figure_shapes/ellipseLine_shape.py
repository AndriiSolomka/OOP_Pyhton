from lab_4.shapes_utils.figure_shapes.ellipse_shape import EllipseShape
from lab_4.shapes_utils.figure_shapes.line_shape import LineShape


class EllipseLineShape(LineShape, EllipseShape):

    def show(self):
        line = LineShape(self.canvas, self._x1, self._y1, self._x2, self._y2)
        line.show()

        radius = 5

        self.draw_circle(self._x1, self._y1, radius)
        self.draw_circle(self._x2, self._y2, radius)

    def draw_circle(self, x, y, radius):
        circle = EllipseShape(self.canvas, x - radius, y - radius, x + 2 * radius, y + 2 * radius)
        circle.show()


print(EllipseLineShape.__mro__)
