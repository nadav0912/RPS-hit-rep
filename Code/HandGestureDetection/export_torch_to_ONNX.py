import torch
import onnx
import pathlib
from Gesture_detection_model import GRUModelV1
from utils import load_model
from utils import TRAINED_MODEL, MODEL, INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS

ONNX_FILE = pathlib.Path(__file__).parent / "models_state_compiled" / (TRAINED_MODEL + ".onnx")

load_model(MODEL, model_name=TRAINED_MODEL)
MODEL.eval()


# ONNX needs dummy input to define itself
x_dummy = torch.randn(1, 1, INPUT_SIZE)             # (batch, seq, keypoints) -> (1,1,63)
h_dummy = torch.zeros(NUM_LAYERS, 1, HIDDEN_SIZE)   # (layers, batch, hidden size)

torch.onnx.export(
    MODEL,
    (x_dummy, h_dummy),                             # tuple with arguments for .forward()
    ONNX_FILE.as_posix(),                           # PATH to save the exported model
    opset_version = 17,                             # ONNX version
    input_names  = ["x", "h0"],
    output_names = ["logits", "h1"],
    dynamic_axes = {
        "x": {0: "batch", 1: "seq"},
        "logits": {0: "batch", 1: "seq"}
    }
)

onnx.checker.check_model(ONNX_FILE)    # raises if anything is wrong
print("✓ exported to", ONNX_FILE)