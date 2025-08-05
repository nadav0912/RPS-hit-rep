import torch
from pathlib import Path
from utils import landmarks_to_tensor
import onnxruntime as ort
import numpy as np
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

        #self.model.load_state_dict(torch.load(model_parameters_path))
        #self.model.eval()

        self.live_wrapper = LiveONNXGRUWrapper("Code/final_models/GRU/front_hand_jap_v3.onnx")


    def predict(self, landmarks: list[list[float]]) -> tuple[str, float]:
        # Convert landmarks to tensor (1, 1, 63)
        tensor = landmarks_to_tensor(landmarks)
        
        # Get logits and Probabilities
        logits = self.live_wrapper.step(tensor)
        logits = torch.tensor(logits, dtype=torch.float32)
        print(logits)
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
    

class LiveONNXGRUWrapper:
    def __init__(self, onnx_path):
        self.session = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
        self.h_n = None
        self.reset()

    def reset(self):
        # infer h_n shape by running with zeros for the ONNX space allocation
        self.h_n = np.zeros((NUM_LAYERS, 1, HIDDEN_SIZE), dtype=np.float32)

    def step(self, row_tensor):
        # row_tensor: (batch size: 1, sequence size: 1, input size: 63)
        x_np = row_tensor.cpu().numpy()     # ONNX expects numpy float32 only

        logits, h1 = self.session.run(None, {"x": x_np, "h0": self.h_n})
        self.h_n = h1
        return logits