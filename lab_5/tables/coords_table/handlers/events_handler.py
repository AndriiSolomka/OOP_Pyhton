from tkinter import messagebox


class TableEventHandler:
    def __init__(self, table, event_manager):
        self.table = table
        self.event_manager = event_manager

    def bind_events(self):
        self.table.bind("<Button-1>", self.on_left_click)
        self.table.bind("<Button-3>", self.on_right_click)

    def on_left_click(self, event):
        selected_item = self.table.identify_row(event.y)
        if selected_item:
            item_values = self.table.item(selected_item, 'values')
            self.event_manager.emit('shape_clicked', item_values)

    def on_right_click(self, event):
        selected_item = self.table.identify_row(event.y)
        if selected_item:
            item_values = self.table.item(selected_item, 'values')
            self.ask_to_delete(item_values)

    def ask_to_delete(self, item_values):
        result = messagebox.askyesno("Access", "Delete?")
        if result:
            self.event_manager.emit('shape_delete', item_values)
