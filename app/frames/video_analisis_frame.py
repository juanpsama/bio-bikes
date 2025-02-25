from tkinter.ttk import Button, Frame, Label
from tkinter import Tk, filedialog


class VideoAnalisisFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)
        self.video_path = None

        self.entry_video_label = Label(self, text="Video de entrada:")
        self.entry_video_label.grid(column=0, row=2)

        self.info_path_label = Label(self, text="Aun no se ha seleccionado un video")
        self.info_path_label.grid(column=1, row=2)
        # This label will be used to show the video
        self.video_label = Label(self)
        self.video_label.grid(column=0, row=3, columnspan=2)

        self.save_button = Button(self, text="Guardar")
        self.save_button = Button(self, text="Informe")
        self.save_button.grid(column=0, row=4, pady=5)

        self.saved_label = Label(self, text="")
        self.saved_label.grid(column=1, row=4, pady=5, padx=5)

        self.open_video_dialog = Button(
            self, text="Elegir video", width=25, command=self._open_video_dialog
        )
        self.open_video_dialog.grid(column=0, row=0, columnspan=2)

        self.process_video_button = Button(
            self, text="Procesar video", width=25, command=self._process_video
        )

    def _open_video_dialog(self):
        video_path = filedialog.askopenfilename(
            filetypes=[
                ("all video format", ".mp4"),
                ("all video format", ".avi"),
                ("all video format", ".mov"),
            ]
        )
        if len(video_path) > 0:
            self.video_path = video_path
            self.info_path_label.configure(text=video_path)
            self.process_video_button.grid(column=0, row=1, columnspan=2)
            # TODO: Make the video play
            return
        self.info_path_label.configure(text="Aún no se ha seleccionado un video")
        self.process_video_button.grid_forget()

    def _process_video(self):
        pass

    # def GuardarDatos():
    #     #Llama a pacients para que guarde los datos en la db
    #     #Actualiza el labbel de guardado
    #     try:
    #         savedLabbel.configure(text = 'Ha ocurrido un error, no se han generado datos correctamente')
    #         # Pacient()
    #         if pacients.save_data():
    #             savedLabbel.configure(text = 'Los datos han sido guardados correctamente')
    #             saveButton.grid(column = 2, row = 3, pady = 5)
    #     except Exception as e:
    #         savedLabbel.configure(text = str(e))
    # def CambiarInfPaciente(id_paciente):
    #     global datos_paciente
    #     ventana.title("Cargar Video")
    #     ventana.geometry("1080x550")
    #     ventanaInfPaciente.pack(fill='both', expand=1)
    #     ventanaPrincipal.pack_forget()
    #     ventanaCargarVideo.pack_forget()
    #     datos_paciente = pacients.get_pacient_data(id_paciente)
    #     paciente : Pacient = session.query(Pacient).filter(Pacient.id==id_paciente).one()
    #     datos_paciente = paciente
    #     ActualizarTextosInforme()
