class EventManagerHandler:
    def __init__(self, event_manager, editor):
        self.event_manager = event_manager
        self.editor = editor

        self.event_manager.on('shape_clicked', self.highlight_shape)
        self.event_manager.on('shape_delete', self.delete_shape)

    def emit_shape_added(self):
        self.event_manager.emit('shape_added')

    def highlight_shape(self, item):
        for shape in self.editor.all_shapes:
            shape_coords = tuple(map(str, shape.get_coordinates()))
            if all(c in shape_coords for c in item):
                self.editor.redraw_all_shapes()
                shape.show('red')

    def delete_shape(self, item):
        for shape in self.editor.all_shapes:
            shape_coords = tuple(map(str, shape.get_coordinates()))
            if all(c in shape_coords for c in item):
                self.editor.all_shapes.remove(shape)
                self.editor.redraw_all_shapes()
