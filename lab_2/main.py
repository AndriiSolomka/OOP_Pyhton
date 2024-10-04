import tkinter as tk

from main_window_utils.main_window.main_window import MainWindow


class Paint:
    def __init__(self):
        self.root = tk.Tk()
        self.app = MainWindow(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    Paint()
