import torch
import os
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import pandas as pd
import numpy as np

label_map = {'rock': 0, 'paper': 1, 'scissors': 2}


# Dataset class, used for dataloader
class handDataset(Dataset):
    def __init__(self):
        self.dataset = []
        self.labels = []
    
    def __getitem__(self, index):
        return self.dataset[index], self.labels[index]
    
    def __len__(self):
        return len(self.dataset)
    
    # label map
    def labelToIndex(self, label):
        return label_map.get(label.lower())

    # Used by addToDataset()
    # input: csv file
    def csvToTensor(self, csv_file):

        df = pd.read_csv(csv_file)  # size of (num_of_rows, 66)
        df = df.sort_values(by='id')
        label = df.iloc[0]['label']
        df = df.drop(columns=['hand-side', 'id', 'label'])  # size of (num_of_rows, 63)

        # df -> numpy -> tensor
        numpy_arr = df.to_numpy()   # size of (num_of_rows, 63)
        tensor_dataframe = torch.tensor(numpy_arr)  # size of (num_of_rows, 63)

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
    '''
    max_length = 0
    length_list = []
    padded_batch = []

    # finds longest example length
    # creates true lengths list
    for example in batch:
        curr_length = example[0].shape[0]

        length_list.append(length)
        if curr_length > max_length:
            max_length = example[0].shape[0]

    # padding
    for example in batch:
        curr_length = example[0].shape[0]

        if curr_length < max_length:
            padding_size = max_length - curr_length
    '''
    # makes two tuples
    tensors, labels = zip(*batch)
    labels = torch.tensor(labels, dtype=torch.long)

    # pads the tensors
    padded_tensors = pad_sequence(tensors, batch_first=True, padding_value=0)
    
    return padded_tensors, labels


if __name__ == "__main__":
    # Test the Dataset and DataLoader with collate_func
    test_folder = os.path.join(os.path.dirname(__file__), 'test_folder')

    # Initialize the dataset
    dataset = handDataset()
    dataset.addToDataset(test_folder)

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