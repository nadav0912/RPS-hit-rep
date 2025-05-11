import torch
import torch.nn as nn

class GRUModelV1(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout_prob=0.3):
        super().__init__()
        
        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,  # (batch, seq, feature)
            dropout=dropout_prob,
        )
        
        self.fc = nn.Linear(hidden_size, num_classes)


    def forward(self, x):
        # x: (batch, seq_len, input_size)
        out, h_n = self.gru(x)  # out: (batch, seq_len, hidden_size)
        
        # Take output from the last time step
        last_time_step = out[:, -1, :]  # shape: (batch, hidden_size)
        
        out = self.fc(last_time_step)  # shape: (batch, num_classes)
        return out