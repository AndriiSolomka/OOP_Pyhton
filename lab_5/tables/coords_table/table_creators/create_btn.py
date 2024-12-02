from tkinter import ttk

from lab_5.tables.coords_table.handlers.csv_hendler import CSVCoordsTableHandler


class CreateBtn:
    def __init__(self, root, table_manager):
        self.root = root
        self.table_manager = table_manager

    def create_save_button(self):
        save_button = ttk.Button(self.root, text="Save CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

    def save_to_csv(self):
        csv_handler = CSVCoordsTableHandler()
        csv_handler.save_to_csv(self.table_manager.table)
