import tkinter as tk

from lab_5.main_window_utils.event_manager.event_emmiter import EventManager
from lab_5.main_window_utils.menu_bar.menu_bar import MenuBar
from lab_5.main_window_utils.table_manager.table_manager import TableManager
from lab_5.main_window_utils.toolbar.toolbar_menu import ToolBar
from lab_5.shapes_utils.MyEditor.myEditor import MyEditor


class MainWindow:
    def __init__(self, root):
        self.__root = root
        self.__setup_window()

        self.toolbar = ToolBar(self.__root, self)
        self.canvas = self.__setup_canvas()
        self.menu_bar = self.__setup_menu_bar()

        self.event_manager = EventManager()
        self.my_editor = MyEditor(self.canvas, self.event_manager)
        self.table_manager = TableManager(self.__root, self.event_manager, self.my_editor)

    def __setup_window(self):
        self.__root.title("Lab 4")
        self.__root.geometry("800x500")
        self.__root.resizable(False, False)

    def __setup_canvas(self):
        canvas = tk.Canvas(self.__root, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)
        return canvas

    def __setup_menu_bar(self):
        menu_bar = MenuBar(self.__root, self)
        menu_bar.create_menu()
        return menu_bar

    def _create_table(self):
        self.table_manager.create_table()

    def _select_figure(self, figure):
        self.my_editor.clear_bindings()
        self.my_editor.start_editor(figure)

    def _read_csv(self):
        self.my_editor.read_csv()
