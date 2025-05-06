# ---------- IMPORTS ---------- #
import mediapipe as mp
import cv2  
import pandas as pd
import sys
import os


# Add the 'utils' directory to sys.path , This allows importing modules from the 'utils' directory in the project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
print(sys.path)

from utils import hand_from_image, landmarks_to_list, add_example_to_dataset


# ---------- initializations ---------- #

# Labels dict
key_label_dict =  {'r':"rock", 'p':"paper", 's':"scissors"}

# Hand Landmarks model and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create an instance of the Hand Landmarks model
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1)

# Computer camera
cap = cv2.VideoCapture(0)


record_mode = False  # Is record example now
label = None  # rock/paper/scissors
hand_side = None  # right/left


# list of maps = [{label: ,hand-side, x0:, y0, .....}]
example_data = []  


# -------- Main Loop -------- #
while cap.isOpened():
    success, image = cap.read()

    hand, image = hand_from_image(success, image, hands)

    # If found hand in image
    if hand: 
        # Draw the landmark on the image
        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                            mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=1, circle_radius=2),
                                            mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=1, circle_radius=1))

        # Check if user press key to add exapmle
        key_code = cv2.waitKey(5) & 0xFF
        key = chr(key_code)

        if key in key_label_dict.keys():
            # Start record mode if he off, and get label and hand side
            if not record_mode:
                record_mode = True
                hand_side = hand.classification[0].label
                label = key_label_dict[key]

                print(f"Start record example of {key_label_dict[key]}...")

            # Add landmarks to data
            landmarks = landmarks_to_list(hand.landmark)
            example_data.append(landmarks)
            

        # Rcorde mode is on and nothing is press
        if key_code == 255 and record_mode:
            print("Stop record example!")

            record_mode = True
            hand_side = None
            label = None

            add_example_to_dataset(label, hand_side, example_data)


    # Show image
    cv2.imshow('Hand Tracking', image) 


# Release resources
cap.release()
cv2.destroyAllWindows() 
hands.close()  
