from lab_4.shapes_utils.figures_editors.shapes_editor import ShapesEditor


class MyEditor:
    def __init__(self, canvas, event_manager):
        self.canvas = canvas
        self.all_shapes = []
        self.event_manager = event_manager
        self.event_manager.on('shape_clicked', self.do_light)
        self.event_manager.on('shape_delete', self.delete_item)

    def clear_bindings(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def redraw_all_shapes(self):
        self.event_manager.emit('shape_added')
        self.canvas.delete("all")
        for shape in self.all_shapes:
            shape.show('black')

    def start_editor(self, shape):
        editor = ShapesEditor(self.canvas, self.all_shapes, self, shape)
        self.canvas.bind("<Button-1>", editor.on_button_press)
        self.canvas.bind("<B1-Motion>", editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", editor.on_button_release)

    def do_light(self, item):
        for shape in self.all_shapes:
            shape_coords = tuple(map(str, shape.get_coordinates()))
            if all(c in shape_coords for c in item):
                self.redraw_all_shapes()
                shape.show('red')

    def delete_item(self, item):
        for shape in self.all_shapes:
            shape_coords = tuple(map(str, shape.get_coordinates()))
            if all(c in shape_coords for c in item):
                self.all_shapes.remove(shape)
                self.redraw_all_shapes()
