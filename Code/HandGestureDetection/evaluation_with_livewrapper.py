# Running an example the same way we run it through our live wrapper
# This is a test to see if the live wrapper works as intended

import numpy as np
import torch
import matplotlib.pyplot as plt

from torch.utils.data import DataLoader, Subset
from torchmetrics.classification import ConfusionMatrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from utils import handDataset, LiveGRUWrapper
from utils import collate_func, confusion_matrix_heat_map, load_model
from utils import TEST_SIZE, BATCH_SIZE, RANDOM_SEED, TRAINED_MODEL, INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE

from Gesture_detection_model import GRUModelV1

dataset = handDataset()

# Create list of indices
indexes = np.arange(len(dataset))

# Split indices
train_indexes, test_indexes = train_test_split(indexes, test_size=TEST_SIZE, random_state=RANDOM_SEED)
print(f"{len(train_indexes)} in train, {len(test_indexes)} in test.")

# Split dataset
test_subset =  Subset(dataset, test_indexes)

# Create dataloader
test_dataloader = DataLoader(
        test_subset,
        batch_size=BATCH_SIZE,  
        shuffle=True,
        collate_fn=collate_func
)

model = GRUModelV1(
        input_size=INPUT_SIZE,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        num_classes=OUTPUT_SIZE,
        dropout_prob=0.3
)

load_model(model, model_name=TRAINED_MODEL)
live_wrapper = LiveGRUWrapper(model)

test_batch, test_label = next(iter(test_dataloader))
pred_labels = []

for idx, example in enumerate(test_batch):
    live_wrapper.reset()
    
    for frame in example:
        logits = live_wrapper.step(frame.unsqueeze(dim=0).unsqueeze(dim=0))

    probs = torch.softmax(logits.squeeze(), dim=0)
    pred_labels.append(probs.argmax().item())

pred_labels = torch.tensor(pred_labels)

report = classification_report(y_true=test_label, y_pred=pred_labels)
print(report)

confmat_fn = ConfusionMatrix(task="multiclass", num_classes=OUTPUT_SIZE)
confusion_matrix_heat_map(confmat_fn, pred_labels, test_label)

plt.show()

