import seaborn as sns
import matplotlib.pyplot as plt
from utils import LABEL_MAP

label_list = list(LABEL_MAP.keys())


def confusion_matrix_heat_map(confmat_fn, y_preds, y_true):
    cm = confmat_fn(y_preds, y_true)
    cm_numpy = cm.numpy() 

    plt.figure(figsize=(8,6))
    sns.heatmap(cm_numpy, annot=True, fmt='d', cmap='Blues', xticklabels=label_list, yticklabels=label_list)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')


def loss_and_acc_graghs(loss_map, num_epochs):
    epochs = range(1, len(loss_map["test_loss"]) + 1)

    plt.figure(figsize=(12, 6))

    # Losses subplot (upper)
    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss_map["train_loss"], label='Train Loss', color='blue')
    plt.plot(epochs, loss_map["test_loss"], label='Test Loss', color='green')
    plt.title('Loss over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    # Accuracies subplot (lower)
    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss_map["train_acc"], label='Train Accuracy', color='blue')
    plt.plot(epochs, loss_map["test_acc"], label='Test Accuracy', color='green')
    plt.title('Accuracy over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
