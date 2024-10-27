from tkinter import ttk

from PIL import Image, ImageTk

from lab_3.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_3.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class EllipseBtn(BaseFrame):

    def create_btn(self):
        image = Image.open("main_window_utils/toolbar/img/ellipse.png")
        resized_image = image.resize((40, 40), Image.Resampling.LANCZOS)
        ellipse_image = ImageTk.PhotoImage(resized_image)

        ellipse_button = ttk.Button(self._frame, image=ellipse_image,
                                    command=lambda: self._main_window.select_figure("Ellipse"))

        ellipse_button.image = ellipse_image
        ellipse_button.pack(side="left", padx=5)
        ToolTip(ellipse_button, "Ellipse")
