import torch
import cv2
import numpy as np
from blazepalm import BlazePalm
from blazehand_landmark import BlazeHandLandmark
from blazebase import resize_pad, denormalize_detections

# Setup device
gpu = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
torch.set_grad_enabled(False)

# Load models
palm_detector = BlazePalm().to(gpu)
palm_detector.load_weights("blazepalm.pth")
palm_detector.load_anchors("anchors_palm.npy")
palm_detector.min_score_thresh = 0.75

hand_regressor = BlazeHandLandmark().to(gpu)
hand_regressor.load_weights("blazehand_landmark.pth")

# Open webcam
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Error: Unable to open camera")
    exit()

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Convert BGR to RGB and resize/pad
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img1, img2, scale, pad = resize_pad(frame_rgb)

    # Detect palms
    normalized_palm_detections = palm_detector.predict_on_image(img1)
    palm_detections = denormalize_detections(normalized_palm_detections, scale, pad)

    if len(palm_detections) > 0:
        # Convert detection to ROI params
        xc, yc, scale, theta = palm_detector.detection2roi(palm_detections.cpu())

        # Extract ROI for landmark model
        img, affine2, box2 = hand_regressor.extract_roi(frame_rgb, xc, yc, theta, scale)

        # Run landmark regressor
        flags, handedness, normalized_landmarks = hand_regressor(img.to(gpu))

        # Denormalize landmarks to original frame coordinates
        landmarks = hand_regressor.denormalize_landmarks(normalized_landmarks.cpu(), affine2)

        # Process detected hands
        for i, flag in enumerate(flags):
            if flag > 0.5:
                keypoints = landmarks[i].numpy()  # shape: (21, 3) - (x,y,z)
                # Print keypoints (x,y,z) for this hand
                print("Hand keypoints (x, y, z):")
                print(keypoints)

    # Break on ESC key
    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
