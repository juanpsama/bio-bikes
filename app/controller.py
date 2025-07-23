from tkinter import Frame
from app.utils import error_handler
from app.video_controller import VideoController
from .frames import (
    SelectPacientFrame,
    PacientDataFrame,
    SelectImageInputFrame,
    VideoAnalisisFrame,
    WebcamImageInputFrame,
    PacientInfoFrame,
    HeaderMenu,
)


class Controller:
    def __init__(self, root):
        self.root = root
        self.current_user = None
        self.current_pacient = None
        self.width=900
        self.height=600
        self.root.geometry(f"{self.width}x{self.height}")

        self.video_controller = VideoController()

        self.frames: dict[str, Frame] = {
            SelectPacientFrame.__name__: SelectPacientFrame,
            PacientDataFrame.__name__: PacientDataFrame,
            SelectImageInputFrame.__name__: SelectImageInputFrame,
            VideoAnalisisFrame.__name__: VideoAnalisisFrame,
            WebcamImageInputFrame.__name__: WebcamImageInputFrame,
            PacientInfoFrame.__name__: PacientInfoFrame,
        }
        self.frames_stack = []
        # Creates the header menu
        self.header_menu = HeaderMenu(parent=root, controller=self, menu_frames=self.frames)
        # Set the header frame to appear in all frames header
        self.root.config(menu=self.header_menu)

        # Show the init frame
        self.show_frame("SelectPacientFrame")

    @error_handler
    def show_frame(self, page_name):
        for frame in self.frames_stack:
            frame.pack_forget()
            frame.on_pack_forget()
            del frame
        self.frames_stack.clear()
        
        frame = self.frames[page_name]
        frame_object = frame(self.root, self)
        frame_object.pack(fill="y", expand=1, padx=10)
        frame_object.on_pack()
        self.frames_stack.append(frame_object)
        # TODO: all frames should have an in and out method to call when the frame is shown or hidden
        # TODO: create a father class for all frames to inherit from, this class should have the in and out methods and the on_pack_forget and on_pack_show methods
        # Consider the option of adding mixins as well
        # The main purpose of defining this callback is to changue the size of the window on the PacientInfoFrame but this approach will be more generic for future possible use cases
        # frame.on_pack_show()
