import torch
from pathlib import Path
from utils import landmarks_to_tensor
from main_hyperparmeters import NUM_CLASSES, NUM_FEATURES

class StaticHandGestureClassifier():
    def __init__(self, model: torch.nn.Module, model_parameters_path: Path):
        # instantiate the model
        self.model = model(input_features=NUM_FEATURES, output_features=NUM_CLASSES)
        self.model.load_state_dict(torch.load(model_parameters_path))
        self.model.eval()

        self.labels = ['rock', 'paper', 'scissors']

    def predict(self, landmarks: list[list[float]]) -> str:
        tensor = landmarks_to_tensor(landmarks).squeeze(0)  # Convert landmarks to tensor (1, 63)

        with torch.inference_mode():
            logits = self.model(tensor)
            logits = logits.squeeze(0)  
            y = torch.softmax(logits, dim=0).argmax(0)

        return self.labels[y.item()]