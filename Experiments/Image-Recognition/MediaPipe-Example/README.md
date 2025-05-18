# MediaPipe Hand Recognition

This example uses Google's MediaPipe framework to detect and map hand keypoints in images. 
This example demonstrates how to process an input image to recognize hand landmarks and visualize the results.

In this example we:
- Detect and map 21 hand keypoints.
- Processes an input image to visualize hand landmarks.
- Saves output images with annotated keypoints.

## Result
As a result of running mp-hand-keypoints.py you'll get two files in the runs folder(Assuming you've only ran it once)
_keypoints.json - Json containins a list of dictionaries that contains the coordinates of keypoints
_output.jpg - Visual of the hand with the keypoints painted on using OpenCV

## Structure

```plaintext
mediapipe-hand-recognition/
├── data/
│   └── input_hand.jpg          # Input hand image
├── runs/
│   └──                         # Output files will be saved here
├── mp-hand_recognition.py      # Python script for processing the image
└── README.md                   # Project documentation
