from tkinter import ttk

from lab_4.main_window_utils.toolbar.shapes_btn.cube_btn import CubeBtn
from lab_4.main_window_utils.toolbar.shapes_btn.ellipse_btn import EllipseBtn
from lab_4.main_window_utils.toolbar.shapes_btn.ellipse_line_btn import EllipseLineBtn
from lab_4.main_window_utils.toolbar.shapes_btn.line_btn import LineBtn
from lab_4.main_window_utils.toolbar.shapes_btn.point_btn import PointBtn
from lab_4.main_window_utils.toolbar.shapes_btn.square_btn import SquareBtn


class ToolBar:
    def __init__(self, root, main_window):
        self._root = root
        self._main_window = main_window
        self.toolbar_frame = ttk.Frame(root, padding="2 2 2 2")
        self.toolbar_frame.pack(side="top", fill="x")

        self.buttons = [
            (PointBtn, "Point"),
            (LineBtn, "Line"),
            (SquareBtn, "Square"),
            (EllipseBtn, "Ellipse"),
            (EllipseLineBtn, "Ellipse Line"),
            (CubeBtn, "Cube")
        ]

        self.create_buttons()

    def create_buttons(self):
        for button_class, button_name in self.buttons:
            btn_instance = button_class(self.toolbar_frame, self._main_window, button_name)
            btn_instance.create_btn()
