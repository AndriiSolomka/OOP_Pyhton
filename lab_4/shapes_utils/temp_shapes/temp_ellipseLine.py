from lab_4.shapes_utils.temp_shapes.temp_ellipse import TempEllipse
from lab_4.shapes_utils.temp_shapes.temp_line import TempLine


class TempEllipseLine(TempLine, TempEllipse):
    def show(self):
        line = TempLine(self.canvas, self._x1, self._y1, self._x2, self._y2)
        circle_start_id = self.create_circle(self._x1, self._y1)
        circle_end_id = self.create_circle(self._x2, self._y2)
        
        return line.show(), circle_start_id, circle_end_id

    def create_circle(self, x, y, radius=10):
        circle = TempEllipse(self.canvas, x - radius, y - radius, x + radius, y + radius)
        return circle.show()
