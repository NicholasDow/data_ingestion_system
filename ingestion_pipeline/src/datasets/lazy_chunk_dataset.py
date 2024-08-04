import pyarrow.parquet as pq
import torch
from torch.utils.data import Dataset


class LazyChunkDataset(Dataset):
    def __init__(self, file_path: str):
        self.table = pq.read_table(file_path)

    def __len__(self):
        return self.table.num_rows

    def __getitem__(self, idx):
        chunk = self.table.take([idx])
        return {
            'id': chunk['id'][0].as_py(),
            'doc_id': chunk['doc_id'][0].as_py(),
            'text': chunk['text'][0].as_py(),
            'embedding': torch.tensor(chunk['embedding'][0].as_py())
        }