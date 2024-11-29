from lab_5.shapes_utils.figures_editors.shape_factory import ShapeFactory
from lab_5.shapes_utils.shape_editor.shape_editor import ShapeEditor


class ShapesEditor(ShapeEditor):
    def draw_temp_shape(self, event, figure):
        if not self.check_coordinates():
            return

        temp_shape_class = ShapeFactory.get_temp_shape_class(self.shape)
        if temp_shape_class:
            temp_shape = temp_shape_class(figure, self._canvas, self._x1, self._y1, event.x, event.y)
            return temp_shape.show()

    def draw_shape(self, figure):
        if not self.check_coordinates():
            return

        shape_class = ShapeFactory.get_shape_class(self.shape)
        if shape_class:
            shape = shape_class(figure, self._canvas, self._x1, self._y1, self._x2, self._y2)
            self._all_shapes.append(shape)
            self._shape_object_editor.redraw_all_shapes()
