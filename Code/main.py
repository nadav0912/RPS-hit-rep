# -------------------- IMPORTS -------------------- #
# Libraries
import cv2 
import time

# Importing main classes
from .classes.BionicHand import HandControlTest
from .classes.HandLandmark import HandLandmark
from .classes.GestureClassifier import GestureClassifier
from .classes.MovePredictor import MovePredictor

from .utils import *



# -------------------- INITIALIZATION -------------------- #
BionicHand = HandControlTest()
HandDetection = HandLandmark()
GestureClassifier = GestureClassifier()
MovePredictor = MovePredictor()

camera = connect_camera()  # Connected to defult camera

game_status = "idle"  # Game state: 
                      # "idle"   - waiting to start,
                      # "active" - currently playing (hand detection and prediction in progress),
                      # "result" - round completed, result is being shown or processed



# -------------------- AUXILIARY FUNCTIONS -------------------- #
def idle_state():
    pass


def active_state():
    pass


def result_state():
    pass


def run_correct_state():
    """
    Run the correct state function based on the current game status.
    """
    global game_status

    if game_status == "idle":
        idle_state()
    elif game_status == "active":
        active_state()
    elif game_status == "result":
        result_state()



# -------------------- MAIN LOOP -------------------- #
while camera.isOpened():
    success, image = camera.read()

    # Get key press
    key = check_key_press()

    # Run Main Cycle
    run_correct_state()

    # Check exit
    if key == 'q':
        print("Stop runing...")
        break

    # Show image
    cv2.imshow('Hand Tracking', image) 



camera.release()  # Release the camera resource.
cv2.destroyAllWindows()  # Close OpenCV windows.








