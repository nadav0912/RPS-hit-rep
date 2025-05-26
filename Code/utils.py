import cv2

def connect_camera():
    """Connect to the camera and return the VideoCapture object."""
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    return cap