from shapes_utils.shape_editor.shape_editor import ShapeEditor
from shapes_utils.figure_shapes.line_shape import LineShape


class LineEditor(ShapeEditor):
    def draw_temp_shape(self, event):
        if not self.check_coordinates():
            return
        return self.canvas.create_line(
            self.x1, self.y1, event.x, event.y, fill="grey", dash=(4, 2)
        )

    def on_button_release(self, event):
        if not self.check_coordinates():
            return
        super().on_button_release(event)
        line = LineShape(self.canvas, self.x1, self.y1, event.x, event.y)
        line.show()
        self.all_shapes.append(line)
