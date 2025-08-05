from pathlib import Path

DETECTION_PROB_TRESHOLD = 0.7
DETECTION_FRAME_TRESHOLD = 10

LABEL_LIST = ['rock', 'paper', 'scissors']

MODELS__FOLDER_PATH = Path(__file__).parent / "final_models"
GRU_MODEL_PATH = MODELS__FOLDER_PATH / "GRU" / "front_hand_jap_v3.onnx"
STATIC_GESTURE_MODEL_PATH = MODELS__FOLDER_PATH / "static_gesture_classifier" /"static_gesture_classifier_parameters.pth"

# Hyperparameters for the GRU model
NUM_LAYERS = 3          # Numer of GRU layers
HIDDEN_SIZE = 256       # Size of hidden state output vector
INPUT_SIZE = 63         # Size of input vector
OUTPUT_SIZE = 3         # Number of classes/labels

# Hyperparameters for the static gesture classifier model
NUM_CLASSES = 3
NUM_FEATURES = 21*3
