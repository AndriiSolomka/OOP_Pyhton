from lab_4.shapes_utils.figure_shapes.line_shape import LineShape
from lab_4.shapes_utils.figure_shapes.square_shape import SquareShape


class CubeShape(LineShape, SquareShape):
    def show(self, color):
        original_coords = (self._x1, self._y1, self._x2, self._y2)

        size = abs(self._x2 - self._x1)
        height = abs(self._y2 - self._y1)

        self._x1, self._y1 = original_coords[0], original_coords[1]
        self._x2, self._y2 = original_coords[0] + size, original_coords[1] + height

        SquareShape.show(self, color)

        offset_x = size / 3  #
        offset_y = height / 3

        self._x1 = original_coords[0] + offset_x
        self._y1 = original_coords[1] - offset_y
        self._x2 = self._x1 + size
        self._y2 = self._y1 + height

        SquareShape.show(self, color)

        self.draw_line(original_coords[0], original_coords[1], self._x1, self._y1, color)
        self.draw_line(original_coords[0] + size, original_coords[1], self._x1 + size, self._y1, color)
        self.draw_line(original_coords[0], original_coords[1] + height, self._x1,
                       self._y1 + height, color)
        self.draw_line(original_coords[0] + size, original_coords[1] + height, self._x1 + size,
                       self._y1 + height, color)

        self._x1, self._y1, self._x2, self._y2 = original_coords

    def draw_line(self, x1, y1, x2, y2, color):
        original_coords = (self._x1, self._y1, self._x2, self._y2)
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2
        LineShape.show(self, color)

        self._x1, self._y1, self._x2, self._y2 = original_coords
