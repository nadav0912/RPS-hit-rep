from pathlib import Path

# try1modelV1   train_70_percent
TRAINED_MODEL = "train_70_percent"

# Paths
DATASET_PATH = Path(__file__).resolve().parent.parent / "data"
MODEL_PATH = Path(__file__).parent.parent / "models_state_dicts"

# Maps
LABEL_MAP = {
    'rock': 0,
    'paper': 1,
    'scissors': 2
}

# Parameters
NUM_LAYERS = 2          # Numer of GRU layers
HIDDEN_SIZE = 128       # Size of hidden state output vector
INPUT_SIZE = 63         # Size of input vector
OUTPUT_SIZE = 3         # Number of classes/labels

TEST_SIZE = 0.4
BATCH_SIZE = 200        # Training batch size
EPOCHS = 130            # Training number of epocs
LEARNING_RATE = 1e-4    # Training learning rate, currently: 10^(-3)
RANDOM_SEED = 42        # Training number seed