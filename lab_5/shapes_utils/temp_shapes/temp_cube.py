from lab_5.shapes_utils.temp_shapes.temp_line import TempLine
from lab_5.shapes_utils.temp_shapes.temp_square import TempSquare


class TempCube(TempLine, TempSquare):
    def show(self):
        original_coords = (self._x1, self._y1, self._x2, self._y2)

        size = abs(self._x2 - self._x1)
        height = abs(self._y2 - self._y1)

        self._x1, self._y1 = original_coords[0], original_coords[1]
        self._x2, self._y2 = original_coords[0] + size, original_coords[1] + height
        square_1 = TempSquare.show(self)

        offset_x = size / 3
        offset_y = height / 3

        self._x1 = original_coords[0] + offset_x
        self._y1 = original_coords[1] - offset_y
        self._x2 = self._x1 + size
        self._y2 = self._y1 + height
        square_2 = TempSquare.show(self)

        line_1 = self.draw_line(original_coords[0], original_coords[1],
                                self._x1, self._y1)
        line_2 = self.draw_line(original_coords[0] + size, original_coords[1],
                                self._x1 + size, self._y1)
        line_3 = self.draw_line(original_coords[0], original_coords[1] + height,
                                self._x1, self._y1 + height)
        line_4 = self.draw_line(original_coords[0] + size, original_coords[1] + height,
                                self._x1 + size, self._y1 + height)

        self._x1, self._y1, self._x2, self._y2 = original_coords

        return line_1, line_2, line_3, line_4, square_1, square_2

    def draw_line(self, x1, y1, x2, y2):
        original_coords = (self._x1, self._y1, self._x2, self._y2)
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2
        line = TempLine.show(self)

        self._x1, self._y1, self._x2, self._y2 = original_coords

        return line
