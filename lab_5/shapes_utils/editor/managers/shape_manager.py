from lab_5.shapes_utils.figures_editors.shape_factory import ShapeFactory


class ShapeManager:
    def __init__(self, canvas, all_shapes):
        self.canvas = canvas
        self.all_shapes = all_shapes
        self.shape_factory = ShapeFactory()

    def draw_all_shapes(self, color):
        for shape in self.all_shapes:
            shape.show(color)

    def add_shape(self, figure_name, coordinates):
        shape_class = self.shape_factory.get_shape_class(figure_name)
        if shape_class:
            shape_instance = shape_class(figure_name, self.canvas, *coordinates)
            self.all_shapes.append(shape_instance)
            shape_instance.show('black')
