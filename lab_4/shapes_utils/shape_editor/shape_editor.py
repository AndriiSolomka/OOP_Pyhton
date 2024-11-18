from abc import abstractmethod

from lab_4.shapes_utils.editor.editor import Editor


class ShapeEditor(Editor):
    def __init__(self, canvas, all_shapes, shape_object_editor, shape):
        self._canvas = canvas
        self.shape = shape
        self._all_shapes = all_shapes
        self._shape_object_editor = shape_object_editor
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._temp_item = None

    def on_button_press(self, event):
        self._x1, self._y1 = event.x, event.y

    def on_mouse_drag(self, event):
        self.delete_temp_item()
        self._temp_item = self.draw_temp_shape(event, self.shape)

    def delete_temp_item(self):
        if not self._temp_item:
            return

        items = self._temp_item if isinstance(self._temp_item, tuple) else [self._temp_item]
        for item in items:
            self._canvas.delete(item)

    def on_button_release(self, event):
        if self._temp_item:
            self._canvas.delete(self._temp_item)
        self._x2, self._y2 = event.x, event.y
        self.draw_shape(self.shape)

    def check_coordinates(self):
        if self._x1 is None or self._y1 is None:
            return False
        return True

    @abstractmethod
    def draw_temp_shape(self, event, shape):
        pass

    @abstractmethod
    def draw_shape(self, shape):
        pass
