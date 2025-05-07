import mediapipe as mp
import cv2  # To use computer camera
import numpy as np


# Initialize hand detection model and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create an instance of the Hands model
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=5)

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():  # Continue looping if the camera is still open
    ret, frame = cap.read()   # Read a frame from the camera. 'ret' is a boolean (True if the frame was read correctly), 'frame' is the image itself.

    # Detection
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB (MediaPipe uses RGB format while the image captured by OpenCV in BGR format)
    image = cv2.flip(image, 1)  # flip on horizontal
    image.flags.writeable = False  # A flag that make the image to read-only befor sending to the model 
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #print(results.multi_hand_landmarks)  # a list with all the landmarks. each one have x, y and z.  (z is depth from the camera)


    # Rendering results
    if results.multi_hand_landmarks:
        for num, hand in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                      mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=1, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=1, circle_radius=1))


    # Show the current frame in a window titled "Hand Tracking".
    cv2.imshow('Hand Tracking', image)  

    # Exit: Wait for 10ms, if 'q' key is pressed, break the loop
    if cv2.waitKey(10) % 0xFF == ord('q'): 
        break


cap.release()  # Release the camera resource (stop using the webcam).
cv2.destroyAllWindows()  # Close all OpenCV windows.

# Manually release the hands model
hands.close()
