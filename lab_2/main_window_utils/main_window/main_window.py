import tkinter as tk

from main_window_utils.menu_bar.menu_bar import MenuBar
from shapes_utils.shapeObjectsEditor.shapeObjectsEditor import ShapeObjectsEditor


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab 2")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.menu_bar = MenuBar(self.root, self)
        self.shape_editor = ShapeObjectsEditor(self.canvas)

    def select_figure(self, figure):
        self.shape_editor.clear_bindings()

        if figure == "Point":
            self.shape_editor.StartPointEditor()

        if figure == "Line":
            self.shape_editor.StartLineEditor()

        if figure == "Square":
            self.shape_editor.StartSquareEditor()

        if figure == "Ellipse":
            self.shape_editor.StartEllipseEditor()
