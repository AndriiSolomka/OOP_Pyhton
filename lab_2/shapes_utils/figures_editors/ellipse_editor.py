from shapes_utils.shape_editor.shape_editor import ShapeEditor
from shapes_utils.figure_shapes.ellipse_shape import EllipseShape


class EllipseEditor(ShapeEditor):

    def draw_temp_shape(self, event):
        if not self.check_coordinates():
            return

        dx = abs(self.x1 - event.x)
        dy = abs(self.y1 - event.y)

        return self.canvas.create_oval(
            self.x1 - dx,
            self.y1 - dy,
            self.x1 + dx,
            self.y1 + dy,
            outline="grey",
            dash=(4, 2),
        )

    def on_button_release(self, event):
        if not self.check_coordinates():
            return

        super().on_button_release(event)
        dx = abs(self.x1 - event.x)
        dy = abs(self.y1 - event.y)
        ellipse = EllipseShape(
            self.canvas, self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy
        )
        ellipse.show()
        self.all_shapes.append(ellipse)
