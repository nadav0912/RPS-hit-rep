import mediapipe as mp
import cv2  
import pandas as pd
import numpy as np
import os
from utils import landmarks_from_image, normolize_landmarks, add_examples_to_dataset

# -------- Initialization -------- #
data = []

dataset_path = "hand-dataset.csv"

# Labels dict
key_label_dict =  {'r':"rock", 'p':"paper", 's':"scissors", 'o': "other"}


# Hand detection model and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create an instance of the Hands model
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1)

# Computer camera
cap = cv2.VideoCapture(0)


# -------- Helper Functions -------- # e
def add_landmarks_to_data(data: list, hand_side:str, hand, label: str):
    """Save hand information to the dataframe"""

    row = {"hand-side": hand_side, "label": label}

    landmarks = normolize_landmarks([[lm.x, lm.y, lm.z] for lm in hand.landmark])

    for i, dot in enumerate(landmarks):
        row[f"x{i}"] = dot[0]
        row[f"y{i}"] = dot[1]
        row[f"z{i}"] = dot[2]
        
    data.append(row)


# -------- Main Loop -------- #
print(f"\n\nPress R for Rock, P for Paper, S for Scissors, O for Other, or E to Exit while posing your hand in the correct gesture.")

while cap.isOpened():
    success, frame = cap.read()

    results, image = landmarks_from_image(success, frame, hands)

    # waits 5 millisecond for a key press and convert it from ASCII to char
    key = chr(cv2.waitKey(5) & 0xFF)

    # If it find hand in the image
    if results.multi_hand_landmarks:
        # Loop over hands in the image
        for num, hand in enumerate(results.multi_hand_landmarks):
            # Add the landmark to the image
            mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=1, circle_radius=2),
                                        mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=1, circle_radius=1))
            
            # Check if user press key to add exapmle
            if key in key_label_dict.keys():  
                add_landmarks_to_data(data, results.multi_handedness[num].classification[0].label, hand, label=key_label_dict[key])
                print(f"Add exaple of {key_label_dict[key]} to datset")


    # Check exit
    if key == 'e':
        print("Stop runing...")
        break

    # Show image
    cv2.imshow('Hand Tracking', image) 


cap.release()  # Release the camera resource.
cv2.destroyAllWindows()  # Close OpenCV windows.
hands.close()  # Release hands model.



# -------- Add data to DataSet -------- #
add_examples_to_dataset(data=data)
