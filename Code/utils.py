import cv2
import math
import torch

def connect_camera(camera_index: int = 0) -> cv2.VideoCapture:
    """Connect to the camera and return the VideoCapture object."""
    
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    return cap


def check_key_press(delay: int = 1) -> str:
    """
    Waits briefly and returns the pressed key as a lowercase letter.
    Requires an active OpenCV window to detect key presses.
    """
    key_code = cv2.waitKey(delay) & 0xFF

    if key_code != 255:
        print(f"Key pressed: {chr(key_code)}")
        return chr(key_code).lower()

    return ''


def counterGesture(gesture: str) -> str:
    """
    Returns the counter gesture for the given gesture.
    """
    counter_gestures = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    
    return counter_gestures[gesture]


def check_robot_win(gesture: str, opponent_gesture: str) -> str:
    """
    Checks the result of the game based on the player's gesture and the opponent's gesture.
    Returns 'win', 'lose', or 'draw'.
    """
    if gesture == opponent_gesture:
        return "draw"
    
    elif (gesture == 'rock' and opponent_gesture == 'scissors') or \
         (gesture == 'paper' and opponent_gesture == 'rock') or \
         (gesture == 'scissors' and opponent_gesture == 'paper'):
        return "win"
    else:
        return "lose"
   

def landmarks_to_tensor(landmarks: list[list[float]]) -> torch.tensor:
    """
    Converts the list to a tensor and reshapes it to (1, 1, 63).
    """

    tensor_lm = torch.tensor(landmarks, dtype=torch.float32).flatten()  # tensor with one dim in size 63
    batch = tensor_lm.unsqueeze(dim=0).unsqueeze(dim=0)  # reshape the tensor from shape (63) to (1, 1, 63)

    return batch


def get_rotation_angle(p1: list, p2: list) -> float:
    """
    Calculate the angle (in radians) between two points.
    The angle is measured in the XY plane using atan2(dy, dx).
    """
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    angle = math.atan2(dy, dx)  # returns the angle in radians
    #print((angle * 180) / math.pi)
    return angle



