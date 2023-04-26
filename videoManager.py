from tkinter import *
from tkinter import filedialog
from PIL import Image 
from PIL import ImageTk
import cv2
from makeVideo import *


def iniciarMostrar(LabelVideo, video_path):
    global cap
    cap = cv2.VideoCapture(video_path)
    visualizar(LabelVideo, None)

#functions for WEBCAM
def visualizarWebcam(LabelVideo):
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (640, 360), interpolation = cv2.INTER_CUBIC)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = processWebcam(frame)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            LabelVideo.configure(image=img)
            LabelVideo.image = img
            LabelVideo.after(10, lambda: visualizarWebcam(LabelVideo))
        else:
            LabelVideo.image = ""
            cap.release()

def iniciar(LabelVideo):
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizarWebcam(LabelVideo)
def finalizar():
    global cap
    cap.release()

#functions for VIDEO FILES
def visualizar(LabelVideo, LabelInfoVideoPath):#leer el video 
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            # frame = imutils.resize(frame, width = 640)
            frame = cv2.resize(frame, (640, 360), interpolation = cv2.INTER_CUBIC)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frame = processImage(frame)
            # cv2.imshow('hola', frame)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image = im) #transformar cada fotograma a formato imageTK
            
            LabelVideo.configure(image = img)
            LabelVideo.image = img
            LabelVideo.after(20, lambda: visualizar(LabelVideo, LabelInfoVideoPath)) #after, llama a cierta funcion (visualizar) despues de un delay en ms
        else:
            if LabelInfoVideoPath != None:
                LabelInfoVideoPath.configure(text = "Aún no se ha seleccionado un video")  #limpiar cuando se cierre el video
            LabelVideo.image = ""
            cap.release()
        
def visualizarVideo(LabelVideo, LabelInfoVideoPath):
    global cap 
    if cap is not None:
        LabelVideo.image = ""
        cap.release()
        cap = None
    video_path = filedialog.askopenfilename(filetypes= [
        ("all video format", ".mp4"),
        ("all video format", ".avi")])
    if len(video_path) > 0:
        # LabelInfoVideoPath.configure(text = "")
        # LabelInfoVideoPath.update()
        LabelInfoVideoPath.configure(text = "procesando....")
        LabelInfoVideoPath.update()
        result_video_path = processVideo(video_path)
        LabelInfoVideoPath.configure(text = result_video_path)
        cap = cv2.VideoCapture(result_video_path)
        visualizar(LabelVideo, LabelInfoVideoPath)
    else:
        print('holaa')
        LabelInfoVideoPath.configure(text = "Aún no se ha seleccionado un video")


cap = None 

