from tkinter.ttk import Button, Frame
from tkinter import Tk

class WebcamImageInputFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)

        