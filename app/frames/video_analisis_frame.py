import threading

from tkinter.ttk import Button, Frame, Label
from tkinter import filedialog
import tkinter as tk

from app.frames.frame_mixin import EnterMethodMixin
from app.video_controller import VideoController


class VideoAnalisisFrame(Frame, EnterMethodMixin):
    display_name = "Analisis de video"
    def __init__(self, parent: tk.Tk, controller):
        super().__init__(parent)
        self.controller = controller
        self.video_controller: VideoController = controller.video_controller
        self.video_path = None

        self.entry_video_label = Label(self, text="Video de entrada:")
        self.entry_video_label.grid(column=0, row=2)

        self.info_path_label = Label(self, text="Aun no se ha seleccionado un video")
        self.info_path_label.grid(column=1, row=2)
        # This label will be used to show the video
        self.video_label = Label(self)
        self.video_label.grid(column=0, row=3, columnspan=2)

        self.save_button = Button(
            self,
            text="Informe",
            command=lambda: self.controller.show_frame("PacientInfoFrame"),
        )

        self.saved_label = Label(self, text="")
        self.saved_label.grid(column=1, row=4, pady=5, padx=5)

        self.open_video_dialog = Button(
            self, text="Elegir video", width=25, command=self._open_video_dialog
        )
        self.open_video_dialog.grid(column=0, row=0, columnspan=2)

        self.process_video_button = Button(
            self, text="Procesar video", width=25, command=self._start_process_thread
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
            self.video_controller.visualizar(
                self.video_label,
                self.info_path_label,
                video_path,
                width=self.controller.root.winfo_width(),
            )

    def _start_process_thread(self):
        print("Starting thread")
        self.process_video_button["state"] = tk.DISABLED
        self.open_video_dialog["state"] = tk.DISABLED
        # self.stop_button['state'] = tk.NORMAL
        # TODO: Show a loading animation while the video is being processed
        self.process_thread = threading.Thread(target=self._process_video).start()
        print("Processing video...")
        self.monitor_tread(self.process_thread)

    def monitor_tread(self, thread: threading.Thread):
        if thread.is_alive():
            # Check the thread every 100ms
            self.after(100, lambda: self.monitor_tread(thread))
        else:
            self.process_video_button["state"] = tk.NORMAL
            print("Procesado")
            # self.stop_button['state'] = tk.DISABLED

    def _process_video(self):
        self.video_controller.process_video(self.video_path)
        # When the process ends the buttons to save appears
        self.save_button.grid(column=0, row=4, pady=5, columnspan=2)
