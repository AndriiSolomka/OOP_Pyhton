from lab_2.shapes_utils.figure_shapes.ellipse_shape import EllipseShape
from lab_2.shapes_utils.shape_editor.shape_editor import ShapeEditor
from lab_2.shapes_utils.temp_shapes.temp_ellipse import TempEllipse


class EllipseEditor(ShapeEditor):

    def draw_temp_shape(self, event):
        if not self.check_coordinates():
            return

        dx = abs(self._x1 - event.x)
        dy = abs(self._y1 - event.y)

        temp_ellipse = TempEllipse(
            self._canvas,
            self._x1 - dx,
            self._y1 - dy,
            self._x1 + dx,
            self._y1 + dy,
        )
        return temp_ellipse.show()

    def draw_shape(self):
        if not self.check_coordinates():
            return

        dx = abs(self._x1 - self._x2)
        dy = abs(self._y1 - self._y2)

        ellipse = EllipseShape(
            self._canvas, self._x1 - dx, self._y1 - dy, self._x1 + dx, self._y1 + dy
        )
        self._all_shapes.append(ellipse)
        self._shape_object_editor.redraw_all_shapes()
