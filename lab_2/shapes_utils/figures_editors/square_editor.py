from shapes_utils.shape_editor.shape_editor import ShapeEditor
from shapes_utils.figure_shapes.square_shape import SquareShape


class SquareEditor(ShapeEditor):

    def draw_temp_shape(self, event):
        if not self.check_coordinates():
            return
        return self.canvas.create_rectangle(
            self.x1, self.y1, event.x, event.y, outline="grey", dash=(4, 2)
        )

    def on_button_release(self, event):
        if not self.check_coordinates():
            return
        super().on_button_release(event)
        square = SquareShape(self.canvas, self.x1, self.y1, event.x, event.y)
        square.show()
        self.all_shapes.append(square)
