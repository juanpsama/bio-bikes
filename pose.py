import cv2
import mediapipe as mp
import numpy as np
import angles
from math import atan, degrees
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def reescaleFrame(frame, scale = 0.75):
    #works for live vide, video and images
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# For static images:
IMAGE_FILES = ['photos/sagital14.jpg']
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_reescaled = reescaleFrame(image, scale = 0.2)
    image_height, image_width, _ = image_reescaled.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image_reescaled, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
      continue
    #
    knee = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x * image_width ), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * image_height)]
    ankle = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x * image_width), int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y * image_height)]
    hip = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * image_width) ,int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * image_height)]
    shoulder = [int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width) ,int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height)]
    knee_angle = angles.getAnglesBetweenPoints(knee, ankle, hip)
    hip_angle = angles.getAnglesBetweenPoints(hip, knee, shoulder)
    print(f'Angulo rodilla: {knee_angle}')
    print(f'Angulo cadera: {hip_angle}')
    annotated_image = image_reescaled.copy()
    # Draw segmentation on the image.
    # To improve segmentation around boundaries, consider applying a joint
    # bilateral filter to "results.segmentation_mask" with "image".
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.putText(annotated_image, f'Rodilla: {round(knee_angle, 3)}', (knee[0] + 50,knee[1] ), cv2.FONT_ITALIC, 1.0, (150,25,255), thickness = 2)
    cv2.imwrite('out/annotated_image' + str(idx) + '.png', annotated_image)
    cv2.imshow('out', annotated_image)


    cv2.waitKey(0)
    