from abc import abstractmethod

from shapes_utils.editor.editor import Editor


class ShapeEditor(Editor):
    def __init__(self, canvas, all_shapes):
        self.canvas = canvas
        self.all_shapes = all_shapes
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.temp_item = None

    def on_button_press(self, event):
        self.x1, self.y1 = event.x, event.y

    def on_mouse_drag(self, event):
        if self.temp_item:
            self.canvas.delete(self.temp_item)
        self.temp_item = self.draw_temp_shape(event)

    def on_button_release(self, event):
        if self.temp_item:
            self.canvas.delete(self.temp_item)
        self.x2, self.y2 = event.x, event.y

    def check_coordinates(self):
        if self.x1 is None or self.y1 is None:
            return False
        return True

    @abstractmethod
    def draw_temp_shape(self, event):
        pass
