from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2

def visualizar_webcam(LabelVideo):
    global cap
    print(type(cap))
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (640, 360), interpolation = cv2.INTER_CUBIC)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            LabelVideo.configure(image=img)
            LabelVideo.image = img
            LabelVideo.after(10, lambda: visualizar_webcam(LabelVideo))
        else:
            LabelVideo.image = ""
            cap.release()
    else:
        print("algo anda mal")

def iniciar(lblVideo):
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar_webcam(lblVideo)
    
def finalizar():
    global cap
    print(type(cap))
    print('pija')
    cap.release()
cap = None 