import numpy as np
import cv2
import math
import pandas as pd
import os
import torch
from pathlib import Path
from final_models.hand_landmark.hand_landmark import HandLandmark
from final_models.palm_detection.palm_detection import PalmDetection

dataset_path = "C:\Data\Projects\Repositories\RPS-hit-rep\Experiments\static hand gesture with jap model\hand-dataset.csv"

def hand_dataset() -> pd.DataFrame:
    return pd.read_csv(dataset_path)

def save_model(model: torch.nn.Module, model_name: str):
    MODEL_PATH = Path("C:\Data\Projects\Repositories\RPS-hit-rep\Experiments\static hand gesture with jap model\models") 
    MODEL_PATH.mkdir(parents=True, exist_ok=True) 
    model_name += '.pth'
    MODEL_SAVE_PATH = MODEL_PATH / model_name
    print(f"Saving model to: {MODEL_SAVE_PATH}")
    torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)  


def add_examples_to_dataset(data: list):
    df = pd.DataFrame(data)

    print("\n\nThe new data you create:")
    print(df.groupby(['hand-side', 'label']).size())

    # Save new data to datset
    if os.path.exists(dataset_path):
        df.to_csv(dataset_path, mode='a', header=False, index=False)  # mode='a' for append mode
    else:
        df.to_csv(dataset_path, mode='w', header=True, index=False)  # mode='w' for write mode


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


def hand_from_image_v2(frame: np.ndarray, palm_detector: PalmDetection, hand_landmark_model: HandLandmark):
    # Detect palm(s)
    hands = palm_detector(frame)
    if hands is None or len(hands) == 0:
        return None, [None]

    images = []
    rects = []

    h, w = frame.shape[:2]

    for hand in hands:
        sqn_rr_size, rotation, cx_norm, cy_norm = hand

        cx = int(cx_norm * w)
        cy = int(cy_norm * h)
        size = int(sqn_rr_size * frame.shape[1])  # convert size from normalized to pixels

        # Crop square region from frame
        xmin = max(cx - size // 2, 0)
        ymin = max(cy - size // 2, 0)
        xmax = min(cx + size // 2, w)
        ymax = min(cy + size // 2, h)

        #print(xmin, ymin, xmax, ymax)
        hand_crop = frame[ymin:ymax, xmin:xmax]         

        if hand_crop.shape[0] == 0 or hand_crop.shape[1] == 0:
            print("hand_crop is empty")
            continue

        images.append(hand_crop)
        rects.append([cx, cy, size, size, rotation])

    if not images:
        return None, [None]

    hand_sides = ["left", "right"]

    rects = np.array(rects, dtype=np.float32)

    # Run hand landmark model
    landmarks, sizes = hand_landmark_model(images, rects)

    if len(landmarks) == 0 or len(sizes) == 0:
        return None, [None]

    #print("landmarks:", landmarks, "sizes:", int(sizes[0][2][0]))

    return landmarks, hand_sides[int(sizes[0][2][0])]


def get_rotation_angle(wrist: list, index_mcp: list) -> float:
    """
    Calculate the angle (in radians) between the wrist and the index MCP joint (מפרק היד לתחילת הזרת).
    The angle is measured in the XY plane using atan2(dy, dx).
    """
    dx = index_mcp[0] - wrist[0]
    dy = index_mcp[1] - wrist[1]
    angle = math.atan2(dy, dx)  # returns the angle in radians
    #print((angle * 180) / math.pi)
    return angle


def rotate_landmarks(landmarks: list[list[float]], angle_rad:float, center:list) -> list[list[float]]:
    """
    Rotates all landmarks by -angle_rad around the center (usually the wrist).
    The rotation is in the XY plane (Z stays the same).
    """

    # Pre-compute cosine and sine of the negative angle for rotation
    # We use -angle_rad because we want to undo the current hand rotation
    cos_angle = math.cos(-angle_rad)
    sin_angle = math.sin(-angle_rad)
    rotated = []

    for x, y, z in landmarks:
        # Step 1: Translate the point so that the rotation center is at the origin (0, 0)
        tx = x - center[0]
        ty = y - center[1]

        # Step 2: Apply 2D rotation formula 
        # This rotates the point (tx, ty) by -angle_rad
        rx = tx * cos_angle - ty * sin_angle
        ry = tx * sin_angle + ty * cos_angle

        # Step 3: Translate the point back to its original coordinate system
        # Only X and Y are affected by rotation; Z remains unchanged
        rotated.append([rx + center[0], ry + center[1], z])

    return rotated


def normalize_position(landmarks: list[list[float]]) -> list[list[float]]:
    """
    Normalize the hand landmarks to remove differences in position and size.
    This moves the hand to start at (0, 0, 0) and scales it so all points are between 0 and 1.
    It helps make the hand look the same in every image, no matter where it is in the image or how big it is.
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


def normalize_landmarks(landmarks: list[list[float]]) -> list[list[float]]:
    """
    Get landmarks as list and return them ofter normalize all values inside.
    landmark format (input and output): [[x0, y0, z0], [x1, y1, z1], ...]
    """
    
    # Normalize angle
    print("landmarks:", len(landmarks))
    angle_rad = get_rotation_angle(wrist=landmarks[0], index_mcp=landmarks[2])
    center = landmarks[0]  # using wrist as the center of rotation

    rotated_landmarks = rotate_landmarks(landmarks, angle_rad, center)

    # Normalize position
    normalized_landmarks = normalize_position(rotated_landmarks)

    """new_angle = get_rotation_angle(normalized_landmarks[0], normalized_landmarks[2])
    print(math.degrees(new_angle))  # Should be close to 0"""

    return normalized_landmarks


