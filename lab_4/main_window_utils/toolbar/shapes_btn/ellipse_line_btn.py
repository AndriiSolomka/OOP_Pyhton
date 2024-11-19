from tkinter import ttk

from PIL import Image, ImageTk

from lab_4.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_4.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class EllipseLineBtn(BaseFrame):

    def create_btn(self):
        image = Image.open("main_window_utils/toolbar/img/ellipse_line.png")
        resized_image = image.resize((40, 40), Image.Resampling.LANCZOS)
        ellipse_line_image = ImageTk.PhotoImage(resized_image)

        ellipse_line_button = ttk.Button(self._frame, image=ellipse_line_image,
                                         command=lambda: self._main_window._select_figure("EllipseLine"))

        ellipse_line_button.image = ellipse_line_image
        ellipse_line_button.pack(side="left", padx=5)
        ToolTip(ellipse_line_button, "EllipseLine")
