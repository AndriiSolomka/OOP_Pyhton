from lab_4.shapes_utils.temp_shapes.temp_ellipse import TempEllipse
from lab_4.shapes_utils.temp_shapes.temp_line import TempLine


class TempEllipseLine(TempLine, TempEllipse):

    def show(self):
        line = TempLine.show(self)

        radius = 5
        start = self.draw_circle(self._x1, self._y1, radius)
        end = self.draw_circle(self._x2, self._y2, radius)

        return line, start, end

    def draw_circle(self, x, y, radius):
        original_coords = (self._x1, self._y1, self._x2, self._y2)

        self._x1, self._y1 = x - radius, y - radius
        self._x2, self._y2 = x + radius, y + radius

        circle = TempEllipse.show(self)
        self._x1, self._y1, self._x2, self._y2 = original_coords

        return circle
