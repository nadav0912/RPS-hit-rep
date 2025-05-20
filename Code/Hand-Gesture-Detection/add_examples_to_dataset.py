# ---------- IMPORTS ---------- #
import mediapipe as mp
import cv2  
import pandas as pd
import sys
import os

from utils import LiveGRUWrapper
from Gesture_detection_model import GRUModelV1
from utils import hand_from_image, landmarks_to_list, add_example_to_dataset, load_model, show_record_example, check_key_press
from utils import INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE, TRAINED_MODEL


# ---------- initializations ---------- #
# Labels dict
key_label_dict =  {'r':"rock", 'p':"paper", 's':"scissors"}

# Get model for show preds on each new example
model = GRUModelV1(
        input_size=INPUT_SIZE,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        num_classes=OUTPUT_SIZE,
        dropout_prob=0.3
)

load_model(model, model_name=TRAINED_MODEL)
live_wrapper = LiveGRUWrapper(model)

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


example_landmarks_data = []   # list of landmarks. each landmarks is list of 21 dots [[x, y, z], ...]
example_images = []


# -------- Main Loop -------- #
while cap.isOpened():
    success, image = cap.read()

    hand, hand_side, image = hand_from_image(success, image, hands)

    key_char = check_key_press()

    # If found hand in image
    if hand: 
        # Draw the landmark on the image
        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                            mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=1, circle_radius=2),
                                            mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=1, circle_radius=1))

        # Add hand to example data if record mode is on
        if record_mode:
            example_landmarks_data.append(landmarks_to_list(hand.landmark))
            example_images.append(image)
            print("....")

        # Check start/stop record example
        if key_char in key_label_dict.keys():
            # Strat record
            if not record_mode:
                record_mode = True
                hand_side = hand_side
                label = key_label_dict[key_char]

                print(f"Start record example of {key_label_dict[key_char]}...")

            # Stop record
            else:
                print("Stop record example!")

                need_to_save = show_record_example(example_images, example_landmarks_data, live_wrapper)
                if need_to_save:
                    add_example_to_dataset(label, hand_side, example_landmarks_data)

                record_mode = False
                hand_side = None
                label = None
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
hands.close()