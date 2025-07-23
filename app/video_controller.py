from time import sleep
import numpy as np
import cv2 as cv
import tkinter as tk
from PIL import Image
from PIL import ImageTk

import mediapipe as mp
from mediapipe import solutions
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2


VisionRunningMode = mp.tasks.vision.RunningMode


base_options = python.BaseOptions(
    model_asset_path="pose_models/pose_landmarker_heavy.task"
)
MP_VIDEO_OPTIONS = vision.PoseLandmarkerOptions(
    base_options=base_options, running_mode=VisionRunningMode.VIDEO
)


class VideoController:
    loop = True
    def visualizar(self, label_video, video_path, label_info_video=None, width: int = 480):
        # Leer el video
        self.loop = True
        cap = cv.VideoCapture(video_path)
        self._visualizar_video(label_video, label_info_video, cap, width=width, video_path=video_path)

    def _visualizar_video(
        self,
        label_video: tk.Label,
        label_info_video_path: tk.Label,
        cap: cv.VideoCapture,
        video_path: str,
        width: int = 480,
    ):
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
            image_tk = ImageTk.PhotoImage(image=image_array)
            label_video.configure(image=image_tk)
            label_video.image = image_tk
            # label.after(): llama a cierta funcion (self.visualizar) despues de un delay en ms
            label_video.after(
                20,
                lambda: self._visualizar_video(label_video, label_info_video_path, cap, video_path, width=width),
            )
        else:
            if self.loop:
                cap = cv.VideoCapture(video_path)
                self._visualizar_video(label_video, label_info_video_path, cap, video_path, width=width)
                return
                
            if label_info_video_path is not None:
                label_info_video_path.configure(
                    text="Aún no se ha seleccionado un video"
                )  # limpiar cuando se cierre el video
            label_video.image = ""
            cap.release()

    def close_video_loop(self):
        """
        Close the video loop, this will stop the video from playing
        """
        self.loop = False

    def _reescale_frame(self, frame: tk.Frame, width: int = None, scale=0.75):
        if width is None:
            width = int(frame.shape[1] * scale)
            height = int(frame.shape[0] * scale)
        else:
            # If width is provided, calculate height based on the aspect ratio
            height = int((frame.shape[0] / frame.shape[1]) * width)
        dimensions = (width, height)
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

    def process_video(self, video_path) -> str:
        # TODO: Call mediapipe to extract the pose data from the video
        print(video_path)
        cap = cv.VideoCapture(video_path)
        result_path = "video_out.avi"
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        size = (frame_width, frame_height)
        result = cv.VideoWriter(result_path, cv.VideoWriter_fourcc(*"MJPG"), 20, size)

        with vision.PoseLandmarker.create_from_options(MP_VIDEO_OPTIONS) as landmarker:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("frames ended.")
                    break

                frame_timestamp_ms = int(cap.get(cv.CAP_PROP_POS_MSEC))
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

                # Perform pose landmarking on the provided single image.
                # The pose landmarker must be created with the video mode.
                pose_landmarker_result = landmarker.detect_for_video(
                    mp_image, frame_timestamp_ms
                )
                annotated_image = self._draw_landmarks_on_image(
                    image, pose_landmarker_result
                )
                result.write(annotated_image)
        cap.release()
        result.release()
        sleep(1)  # Wait for the video to be saved properly
        return result_path

    def _draw_landmarks_on_image(self, rgb_image, detection_result):
        pose_landmarks_list = detection_result.pose_landmarks
        annotated_image = np.copy(rgb_image)

        # Loop through the detected poses to visualize.
        for idx in range(len(pose_landmarks_list)):
            pose_landmarks = pose_landmarks_list[idx]
            # print(f"Pose landmarks for pose {idx}: {pose_landmarks}\n")

            # Draw the pose landmarks.
            pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            pose_landmarks_proto.landmark.extend(
                [
                    landmark_pb2.NormalizedLandmark(
                        x=landmark.x, y=landmark.y, z=landmark.z
                    )
                    for landmark in pose_landmarks
                ]
            )
            solutions.drawing_utils.draw_landmarks(
                annotated_image,
                pose_landmarks_proto,
                solutions.pose.POSE_CONNECTIONS,
                solutions.drawing_styles.get_default_pose_landmarks_style(),
            )
        return annotated_image

    def get_image_from_path(self, img_path: str, width: int) -> ImageTk.PhotoImage:
        frame = cv.imread(img_path)
        frame = self._reescale_frame(frame, width=width)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image_array = Image.fromarray(frame)
        return ImageTk.PhotoImage(image=image_array)
    
    def show_placeholder_image(self, label: tk.Label, widht: int = 480):
        """
        Show a placeholder image on the given label.
        """
        image_tk = self.get_image_from_path("assets/placeholder.png", width=widht)
        label.configure(image=image_tk)
        label.image = image_tk

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
