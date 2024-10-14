from tkinter import ttk

from PIL import Image, ImageTk

from lab_3.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_3.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class LineBtn(BaseFrame):
    def create_btn(self):
        image = Image.open("main_window_utils/toolbar/img/line.png")
        resized_image = image.resize((40, 40), Image.Resampling.LANCZOS)
        line_image = ImageTk.PhotoImage(resized_image)

        line_button = ttk.Button(self._frame, image=line_image,
                                 command=lambda: self._main_window.select_figure("Line"))

        line_button.image = line_image
        line_button.pack(side="left", padx=5)
        ToolTip(line_button, "Line")
