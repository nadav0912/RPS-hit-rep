import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np

num_of_keypoints = 21

# create a dataset from a csv
class GestureDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.keypoint_columns = [f'x{i}' for i in range(num_of_keypoints)] + [f'y{i}' for i in range(num_of_keypoints)] + [f'z{i}' for i in range(num_of_keypoints)]
        
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        label = self.get_label(row['label'])
        frames = self.get_frames(row)
        return {'label': label, 'frames': frames}
    
    def get_label(self, label):
        label_map = {'paper': 0, 'rock': 1, 'scissors': 2}
        return label_map[label]
    
    def get_frames(self, row):
        # Ensure the columns are numeric, replacing non-numeric with 0.0
        frames = pd.to_numeric(row[self.keypoint_columns], errors='coerce').fillna(0.0).values.reshape(-1, 3)
        frames_tensor = torch.tensor(frames, dtype=torch.float32)   # convert numpy array to tensor
        return frames_tensor

# Padding function for dataloader
# Handles variable-length sequences, Pads them to the same length, Returns them in a form the model can process
# batch - dict of {'frames': Tensor of shape [T_i, 21, 3], 'label': int}
#         T_i - number of frames in specific sample
#         21 - number of keypoints
#         3 - number of dimensions(x,y,z)
# This function takes a list of samples (from the Dataset)
# and turns them into a single batch
def custom_collate(batch):

    # list of labels from each sample
    # then turn labels into a tensor
    labels = [item['label'] for item in batch]
    labels_tensor = torch.tensor(labels, dtype=torch.long)  # shape: [batch_size]

    # list that stores all the frame tensors from the batch
    # each tensor has shape [num_of_frames_in_sample, 21, 3]
    sequences = [item['frames'] for item in batch]

    # Pad all frame sequences to the same length (max sequence length in batch)
    # This turns them into shape: [batch_size, max_sequence_length, 21, 3]
    # pad_sequence - adds zeros to the end of the shorter sequences so that all 
    #                sequences have the same number of frames, what we call T_max
    padded_sequences = pad_sequence(sequences, batch_first=True)

    # mask to tell the model where the real data is (not padding)
    # then turn into a tensor that holds the length of each sequence
    lengths = [seq.shape[0] for seq in sequences]
    lengths_tensor = torch.tensor(lengths, dtype=torch.long)

    # build the mask -  for each position, check if it's less than the real length
    # the model can use the mask to ignore padding
    # True is valid, False is part of mask- model can ignore
    batch_size = len(sequences)
    max_length = padded_sequences.shape[1]
    mask = torch.zeros(batch_size, max_length, dtype=torch.bool)
    for i in range(batch_size):
        for t in range(lengths[i]):
            mask[i][t] = True  # Not padding

    # B - Batch size
    # T_max - Length of the longest sequence in the batch after padding
    # 21 - Number of keypoints
    # 3 - feature dimension - (x,y,z)
    return {
        'frames': padded_sequences,  # shape: [B, T_max, 21, 3]
        'label': labels_tensor,      # shape: [B]
        'mask': mask                 # shape: [B, T_max]
    }


csv_file = '2.csv'  # Replace with the path to your CSV file

# Initialize the dataset
gesture_dataset = GestureDataset(csv_file=csv_file)

# Create the DataLoader
gesture_loader = DataLoader(
    gesture_dataset,
    batch_size=28,          # You can change this to any batch size you want
    shuffle=True,          # Shuffles the data for each epoch
    collate_fn=custom_collate  # Uses your custom collate function
)

# Test the DataLoader
for batch in gesture_loader:
    print("Frames (Tensor):", batch['frames'].shape)   # [B, T_max, 21, 3]
    print("Labels (Tensor):", batch['label'].shape)    # [B]
    print("Mask (Tensor):", batch['mask'].shape)       # [B, T_max]
    print("\nSample Data (First Batch):")
    print("Frames:", batch['frames'][0])               # First sample's frames
    print("Label:", batch['label'][0])                 # First sample's label
    print("Mask:", batch['mask'][0])                   # First sample's mask
    break  # Only show the first batch