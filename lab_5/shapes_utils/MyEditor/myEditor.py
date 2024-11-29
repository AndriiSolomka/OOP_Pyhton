from lab_5.shapes_utils.editor.managers.CSV_handler import CSVHandler
from lab_5.shapes_utils.editor.managers.event_manager import EventManagerHandler
from lab_5.shapes_utils.editor.managers.shape_manager import ShapeManager
from lab_5.shapes_utils.figures_editors.shapes_editor import ShapesEditor


class MyEditor:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, canvas, event_manager):
        if not hasattr(self, "initialized"):
            self.canvas = canvas
            self.all_shapes = []
            self.event_manager = EventManagerHandler(event_manager, self)
            self.shape_manager = ShapeManager(canvas, self.all_shapes)
            self.csv_handler = CSVHandler(self.shape_manager)
            self.initialized = True

    def clear_bindings(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def redraw_all_shapes(self):
        self.event_manager.emit_shape_added()
        self.canvas.delete("all")
        self.shape_manager.draw_all_shapes('black')

    def start_editor(self, shape):
        editor = ShapesEditor(self.canvas, self.all_shapes, self, shape)
        self.canvas.bind("<Button-1>", editor.on_button_press)
        self.canvas.bind("<B1-Motion>", editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", editor.on_button_release)

    def read_csv(self):
        self.csv_handler.load_shapes_from_csv()
