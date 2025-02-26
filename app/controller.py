from tkinter import Frame
from app.utils import error_handler
from app.video_controller import VideoController
from .frames import (SelectPacientFrame,
                     PacientDataFrame,
                     SelectImageInputFrame,
                     VideoAnalisisFrame,
                     WebcamImageInputFrame,
                     PacientInfoFrame,
                     HeaderMenuFrame)

class Controller:
    def __init__(self, root):
        self.root = root
        self.current_user=None
        self.current_pacient=None
        self.video_controller = VideoController()
        self.frames : dict[str, Frame] = {
            SelectPacientFrame.__name__ : SelectPacientFrame(parent=root, controller=self),
            PacientDataFrame.__name__ : PacientDataFrame(parent=root, controller=self),
            SelectImageInputFrame.__name__ : SelectImageInputFrame(parent=root, controller=self),
            VideoAnalisisFrame.__name__ : VideoAnalisisFrame(parent=root, controller=self),
            WebcamImageInputFrame.__name__ : WebcamImageInputFrame(parent=root, controller=self),
            PacientInfoFrame.__name__ : PacientInfoFrame(parent=root, controller=self)
        }
        HeaderMenuFrame(self.root, self).pack(side="top", fill="x")
        self.show_frame("SelectPacientFrame")

    @error_handler
    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.pack_forget()
            # frame.on_pack_forget()
        frame = self.frames[page_name]
        frame.pack(fill='both', expand=1)
        # TODO: all frames should have an in and out method to call when the frame is shown or hidden
        # TODO: create a father class for all frames to inherit from, this class should have the in and out methods and the on_pack_forget and on_pack_show methods
        # Consider the option of adding mixins as well
        # The main purpose of defining this callback is to changue the size of the window on the PacientInfoFrame but this approach will be more generic for future possible use cases 
        # frame.on_pack_show()