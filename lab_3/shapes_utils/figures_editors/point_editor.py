from lab_3.shapes_utils.figure_shapes.point_shape import PointShape
from lab_3.shapes_utils.shape_editor.shape_editor import ShapeEditor


class PointEditor(ShapeEditor):
    def on_button_press(self, event):
        point = PointShape(self._canvas, event.x, event.y)
        self._all_shapes.append(point)
        self._shape_object_editor.redraw_all_shapes()

    def draw_temp_shape(self, event):
        pass

    def draw_shape(self):
        pass
