from shapes_utils.figures_editors.ellipse_editor import EllipseEditor
from shapes_utils.figures_editors.line_editor import LineEditor
from shapes_utils.figures_editors.point_editor import PointEditor
from shapes_utils.figures_editors.square_editor import SquareEditor


class ShapeObjectsEditor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.all_shapes = []

    def clear_bindings(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def StartPointEditor(self):
        self.point_editor = PointEditor(self.canvas, self.all_shapes)
        self.canvas.bind("<Button-1>", self.point_editor.on_button_press)
        

    def StartLineEditor(self):
        self.line_editor = LineEditor(self.canvas, self.all_shapes)
        self.canvas.bind("<Button-1>", self.line_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", self.line_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.line_editor.on_button_release)

    def StartSquareEditor(self):
        self.square_editor = SquareEditor(self.canvas, self.all_shapes)
        self.canvas.bind("<Button-1>", self.square_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", self.square_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.square_editor.on_button_release)

    def StartEllipseEditor(self):
        self.ellipse_editor = EllipseEditor(self.canvas, self.all_shapes)
        self.canvas.bind("<Button-1>", self.ellipse_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", self.ellipse_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.ellipse_editor.on_button_release)
