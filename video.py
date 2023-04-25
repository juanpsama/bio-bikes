import cv2 as cv
import random
import mediapipe as mp
import angles
from mediapipe.python.solutions.pose import PoseLandmark
from mediapipe.python.solutions.drawing_utils import DrawingSpec
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
def reescaleFrame(frame, scale = 0.75):
    #works for live vide, video and images
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


video_to_capture = [0, 1, 'videos/sagital1.mp4']
capture_index = 2
scale_ratio = 0
if capture_index == 0 or capture_index == 1:
  scale_ratio = 1.5
else:
  scale_ratio = 0.5

color_flag_knee = (150,25,255)
color_flag_hip = (150,25,255)
max_knee_angle = 0 
min_hip_angle = 400
cap = cv.VideoCapture(video_to_capture[capture_index])
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
#Custom landmarks

custom_style = mp_drawing_styles.get_default_pose_landmarks_style()
custom_connections = list(mp_pose.POSE_CONNECTIONS)

# list of landmarks to exclude from the drawing
excluded_landmarks = [
    PoseLandmark.LEFT_EYE, 
    PoseLandmark.RIGHT_EYE, 
    PoseLandmark.LEFT_EYE_INNER, 
    PoseLandmark.RIGHT_EYE_INNER, 
    PoseLandmark.LEFT_EAR,
    PoseLandmark.RIGHT_EAR,
    PoseLandmark.LEFT_EYE_OUTER,
    PoseLandmark.RIGHT_EYE_OUTER,
    PoseLandmark.NOSE,
    PoseLandmark.MOUTH_LEFT,
    PoseLandmark.MOUTH_RIGHT ]

for landmark in excluded_landmarks:
    # we change the way the excluded landmarks are drawn
    custom_style[landmark] = DrawingSpec(color=(255,255,0), thickness=None) 
    # we remove all connections which contain these landmarks
    custom_connections = [connection_tuple for connection_tuple in custom_connections 
                            if landmark.value not in connection_tuple]

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
rand_name_file = random.randint(2,100)
result = cv.VideoWriter(f'videos_out/video_prueba{rand_name_file}.avi',
						cv.VideoWriter_fourcc(*'MJPG'),
						20, size)

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        print(f'Angulo maximo en extension de cadera: {max_knee_angle}')
        print(f'Angulo minimo en flexion de cadera: {min_hip_angle}')
        with open('videos_out/readme.txt', 'w') as f:
          f.write(f'Angulo maximo en extension de cadera: {max_knee_angle}')
          f.write('\n')
          f.write(f'Angulo minimo en flexion de cadera: {min_hip_angle}')
        # If loading a video, use 'break' instead of 'continue'.
        break
      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
      results = pose.process(image)

      # Draw the pose annotation on the image.
      image.flags.writeable = True
      image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
  
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
        hip = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * image_width) ,int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * image_height)]
        shoulder = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width) ,int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height)]
      except:
        cv.putText(image, f'Persona no encontrada', (20, 20 ), cv.FONT_ITALIC, 1.0, (0,0,255), thickness = 2)
      else:
        knee_angle = angles.getAnglesBetweenPoints(knee, ankle, hip)
        hip_angle = angles.getAnglesBetweenPoints(hip, shoulder, knee)
        if knee_angle > max_knee_angle:
          max_knee_angle = knee_angle

        if knee_angle < min_hip_angle:
          min_hip_angle = knee_angle

        if knee_angle < 150 and knee_angle > 67:
          color_flag_knee = (0,255,0) 
        else:
          color_flag_knee = (150,25,255)
        cv.putText(image, f'Rodilla: {round(knee_angle, 3)}', (knee[0] + 50 , knee[1] ), cv.FONT_ITALIC, 1.0, color_flag_knee, thickness = 2)
        cv.putText(image, f'Cadera: {round(hip_angle, 3)}', (hip[0] - 150 , hip[1] ), cv.FONT_ITALIC, 1.0, color_flag_hip, thickness = 2)
        print(f'Angulo rodilla: {knee_angle}')
        print(f'Angulo cadera: {hip_angle}')
        
      result.write(image)
      image_reescaled = reescaleFrame(image, scale = scale_ratio)
    #cv.imshow('MediaPipe Pose', image_reescaled)
      if cv.waitKey(1) & 0xFF == 27:
      # print(f'Angulo maximo en extension de cadera: {max_knee_angle}')
      # print(f'Angulo minimo en flexion de cadera: {min_hip_angle}')
        break

cap.release()