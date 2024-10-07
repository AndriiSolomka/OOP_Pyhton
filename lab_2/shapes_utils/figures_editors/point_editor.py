from shapes_utils.figure_shapes.point_shape import PointShape
from shapes_utils.shape_editor.shape_editor import ShapeEditor


class PointEditor(ShapeEditor):
    def on_button_press(self, event):
        point = PointShape(self.canvas, event.x, event.y)
        point.show()
        self.all_shapes.append(point)

    def draw_temp_shape(self):
        pass
