from lab_5.tables.coords_table.handlers.events_handler import TableEventHandler
from lab_5.tables.coords_table.modal_window.modal_window import ModalWindow
from lab_5.tables.coords_table.table_creators.create_btn import CreateBtn
from lab_5.tables.coords_table.table_creators.create_table import CreateTable


class CoordsTable(ModalWindow):
    def create_window(self):
        self.table_manager = CreateTable(self.root)
        self.table_manager.create_table()
        self.button_manager = CreateBtn(self.root, self.table_manager)
        self.button_manager.create_save_button()
        self.event_handler = TableEventHandler(self.table_manager.table, self.event_manager)
        self.event_handler.bind_events()

    def update(self, new_coords):
        self.table_manager.update_table(new_coords)
