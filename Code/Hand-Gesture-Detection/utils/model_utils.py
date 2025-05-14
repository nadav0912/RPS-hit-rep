import numpy as np
import mediapipe as mp
import torch
import cv2
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models_state_dicts"

class LiveGRUWrapper:
    def __init__(self, model):
        self.model = model
        self.h_n = None

    def reset(self):
        self.h_n = None

    def step(self, row_tensor):
        # row_tensor: (batch size: 1, sequence size: 1, input size: 63)
        self.model.eval()
        with torch.inference_mode():
            output, self.h_n = self.model(row_tensor, self.h_n)

        return output



def hand_from_image(success: bool, frame: np.ndarray, hands_model: mp.solutions.hands.Hands):
    """
    If the frame is successfully captured, processes the image using the hands model.
    Work only on 1 hand in image.
    input: 
        success - Is frame successfully taken.
        frame - The image itself.
        hands_model - A instance of the Hands landmarks model from mediapipe
    return: 
        hand - The hand that found in image. if not found so None
        hand_side - string "right" or "left" if found hand in image. else it be None
        image - Same image from input, only change is flip on horizontal the image.
    """

    if not success:
        raise Exception("Failed to capture image from computer webcam.")

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    image = cv2.flip(image, 1)  # flip on horizontal
    image.flags.writeable = False

    # Get predicted landmarks. 
    results = hands_model.process(image)

    # If find hand in image save hand and hand_side
    hand = None if not results.multi_hand_landmarks else results.multi_hand_landmarks[0]
    hand_side = None if not results.multi_handedness else results.multi_handedness[0].classification[0].label

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # RGB -> BGR

    return hand, hand_side, image


def landmarks_to_list(landmarks) -> list[list[int]]:
    return [[lm.x, lm.y, lm.z] for lm in landmarks]


def normalize_landmarks(landmarks: list[list[int]]) -> list[list[int]]:
    """
    Get landmarks as list and return them ofter normalize all values inside.
    landmark format (input and output): [[x0, y0, z0], [x1, y1, z1], ...]
    """
    landmarks = np.array(landmarks, dtype=float)

    # Find min & max for x, y and z  
    x_coordinates, y_coordinates, z_coordinates= landmarks[:, 0], landmarks[:, 1], landmarks[:, 2]

    x_min, x_max = np.min(x_coordinates), np.max(x_coordinates)
    y_min, y_max = np.min(y_coordinates), np.max(y_coordinates)
    z_min, z_max = np.min(z_coordinates), np.max(z_coordinates)

    # Subtract the minimum value of x, y, and z from their respective coordinates.
    landmarks[:, 0] -= x_min
    landmarks[:, 1] -= y_min
    landmarks[:, 2] -= z_min

    # Calculate width, height, and depth
    width, height, depth = (x_max - x_min), (y_max - y_min), abs(z_max - z_min)

    # Normalize the landmarks coordinates (x, y, z) by their respective bounding box dimensions (width, height, depth).
    landmarks[:, 0] /= width
    landmarks[:, 1] /= height
    landmarks[:, 2] /= depth

    """print(f"width: {width}, hight: {height}, depth: {depth}")
    print(f"x range: {x_min} to {x_max}, y range: {y_min} to {y_max}, z range: {z_min} to {z_max}")
    print("\n\n", landmarks)"""

    return landmarks.tolist()


def prepare_landmarks_to_model(landmarks) -> torch.tensor:
    """
    Converts MediaPipe hand landmarks (hand.landmark) to a tensor for live GRU model.
    1. Converts landmarks to a list of normalized coordinates.
    2. Converts the list to a tensor and reshapes it to (1, 1, 63).

    Args: landmarks (list): List of MediaPipe NormalizedLandmark objects from `hand.landmark`.

    Returns: torch.tensor: A tensor with shape (1, 1, 63) ready for model input.
    """
    lm = landmarks_to_list(landmarks)
    normalized_lm = normalize_landmarks(lm)
    tensor_lm = torch.tensor(normalized_lm, dtype=torch.float32).flatten()  # tensor with one dim in size 63 (given list in the format [[x, y, z], ...])
    batch = tensor_lm.unsqueeze(dim=0).unsqueeze(dim=0)  # reshape the tensor from shape (63,) to (1, 1, 63)

    return batch
 

def save_model(model: torch.nn.Module, model_name: str):
    MODEL_PATH.mkdir(parents=True, exist_ok=True) 
    model_name += '.pth'
    MODEL_SAVE_PATH = MODEL_PATH / model_name
    print(f"Saving model to: {MODEL_SAVE_PATH}")
    torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)  


def load_model(model: torch.nn.Module, model_name: str):
    model_name += '.pth'
    MODEL_SAVE_PATH = MODEL_PATH / model_name
    model.load_state_dict(torch.load(f=MODEL_SAVE_PATH))