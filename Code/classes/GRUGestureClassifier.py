import torch
from pathlib import Path
from utils import landmarks_to_tensor
from main_hyperparmeters import LABEL_LIST, INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE

class GRUGestureClassifier():
    def __init__(self, model: torch.nn.Module, model_parameters_path: Path):
         # instantiate the model
        self.model = model(
                input_size=INPUT_SIZE,
                hidden_size=HIDDEN_SIZE,
                num_layers=NUM_LAYERS,
                num_classes=OUTPUT_SIZE,
        )  
        self.model.load_state_dict(torch.load(model_parameters_path))
        self.model.eval()

        self.live_wrapper = LiveGRUWrapper(self.model)


    def predict(self, landmarks: list[list[float]]) -> tuple[str, float]:
        # Convert landmarks to tensor (1, 1, 63)
        tensor = landmarks_to_tensor(landmarks)
        
        # Get logits and Probabilities
        logits = self.live_wrapper.step(tensor)
        probs = torch.softmax(logits.squeeze(), dim=0)

        label_idx = probs.argmax().item()

        return LABEL_LIST[label_idx], probs.max().item()

    def reset(self):
        self.live_wrapper.reset()



class LiveGRUWrapper:
    def __init__(self, model):
        self.model = model
        self.h_n = None

    def reset(self):
        self.h_n = None

    def step(self, row_tensor):
        # row_tensor: (batch size: 1, sequence size: 1, input size: 63)
        with torch.inference_mode():
            output, self.h_n = self.model(row_tensor, self.h_n)

        return output