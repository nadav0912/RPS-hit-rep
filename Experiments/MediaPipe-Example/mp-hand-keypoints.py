import mediapipe as mp
import numpy as np
import cv2
import os
import json

###########################################################################################
#   General Setup                                                                       
###########################################################################################
data_dir = 'data'
runs_dir = 'result'
input = 'hand1.jpg'                 # Change depending on your image
hand_keypoints = []

if not os.path.exists(runs_dir):
    os.makedirs(runs_dir)

# Make output names
name, ext = os.path.splitext(input)
output_image_filename = f"{name}_output.jpg"                
keypoints_output_filename = f"{name}_keypoints.json"

# Paths
input_image_path = f".\\{data_dir}\\{input}"
output_image_path = f".\\{runs_dir}\\{output_image_filename}"
keypoints_output_path = f".\\{runs_dir}\\{keypoints_output_filename}"

print(f"Processing file '{input}...'\n")

###########################################################################################
#   Code                                                                   
###########################################################################################

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,        # Static image mode
    max_num_hands=1,               # Maximum number of hands to detect
    min_detection_confidence=0.5   # Minimum confidence for detection
)

# Initialize MediaPipe Drawing  
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Read the image using OpenCV
image = cv2.imread(input_image_path)

# Convert the BGR image to RGB before processing
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Process the image and detect hands
results = hands.process(rgb_image)

###########################################################################################
#   Results                                                              
###########################################################################################

for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
    # Draw hand landmarks on the image using OpenCV
    mp_drawing.draw_landmarks(
        image,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style()
    )
    
    # Extract keypoints
    keypoints = []
    for lm in hand_landmarks.landmark:
        # Each landmark has x, y, z normalized coordinates
        keypoints.append((lm.x, lm.y, lm.z))
    
    # Append to the main list with hand index
    hand_keypoints.append({
        'hand_id': idx,
        'keypoints': keypoints
    })

cv2.imwrite(output_image_path, image)
print(f"Annotated image saved as '{output_image_filename}'.")

with open(keypoints_output_path, 'w') as f:
    json.dump(hand_keypoints, f, indent=4)
print(f"Hand keypoints saved as '{keypoints_output_filename}'.")

for hand in hand_keypoints:
    print(f"Hand {hand['hand_id']} keypoints:")
    for idx, point in enumerate(hand['keypoints']):
        print(f"  Landmark {idx}: (x={point[0]:.4f}, y={point[1]:.4f}, z={point[2]:.4f})")
    print()