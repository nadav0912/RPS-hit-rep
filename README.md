# RPS-hit-project

## Requirements!
Follow the steps below to set up the project after pulling the repository:

1. **Open Your IDE with Admin Privileges**
   - Use **VS Code** or any other IDE.
   - Ensure it is launched with administrator rights for proper setup(Neccecary for python install).
   - Make sure you're in the main folder of the project

2. **Run the `setup_environment.cmd` File**
   - This script performs the following tasks:
     1. Creates a virtual environment named `venv/`.
     2. Downloads and installs **Python 3.12** within `venv/`.
     3. Installs all required libraries listed in `requirements.txt`.
     This may take a while, please be patient. it may seem as if your IDE's terminal is frozen, don't worry, wait and just let it do it's thing :)

3. **Activate the Virtual Environment**
   - Execute the following command:
     venv\Scripts\activate

4. **Select the correct Python interpreter(Instructions for VScode)**
   - Follow these steps while inside VScode, If using a different IDE figure it out on your own :)
     1. Ctrl + Shift + P
     2. Type in "Python: Select Interpreter" and press Enter
     3. Select the python version corresponding to ('venv')

---

Feel free to reach out for further assistance


## File Architecture

```plaintext
REPOSITORY/
├── Code/                              # Directory containing all Python code files
|   |
│   ├── class/                           # Directory for class definitions
│   │   ├── BionicHand.py                    # Class for controlling the bionic hand
│   │   ├── HandDetection.py                 # Class for hand gesture detection
│   │   ├── LLMagent.py                      # Class for interacting with a Large Language Model (LLM)
│   │   └── Game.py                          # Class for game logic and management
|   |   
│   ├── models/                          # Directory for trained machine learning models
|   |   |
│   │   ├── Hand-Gesture-Detection/         # Directory for hand gesture detection model
|   |   |   ├── Gesture-detection-model.py      # Neural Network Model for hand gesture detection
│   │   │   ├── parameters.pth                  # Configuration parameters for the hand gesture detection model
│   │   |   └── Train-gesture-detection.py      # Script to train the hand gesture detection model
|   |   |
│   │   └── hand-recognition/               # Directory for hand recognition models
│   │       ├── Hand-recognition-model.py       # Neural Network Model for hand recognition
│   │       ├── parameters.pth                  # Configuration parameters for the hand recognition model
│   │       └── Train-hand-recognition.py       # Script to train the hand recognition model
|   |
│   └── utils/                           # Directory for utility functions and helper scripts
│   |   ├── Environment-fetching.py         # Functions for fetching environment information
│   |   └── LLM-auxiliary-functions.py      # LLM-related utility functions
|   |
│   └── main.py                          # Main entry point of the application
```

---

## Hardware Structure

***Components used:***
  - Raspberry Pi 4b
  - PCA9685 Servo Controler
  - Sg90 Servo * 5
  - 6v Battery holder
  - Portable charger
  - USB Camera
  - USB Microphone
  - Bluetooth speaker

![screenshot](./Hardware/design-photo.png)
