import csv
from tkinter import filedialog


class CSVReader:
    def __init__(self):
        self.rows = []

    def open_file(self):

        file_path = filedialog.askopenfilename(
            title="Chose CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not file_path:
            print("File not found.")
            return

        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.rows = [tuple(row) for row in reader]
        except Exception as e:
            print(f"Error while reading file: {e}")

    def get_rows(self):
        return self.rows
