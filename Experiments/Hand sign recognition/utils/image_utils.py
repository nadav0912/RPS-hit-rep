import numpy as np
import cv2
import mediapipe as mp


def landmarks_from_image(success: bool, frame: np.ndarray, hands: mp.solutions.hands.Hands):

    """If the frame is successfully captured, processes the image using the hands model and returns the result."""

    if not success:
        raise Exception("Failed to capture image from computer webcam.")

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    image = cv2.flip(image, 1)  # flip on horizontal

    # Get predicted landmarks. 
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # RGB -> BGR

    return results, image


def draw_box_text(hand, image, label_text):
    """Get one hand and image and add to the image a box around the hand and label text. return image"""
    landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark])
    height, width, channels = image.shape

    x_coordinates = landmarks[:, 0]
    y_coordinates = landmarks[:, 1]

    x_min = int(np.min(x_coordinates) * width)
    x_max = int(np.max(x_coordinates) * width)
    y_min = int(np.min(y_coordinates) * height)
    y_max = int(np.max(y_coordinates) * height)


    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=1)
    cv2.putText(image, label_text, (x_min, y_max), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)

    return image

