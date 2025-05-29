from pathlib import Path
from Gesture_detection_model import GRUModelV1

# try1modelV1   train_70_percent  3l_190ep_70per
TRAINED_MODEL = "3l_190ep_70per"

# Paths
DATASET_PATH = Path(__file__).resolve().parent.parent / "data"
MODEL_PATH = Path(__file__).parent.parent / "models_state_dicts"

# Maps
LABEL_MAP = {
    'rock': 0,
    'paper': 1,
    'scissors': 2
}

LABEL_LIST = ['rock', 'paper', 'scissors']


# Parameters
NUM_LAYERS = 3          # Numer of GRU layers
HIDDEN_SIZE = 128       # Size of hidden state output vector
INPUT_SIZE = 63         # Size of input vector
OUTPUT_SIZE = 3         # Number of classes/labels
DROP_OUT = 0.3

TEST_SIZE = 0.3
BATCH_SIZE = 200        # Training batch size
EPOCHS = 190            # Training number of epocs
LEARNING_RATE = 1e-4    # Training learning rate, currently: 10^(-3)
RANDOM_SEED = 142        # Training number seed

MODEL = GRUModelV1(
        input_size=INPUT_SIZE,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        num_classes=OUTPUT_SIZE,
        dropout_prob=DROP_OUT
)