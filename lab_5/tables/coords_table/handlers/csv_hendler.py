import csv
from tkinter import filedialog
from tkinter import messagebox


class CSVCoordsTableHandler:
    def save_to_csv(self, table):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if not file_path:
            return

        rows = [table.item(item, 'values') for item in table.get_children()]
        headers = table['columns']

        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)
            messagebox.showinfo("Save CSV", f"Data saved successfully: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")
