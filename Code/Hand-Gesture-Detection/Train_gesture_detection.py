# ---------- IMPORTS ---------- #
import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader, Subset
from torchmetrics.classification import Accuracy, ConfusionMatrix
from tqdm.auto import tqdm 
from sklearn.model_selection import train_test_split

from utils import handDataset, collate_func
from Gesture_detection_model import GRUModelV1


# ---------- HYPERPARAMETERS ---------- #
NUM_LAYERS = 2
HIDDEN_SIZE = 128  # test 64 to 128
INPUT_SIZE = 63
OUTPUT_SIZE = 3

BATCH_SIZE = 200

EPOCHS = 100
LEARNING_RATE = 1e-3  # 10^(-3)

RANDOM_SEED = 42


# Device agonstic code
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device.")

label_map = {'rock': 0, 'paper': 1, 'scissors': 2}



# ---------- GET DATASET ---------- #
dataset = handDataset()

# Create list of indices
indexes = np.arange(len(dataset))

# Split indices
train_indexes, test_indexes = train_test_split(indexes, test_size=0.4, random_state=RANDOM_SEED)

# Split dataset
train_subset = Subset(dataset, train_indexes)
test_subset =  Subset(dataset, test_indexes)

# Create dataloaders
train_dataloader = DataLoader(
        train_subset,
        batch_size=BATCH_SIZE,  
        shuffle=True,
        collate_fn=collate_func
)

test_dataloader = DataLoader(
        test_subset,
        batch_size=BATCH_SIZE,  
        shuffle=True,
        collate_fn=collate_func
)


# ---------- INSTANCE OF THE MODEL ---------- #
torch.manual_seed(RANDOM_SEED)
model = GRUModelV1(
        input_size=INPUT_SIZE,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        num_classes=OUTPUT_SIZE,
        dropout_prob=0.3
)
print("\nMODEL:\n", model)



# ---------- LOSS & OPTIMIZER ---------- #
loss_fn = nn.CrossEntropyLoss()

accuracy_fn = Accuracy(task="multiclass", num_classes=OUTPUT_SIZE)
confmat_fn = ConfusionMatrix(task="multiclass", num_classes=OUTPUT_SIZE)

optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)


# ---------- TRAINING & TESTING ---------- #
def train():
        model.train()

        for batch, labels in train_dataloader:
                y_logits = model(batch)
                y_preds = torch.softmax(y_logits, dim=1).argmax(dim=1)

                loss = loss_fn(y_logits, labels)
                acc = accuracy_fn(y_preds, labels)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        return loss, acc


def test():
        model.eval()
        with torch.inference_mode():
                for batch, labels in test_dataloader:
                        y_logits = model(batch)
                        y_preds = torch.softmax(y_logits, dim=1).argmax(dim=1)
                        
                        loss = loss_fn(y_logits, labels)
                        acc = accuracy_fn(y_preds, labels)

        return loss, acc



# ---------- MAIN LOOP ---------- #
for epoch in tqdm(range(EPOCHS)):
        train_loss, train_acc = train()
        test_loss, test_acc = test()

        if epoch % 10 == 0:
                print(f"Epoch: {epoch} | Train loss: {train_loss:.5f} | Train acc: {train_acc:.2f}% | Test loss: {test_loss:.5f} | Test acc: {test_acc:.2f}%")




# -------- Final Results -------- #
# Need to add data to the dataset



# -------- Saving Model -------- #
