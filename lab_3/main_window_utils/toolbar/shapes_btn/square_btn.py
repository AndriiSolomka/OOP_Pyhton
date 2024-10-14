from tkinter import ttk

from lab_3.main_window_utils.toolbar.base_frame.base_frame import BaseFrame
from lab_3.main_window_utils.toolbar.tool_lip.tool_lip import ToolTip


class SquareBtn(BaseFrame):

    def create_btn(self):
        square_button = ttk.Button(self._frame, text=self._name,
                                   command=lambda: self._main_window.select_figure("Square"))
        square_button.pack(side="left", padx=5)

        ToolTip(square_button, "Square")
