import torch
import numpy as np
from utils.model_utils import LiveONNXGRUWrapper
from utils.hyperparams import INPUT_SIZE, NUM_LAYERS, HIDDEN_SIZE, TRAINED_MODEL
from pathlib import Path

def main():
    #Path to ONNX file
    onnx_path = Path(__file__).parent / "models_state_compiled" / f"{TRAINED_MODEL}.onnx"
    if not onnx_path.exists():
        raise FileNotFoundError(f"ONNX file not found: {onnx_path}")

    print(f"Found ONNX model at: {onnx_path}, called {TRAINED_MODEL}.onnx")

    # Use ONNX wrapper
    model = LiveONNXGRUWrapper(onnx_path)

    # Simulation of dummy input to model
    model.reset()
    sequence_length = 10

    print("\nRunning dummy inference on random input...")
    for t in range(sequence_length):
        x_t = torch.randn(1, 1, INPUT_SIZE)  # shape: (batch=1, seq=1, features=63)
        logits = model.step(x_t)
        predicted_class = np.argmax(logits, axis=-1).item()
        print(f"Frame {t+1:02d}: class index = {predicted_class}, logits = {logits.squeeze()}")

if __name__ == "__main__":
    main()
