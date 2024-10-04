import tkinter as tk

from constants import slider_const as const


def open_slider():

    CHOSEN_VALUE = None

    def on_confirm():
        nonlocal CHOSEN_VALUE
        CHOSEN_VALUE = scale.get()
        root.destroy()

    def on_cancel():
        root.destroy()

    def on_closing():
        root.destroy()

    root = tk.Tk()
    root.title(const.TITLE)
    root.geometry(const.GEOMETRY)
    root.resizable(width=False, height=False)

    label_text_info = tk.Label(
        root, width=const.LABEL_WIDTH, font=const.FONT, text=const.LABEL_TEXT
    )
    label_text_info.pack(pady=const.LABEL_PADY)

    scale = tk.Scale(
        root,
        from_=const.START,
        to=const.FINAL,
        orient=tk.HORIZONTAL,
        length=const.LENGTH,
    )
    scale.pack()

    btn_access = tk.Button(
        root,
        text=const.ACCESS_BTN_TEXT,
        font=const.FONT,
        width=const.ACCESS_BTN_WIDTH,
        command=on_confirm,
    )
    btn_access.place(x=const.ACCESS_BTN_X, y=const.ACCESS_BTN_Y)

    btn_cancel = tk.Button(
        root,
        text=const.CANCEL_BTN_TEXT,
        font=const.FONT,
        width=const.CANCEL_BTN_WIDTH,
        command=on_cancel,
    )
    btn_cancel.place(x=const.CANCEL_BTN_X, y=const.CANCEL_BTN_Y)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.wait_window()

    return CHOSEN_VALUE
