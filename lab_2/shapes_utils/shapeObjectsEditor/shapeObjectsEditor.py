from lab_2.shapes_utils.figures_editors.ellipse_editor import EllipseEditor
from lab_2.shapes_utils.figures_editors.line_editor import LineEditor
from lab_2.shapes_utils.figures_editors.point_editor import PointEditor
from lab_2.shapes_utils.figures_editors.square_editor import SquareEditor


class ShapeObjectsEditor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.all_shapes = []

    def clear_bindings(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def redraw_all_shapes(self):
        self.canvas.delete("all")
        for shape in self.all_shapes:
            shape.show()

    def start_point_editor(self):
        point_editor = PointEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", point_editor.on_button_press)

    def start_line_editor(self):
        line_editor = LineEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", line_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", line_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", line_editor.on_button_release)

    def start_square_editor(self):
        square_editor = SquareEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", square_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", square_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", square_editor.on_button_release)

    def start_ellipse_editor(self):
        ellipse_editor = EllipseEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", ellipse_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", ellipse_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", ellipse_editor.on_button_release)
