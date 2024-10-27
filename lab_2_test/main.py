import tkinter as tk

from classes import ShapeObjectsEditor


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab 2")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.menu = self.create_menu()
        self.root.config(menu=self.menu)

        self.shape_editor = ShapeObjectsEditor(self.canvas)

    def create_menu(self):
        menu = tk.Menu(self.root)
        tabs_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Objects", menu=tabs_menu)

        tabs_menu.add_command(
            label="Point",
            command=lambda: self.select_figure("Point"),
        )

        tabs_menu.add_command(
            label="Line",
            command=lambda: self.select_figure("Line"),
        )

        tabs_menu.add_command(
            label="Square",
            command=lambda: self.select_figure("Square"),
        )

        tabs_menu.add_command(
            label="Ellipse",
            command=lambda: self.select_figure("Ellipse"),
        )

        return menu

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


if __name__ == "__main__":

    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
