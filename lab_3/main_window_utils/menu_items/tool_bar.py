from tkinter import ttk


class ToolBar:
    def __init__(self, root, main_window):
        self._root = root
        self._main_window = main_window

        self.toolbar_frame = ttk.Frame(root, padding="2 2 2 2")
        self.toolbar_frame.pack(side="top", fill="x")

        self.create_tool_bar_items()

        self.create_point = PointBtn(self.toolbar_frame, main_window, "Point")
        self.create_point.create()

    def create_tool_bar_items(self):
        self.line_button = ttk.Button(self.toolbar_frame, text="Line",
                                      command=lambda: self._main_window._select_figure("Line"))
        self.line_button.pack(side="left", padx=5)

        self.rectangle_button = ttk.Button(self.toolbar_frame, text="Square",
                                           command=lambda: self._main_window._select_figure("Square"))
        self.rectangle_button.pack(side="left", padx=5)

        self.ellipse_button = ttk.Button(self.toolbar_frame, text="Ellipse",
                                         command=lambda: self._main_window._select_figure("Ellipse"))
        self.ellipse_button.pack(side="left", padx=5)


class PointBtn:
    def __init__(self, frame, main_window, name):
        self._frame = frame
        self._main_window = main_window
        self._name = name

    def create(self):
        point_button = ttk.Button(self._frame, text=self._name,
                                  command=lambda: self._main_window._select_figure("Point"))
        point_button.pack(side="left", padx=5)
