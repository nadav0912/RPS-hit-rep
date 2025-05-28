import cv2

def connect_camera():
    """Connect to the camera and return the VideoCapture object."""
    
    cap = cv2.VideoCapture(0)
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
