import torch
from ..utils import landmarks_to_tensor
from ..main_hyperparmeters import LABEL_LIST

class MovePredictor():
    def __init__(self, model: torch.nn.Module, model_path: str):
        self.model = model
        self.model.load_state_dict(torch.load(model_path + '.pth'))
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