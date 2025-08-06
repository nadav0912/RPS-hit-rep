import mediapipe as mp
import cv2  
import pandas as pd
import numpy as np
import os

from final_models.hand_landmark.hand_landmark import HandLandmark
from final_models.palm_detection.palm_detection import PalmDetection

from utils import hand_from_image_v2, check_key_press, normalize_landmarks, add_examples_to_dataset

# -------- Initialization -------- #
data = []

dataset_path = "hand-dataset.csv"

# Labels dict
key_label_dict =  {'r':"rock", 'p':"paper", 's':"scissors", 'o': "other"}

# Computer camera
cap = cv2.VideoCapture(0)

# Instance of the Models
palm_detector = PalmDetection()
hand_landmark_model = HandLandmark()

# -------- Helper Functions -------- # e
def add_landmarks_to_data(landmarks: list[list], hand_side:str, label: str):
    """Save hand information to the dataframe"""

    row = {"hand-side": hand_side, "label": label}

    for i, dot in enumerate(landmarks):
        row[f"x{i}"] = dot[0]
        row[f"y{i}"] = dot[1]
        row[f"z{i}"] = dot[2]
        
    data.append(row)


# -------- Main Loop -------- #
print(f"\n\nPress R for Rock, P for Paper, S for Scissors, O for Other, or E to Exit while posing your hand in the correct gesture.")

while cap.isOpened():
    success, image = cap.read()

    landmarks, hand_side_pred = hand_from_image_v2(image, palm_detector, hand_landmark_model)

    # waits 5 millisecond for a key press and convert it from ASCII to char
    key = check_key_press(5)

    # If found hand in image
    if landmarks is not None: 

        landmark = landmarks[0]  # Get the first hand's landmarks

        # Draw the landmark on the image
        for dot in landmark:
                x, y = int(dot[0]), int(dot[1])
                cv2.circle(image, (x, y), int(abs(dot[2])/4), (0, 255, 0), -1)

        # Check if user press key to add exapmle
        if key in key_label_dict.keys():  
            add_landmarks_to_data(normalize_landmarks(landmark), hand_side_pred, label=key_label_dict[key])
            print(f"Add exaple of {key_label_dict[key]} to datset")

    # Check exit
    if key == 'e':
        print("Stop runing...")
        break

    # Show image
    cv2.imshow('Hand Tracking', image) 


cap.release()  # Release the camera resource.
cv2.destroyAllWindows()  # Close OpenCV windows.


# -------- Add data to DataSet -------- #
add_examples_to_dataset(data=data)