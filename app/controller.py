from tkinter import Frame
from app.utils import error_handler
from app.video_controller import VideoController
from .frames import (SelectPacientFrame,
                     PacientDataFrame,
                     SelectImageInputFrame,
                     VideoAnalisisFrame,
                     WebcamImageInputFrame)

class Controller:
    def __init__(self, root):
        self.root = root
        self.frames : dict[str, Frame] = {
            SelectPacientFrame.__name__ : SelectPacientFrame(parent=root, controller=self),
            PacientDataFrame.__name__ : PacientDataFrame(parent=root, controller=self)
        }
        self.show_frame("SelectPacientFrame")
        self.current_user=None
        self.current_pacient=None

    @error_handler
    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames[page_name]
        frame.pack(fill='both', expand=1)