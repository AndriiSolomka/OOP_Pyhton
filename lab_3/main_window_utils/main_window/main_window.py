import tkinter as tk

from lab_3.main_window_utils.menu_bar.menu_bar import MenuBar
from lab_3.main_window_utils.toolbar.toolbar_menu import ToolBar
from lab_3.shapes_utils.shapeObjectsEditor.shapeObjectsEditor import ShapeObjectsEditor


class MainWindow:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Lab 3")
        self.__root.geometry("800x500")
        self.__root.resizable(False, False)

        # Tool Bar
        self.toolbar = ToolBar(self.__root, self)

        self.__canvas = tk.Canvas(root, bg="white")
        self.__canvas.pack(fill=tk.BOTH, expand=True)

        self.__menu_bar = MenuBar(self.__root, self)
        self.shape_editor = ShapeObjectsEditor(self.__canvas)

    def select_figure(self, figure):
        self.shape_editor.clear_bindings()
        self.__menu_bar.select_name(figure)

        if figure == "Point":
            self.shape_editor.start_point_editor()

        if figure == "Line":
            self.shape_editor.start_line_editor()

        if figure == "Square":
            self.shape_editor.start_square_editor()

        if figure == "Ellipse":
            self.shape_editor.start_ellipse_editor()
