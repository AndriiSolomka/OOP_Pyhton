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
        self.__menu_bar.create_menu()
        self.my_editor = MyEditor(self.__canvas)

        # Table
        self.my_editor.event_manager.on('shape_added', self.emmit_table_cords)
        self.coords_table = None

    def emmit_table_cords(self):
        if self.coords_table:
            self.coords_table.update(self.my_editor.shapes_coords)

    def select_table(self, table):
        if table == "Coords":
            self.coords_table = CoordsTable(self.__root, self.my_editor.shapes_coords)

    def select_figure(self, figure):
        self.my_editor.clear_bindings()
        # self.__menu_bar.select_name(figure)
        self.my_editor.start_editor(figure)
