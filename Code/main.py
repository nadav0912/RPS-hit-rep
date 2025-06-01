# -------------------- IMPORTS -------------------- #
# Libraries
import cv2 
import time

# Importing main classes
from .classes.BionicHandControl import BionicHandControlTest
from .classes.HandDetection import HandDetection
from .classes.GestureClassifier import GestureClassifier
from .classes.MovePredictor import MovePredictor

from .utils import *
from .main_hyperparmeters import *



# -------------------- INITIALIZATION -------------------- #
bionicHandControl = BionicHandControlTest()
handDetection = HandDetection()
gestureClassifier = GestureClassifier()
movePredictor = MovePredictor()

camera = connect_camera()  # Connected to defult camera

game_status = "idle"  # Game state: 
                      # "idle"   - waiting to start,
                      # "active" - currently playing (hand detection and prediction in progress),
                      # "result" - round completed, result is being shown or processed

frame_counter = 0

bionic_hand_gesture = None  # Opponent's gesture, used for result state






# -------------------- AUXILIARY FUNCTIONS -------------------- #
def idle_state(key: str):
    global game_status

    if key == 's':
        bionicHandControl.ledOn()

        for _ in range(2):
            time.sleep(1) 
            bionicHandControl.ledOff()
            time.sleep(1) 
            bionicHandControl.ledOn()

    game_status = "active"
    print("Active state: Hand detection and Move prediction in progress...")


def active_state(image: cv2.Mat):
    global game_status, frame_counter, bionic_hand_gesture

    # Hand detection
    landmarks = handDetection.landmarks_from_image(image)

    if landmarks:
        frame_counter += 1

        # Pass through GRU model
        gesture, prob = movePredictor.predict(landmarks)

        # Check stop condition
        if prob > DETECTION_PROB_TRESHOLD and frame_counter > DETECTION_FRAME_TRESHOLD:
            bionic_hand_gesture = counterGesture(gesture) # Save bionic hand gesture
            bionicHandControl.move(bionic_hand_gesture) # Tell bionic hand to make counter move
            movePredictor.reset() # Reset previous information in GRU model 
            frame_counter = 0
            game_status = "result"


def result_state():
    global game_status, bionic_hand_gesture

    # Hand detection
    landmarks = handDetection.landmarks_from_image(image)

    if landmarks:
        time.sleep(1)
        # Predict gesture using the classifier
        gesture = gestureClassifier.predict(landmarks)
    
        print(f"Opponent's gesture: {gesture}, Hand gesture: {bionic_hand_gesture}")
        print(f"Result: {check_robot_win(gesture, bionic_hand_gesture)}")
        
        bionicHandControl.ledOff()
        bionicHandControl.move("idle")

        game_status = "idle"
        print("Press 's' to start a new game...")
        




# -------------------- MAIN LOOP -------------------- #
print("Once the game starts, wait for the third blink of the led and make your move!")
print("Press 'q' stop the program completely...")
print("Press 's' to start a new game...")
bionicHandControl.move("idle")  # Initial move to start the game

while camera.isOpened():
    success, image = camera.read()

    # Get key press
    key = check_key_press()

    # Run Main Cycle
    if game_status == "idle":
        idle_state(key)
    elif game_status == "active":
        active_state(image)
    elif game_status == "result":
        result_state()


    # Check exit
    if key == 'q':
        print("Stop runing...")
        break


camera.release()  # Release the camera resource.