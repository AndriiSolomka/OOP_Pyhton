from tkinter import ttk

from PIL import Image, ImageTk

from lab_4.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_4.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class SquareBtn(BaseFrame):

    def create_btn(self):
        image = Image.open("main_window_utils/toolbar/img/square.png")
        resized_image = image.resize((40, 40), Image.Resampling.LANCZOS)
        square_image = ImageTk.PhotoImage(resized_image)

        square_button = ttk.Button(self._frame, image=square_image,
                                   command=lambda: self._main_window._select_figure("Square"))

        square_button.image = square_image
        square_button.pack(side="left", padx=5)
        ToolTip(square_button, "Square")
