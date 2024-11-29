from tkinter import ttk

from PIL import Image, ImageTk
from lab_5.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_5.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class CubeBtn(BaseFrame):

    def create_btn(self):
        image = Image.open("main_window_utils/toolbar/img/cube.png")
        resized_image = image.resize((40, 40), Image.Resampling.LANCZOS)
        cube_image = ImageTk.PhotoImage(resized_image)

        cube_button = ttk.Button(self._frame, image=cube_image,
                                 command=lambda: self._main_window._select_figure("Cube"))

        cube_button.image = cube_image
        cube_button.pack(side="left", padx=5)
        ToolTip(cube_button, "Cube")
