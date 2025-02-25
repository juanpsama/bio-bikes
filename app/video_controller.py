import cv2 as cv
from PIL import Image 
from PIL import ImageTk
import tkinter as tk

class VideoController:
    def visualizar(self, label_video, label_info_video, video_path, width:int = 480):
        # Leer el video 
        cap = cv.VideoCapture(video_path)
        self._visualizar_video(label_video, label_info_video, cap, width=width)

    def _visualizar_video(self, label_video: tk.Label, label_info_video_path: tk.Label, cap: cv.VideoCapture, width:int = 480):
        """
        Funcion recursiva que se encarga de leer y mostrar el video en sobre la interfaz en 
        la etiqueta label_video y de actualizar el label_info_video_path con la ruta del video
        """
        if cap is None:
            return
        ret, frame = cap.read()
        if ret:
            frame = self._reescale_frame(frame, width=width)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            image_array = Image.fromarray(frame)
            # Transformar cada fotograma a formato imageTK
            image_tk = ImageTk.PhotoImage(image = image_array) 
            label_video.configure(image = image_tk)
            label_video.image = image_tk
            self.last_image = image_tk
            # label.after(): llama a cierta funcion (self.visualizar) despues de un delay en ms             
            label_video.after(20, lambda: self._visualizar_video(label_video, label_info_video_path, cap)) 
        else:   
            if label_info_video_path is not None:
                label_info_video_path.configure(text = "Aún no se ha seleccionado un video")  #limpiar cuando se cierre el video
            label_video.image = ""
            cap.release()  

    def _reescale_frame(self, frame : tk.Frame, width:int = None, scale=0.75):
        if width is None:
            width = int(frame.shape[1] * scale)
            height = int(frame.shape[0] * scale)
        else:
            # If width is provided, calculate height based on the aspect ratio
            height = int((frame.shape[0] / frame.shape[1]) * width)
        dimensions = (width, height)
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
    def process_video(self, video_path):
        pass

    # Dump here all the video related methods
    # def open_video_dialog(self, label_video):
    #     if cap is not None:
    #         label_video.image = ""
    #         cap.release()
    #         cap = None
    #         video_path = filedialog.askopenfilename(filetypes= [
    #         ("all video format", ".mp4"),
    #         ("all video format", ".avi"), 
    #         ("all video format", ".mov") ])
    #     if len(video_path) > 0:
    #         # LabelInfoVideoPath.configure(text = "")
    #         # LabelInfoVideoPath.update()
    #         LabelInfoVideoPath.configure(text = "procesando....")
    #         LabelInfoVideoPath.update()
    #         result_video_path = processVideo(video_path)
    #         LabelInfoVideoPath.configure(text = result_video_path)
    #         cap = cv.VideoCapture(result_video_path)
    #         visualizar(LabelVideo, LabelInfoVideoPath)
    #     else:
    #         LabelInfoVideoPath.configure(text = "Aún no se ha seleccionado un video")