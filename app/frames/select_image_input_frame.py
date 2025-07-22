from tkinter.ttk import Button, Frame
from tkinter import Tk

class SelectImageInputFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)
        self.display_name = "Selecciona opcion de entrada"

        self.controller = controller
        video_button =  Button(self, text = "Seleccionar Video", command=lambda: controller.show_frame("VideoAnalisisFrame"))
        webcam_button =  Button(self, text = "Utilizar Webcam", command=lambda: controller.show_frame("WebcamImageInputFrame"))
        video_button.pack(pady=50)
        webcam_button.pack(pady=50)

    



