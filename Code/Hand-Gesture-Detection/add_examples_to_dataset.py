# ---------- IMPORTS ---------- #
import mediapipe as mp
import cv2  
import pandas as pd
import sys
import os

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


example_landmarks_data = []   # list of landmarks. each landmarks is list of 21 dots [[x, y, z], ...]
example_images = []

# Helper function to show example record images
def show_record_example(example_images: list[list[int]], delay: float):
    """
    Displays the example images as a sequence with a delay between each frame.
    Input:
        example_images (list): A list containing all the frames to be displayed.
        delay (int): The delay (in milliseconds) between displaying each frame.
    """

    print("\nShow example (press s to stop)...")
    size = len(example_images)
    count = size
    key = ''

    while key != 'q':
        key = chr(cv2.waitKey(delay) & 0xFF)
        count -= 1
        i = count%size

        # pick image and add frame number to it
        image = example_images[i]
        cv2.putText(image, str(i), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (2, 57, 66), 3, lineType=cv2.LINE_AA)

        cv2.imshow("example", example_images[i])




# -------- Main Loop -------- #
while cap.isOpened():
    success, image = cap.read()

    hand, hand_side, image = hand_from_image(success, image, hands)

    # Check if user press key
    key_code = cv2.waitKey(5) & 0xFF
    key = chr(key_code).lower()

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
        if key in key_label_dict.keys():
            # Strat record
            if not record_mode:
                record_mode = True
                hand_side = hand_side
                label = key_label_dict[key]

                print(f"Start record example of {key_label_dict[key]}...")

            # Stop record
            else:
                print("Stop record example!")
                show_record_example(example_images, 100)
                add_example_to_dataset(label, hand_side, example_landmarks_data)

                record_mode = False
                hand_side = None
                label = None
                example_landmarks_data.clear()
                example_images.clear()

    # Check exit
    if key == 'q':
        print("Stop runing...")
        break

    # Show image
    cv2.imshow('Hand Tracking', image) 


# Release resources
cap.release()
cv2.destroyAllWindows() 
hands.close()