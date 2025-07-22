from tkinter.ttk import Button, Frame, Label
import tkinter as tk

from app.models import Pacient
from app.video_controller import VideoController


class PacientInfoFrame(Frame):
    def __init__(self, parent: tk.Tk, controller):
        super().__init__(parent)
        self.display_name = "Informacion del paciente"

        self.controller = controller
        # controller.root.geometry("1080x550")
        self.video_controller: VideoController = controller.video_controller

        self.title_label = Label(self, text="Datos de paciente", font=("Arial", 18))
        self.title_label.grid(column=0, row=0, padx=10)
        self.second_title_label = Label(
            self, text="Datos goniometricos", font=("Arial", 18)
        )
        self.second_title_label.grid(column=1, row=0, columnspan=3)

        self.id_info_label = Label(self, text="ID: ")
        self.id_info_label.grid(row=1, column=0, padx=5)
        self.name_info_label = Label(self, text="Nombre:")
        self.name_info_label.grid(row=2, column=0, padx=5)
        self.last_name_info_label = Label(self, text="Apellido")
        self.last_name_info_label.grid(row=3, column=0, padx=5)
        self.age_label = Label(self, text="Edad:")  # solo admitira 2 numeros
        self.age_label.grid(row=4, column=0, padx=5)
        self.height_label = Label(self, text="Altura:")  # solo admitira 2 numeros
        self.height_label.grid(row=5, column=0, padx=5)
        self.adjustment_label = Label(self, text="Ajustes", font=("Arial", 12))
        self.adjustment_label.grid(column=0, row=6, pady=5)
        self.suggested_ajusdment_label = Label(self, text="Ej. Bajar sillin")
        self.suggested_ajusdment_label.grid(column=0, row=7, padx=(15, 0), pady=5)
        self.process_info_again_button = Button(
            self, text="Analizar de nuevo", width=15
        )  # , command = EjecutarAnalisisDenuevo)
        self.process_info_again_button.grid(column=0, row=8, rowspan=3, padx=5, pady=5)
        self.back_button = Button(
            self, text="Volver", width=15
        )  # , command = CambiarVentanaPrincipal)
        self.back_button.grid(column=0, row=11, rowspan=3, pady=5)

        # botonVideo = Button(self, text = "Elegir y Visualizar video", width = 20, height = 5, command = lambda: visualizarVideo(LabelVideo, LabelInfoVideoPath))
        # botonVideo.grid(column = 2, row = 2, columnspan=2)
        self.video_title_label = Label(
            self, text="Video procesado: "
        )  # solo admitira 2 numeros
        self.video_title_label.grid(column=1, row=1, pady=5, padx=(0, 30))

        self.process_video = Label(self)
        self.process_video.grid(column=1, row=2, rowspan=6, columnspan=2)

        self.angles_title_label = Label(self, text="Angulos:")  # solo admitira 2 numeros
        self.angles_title_label.grid(column=1, row=8)
        self.knee_angle_label = Label(self, text="Rodilla:")  # solo admitira 2 numeros
        self.knee_angle_label.grid(column=1, row=9, padx=5)
        self.hip_angle_label = Label(self, text="Cadera: ")  # solo admitira 2 numeros
        self.hip_angle_label.grid(column=1, row=10, padx=5)
        self.shoulder_angle_label = Label(self, text="Hombro: ")  # solo admitira 2 numeros
        self.shoulder_angle_label.grid(column=1, row=11, padx=5)
        self.hip_translation_label = Label(
            self,
            text="Traslacion de cadera:\n Vertical:  -  Horizontal: "
        )  # solo admitira 2 numeros
        self.hip_translation_label.grid(column=1, row=12, padx=5)

        self.title_image_min_knee = Label(
            self, text="Angulo minimo de rodilla: "
        )  # solo admitira 2 numeros
        self.title_image_min_knee.grid(column=3, row=1, pady=5)

        self.image_min_knee = Label(self)
        self.image_min_knee.grid(column=3, row=2, rowspan=4)

        self.title_image_max_knee = Label(
            self, text="Angulo maximo de rodilla: "
        )  # solo admitira 2 numeros
        self.title_image_max_knee.grid(column=3, row=6, pady=5)

        self.image_max_knee = Label(self)
        self.image_max_knee.grid(column=3, row=7, rowspan=6)

        self._update_pacient_info()

    def _update_pacient_info(self):
        # TODO: Assign video and images to the labels
        # muestra el video en el labelvideo3
        # videoManager.iniciarMostrar(LabelVideo3, datos_paciente['url_video'])
        # #muestra las imagenes en las etiquetas correspondientes
        # videoManager.visualizarImagen(etiquetaImagenMax, datos_paciente['url_img_max'])
        # videoManager.visualizarImagen(etiquetaImagenMin, datos_paciente['url_img_min'])
        # Actualiza las etiquetas de informacion
        if self.controller.current_pacient is None:
            
            return
        pacient: Pacient = self.controller.current_pacient
        self.id_info_label.configure(text=f"ID: {pacient.id}")
        self.name_info_label.configure(text=f"Nombre: {pacient.name}")
        self.last_name_info_label.configure(text=f"Apellido: {pacient.last_name}")
        self.age_label.configure(text=f"Edad: {pacient.age} años")
        self.height_label.configure(text=f"Altura: {pacient.height} cm")
        self.knee_angle_label.configure(
            text=f"Rodilla: {pacient.knee_min} - {pacient.knee_max}"
        )
        self.hip_angle_label.configure(
            text=f"Cadera: {pacient.hip_min} - {pacient.hip_min}"
        )
        self.shoulder_angle_label.configure(text=f"Hombro promedio: {pacient.shoulder_avg} ")
        # TODO: The angles should be calculated when the video is processed and stored in the db
        # self.etiquetaAjusteRecomendado.configure(text = angles.ProcessAngles(datos_paciente['knee_min'], datos_paciente['knee_max']))
        self.hip_translation_label.configure(
            text=f"Traslacion de cadera:\n Vertical: {pacient.hip_translation_horizontal}  Horizontal: {pacient.hip_translation_vertical}  "
        )
