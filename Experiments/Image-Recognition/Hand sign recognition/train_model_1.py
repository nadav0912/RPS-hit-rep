# ---------- IMPORTS ---------- #
import torch
import torch.nn as nn
from torchmetrics.classification import Accuracy, ConfusionMatrix
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tqdm.auto import tqdm 
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from RPS_model_class import RPSModelV1
from utils import save_model, hand_dataset

os.chdir(os.path.dirname(__file__))


# ---------- SET HYPERPARAMETERS & INITIALIZATION ---------- #
NUM_CLASSES = 4
NUM_FEATURES = 21*3
RANDOM_SEED = 42

# Device agonstic code
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device.")

dataset_path = "hand-dataset.csv"

labels_map = {
    'rock': 0,
    'paper': 1,
    'scissors': 2,
    'other': 3
}

labels = list(labels_map.keys())


# ---------- GET DATASET ---------- #
df = hand_dataset()

X_df = df.drop(columns=['label', 'hand-side'])
y_df = df['label'].map(labels_map)

X_tensor = torch.from_numpy(X_df.values).type(torch.float32)
y_tensor = torch.from_numpy(y_df.values).type(torch.long)  

print(f"Get dataset:\n   X_tensor shape {X_tensor.shape}\n   y_tensor shape {y_tensor.shape}")

# split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_tensor,
                                                     y_tensor,
                                                     test_size=0.3,
                                                     shuffle=True,
                                                     random_state=RANDOM_SEED)

print(f"X_train: {X_train.shape}, X_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}")
print("y_test:", y_test)


# ---------- INSTANCE OF THE MODEL ---------- #
torch.manual_seed(RANDOM_SEED)
model = RPSModelV1(input_features=NUM_FEATURES, output_features=NUM_CLASSES).to(device)
print("MODEL:\n", model)



# ---------- LOSS & OPTIMIZER ---------- #
loss_fn = nn.CrossEntropyLoss()

accuracy_fn = Accuracy(task="multiclass", num_classes=NUM_CLASSES)
confmat_fn = ConfusionMatrix(task="multiclass", num_classes=NUM_CLASSES)


optimizer = torch.optim.SGD(params=model.parameters(), lr=0.1)


# ---------- TRAINING & TESTING ---------- #
epochs = 450

for epoch in tqdm(range(epochs)):
    ### Training
    model.train()

    y_train_logits = model(X_train)
    y_train_preds = torch.softmax(y_train_logits, dim=1).argmax(dim=1)  # useing dim=1 for doing this function on each example (row)

    train_loss = loss_fn(y_train_logits, y_train)
    train_acc = accuracy_fn(y_train_preds, y_train)  # (preds, y_true)

    optimizer.zero_grad()
    train_loss.backward()
    optimizer.step()


    ### Testing
    model.eval()
    with torch.inference_mode():
        test_logits = model(X_test)
        tets_preds = torch.softmax(test_logits, dim=1).argmax(dim=1)

        test_loss = loss_fn(test_logits, y_test)
        test_acc = accuracy_fn(tets_preds, y_test)


    ### Print loss & metrics
    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | Train loss: {train_loss:.5f} | Train acc: {train_acc:.2f}% | Test loss: {test_loss:.5f} | Test acc: {test_acc:.2f}%")



# -------- Final Results -------- #
model.eval()
with torch.inference_mode():
    y_logits = model(X_test)
    y_preds = torch.softmax(y_logits, dim=1).argmax(dim=1)


report = classification_report(y_true=y_test, y_pred=y_preds)
print(report)

cm = confmat_fn(y_preds, y_test)  # get tensor represent CM numbers
cm_numpy = cm.numpy()  # Convert to numpay array

plt.figure(figsize=(8,6))
sns.heatmap(cm_numpy, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

"""
Best results for now: 
        epochs = 450,
        lr=0.1,
        RPSModel(
            (layers_stack): Sequential(
            (0): Linear(in_features=63, out_features=64, bias=True)
            (1): ReLU()
            (2): Linear(in_features=64, out_features=64, bias=True)
            (3): ReLU()
            (4): Linear(in_features=64, out_features=4, bias=True)
            )
        )
"""


# -------- Saving Model -------- #
is_saving = input("\n\nDo you want to save this (y/n): ") == 'y'
if is_saving:
    name = input("Enter name for this results: ")
    save_model(model, name)
