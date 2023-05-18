from tkinter import *
from tkinter import filedialog
from PIL import Image 
from PIL import ImageTk
import cv2
from makeVideo import *

max_knee_angle = 0 
min_knee_angle = 400
max_hip_angle = 0 
min_hip_angle = 400
avg_shoulder_angle = None
shoulder_angles = []
result_path = None 
result = None

def reescaleFrame(frame, width = 480):
    #works for live vide, video and image
    heigth = int((frame.shape[0] / frame.shape[1]) * width)
    dimensions = (width, heigth)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def iniciarMostrar(LabelVideo, video_path):
    global cap
    cap = cv2.VideoCapture(video_path)
    visualizar(LabelVideo, None)

#functions for WEBCAM
def visualizarWebcam(LabelVideo):
    global cap, result, max_knee_angle, min_knee_angle, max_hip_angle, min_hip_angle, avg_shoulder_angle, shoulder_angles
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (640, 360), interpolation = cv2.INTER_CUBIC)
            data = processImage(frame)
            if data['knee_angle']  != None:
                knee_angle = data['knee_angle']  
                hip_angle = data['hip_angle'] 
                shoulder_angle = data['shoulder_angle']
                shoulder_angles.append(shoulder_angle)

                if knee_angle > max_knee_angle:
                    max_knee_angle = knee_angle
                    cv.imwrite(f'img_out/max_angle{rand_name_file}.png', data['image'])
                if knee_angle < min_knee_angle:
                    min_knee_angle = knee_angle
                    cv.imwrite(f'img_out/min_angle{rand_name_file}.png', data['image'])
                if hip_angle > max_hip_angle:
                    max_hip_angle = hip_angle
                if hip_angle < min_hip_angle:
                    min_hip_angle = hip_angle

            frame = data['image']
            result.write(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            LabelVideo.configure(image=img)
            LabelVideo.image = img
            LabelVideo.after(10, lambda: visualizarWebcam(LabelVideo))
        else:
            LabelVideo.image = ""
            cap.release()

def iniciar(LabelVideo):
    global cap, result, result_path, rand_name_file
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    size = (640, 360)
    rand_name_file = random.randint(2,100)
    result_path = f'videos_out/video_prueba{rand_name_file}.avi'
    print(result_path)
    result = cv.VideoWriter(result_path,
						    cv.VideoWriter_fourcc(*'MJPG'),
						    20, 
                            size)
    visualizarWebcam(LabelVideo)
def finalizar():
    global cap, result_path
    avg_shoulder_angle = fmean(shoulder_angles)
    pacients.set_goniometric_data(
        url_video = result_path,
        knee_min = min_knee_angle,
        knee_max = max_knee_angle, 
        hip_min = min_hip_angle,
        hip_max = max_hip_angle, 
        shoulder_avg = avg_shoulder_angle)
    pacients.save_data()
    cap.release()

#functions for VIDEO FILES
def visualizar(LabelVideo, LabelInfoVideoPath):#leer el video 
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            # frame = imutils.resize(frame, width = 640)
            frame = reescaleFrame(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
        LabelInfoVideoPath.configure(text = "Aún no se ha seleccionado un video")

def visualizarImagen(LabelVideo, img_path):
    frame = cv2.imread(img_path)
    frame = reescaleFrame(frame, width = 360)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(frame)
    img = ImageTk.PhotoImage(image = im) #transformar cada fotograma a formato imageTK
    LabelVideo.configure(image = img)
    LabelVideo.image = img
cap = None 

