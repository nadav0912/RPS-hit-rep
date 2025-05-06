import numpy as np
import mediapipe as mp
import cv2


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
        image - Same image from input, only change is flip on horizontal the image.
    """

    if not success:
        raise Exception("Failed to capture image from computer webcam.")

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    image = cv2.flip(image, 1)  # flip on horizontal

    # Get predicted landmarks. 
    results = hands_model.process(image)

    # If find hand in image save it in hand
    hand = None if not results.multi_hand_landmarks else results.multi_hand_landmarks[0]

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # RGB -> BGR

    return hand, image


def landmarks_to_list(landmarks) -> list[list[int]]:
    return [[lm.x, lm.y, lm.z] for lm in landmarks]


def normalize_landmarks(landmarks: list[list[int]]) -> list[list[int]]:
    """
    Get landmarks as list and return them ofter normalize all values inside.
    landmark format (input and output): [[x0, y0, z0], [x1, y1, z1], ...]
    """
    landmarks = np.array(landmarks)

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