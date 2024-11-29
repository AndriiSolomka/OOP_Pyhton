from abc import ABC, abstractmethod


class Editor(ABC):
    @abstractmethod
    def on_button_press(self, event):
        pass

    @abstractmethod
    def on_button_release(self, event):
        pass

    @abstractmethod
    def on_mouse_drag(self, event):
        pass
