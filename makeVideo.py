import cv2 as cv
import random
from statistics import fmean

import angles
import pacients

import mediapipe as mp
from mediapipe.python.solutions.pose import PoseLandmark
from mediapipe.python.solutions.drawing_utils import DrawingSpec
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def reescaleFrame(frame, scale = 0.75):
    #works for live vide, video and images
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#model declaration
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.7,
    model_complexity=2,
    smooth_landmarks = True)

color_flag_knee = (150,25,255)
color_flag_hip = (150,25,255)

#Custom landmarks

custom_style = mp_drawing_styles.get_default_pose_landmarks_style()
custom_connections = list(mp_pose.POSE_CONNECTIONS)

# list of landmarks to exclude from the drawing
excluded_landmarks = [
    PoseLandmark.RIGHT_EYE, 
    PoseLandmark.LEFT_EYE, 
    PoseLandmark.RIGHT_EYE_INNER, 
    PoseLandmark.LEFT_EYE_INNER, 
    PoseLandmark.RIGHT_EAR,
    PoseLandmark.LEFT_EAR,
    PoseLandmark.RIGHT_EYE_OUTER,
    PoseLandmark.LEFT_EYE_OUTER,
    PoseLandmark.NOSE,
    PoseLandmark.MOUTH_RIGHT,
    PoseLandmark.MOUTH_LEFT,
    PoseLandmark.LEFT_HEEL,
    PoseLandmark.LEFT_ANKLE,
    PoseLandmark.LEFT_FOOT_INDEX,
    PoseLandmark.LEFT_KNEE]

for landmark in excluded_landmarks:
    # we change the way the excluded landmarks are drawn
    custom_style[landmark] = DrawingSpec(color=(255,255,0), thickness=None) 
    # we remove all connections which contain these landmarks
    custom_connections = [connection_tuple for connection_tuple in custom_connections 
                            if landmark.value not in connection_tuple]
def processImage(image):
    global pose
    knee_angle = None
    hip_angle = None
    shoulder_angle = None
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    results = pose.process(image)
        # Draw the pose annotation on the image.
    image.flags.writeable = True
    # image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        connections = custom_connections,
        landmark_drawing_spec = custom_style)
    # Flip the image horizontally for a selfie-view display.
    image_height, image_width, _ = image.shape
    try:
        knee = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x * image_width ), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * image_height)]
        ankle = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x * image_width), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y * image_height)]
        hip = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * image_width), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * image_height)]
        shoulder = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height)]
        wrist = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * image_width), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image_height)]
    except:
        cv.putText(image, f'Persona no encontrada', (20, 20 ), cv.FONT_ITALIC, 1.0, (255,0,0), thickness = 2)
    else:
        knee_angle = angles.getAnglesBetweenPoints(knee, ankle, hip)
        hip_angle = angles.getAnglesBetweenPoints(hip, shoulder, knee)
        shoulder_angle = angles.getAnglesBetweenPoints(hip, shoulder, wrist)
        # print(f'{knee} {ankle} {hip}')

        if knee_angle < 150 and knee_angle > 67:
            color_flag_knee = (0,255,0) 
        else:
            color_flag_knee = (150,25,255)

        cv.putText(image, f'Rodilla: {round(knee_angle, 3)}', (knee[0] + 50 , knee[1] ), cv.FONT_ITALIC, 1.0, color_flag_knee, thickness = 2)
        cv.putText(image, f'Cadera: {round(hip_angle, 3)}', (hip[0] - 150 , hip[1] ), cv.FONT_ITALIC, 1.0, color_flag_hip, thickness = 2)
        cv.putText(image, f'hombro: {round(shoulder_angle, 3)}', (shoulder[0] - 150 , shoulder[1] ), cv.FONT_ITALIC, 1.0, color_flag_hip, thickness = 2)
        # print(f'Angulo rodilla: {knee_angle}')
        # print(f'Angulo cadera: {hip_angle}')
    results = {'image' : image, 'knee_angle' : knee_angle, 'hip_angle' : hip_angle, 'shoulder_angle' : shoulder_angle, 'hip_height': hip[1]}
    return results

# def processWebcam(image):
#     results_processed = processImage(image)
#     image_processed = results_processed['image']
#     if results_processed['knee_angle']  != None:
#         knee_angle = results_processed['knee_angle']  
#         hip_angle = results_processed['hip_angle'] 
#     return image_processed

def processVideo(videoPath):
    global custom_connections, custom_style
    #Goniometric variables
    knee_angle = 0
    hip_angle = 0
    #max and min values of goniometric variables
    max_knee_angle = 0 
    min_knee_angle = 400
    max_hip_angle = 0 
    min_hip_angle = 400
    avg_shoulder_angle = None
    shoulder_angles = []
    #hip traslation variable
    max_hip_height = 0 
    min_hip_height = 4000
    hip_height_diff = 0
    
    cap = cv.VideoCapture(videoPath)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    # print(videoPath)
    rand_name_file = random.randint(2,100)
    result_path = f'videos_out/video_prueba_{rand_name_file}.avi'
    result = cv.VideoWriter(result_path,
						    cv.VideoWriter_fourcc(*'MJPG'),
						    20, 
                            size)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
            break
        results_processed = processImage(image)
        image_processed = results_processed['image']
        if results_processed['knee_angle']  != None:
            knee_angle = results_processed['knee_angle']  
            hip_angle = results_processed['hip_angle'] 
            shoulder_angle = results_processed['shoulder_angle']
            shoulder_angles.append(shoulder_angle)
            hip_height= results_processed['hip_height']

        if knee_angle > max_knee_angle:
            max_knee_angle = knee_angle
            cv.imwrite(f'img_out/max_angle_{rand_name_file}.png', results_processed['image'])
        if knee_angle < min_knee_angle:
            min_knee_angle = knee_angle
            cv.imwrite(f'img_out/min_angle_{rand_name_file}.png', results_processed['image'])
        
        if hip_angle > max_hip_angle:
            max_hip_angle = hip_angle
        if hip_angle < min_hip_angle:
            min_hip_angle = hip_angle

        if hip_height > max_hip_height:
            max_hip_height = hip_height
        if hip_angle < min_hip_height:
            min_hip_height = hip_height


        result.write(image_processed)
        # image_reescaled = reescaleFrame(image, scale = 0.5)
        # cv.imshow('MediaPipe Pose', image_reescaled)
        if cv.waitKey(1) & 0xFF == 27:
        # print(f'Angulo maximo en extension de cadera: {max_knee_angle}')
        # print(f'Angulo minimo en flexion de cadera: {min_hip_angle}')
            break

    cap.release()
    #this hip difference the less the better, gives an indicator of bad position
    hip_height_diff = max_hip_height - min_hip_height
    avg_shoulder_angle = fmean(shoulder_angles)

    print(f'max knee angle: {max_knee_angle}')
    print(f'min knee angle: {min_knee_angle}')
    print(f'max hip angle: {max_hip_angle}')
    print(f'min hip angle: {min_hip_angle}')
    print(f'hip height difference: {hip_height_diff}')
    print(f'average shoulder angle: {avg_shoulder_angle}')
    pacients.set_goniometric_data(
        url_video = result_path,
        knee_min = min_knee_angle,
        knee_max = max_knee_angle, 
        hip_min = min_hip_angle,
        hip_max = max_hip_angle, 
        shoulder_avg = avg_shoulder_angle)

    return result_path
