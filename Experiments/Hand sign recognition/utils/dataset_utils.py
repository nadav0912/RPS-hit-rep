import pandas as pd
import os

dataset_path = "C:\Data\Projects\Hand sign recognition\hand-dataset.csv"

def add_examples_to_dataset(data: list):
    df = pd.DataFrame(data)

    print("\n\nThe new data you create:")
    print(df.groupby(['hand-side', 'label']).size())

    # Save new data to datset
    if os.path.exists(dataset_path):
        df.to_csv(dataset_path, mode='a', header=False, index=False)  # mode='a' for append mode
    else:
        df.to_csv(dataset_path, mode='w', header=True, index=False)  # mode='w' for write mode


def hand_dataset() -> pd.DataFrame:
    return pd.read_csv(dataset_path)



if __name__ == "__main__":
    df = hand_dataset()
    num_rows = df.shape[0]
    label_counts = df['label'].value_counts()
    hand_side_counts = df['hand-side'].value_counts()
    label_hand_side_counts = df.groupby(['label', 'hand-side']).size().reset_index(name='counts')

    print(f"The number of rows in the dataset is: {num_rows}")

    print("\nCount of Examples by Label:")
    print(label_counts)

    print("\nCount of Examples by Hand Side:")
    print(hand_side_counts)
    
    print("\nCount of Examples by Label and Hand Side:")
    print(label_hand_side_counts)
