import tkinter as tk

from lab_4.main_window_utils.menu_bar.menu_bar import MenuBar
from lab_4.main_window_utils.toolbar.toolbar_menu import ToolBar
from lab_4.shapes_utils.MyEditor.myEditor import MyEditor
from lab_4.tables.table_cords import CoordsTable


class MainWindow:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Lab 4")
        self.__root.geometry("800x500")
        self.__root.resizable(False, False)

        # Tool Bar
        self.toolbar = ToolBar(self.__root, self)

        self.__canvas = tk.Canvas(root, bg="white")
        self.__canvas.pack(fill=tk.BOTH, expand=True)

        self.__menu_bar = MenuBar(self.__root, self)
        self.my_editor = MyEditor(self.__canvas)

        # Table
        self.coords_table = None

    def get_all_shapes_coords(self):
        return self.my_editor.shapes_coords

    def select_table(self, table):
        coords = self.get_all_shapes_coords()

        if self.coords_table is None or not self.coords_table.root.winfo_exists():
            if table == "Coords":
                self.coords_table = CoordsTable(self.__root, coords)

    def select_figure(self, figure):
        self.my_editor.clear_bindings()
        self.__menu_bar.select_name(figure)
        self.my_editor.start_editor(figure)
