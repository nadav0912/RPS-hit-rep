# RPS-hit-project

## Requirements!
Follow the steps below to set up the project after pulling the repository:

1. **Open Your IDE with Admin Privileges**
   - Use **VS Code** or any other IDE.
   - Ensure it is launched with administrator rights for proper setup(Neccecary for python install).

2. **Run the `setup_environment.cmd` File**
   - This script performs the following tasks:
     1. Creates a virtual environment named `venv/`.
     2. Downloads and installs **Python 3.12** within `venv/`.
     3. Installs all required libraries listed in `requirements.txt`.
     This may take a while, please be patient. it may seem as if your IDE's terminal is frozen, don't worry, wait and just let it do it's thing :)

3. **Activate the Virtual Environment**
   - Execute the following command:
     venv\Scripts\activate

---

Feel free to reach out for further assistance


## File Architecture
<br/>.<br/>
├── Code/                        # Directory containing all Python code files<br/>
│   ├── class/                   # Directory for class definitions<br/>
│   │   ├── BionicHand.py        # Class for controlling the bionic hand<br/>
│   │   ├── HandDetection.py     # Class for hand gesture detection<br/>
│   │   ├── LLMAgent.py          # Class for interacting with a Large Language Model (LLM)<br/>
│   │   └── Game.py              # Class for game logic and management<br/>
│<br/>
├── models/                      # Directory for trained machine learning models<br/>
│   ├── Hand-Gesture-Detection/  # Directory for hand gesture detection model<br/>
│   │   ├── Gesture-detection-model.py  # Neural Network Model for hand gesture detection<br/>
│   │   ├── parameters.pth              # Configuration parameters for the hand gesture detection model<br/>
│   │   └── Train-gesture-detection.py  # Script to train the hand gesture detection model<br/>
│   ├── hand-recognition/        # Directory for hand recognition models<br/>
│   │   ├── Hand-recognition-model.py   # Neural Network Model for hand recognition<br/>
│   │   ├── parameters.pth               # Configuration parameters for the hand recognition model<br/>
│   │   └── Train-hand-recognition.py    # Script to train the hand recognition model<br/>
│<br/>
├── utils/                       # Directory for utility functions and helper scripts<br/>
│   ├── Environment-fetching.py  # Functions for fetching environment information<br/>
│   └── LLM-auxiliary-functions.py # LLM-related utility functions<br/>
│<br/>
└── main.py                      # Main entry point of the application<br/>
