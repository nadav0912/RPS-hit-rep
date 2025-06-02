import cv2
import mediapipe as mp
import math
import numpy as np
from utils import get_rotation_angle


class HandLandmarksDetection():
    def __init__(self):
        mp_hands = mp.solutions.hands
        
        # Hand detection model
        self.hands_model = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=1)


    def landmarks_from_image(self, frame: cv2.Mat) -> list[list[float]]:
        # get landmarks from image
        landmarks = self.hand_from_image(frame)

        if not landmarks:
            return None

        # Convert landmarks to list of dots
        landmarks = self.landmarks_to_list(landmarks.landmark)
        
        # Choose points for rotation and center
        angle_rad = get_rotation_angle(landmarks[0], landmarks[2])
        center = landmarks[0]  

        # Normalize angle
        rotated_landmarks = self.normalize_rotation(landmarks, angle_rad, center)

        # Normalize position
        normalized_landmarks = self.normalize_position(rotated_landmarks)

        return normalized_landmarks


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
    

    def landmarks_to_list(self, landmarks) -> list[list[float]]:
       return [[lm.x, lm.y, lm.z] for lm in landmarks]


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