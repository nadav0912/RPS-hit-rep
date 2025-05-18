import mediapipe as mp
import cv2 
import torch
import numpy as np
from RPS_model_class import RPSModelV2
from utils import load_model, landmarks_from_image, label_from_RPSmodel, draw_box_text

# -------- INITIALIZATION -------- #
NUM_CLASSES = 4
NUM_FEATURES = 21*3
labels = ['rock', 'paper', 'scissors', 'other']

# Hand detection model and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create an instance of the Hands model
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=2)

# Computer camera
cap = cv2.VideoCapture(0)

# Load RPSmodel
model = RPSModelV2(input_features=NUM_FEATURES, output_features=NUM_CLASSES)
load_model(model, "RPSmodelV2")


# -------- Main Loop -------- #
while cap.isOpened():
    success, frame = cap.read()

    results, image = landmarks_from_image(success, frame, hands)

    # If found hands in image
    if results.multi_hand_landmarks:
        # Loop over hands in the image
        for num, hand in enumerate(results.multi_hand_landmarks):
            # Get label and draw box with label text
            landmarks = [[lm.x, lm.y, lm.z] for lm in hand.landmark]
            label = label_from_RPSmodel(model, landmarks)
            draw_box_text(hand, image, label)

    # Check exit
    if cv2.waitKey(5) & 0xFF == ord('e'):
        print("Stop runing...")
        break

    # Show image
    cv2.imshow('Hand Tracking', image) 



cap.release()  # Release the camera resource.
cv2.destroyAllWindows()  # Close OpenCV windows.
hands.close()  # Release hands model.

