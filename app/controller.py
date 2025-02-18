from tkinter import Frame
from .frames import SelectPacientFrame

class Controller:
    def __init__(self, root):
        self.root = root
        self.frames : dict[str, Frame] = {
            SelectPacientFrame.__name__ : SelectPacientFrame(parent=root, controller=self)
        }
        self.show_frame("SelectPacientFrame")

    def show_frame(self, page_name):
        frame:Frame = self.frames[page_name]
        frame.tkraise()