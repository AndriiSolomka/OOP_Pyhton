from lab_4.shapes_utils.figures_editors.shapes_editor import ShapesEditor


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

    def start_editor(self, shape):
        print(shape)
        editor = ShapesEditor(self.canvas, self.all_shapes, self, shape)
        self.canvas.bind("<Button-1>", editor.on_button_press)
        self.canvas.bind("<B1-Motion>", editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", editor.on_button_release)
