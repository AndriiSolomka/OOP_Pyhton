import tkinter as tk
from abc import abstractmethod


class ModalWindow:
    def __init__(self, parent, event_manager):
        self.root = tk.Toplevel(parent)
        self.event_manager = event_manager
        self.root.geometry("1000x500")
        self.is_active = True
        self.table_manager = None
        self.button_manager = None
        self.event_handler = None
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.create_window()

    @abstractmethod
    def create_window(self):
        pass

    def close_window(self):
        self.is_active = False
        self.root.destroy()
