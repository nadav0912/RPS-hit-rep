import mediapipe as mp
import cv2 
import numpy as np
import torch
from Gesture_detection_model import GRUModelV1
from utils import LiveGRUWrapper, load_model, hand_from_image, landmarks_to_list, prepare_landmarks_to_model

# -------- INITIALIZATION -------- #
NUM_LAYERS = 2
HIDDEN_SIZE = 128 
INPUT_SIZE = 63
OUTPUT_SIZE = 3

model = GRUModelV1(
        input_size=INPUT_SIZE,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        num_classes=OUTPUT_SIZE,
        dropout_prob=0.3
)

load_model(model, model_name="train_70_percent")
live_wrapper = LiveGRUWrapper(model)

labels = ['rock', 'paper', 'scissors']

# Hand detection model and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create an instance of the Hands model
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=2)

# Computer camera
cap = cv2.VideoCapture(0)


currently_detecting = False


# -------- HELPER FUNC -------- #
def draw_label_on_image(landmarks, image, label_text):
    landmarks = np.array(landmarks_to_list(landmarks))
    height, width, channels = image.shape

    x_coordinates = landmarks[:, 0]
    y_coordinates = landmarks[:, 1]

    x_min = int(np.min(x_coordinates) * width)
    x_max = int(np.max(x_coordinates) * width)
    y_min = int(np.min(y_coordinates) * height)
    y_max = int(np.max(y_coordinates) * height)


    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=1)
    cv2.putText(image, label_text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (40, 240, 40), 2, lineType=cv2.LINE_AA)

    return image


# -------- Main Loop -------- #
while cap.isOpened():
    success, frame = cap.read()

    hand, hand_side, image = hand_from_image(success, frame, hands)

    # Get key press
    key_code = cv2.waitKey(5) & 0xFF
    key = chr(key_code).lower()
    
    # If found hand in image
    if hand: 
        # Draw the landmark on the image
        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                            mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=1, circle_radius=2),
                                            mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=1, circle_radius=1))

        if currently_detecting:
            # Stop detecting when press s and in detecting mode
            if key == 's':
                currently_detecting = False
                print("Stop detecting...")

            # Process hand frame in model
            landmarks = prepare_landmarks_to_model(hand.landmark)
            logits = live_wrapper.step(landmarks)
            probs = torch.softmax(logits.squeeze(), dim=0)
            label_idx = probs.argmax().item()
            
            # Draw predicted label on image
            text = f"{labels[label_idx]} {(probs.max().item() * 100):.2f}%"
            draw_label_on_image(hand.landmark, image, text)
            
        else:
            # Start detecting when press s
            if key == 's':
                currently_detecting = True
                live_wrapper.reset()
                print("Start detecting...")


    # Check exit
    if key == 'q':
        print("Stop runing...")
        break

    # Show image
    cv2.imshow('Hand Tracking', image) 



cap.release()  # Release the camera resource.
cv2.destroyAllWindows()  # Close OpenCV windows.
hands.close()  # Release hands model.