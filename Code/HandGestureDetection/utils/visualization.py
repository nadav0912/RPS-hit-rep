import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2
import threading

from .hyperparams import LABEL_MAP, LABEL_LIST
from .model_utils import LiveGRUWrapper
from .model_utils import landmarks_to_list, normalize_landmarks, get_label_list_from_example


def check_key_press(delay: int = 1) -> str:
    """
    Waits briefly and returns the pressed key as a lowercase letter.
    Requires an active OpenCV window to detect key presses.
    """
    key_code = cv2.waitKey(delay) & 0xFF

    if key_code != 255:
        print(f"Key pressed: {chr(key_code)}")
        return chr(key_code).lower()

    return ''


def confusion_matrix_heat_map(confmat_fn, y_preds, y_true):
    cm = confmat_fn(y_preds, y_true).cpu()
    cm_numpy = cm.numpy() 

    plt.figure(figsize=(8,6))
    sns.heatmap(cm_numpy, annot=True, fmt='d', cmap='Blues', xticklabels=LABEL_LIST, yticklabels=LABEL_LIST)
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


def draw_label_on_image(landmarks, image, label_text):
    landmarks = np.array(landmarks_to_list(landmarks))
    height, width, channels = image.shape

    x_coordinates = landmarks[:, 0]
    y_coordinates = landmarks[:, 1]

    x_min = int(np.min(x_coordinates) * width)
    x_max = int(np.max(x_coordinates) * width)
    y_min = int(np.min(y_coordinates) * height)
    y_max = int(np.max(y_coordinates) * height)


    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=1)
    cv2.putText(image, label_text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (40, 240, 40), 2, lineType=cv2.LINE_AA)

    return image


def show_record_example(example_images: list[list[int]], example_landmarks: list[list[list[int]]], live_wrapper: LiveGRUWrapper) -> bool:
    """
    Display a sequence of example images with predicted labels, allowing the user to confirm or discard the example.
    
    Args:
        example_images (list of list): A list of images (frames) to display.
        example_landmarks (list of list of list): Corresponding landmarks for each frame.
        live_wrapper (LiveGRUWrapper): Wrapper containing the model used for prediction.
    
    Returns:
        bool: True if the user chooses to save the example ('s' key), False if the user cancels ('c' key).
    """
    size = len(example_images)
    count = 0

    # Normalize all landmarks in example_landmarks
    for i in range(len(example_landmarks)):
        example_landmarks[i] = normalize_landmarks(example_landmarks[i])

    # Convert example_landmarks to tensor
    example = torch.tensor(example_landmarks).flatten(start_dim=1)

    # Get the predicted labels for the example
    probs_list = get_label_list_from_example(live_wrapper, example)  

    print("\nShow example. press s to save and c to cancel...")
    while True:
        # Check if user press key
        key = check_key_press(delay=100)

        # Update index (i)
        count += 1
        i = count%size

        # If user press 's' key, save example
        if key == 's':
            print("Save example!")
            return True
        
        # If user press 'c' key, cancel example 
        elif key == 'c':
            print("Cancel example!")
            return False

        # Draw predicted label on image and show the image
        image = example_images[i]
        probs = probs_list[i]
        label = LABEL_LIST[probs.index(max(probs))]
        text = f"frame: {str(i)} | pred: {label} | {[f'{p * 100:.2f}%' for p in probs]} | {LABEL_LIST}"

        cv2.putText(image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (2, 57, 66), 1, lineType=cv2.LINE_AA)
        cv2.imshow("example", image)