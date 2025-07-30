from pathlib import Path

# try1modelV1   train_70_percent  3l_190ep_70per front_hand_jap front_hand_jap_v2 front_hand_jap_v3
'''
front_hand_jap_v3: 
    FRAME_PERCENTAGE = 0.7

    NUM_LAYERS = 3          
    HIDDEN_SIZE = 256       
    INPUT_SIZE = 63         
    OUTPUT_SIZE = 3      

    TEST_SIZE = 0.3
    BATCH_SIZE = 200   
    EPOCHS = 200          
    LEARNING_RATE = 1e-3    
    RANDOM_SEED = 142      

                precision    recall  f1-score   support

           0       1.00      1.00      1.00        21
           1       1.00      0.95      0.98        21
           2       0.96      1.00      0.98        24

    accuracy                           0.98        66
   macro avg       0.99      0.98      0.99        66
weighted avg       0.99      0.98      0.98        66

'''


TRAINED_MODEL = "front_hand_jap_v3"

# Paths
DATASET_PATH = Path(__file__).resolve().parent.parent / "data_v2_front"
MODEL_PATH = Path(__file__).parent.parent / "models_state_dicts"

# Maps
LABEL_MAP = {
    'rock': 0,
    'paper': 1,
    'scissors': 2
}

LABEL_LIST = ['rock', 'paper', 'scissors']


# Parameters
FRAME_PERCENTAGE = 0.7  # percent of frames to use from each example from the begining

NUM_LAYERS = 3          # Numer of GRU layers
HIDDEN_SIZE = 256       # Size of hidden state output vector
INPUT_SIZE = 63         # Size of input vector
OUTPUT_SIZE = 3         # Number of classes/labels

TEST_SIZE = 0.3
BATCH_SIZE = 200        # Training batch size
EPOCHS = 300          # Training number of epocs
LEARNING_RATE = 1e-3    # Training learning rate, currently: 10^(-3)
RANDOM_SEED = 142        # Training number seed