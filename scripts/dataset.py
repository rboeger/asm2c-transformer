import torch
from torch.utils.data import Dataset
import pandas as pd

class AsmCDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=512):
        self.data = pd.read_csv(file_path, sep="\t")
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        asm = self.data.iloc[idx]['assembly']
        c_code = self.data.iloc[idx]['c_code']

        inputs = self.tokenizer(
            asm, truncation=True, padding='max_length', max_length=self.max_length, return_tensors="pt"
        )
        targets = self.tokenizer(
            c_code, truncation=True, padding='max_length', max_length=self.max_length, return_tensors="pt"
        )

        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'labels': targets['input_ids'].squeeze()
        }