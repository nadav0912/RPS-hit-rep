import torch
from torch import nn

class staticGestureModelV1(nn.Module):
    def __init__(self, input_features, output_features, hidden_units=64, dropout_prob=0.5):
        super().__init__()

        self.layers_stack = nn.Sequential(
            nn.Linear(in_features=input_features, out_features=hidden_units),
            nn.ReLU(),
            nn.Dropout(p=dropout_prob),  # Dropout after the first hidden layer
            nn.Linear(in_features=hidden_units, out_features=hidden_units),
            nn.ReLU(),
            nn.Dropout(p=dropout_prob),  # Dropout after the second hidden layer
            nn.Linear(in_features=hidden_units, out_features=output_features),
        )

    def forward(self, x):
        return self.layers_stack(x)