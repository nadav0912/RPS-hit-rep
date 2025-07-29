import numpy as np
import mediapipe as mp
import torch
import cv2
import math
from pathlib import Path
from .hyperparams import MODEL_PATH
from landmark_hand_models.hand_landmark.hand_landmark import HandLandmark
from landmark_hand_models.palm_detection.palm_detection import PalmDetection

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


def landmarks_to_list(landmarks) -> list[list[float]]:
    return [[lm.x, lm.y, lm.z] for lm in landmarks]



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
    batch = tensor_lm.unsqueeze(dim=0).unsqueeze(dim=0)  # reshape the tensor from shape (63) to (1, 1, 63)

    return batch
 

def get_label_list_from_example(live_wrapper: LiveGRUWrapper, example: list[list[float]]) -> list[list[float]]:
    """
    Predicts a label for each frame in the example using the LiveGRUWrapper.
    Args:
        live_wrapper: The model that processes each frame sequentially.
        example: A list of frames, each a list of integers (features).
    Returns:
        A list of probabilities [_, _, _], one per frame.
    """
    probs_list = []

    live_wrapper.reset()

    for frame in example:
        logits = live_wrapper.step(frame.unsqueeze(dim=0).unsqueeze(dim=0))
        probs = torch.softmax(logits.squeeze(), dim=0).tolist()
        probs_list.append(probs)

    return probs_list


def MSS(landmarks1: list[list[float]], landmarks2: list[list[float]]) -> float:
    """Calculate the Mean Squared Error (MSE) between two sets of 3D landmarks."""
    sum = 0.0

    for i in range(len(landmarks1)):
        x1, y1, z1 = landmarks1[i]
        x2, y2, z2 = landmarks2[i]
        sum += (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

    return sum / len(landmarks1)  # Return the average squared distance


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


if __name__ == "__main__":
    landmarks = [
        [0.6955205145482962, 1.0, 1.0],
        [0.9773422803717327, 0.7087313536640676, 0.927950594908701],
        [1.0, 0.39765544258018215, 0.8454478169405663],
        [0.8294236834470431, 0.1896141443697501, 0.753668469299306],
        [0.6404385546227925, 0.1004877962582955, 0.663164808172139],
        [0.9882265959139362, 0.0729419877674871, 0.9192629502553304],
        [0.7703548633143349, 0.12597317981449604, 0.584617913080347],
        [0.7359798925606686, 0.3182530768181693, 0.2312666416408709],
        [0.7768843997716446, 0.48688826674653124, 0.0],
        [0.7301417394315448, 0.0, 0.827370213623545],
        [0.5316006635408185, 0.1613341041897648, 0.7344558560081608],
        [0.5201045146980374, 0.33079595608474405, 0.5855316837626131],
        [0.5895575380670279, 0.4533075313911799, 0.4227411205378104],
        [0.4642522063434128, 0.040204905238576595, 0.7194609288473441],
        [0.272090340754883, 0.22453126748642657, 0.5369016638261388],
        [0.286380684317414, 0.39370200931642824, 0.42789409500377945],
        [0.3752404048628464, 0.5065734238485521, 0.3134015591914682],
        [0.20456933018876752, 0.12121687178787795, 0.6047103867117644],
        [0.0, 0.29701133041150957, 0.3080773066708457],
        [0.018719408334971127, 0.46446554230973297, 0.24717408582888584],
        [0.09953463233849005, 0.5548152323284863, 0.2646875238137384]
    ]

    normalize_landmarks(landmarks)