import cv2
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

def on_result(result, output_image, timestamp_ms):
    # This function is called every time a result is ready
    if result.handedness:
        print(f"Hands detected: {len(result.handedness)}")
    else:
        print("No hands detected")

    # Draw landmarks on output_image (OpenCV uses BGR)
    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            for lm in hand_landmarks.landmark:
                x_px = int(lm.x * output_image.shape[1])
                y_px = int(lm.y * output_image.shape[0])
                cv2.circle(output_image, (x_px, y_px), 5, (0, 255, 0), -1)

    cv2.imshow('MediaPipe Hand Landmarker GPU Test', output_image)
    if cv2.waitKey(1) & 0xFF == 27:
        # Exit on ESC key
        raise KeyboardInterrupt

def main():
    base_options = python.BaseOptions(model_asset_path='hand_landmarker.task', delegate='GPU')

    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.LIVE_STREAM,
        num_hands=2,
        result_callback=on_result  # Add the callback here
    )
    hand_landmarker = vision.HandLandmarker.create_from_options(options)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Convert BGR to RGB for MediaPipe input
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Send frame to the hand landmarker asynchronously
            hand_landmarker.send(rgb_frame, int(time.time() * 1000))

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
