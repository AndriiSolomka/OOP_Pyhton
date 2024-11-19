from tkinter import ttk

from PIL import Image, ImageTk

from lab_3.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_3.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class PointBtn(BaseFrame):
    def create_btn(self):
        image = Image.open("main_window_utils/toolbar/img/point.png")
        resized_image = image.resize((40, 40), Image.Resampling.LANCZOS)
        point_image = ImageTk.PhotoImage(resized_image)

        point_button = ttk.Button(self._frame, image=point_image,
                                  command=lambda: self._main_window._select_figure("Point"))

        point_button.image = point_image
        point_button.pack(side="left", padx=5)
        ToolTip(point_button, "Point")
