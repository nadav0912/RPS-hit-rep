# ---------- IMPORTS ---------- #
import torch
import torch.nn as nn
import numpy as np
import torch.optim.adam
from torch.utils.data import DataLoader, Subset
from torchmetrics.classification import Accuracy, ConfusionMatrix
from tqdm.auto import tqdm 
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from utils import handDataset, collate_func, confusion_matrix_heat_map, loss_and_acc_graghs, save_model
from utils import TEST_SIZE, NUM_LAYERS, HIDDEN_SIZE, INPUT_SIZE, OUTPUT_SIZE, BATCH_SIZE, EPOCHS, LEARNING_RATE, RANDOM_SEED
from Gesture_detection_model import GRUModelV1


# Device agonstic code
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device.")

label_map = {'rock': 0, 'paper': 1, 'scissors': 2}


# ---------- GET DATASET ---------- #
dataset = handDataset()

# Create list of indices
indexes = np.arange(len(dataset))

# Split indices
train_indexes, test_indexes = train_test_split(indexes, test_size=TEST_SIZE, random_state=RANDOM_SEED)
print(f"{len(train_indexes)} in train, {len(test_indexes)} in test.")

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
).to(device)
print("\nMODEL:\n", model)


# ---------- LOSS & OPTIMIZER ---------- #
loss_fn = nn.CrossEntropyLoss()

accuracy_fn = Accuracy(task="multiclass", num_classes=OUTPUT_SIZE)
confmat_fn = ConfusionMatrix(task="multiclass", num_classes=OUTPUT_SIZE)

optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)


# ---------- TRAINING & TESTING ---------- #
def train():
        model.train()

        for batch, labels in train_dataloader:
                y_logits, _ = model(batch)
                y_preds = torch.softmax(y_logits, dim=1).argmax(dim=1)

                loss = loss_fn(y_logits, labels)
                acc = accuracy_fn(y_preds, labels)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        return loss.item(), acc


def test():
        model.eval()
        with torch.inference_mode():
                for batch, labels in test_dataloader:
                        y_logits, _ = model(batch)
                        y_preds = torch.softmax(y_logits, dim=1).argmax(dim=1)
                        
                        loss = loss_fn(y_logits, labels)
                        acc = accuracy_fn(y_preds, labels)

        return loss.item(), acc


# ---------- MAIN LOOP ---------- #
loss_map = {"test_loss": [], "train_loss": [],"test_acc": [], "train_acc": []}

for epoch in tqdm(range(EPOCHS)):
        train_loss, train_acc = train()
        test_loss, test_acc = test()

        for key, val in zip(loss_map.keys(), [test_loss, train_loss, test_acc, train_acc]):
               loss_map[key].append(val)

        if epoch % 10 == 0:
                print(f"Epoch: {epoch} | Train loss: {train_loss:.5f} | Train acc: {train_acc:.2f}% | Test loss: {test_loss:.5f} | Test acc: {test_acc:.2f}%")




# -------- Final Results -------- #

# Get all test data in one tensor
all_test_exampels = []
all_test_labels = []

for batch, labels in test_dataloader:
    all_test_exampels.append(batch)
    all_test_labels.append(labels)

all_test_exampels = torch.cat(all_test_exampels, dim=0)
all_test_labels = torch.cat(all_test_labels, dim=0)

# Process all test data through the model
model.eval()
with torch.inference_mode():
    y_logits, _ = model(all_test_exampels)
    y_preds = torch.softmax(y_logits, dim=1).argmax(dim=1)


report = classification_report(y_true=all_test_labels, y_pred=y_preds)
print(report)

confusion_matrix_heat_map(confmat_fn, y_preds, all_test_labels)

loss_and_acc_graghs(loss_map, num_epochs=EPOCHS)

plt.show()


# -------- Saving Model -------- #
model_name = input("Do you want save this (n->no):")

if model_name != "n":
       save_model(model, model_name)