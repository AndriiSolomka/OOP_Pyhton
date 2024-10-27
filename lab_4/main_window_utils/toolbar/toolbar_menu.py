from tkinter import ttk

from lab_4.main_window_utils.toolbar.shapes_btn.ellipse_btn import EllipseBtn
from lab_4.main_window_utils.toolbar.shapes_btn.line_btn import LineBtn
from lab_4.main_window_utils.toolbar.shapes_btn.point_btn import PointBtn
from lab_4.main_window_utils.toolbar.shapes_btn.square_btn import SquareBtn


class ToolBar:
    def __init__(self, root, main_window):
        self._root = root
        self._main_window = main_window

        self.toolbar_frame = ttk.Frame(root, padding="2 2 2 2")
        self.toolbar_frame.pack(side="top", fill="x")

        # Make Point btn
        self.point_btn = PointBtn(self.toolbar_frame, main_window, "Point")
        self.point_btn.create_btn()

        # Make Line btn
        self.line_btn = LineBtn(self.toolbar_frame, main_window, "Line")
        self.line_btn.create_btn()

        # Make Square btn
        self.square_btn = SquareBtn(self.toolbar_frame, main_window, "Square")
        self.square_btn.create_btn()

        # Make Ellipse btn
        self.ellipse_btn = EllipseBtn(self.toolbar_frame, main_window, "Ellipse")
        self.ellipse_btn.create_btn()
