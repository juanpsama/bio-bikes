from tkinter.ttk import Frame, Button, Label
from tkinter import Tk

class WebcamImageInputFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)
        self.display_name = "Analisis webcam"

        self.controller = controller
        btnIniciar = Button(self, text="Iniciar", width=45) #, command = lambda: videoManager.iniciarMostrar(LabelVideoWebcam, 0))
        btnIniciar.grid(column=0, row=0, padx=5, pady=5)

        btnFinalizar = Button(self, text="Finalizar", width=45)#, command = finalizarGrabacion)
        btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

        btnIniciar = Button(self, text="Iniciar Grabacion", width=45)#, command = lambda: videoManager.iniciar(LabelVideoWebcam))
        btnIniciar.grid(column=0, row=1, padx=5, pady=5, columnspan = 2)

        LabelVideoWebcam = Label(self)
        LabelVideoWebcam.grid(column=0, row=2, columnspan=2)

        savedLabbelCam = Label(self, text='')
        savedLabbelCam.grid(column = 0, row = 3, pady = 5, padx=5)


        