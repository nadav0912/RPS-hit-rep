import torch
import os
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import pandas as pd
import numpy as np
from pathlib import Path
from utils import LABEL_MAP, DATASET_PATH


# Dataset class, used for dataloader
class handDataset(Dataset):
    def __init__(self):
        self.dataset = []  # list of tensors
        self.labels = []  # list of int

        self.addToDataset(DATASET_PATH)

    def __getitem__(self, index):
        return self.dataset[index], self.labels[index]
    
    def __len__(self):
        return len(self.dataset)
    
    # label map
    def labelToIndex(self, label):
        return LABEL_MAP.get(label.lower())

    # Used by addToDataset()
    # input: csv file
    def csvToTensor(self, csv_file):

        df = pd.read_csv(csv_file)  # size of (num_of_rows, 66)
        percent = 0.7
        df = df.iloc[:int(len(df)*percent)]
        print(f"this is without the last {percent}% of each example")
        df = df.sort_values(by='id')
        label = df.iloc[0]['label']
        df = df.drop(columns=['hand-side', 'id', 'label'])  # size of (num_of_rows, 63)

        # df -> numpy -> tensor
        numpy_arr = df.to_numpy()   # size of (num_of_rows, 63)
        tensor_dataframe = torch.tensor(numpy_arr, dtype=torch.float32)  # size of (num_of_rows, 63)

        return tensor_dataframe, label

    # adds all the csv's in a folder as tensors to the class dataset/lables lists
    def addToDataset(self, folder):
        for csv_file in os.listdir(folder):
            csv_path = os.path.join(folder, csv_file)
            data, label = self.csvToTensor(csv_path)
            self.dataset.append(data)
            self.labels.append(self.labelToIndex(label))


# collate function, used for dataloader
# batch =   [(tensor, label),...] 
#           tensor - (num_of_frames, 63)
def collate_func(batch):
    # makes two tuples
    tensors, labels = zip(*batch)
    labels = torch.tensor(labels, dtype=torch.long)

    # pads the tensors
    padded_tensors = pad_sequence(tensors, batch_first=True, padding_value=0)
    
    return padded_tensors, labels


if __name__ == "__main__":
    # Initialize the dataset
    dataset = handDataset()

    # Check if dataset is loaded correctly
    print(f"Total examples loaded: {len(dataset)}")
    for i in range(len(dataset)):
        print(f"Example {i + 1} - Tensor shape: {dataset[i][0].shape}, Label: {dataset[i][1]}")

    # Create a DataLoader with the custom collate function
    dataloader = DataLoader(
        dataset,
        batch_size=2,   # Test with a batch size of 2
        shuffle=False,
        collate_fn=collate_func
    )

    # Testing the DataLoader
    print("\nTesting DataLoader with custom collate function:")
    for batch_data, batch_labels in dataloader:
        print(f"Padded Data Shape: {batch_data.shape}")  # (batch_size, max_num_of_frames, 63)
        print(f"Labels: {batch_labels}\n")