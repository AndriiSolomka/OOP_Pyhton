from tkinter import ttk

from PIL import Image, ImageTk

from lab_3.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_3.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class PointBtn(BaseFrame):
    def create_btn(self):
        # Загрузка изображения
        image = Image.open("path/to/your/point_image.png")
        image = image.resize((20, 20), Image.ANTIALIAS)
        self.point_image = ImageTk.PhotoImage(image)

        point_button = ttk.Button(self._frame, image=self.point_image,
                                  command=lambda: self._main_window.select_figure("Point"))
        point_button.pack(side="left", padx=5)

        ToolTip(point_button, "Point")
