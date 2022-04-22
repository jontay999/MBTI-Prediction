import numpy as np
from torch.utils.data import Dataset
import torch
from transformers import *

import utils.dataset_processors as dataset_processors


class MyMapDataset(Dataset):
    def __init__(self, tokenizer, token_length, DEVICE, reddit_file):
        print(f"Loading in dataset...")
        author_ids, input_ids, targets = dataset_processors.reddit_embeddings(reddit_file, tokenizer, token_length)
        print("Length of data:", len(author_ids))
        author_ids = torch.from_numpy(np.array(author_ids)).long().to(DEVICE)
        input_ids = torch.from_numpy(np.array(input_ids)).long().to(DEVICE)
        targets = torch.from_numpy(np.array(targets))
        targets = targets.long().to(DEVICE)

        self.author_ids = author_ids
        self.input_ids = input_ids
        self.targets = targets

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, idx):
        return (self.author_ids[idx], self.input_ids[idx], self.targets[idx])
