import pandas as pd
from pathlib import Path

from utils import normalize_landmarks
from .hyperparams import DATASET_PATH


def add_example_to_dataset(label:str, hand_side: str, landmarks_data: list[list[list[int]]]):
    """
    Add the new example as one csv file to the 'data' directory (our dataset).
    Normalize the landmarks relative to each individual frame.
    Assign a sequence ID to preserve the order within the sequence.
    Find Last example file id to create new file path.
    Save the file in dataset path.

    input: 
        label - rock/paper/scissors
        hand_side - left/right
        data - a list of all ladmarks, each landmark is [[x0, y0, z0], [x1, y1, z1], ...]
    
        return: None
    """
    # Normalize all landmarks in landmarks_data
    for i in range(len(landmarks_data)):
        landmarks_data[i] = normalize_landmarks(landmarks_data[i])

    # Get data in right format
    data = prepare_data_to_df(landmarks_data, label, hand_side)
    
    # Create DataFrame from data
    df = pd.DataFrame(data)

    # Create new file path
    file_id = get_last_example_id() + 1
    file_path = DATASET_PATH / (str(file_id) + ".csv")
    
    # Save df as csv file in data
    df.to_csv(file_path, index=False)

    print(f"Add new example:\n  path - {file_path}\n  label- {label}\n  hand_side - {hand_side}\n  num frames in example - {len(df)}")


def prepare_data_to_df(landmarks_data: list[list[list[int]]], label:str, hand_side: str) -> list[dict]:
    """ Create list with all rows. each row is a dict in the format {"hand-side": , "label": ,"id": ,x1:, y1:, z1:, x2: , ....}
        To each roe it add is sequence id as id """
    rows = []
    for i, landmark in enumerate(landmarks_data):
        row = {"hand-side": hand_side, "label": label, "id": i}
        for i, dot in enumerate(landmark):
            row[f"x{i}"] = dot[0]
            row[f"y{i}"] = dot[1]
            row[f"z{i}"] = dot[2]
        
        rows.append(row)

    return rows


def get_last_example_id()-> int:
    """ return:
            last_id - the last csv file name that in data folder. if data folder is empty reurn -1.
    """
    # Get all files inside dataset
    entries = list(DATASET_PATH.iterdir())

    # Find max file id (name)
    max = -1
    for entrie in entries:
        id = int(entrie.name.replace(".csv", ""))
        if id > max:
            max = id

    return max


if __name__ == "__main__":
    add_example_to_dataset("rock", "right", [[[i, i+1, i+2] for i in range(7)], [[i, i+1, i+2] for i in range(7)],[[i, i+1, i+2] for i in range(10, 17)]])