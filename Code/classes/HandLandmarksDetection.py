import cv2
import mediapipe as mp
import math
import numpy as np

from final_models.palm_detection.palm_detection import PalmDetection
from final_models.hand_landmark.hand_landmark import HandLandmark
from utils import get_rotation_angle


class HandLandmarksDetection():
    def __init__(self):
        
        self.palm_detector = PalmDetection()

        self.hand_landmark_model = HandLandmark()
        
        """
        mp_hands = mp.solutions.hands
        
        # Hand detection model
        self.hands_model = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1)
        """


    def landmarks_from_image(self, frame: cv2.Mat) -> list[list[float]]:
        # get landmarks from image
        landmarks = self.hands_recognition(frame)

        print(f"Landmarks: {landmarks}")

        if not landmarks or len(landmarks[0]) != 21:
            return None

        landmarks = landmarks[0]  # take only first hand landmarks

        # Choose points for rotation and center
        angle_rad = get_rotation_angle(landmarks[0], landmarks[2])
        center = landmarks[0]  

        # Normalize angle
        rotated_landmarks = self.normalize_rotation(landmarks, angle_rad, center)

        # Normalize position
        normalized_landmarks = self.normalize_position(rotated_landmarks)

        return normalized_landmarks
    

    def hands_recognition(self, frame: cv2.Mat) -> list[list[float]]:
        # Detect palm(s)
        hands = self.palm_detector(frame)
        if hands is None or len(hands) == 0:
            return None

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
            return None

        rects = np.array(rects, dtype=np.float32)

        # Run hand landmark model
        landmarks, sizes = self.hand_landmark_model(images, rects)

        if len(landmarks) == 0 or len(sizes) == 0:
            return None
        #print(sizes) # rotated_image_width, rotated_image_height, left_hand_0_or_right_hand_1]

        return landmarks


    def normalize_rotation(self, landmarks: list[list[float]], angle_rad:float, center:list) -> list[list[float]]:
        """
        Rotates all landmarks by -angle_rad around the center (point 0 the wrist).
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


    def normalize_position(self, landmarks: list[list[float]]) -> list[list[float]]:
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

        return landmarks.tolist()
    



"""
    def landmarks_to_list(self, landmarks) -> list[list[float]]:
       return [[lm.x, lm.y, lm.z] for lm in landmarks]

    def hand_from_image(self, frame: cv2.Mat):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB
        image = cv2.flip(image, 1)  # flip on horizontal
        image.flags.writeable = False

        # Get predicted landmarks. 
        results = self.hands_model.process(image)

        # If find hand in image save hand else None
        hand = None if not results.multi_hand_landmarks else results.multi_hand_landmarks[0]

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # RGB -> BGR

        return hand
"""