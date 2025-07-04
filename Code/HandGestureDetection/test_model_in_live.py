import mediapipe as mp
import cv2 
import numpy as np
import torch
import time

from Gesture_detection_model import GRUModelV1
from pathlib import Path
from utils import NUM_LAYERS, HIDDEN_SIZE, INPUT_SIZE, OUTPUT_SIZE, TRAINED_MODEL, LABEL_LIST
from utils import LiveGRUWrapper, LiveONNXGRUWrapper
from utils import draw_label_on_image, load_model, hand_from_image, landmarks_to_list, prepare_landmarks_to_model, check_key_press, MSS
from utils import TRAINED_MODEL, LABEL_LIST


'''
MODEL = GRUModelV1(
        input_size=INPUT_SIZE,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        num_classes=OUTPUT_SIZE,
        dropout_prob=DROP_OUT
)
load_model(MODEL, model_name=TRAINED_MODEL)
live_wrapper = LiveGRUWrapper(MODEL)
'''

#Path to ONNX file
onnx_path = Path(__file__).parent / "models_state_compiled" / f"{TRAINED_MODEL}.onnx"
if not onnx_path.exists():
    raise FileNotFoundError(f"ONNX file not found: {onnx_path}")

print(f"Found ONNX model at: {onnx_path}, called {TRAINED_MODEL}.onnx")
live_wrapper = LiveONNXGRUWrapper(onnx_path)

# Hand detection model and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create an instance of the Hands model
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=2)

# Computer camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Ensure MJPEG
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)


currently_detecting = False

prev_landmarks = None  # For calculate distance between previous and current landmarks
mss = 100

# For FPS calculation
start_time = time.time()
prev_time = start_time
count_frames = 0

sum_mediapip_time = 0.0

# -------- Main Loop -------- #
while cap.isOpened():
    success, frame = cap.read()

    start_mediapipe_time = time.time() # Measure time for mediapipe processing
    hand, hand_side, image = hand_from_image(success, frame, hands)
    end_mediapipe_time = time.time() 

    sum_mediapip_time += (end_mediapipe_time - start_mediapipe_time)

    key = check_key_press()
    
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


            # Calculate and print the Mean Squared Error (MSS) between previous and current landmarks
            landmarks_list = landmarks_to_list(hand.landmark)
            if prev_landmarks:
                mss = MSS(prev_landmarks, landmarks_list)
                #print(f"MSS: {mss:.7f}")

            prev_landmarks = landmarks_list

            if mss > 0.0001:
                print(f"Landmarks changed, MSS: {mss:.7f}")
                # Process hand frame in model
                landmarks = prepare_landmarks_to_model(hand.landmark)
                logits = live_wrapper.step(landmarks)
                logits = torch.tensor(logits, dtype=torch.float32)
                print(f"Logits: {logits}, {logits.shape}, {logits}")
                probs = torch.softmax(logits.squeeze(), dim=0)
                label_idx = probs.argmax().item()
                
                # Draw predicted label on image
                text = f"{LABEL_LIST[label_idx]} {(probs.max().item() * 100):.2f}%"

            draw_label_on_image(hand.landmark, image, text)

        else:
            # Start detecting when press s
            if key == 's':
                currently_detecting = True
                live_wrapper.reset()
                print("Start detecting...")

    # Measure and add to screen the FPS in live video
    count_frames += 1
    current_time = time.time()
    fps = 1 / (current_time - prev_time) # fps for this frame, 1 / time from previous frame
    prev_time = current_time
    cv2.putText(image, f"FPS: {fps:.2f}", (400, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


    # Check exit
    if key == 'q':
        print("Stop runing...")
        break
    
    # Show image
    cv2.imshow('Hand Tracking', image) 


# Take time when main loop stops
current_time = time.time()


cap.release()  # Release the camera resource.
cv2.destroyAllWindows()  # Close OpenCV windows.
hands.close()  # Release hands model.


# Calculate FPS and print results
total_time = current_time - start_time
fps = count_frames / total_time
print(f"\nProgram Run in total {(total_time):.4f} seconds\nNum frames: {count_frames}\nAvarage FPS: {fps:.2f}")
print(f"Avarge time between frames: {total_time/count_frames:.4f} seconds")

print(f"Total time for mediapipe processing: {sum_mediapip_time:.4f} seconds")
print(f"Average time for mediapipe processing: {sum_mediapip_time / count_frames:.4f} seconds per frame")
print(f"mediapipe time precentage from total time: {(sum_mediapip_time / total_time) * 100:.4f}%")

