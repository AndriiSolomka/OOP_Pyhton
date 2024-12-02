import tkinter as tk
from tkinter import ttk


class CreateTable:
    def __init__(self, root):

        self.root = root
        self.table = None

    def create_table(self):
        self.root.title("Coords Table")
        heads = ['Name', 'X1', 'X2', 'Y1', 'Y2']
        self.table = ttk.Treeview(self.root, show='headings', columns=heads)

        for header in heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center')

        scroll_pane = ttk.Scrollbar(self.root, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)

    def update_table(self, new_coords):
        if not self.table.winfo_exists():
            return

        for item in self.table.get_children():
            self.table.delete(item)

        for row in new_coords:
            self.table.insert('', tk.END, values=row.get_coordinates())
