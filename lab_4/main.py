import tkinter as tk

from lab_4.main_window_utils.main_window.main_window import MainWindow


class Paint:
    def __init__(self):
        self.__root = tk.Tk()
        self.__app = MainWindow(self.__root)
        self.__root.mainloop()


if __name__ == "__main__":
    Paint()
    
