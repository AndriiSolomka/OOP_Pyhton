from lab_5.CSVReader.csv_reader import CSVReader


class CSVHandler:

    def __init__(self, shape_manager):
        self.shape_manager = shape_manager

    def load_shapes_from_csv(self):
        csv_reader = CSVReader()
        csv_reader.open_file()
        rows = csv_reader.get_rows()

        for row in rows[1:]:
            figure_name = row[0]
            coordinates = tuple(map(int, row[1:]))
            self.shape_manager.add_shape(figure_name, coordinates)
