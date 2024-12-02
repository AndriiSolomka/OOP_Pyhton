from lab_5.tables.coords_table.table_cords import CoordsTable


class TableManager:

    def __init__(self, root, event_manager, my_editor):
        self.root = root
        self.event_manager = event_manager
        self.my_editor = my_editor
        self.coords_table = None
        self.event_manager.on('shape_added', self.update_table)

    def create_table(self):
        if self.coords_table and self.coords_table.is_active:
            return
        self.coords_table = CoordsTable(self.root, self.event_manager)
        self.update_table()

    def update_table(self):
        if self.coords_table:
            self.coords_table.update(self.my_editor.all_shapes)
