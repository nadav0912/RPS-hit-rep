# ---------- IMPORTS ---------- #
import mediapipe as mp
import cv2  
import pandas as pd
import sys
import os


from utils import LiveGRUWrapper
from Gesture_detection_model import GRUModelV1
from utils import hand_from_image_v2, add_example_to_dataset, load_model, show_record_example, check_key_press
from utils import INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE, TRAINED_MODEL

from landmark_hand_models.hand_landmark.hand_landmark import HandLandmark
from landmark_hand_models.palm_detection.palm_detection import PalmDetection

# ---------- initializations ---------- #
# Labels dict
key_label_dict =  {'r':"rock", 'p':"paper", 's':"scissors"}


# Instance of the Models
palm_detector = PalmDetection()
hand_landmark_model = PalmDetection()

# Computer camera
cap = cv2.VideoCapture(1)


record_mode = False  # Is record example now
label = None  # rock/paper/scissors
hand_side = None

example_landmarks_data = []   # list of landmarks. each landmarks is list of 21 dots [[x, y, z], ...]
example_images = []


# -------- Main Loop -------- #
while cap.isOpened():
    success, image = cap.read()

    landmark, hand_side_pred = hand_from_image_v2(image, palm_detector, hand_landmark_model)

    key_char = check_key_press()

    # If found hand in image
    if landmark: 
        # Draw the landmark on the image
        for i, lm_list in enumerate(landmark):
            for lm in lm_list:
                x, y = int(lm[0]), int(lm[1])
                cv2.circle(image, (x, y), int(abs(lm[2])/10), (0, 255, 0), -1)

        # Add hand to example data if record mode is on
        if record_mode:
            example_landmarks_data.append(landmark)
            example_images.append(image)
            print("....")

        # Check start/stop record example
        if key_char in key_label_dict.keys():
            # Strat record
            if not record_mode:
                record_mode = True
                hand_side = hand_side_pred
                label = key_label_dict[key_char]

                print(f"Start record example of {key_label_dict[key_char]}...")

            # Stop record
            else:
                print("Stop record example!")

                #need_to_save = show_record_example(example_images, example_landmarks_data, live_wrapper)
                add_example_to_dataset(label, hand_side, example_landmarks_data)

                record_mode = False
                label = None
                hand_side = None
                example_landmarks_data.clear()
                example_images.clear()

    # Check exit
    if key_char == 'q':
        print("Stop runing...")
        break

    cv2.imshow('Hand Tracking', image)  # Show image
    

# Release resources
cap.release()
cv2.destroyAllWindows() 