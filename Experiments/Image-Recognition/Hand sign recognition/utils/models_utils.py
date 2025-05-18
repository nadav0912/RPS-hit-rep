import torch
import numpy as np
from pathlib import Path


def save_model(model: torch.nn.Module, model_name: str):
    MODEL_PATH = Path("c:\Data\Projects\Hand sign recognition\models") 
    MODEL_PATH.mkdir(parents=True, exist_ok=True) 
    model_name += '.pth'
    MODEL_SAVE_PATH = MODEL_PATH / model_name
    print(f"Saving model to: {MODEL_SAVE_PATH}")
    torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)  


def load_model(model: torch.nn.Module, model_name: str):
    MODEL_PATH = Path("c:\Data\Projects\Hand sign recognition\models") 
    model_name += '.pth'
    MODEL_SAVE_PATH = MODEL_PATH / model_name
    model.load_state_dict(torch.load(f=MODEL_SAVE_PATH))


def normolize_landmarks(landmarks: list) -> list:
    landmarks = np.array(landmarks)

    # Find min & max for x, y and z  
    x_coordinates, y_coordinates, z_coordinates= landmarks[:, 0], landmarks[:, 1], landmarks[:, 2]

    x_min, x_max = np.min(x_coordinates), np.max(x_coordinates)
    y_min, y_max = np.min(y_coordinates), np.max(y_coordinates)
    z_min, z_max = np.min(z_coordinates), np.max(z_coordinates)

    # Subtract the minimum value of x, y, and z from their respective coordinates.
    landmarks[:, 0] -= x_min
    landmarks[:, 1] -= y_min
    landmarks[:, 2] -= z_min

    # Calculate width, height, and depth
    width, height, depth = (x_max - x_min), (y_max - y_min), abs(z_max - z_min)

    # Normalize the landmarks coordinates (x, y, z) by their respective bounding box dimensions (width, height, depth).
    landmarks[:, 0] /= width
    landmarks[:, 1] /= height
    landmarks[:, 2] /= depth

    """print(f"width: {width}, hight: {height}, depth: {depth}")
    print(f"x range: {x_min} to {x_max}, y range: {y_min} to {y_max}, z range: {z_min} to {z_max}")
    print("\n\n", landmarks)"""

    return landmarks.tolist()


def process_one_example(model: torch.nn.Module, X: torch.tensor):
    """
    Processes a single input through the RPS model and returns the predicted label.

    Args -> model (torch.nn.Module): Trained RPS model.
            X (torch.tensor): 1D tensor of size 63 representing the input.

    Returns -> str: Predicted label ('rock', 'paper', 'scissors', or 'other').
    """
    labels = ['rock', 'paper', 'scissors', 'other']

    model.eval()
    with torch.inference_mode():
        logits = model(X)
        y = torch.softmax(logits, dim=0).argmax(0)

    return labels[y]



def label_from_RPSmodel(model: torch.nn.Module, landmarks: list):
    if len(landmarks) != 21:
        return "other"

    x = torch.tensor(normolize_landmarks(landmarks)).flatten(0)

    return process_one_example(model, x)