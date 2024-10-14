from lab_2.shapes_utils.figure_shapes.line_shape import LineShape
from lab_2.shapes_utils.shape_editor.shape_editor import ShapeEditor
from lab_2.shapes_utils.temp_shapes.temp_line import TempLine


class LineEditor(ShapeEditor):
    def draw_temp_shape(self, event):
        if not self.check_coordinates():
            return
        temp_line = TempLine(self._canvas, self._x1, self._y1, event.x, event.y)
        return temp_line.show()

    def draw_shape(self):
        if not self.check_coordinates():
            return

        line = LineShape(self._canvas, self._x1, self._y1, self._x2, self._y2)
        self._all_shapes.append(line)
        self._shape_object_editor.redraw_all_shapes()
